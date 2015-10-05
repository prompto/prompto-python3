from antlr4 import ParseTreeWalker
from prompto.parser.Dialect import Dialect
from prompto.parser.ECleverParser import ECleverParser
from prompto.parser.EPromptoBuilder import EPromptoBuilder
from prompto.parser.OCleverParser import OCleverParser
from prompto.parser.OPromptoBuilder import OPromptoBuilder
from prompto.parser.SCleverParser import SCleverParser
from prompto.parser.SPromptoBuilder import SPromptoBuilder
from prompto.declaration.TestMethodDeclaration import TestMethodDeclaration
from prompto.runtime.Context import Context
from prompto.runtime.Interpreter import Interpreter
from prompto.runtime.utils.Out import Out
from prompto.utils.CodeWriter import CodeWriter

import os
import unittest


class BaseParserTest(unittest.TestCase):

    def __init__(self, args=None):
        super(BaseParserTest, self).__init__(args)
        self.coreContext = None

    def setUp(self):
        self.context = Context.newGlobalContext()

    def loadDependency(self, name):
        if self.coreContext is None:
            self.coreContext = Context.newGlobalContext()
        files = self.listLibraryFiles(name)
        if files is not None:
            for file in files:
                resourceName = name + "/" + file
                stmts = self.parseResource(resourceName)
                stmts.register(self.coreContext)

    def listLibraryFiles(self, libraryName):
        idx = __file__.index("/prompto-python3/Python3-Core/")
        dir = __file__[0:idx] + "/prompto-libraries/" + libraryName
        if os.path.isdir(dir):
            files = os.listdir(dir)
            def validFile(file):
                return ".pec" in file or ".poc" in file or ".psc" in file
            return filter(validFile, files )
        else:
            return None

    def runTests(self, resource):
        stmts = self.parseResource(resource)
        for decl in stmts:
            if not isinstance(decl, TestMethodDeclaration):
                continue
            Out.reset()
            Interpreter.interpretTest(self.coreContext, decl.name)
            expected = decl.name + " test successful"
            read = Out.read()
            self.assertEqual(read, expected)

    def getResourceAsString(self, resourceName, mode):
        idx = __file__.index("/prompto-python3/Python3-Core/")
        file = __file__[0:idx] + "/prompto-tests/Tests/resources/" + resourceName
        if not os.path.exists(file):
            file = __file__[0:idx] + "/prompto-libraries/" + resourceName
        with open(file, mode) as input:
            return input.read()

    def getResourceAsStream(self, resourceName, mode):
        idx = __file__.index("/prompto-python3/Python3-Core/")
        file = __file__[0:idx] + "/prompto-tests/Tests/resources/" + resourceName
        if not os.path.exists(file):
            file = __file__[0:idx] + "/prompto-libraries/" + resourceName
        return open(file, mode)

    def loadResource(self, resourceName):
        stmts = self.parseResource(resourceName)
        stmts.register(self.context)
        stmts.check(self.context)

    def parseResource(self, resourceName):
        raise Exception("You must override parseResource")

    def runResource(self, resourceName):
        self.loadResource(resourceName)
        if self.context.hasTests():
            Interpreter.interpretTests(self.context)
        else:
            Interpreter.interpretMainNoArgs(self.context)

    def runResourceMethod(self, resourceName, methodName, cmdLineArgs):
        self.loadResource(resourceName)
        Interpreter.interpret(self.context, methodName, cmdLineArgs)

    def checkOutput(self, resource):
        self.runResource(resource)
        self.checkExpected(resource)

    def checkExpected(self, resource):
        read = Out.read()
        expected = self.readExpected(resource)
        if len(expected) == 1:
            self.assertEquals(expected[0], read)
        else:
            for ex in expected:
                if ex == read:
                    return
            self.assertEquals(expected[0], read)  # to get a display

    def readExpected(self, resourceName):
        idx = resourceName.index('.')
        resourceName = resourceName[0:idx] + ".txt"
        input = self.getResourceAsStream(resourceName, 'r')
        self.assertIsNotNone("resource not found:" + resourceName, input)
        try:
            return [ s.strip() for s in input.readlines()]
        finally:
            input.close()

    def parse(self, builder, parser):
        tree = parser.declaration_list()
        builder = builder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

    def parseEString(self, code):
        parser = ECleverParser(text=code)
        return self.parse(EPromptoBuilder, parser)

    def parseEResource(self, resourceName):
        stream = self.getResourceAsStream(resourceName, 'rb')
        self.assertIsNotNone("resource not found:" + resourceName, stream)
        parser = ECleverParser(stream=stream)
        return self.parse(EPromptoBuilder, parser)

    def parseOString(self, code):
        parser = OCleverParser(text=code)
        return self.parse(OPromptoBuilder, parser)

    def parseSString(self, code):
        parser = SCleverParser(text=code)
        return self.parse(SPromptoBuilder, parser)

    def parseOResource(self, resourceName):
        stream = self.getResourceAsStream(resourceName, 'rb')
        self.assertIsNotNone("resource not found:" + resourceName, stream)
        parser = OCleverParser(stream=stream)
        return self.parse(OPromptoBuilder, parser)

    def compareResourceEOE(self, resourceName):
        expected = self.getResourceAsString(resourceName, 'r')
        # print(expected)
        # parse e source code
        dle = self.parseEString(expected)
        context = Context.newGlobalContext()
        dle.register(context)
        # rewrite as o
        writer = CodeWriter(Dialect.O, context)
        dle.toDialect(writer)
        o = str(writer)
        # print(o)
        # parse o source code
        dlo = self.parseOString(o)
        context = Context.newGlobalContext()
        dlo.register(context)
        # rewrite as e
        writer = CodeWriter(Dialect.E, context)
        dlo.toDialect(writer)
        actual = str(writer)
        # print(actual)
        # ensure equivalent
        self.assertEquivalent(expected, actual)

    def compareResourceESE(self, resourceName):
        expected = self.getResourceAsString(resourceName, 'r')
        # print(expected)
        # parse e source code
        dle = self.parseEString(expected)
        context = Context.newGlobalContext()
        dle.register(context)
        # rewrite as p
        writer = CodeWriter(Dialect.S, context)
        dle.toDialect(writer)
        p = str(writer)
        # print(p)
        # parse p source code
        dlp = self.parseSString(p)
        context = Context.newGlobalContext()
        dlp.register(context)
        # rewrite as e
        writer = CodeWriter(Dialect.E, context)
        dlp.toDialect(writer)
        actual = str(writer)
        # print(actual)
        # ensure equivalent
        self.assertEquivalent(expected, actual)

    def compareResourceOEO(self, resourceName):
        expected = self.getResourceAsString(resourceName, 'r')
        # print(expected)
        # parse o source code
        dlo = self.parseOString(expected)
        context = Context.newGlobalContext()
        dlo.register(context)
        # rewrite as e
        writer = CodeWriter(Dialect.E, context)
        dlo.toDialect(writer)
        e = str(writer)
        # print(e)
        # parse e source code
        dle = self.parseEString(e)
        context = Context.newGlobalContext()
        dle.register(context)
        # rewrite as o
        writer = CodeWriter(Dialect.O, context)
        dle.toDialect(writer)
        actual = str(writer)
        # print(actual)
        # ensure equivalent
        self.assertEquivalent(expected, actual)

    def compareResourceOSO(self, resourceName):
        expected = self.getResourceAsString(resourceName, 'r')
        # print(expected)
        # parse o source code
        dlo = self.parseOString(expected)
        context = Context.newGlobalContext()
        dlo.register(context)
        # rewrite as p
        writer = CodeWriter(Dialect.S, context)
        dlo.toDialect(writer)
        p = str(writer)
        # print(p)
        # parse p source code
        dlp = self.parseSString(p)
        context = Context.newGlobalContext()
        dlp.register(context)
        # rewrite as o
        writer = CodeWriter(Dialect.O, context)
        dlp.toDialect(writer)
        actual = str(writer)
        # print(actual)
        # ensure equivalent
        self.assertEquivalent(expected, actual)

    def assertEquivalent(self, expected, actual):
        expected = self.removeWhitespace(expected).replace("modulo","%")
        actual = self.removeWhitespace(actual).replace("modulo","%")
        self.assertEquals(expected, actual)

    def removeWhitespace(self, s):
        return s.replace(" ", "").replace("\t", "").replace("\n", "")

