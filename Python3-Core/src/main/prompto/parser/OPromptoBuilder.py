from antlr4 import Token
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Tree import ParseTree

from prompto.literal.TypeLiteral import TypeLiteral
from prompto.param.CategoryParameter import CategoryParameter
from prompto.param.CodeParameter import CodeParameter
from prompto.param.ExtendedParameter import ExtendedParameter
from prompto.param.UnresolvedParameter import UnresolvedParameter
from prompto.constraint.MatchingCollectionConstraint import MatchingCollectionConstraint
from prompto.constraint.MatchingExpressionConstraint import MatchingExpressionConstraint
from prompto.constraint.MatchingPatternConstraint import MatchingPatternConstraint
from prompto.csharp.CSharpBooleanLiteral import CSharpBooleanLiteral
from prompto.csharp.CSharpCharacterLiteral import CSharpCharacterLiteral
from prompto.csharp.CSharpDecimalLiteral import CSharpDecimalLiteral
from prompto.csharp.CSharpExpressionList import CSharpExpressionList
from prompto.csharp.CSharpIdentifierExpression import CSharpIdentifierExpression
from prompto.csharp.CSharpIntegerLiteral import CSharpIntegerLiteral
from prompto.csharp.CSharpMethodExpression import CSharpMethodExpression
from prompto.csharp.CSharpNativeCall import CSharpNativeCall
from prompto.csharp.CSharpNativeCategoryBinding import CSharpNativeCategoryBinding
from prompto.csharp.CSharpStatement import CSharpStatement
from prompto.csharp.CSharpTextLiteral import CSharpTextLiteral
from prompto.csharp.CSharpThisExpression import CSharpThisExpression
from prompto.css.CssCode import CssCode
from prompto.css.CssExpression import CssExpression
from prompto.css.CssField import CssField
from prompto.css.CssText import CssText
from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.declaration.ConcreteWidgetDeclaration import ConcreteWidgetDeclaration
from prompto.declaration.DeclarationList import DeclarationList
from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from prompto.declaration.GetterMethodDeclaration import GetterMethodDeclaration
from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from prompto.declaration.NativeGetterMethodDeclaration import NativeGetterMethodDeclaration
from prompto.declaration.NativeMethodDeclaration import NativeMethodDeclaration
from prompto.declaration.NativeResourceDeclaration import NativeResourceDeclaration
from prompto.declaration.NativeSetterMethodDeclaration import NativeSetterMethodDeclaration
from prompto.declaration.NativeWidgetDeclaration import NativeWidgetDeclaration
from prompto.declaration.OperatorMethodDeclaration import OperatorMethodDeclaration
from prompto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration
from prompto.declaration.TestMethodDeclaration import TestMethodDeclaration
from prompto.expression.ArrowExpression import ArrowExpression
from prompto.expression.MutableExpression import MutableExpression
from prompto.expression.PlusExpression import PlusExpression
from prompto.expression.AndExpression import AndExpression
from prompto.expression.BlobExpression import BlobExpression
from prompto.expression.CastExpression import CastExpression
from prompto.expression.CategorySymbol import CategorySymbol
from prompto.expression.CodeExpression import CodeExpression
from prompto.expression.CompareExpression import CompareExpression
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.ContainsExpression import ContainsExpression
from prompto.expression.DivideExpression import DivideExpression
from prompto.expression.DocumentExpression import DocumentExpression
from prompto.expression.EqualsExpression import EqualsExpression
from prompto.expression.ExecuteExpression import ExecuteExpression
from prompto.expression.FetchManyExpression import FetchManyExpression
from prompto.expression.FilteredExpression import FilteredExpression
from prompto.expression.FetchOneExpression import FetchOneExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.IntDivideExpression import IntDivideExpression
from prompto.expression.ItemSelector import ItemSelector
from prompto.expression.IteratorExpression import IteratorExpression
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.MethodExpression import MethodExpression
from prompto.expression.MinusExpression import MinusExpression
from prompto.expression.ModuloExpression import ModuloExpression
from prompto.expression.MultiplyExpression import MultiplyExpression
from prompto.expression.NativeSymbol import NativeSymbol
from prompto.expression.NotExpression import NotExpression
from prompto.expression.OrExpression import OrExpression
from prompto.expression.ParenthesisExpression import ParenthesisExpression
from prompto.expression.ReadAllExpression import ReadAllExpression
from prompto.expression.ReadOneExpression import ReadOneExpression
from prompto.expression.SliceSelector import SliceSelector
from prompto.expression.SortedExpression import SortedExpression
from prompto.expression.SubtractExpression import SubtractExpression
from prompto.expression.SymbolExpression import SymbolExpression
from prompto.expression.TernaryExpression import TernaryExpression
from prompto.expression.ThisExpression import ThisExpression
from prompto.expression.TypeExpression import TypeExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.expression.UnresolvedSelector import UnresolvedSelector
from prompto.grammar.Annotation import Annotation
from prompto.grammar.Argument import Argument
from prompto.grammar.ArgumentList import ArgumentList
from prompto.param.ParameterList import ParameterList
from prompto.grammar.CategorySymbolList import CategorySymbolList
from prompto.grammar.CmpOp import CmpOp
from prompto.grammar.ContOp import ContOp
from prompto.grammar.EqOp import EqOp
from prompto.grammar.IdentifierList import IdentifierList
from prompto.grammar.MethodDeclarationList import MethodDeclarationList
from prompto.grammar.NativeCategoryBindingList import NativeCategoryBindingList
from prompto.grammar.NativeSymbolList import NativeSymbolList
from prompto.grammar.Operator import Operator
from prompto.grammar.OrderByClause import OrderByClause
from prompto.grammar.OrderByClauseList import OrderByClauseList
from prompto.instance.ItemInstance import ItemInstance
from prompto.instance.MemberInstance import MemberInstance
from prompto.instance.VariableInstance import VariableInstance
from prompto.java.JavaBooleanLiteral import JavaBooleanLiteral
from prompto.java.JavaCharacterLiteral import JavaCharacterLiteral
from prompto.java.JavaDecimalLiteral import JavaDecimalLiteral
from prompto.java.JavaExpressionList import JavaExpressionList
from prompto.java.JavaIdentifierExpression import JavaIdentifierExpression
from prompto.java.JavaIntegerLiteral import JavaIntegerLiteral
from prompto.java.JavaItemExpression import JavaItemExpression
from prompto.java.JavaMethodExpression import JavaMethodExpression
from prompto.java.JavaNativeCall import JavaNativeCall
from prompto.java.JavaNativeCategoryBinding import JavaNativeCategoryBinding
from prompto.java.JavaStatement import JavaStatement
from prompto.java.JavaTextLiteral import JavaTextLiteral
from prompto.java.JavaThisExpression import JavaThisExpression
from prompto.javascript.JavaScriptBooleanLiteral import JavaScriptBooleanLiteral
from prompto.javascript.JavaScriptCharacterLiteral import JavaScriptCharacterLiteral
from prompto.javascript.JavaScriptDecimalLiteral import JavaScriptDecimalLiteral
from prompto.javascript.JavaScriptExpressionList import JavaScriptExpressionList
from prompto.javascript.JavaScriptIdentifierExpression import JavaScriptIdentifierExpression
from prompto.javascript.JavaScriptIntegerLiteral import JavaScriptIntegerLiteral
from prompto.javascript.JavaScriptMemberExpression import JavaScriptMemberExpression
from prompto.javascript.JavaScriptMethodExpression import JavaScriptMethodExpression
from prompto.javascript.JavaScriptModule import JavaScriptModule
from prompto.javascript.JavaScriptNativeCall import JavaScriptNativeCall
from prompto.javascript.JavaScriptNativeCategoryBinding import JavaScriptNativeCategoryBinding
from prompto.javascript.JavaScriptNewExpression import JavaScriptNewExpression
from prompto.javascript.JavaScriptStatement import JavaScriptStatement
from prompto.javascript.JavaScriptTextLiteral import JavaScriptTextLiteral
from prompto.javascript.JavaScriptThisExpression import JavaScriptThisExpression
from prompto.jsx.JsxClosing import JsxClosing
from prompto.literal.BooleanLiteral import BooleanLiteral
from prompto.literal.CharacterLiteral import CharacterLiteral
from prompto.literal.DateLiteral import DateLiteral
from prompto.literal.DateTimeLiteral import DateTimeLiteral
from prompto.literal.DecimalLiteral import DecimalLiteral
from prompto.literal.DictEntry import DictEntry
from prompto.literal.DictEntryList import DictEntryList
from prompto.literal.DictIdentifierKey import DictIdentifierKey
from prompto.literal.DictLiteral import DictLiteral
from prompto.literal.DictTextKey import DictTextKey
from prompto.literal.DocEntryList import DocEntryList
from prompto.literal.DocumentLiteral import DocumentLiteral
from prompto.literal.HexaLiteral import HexaLiteral
from prompto.literal.IntegerLiteral import IntegerLiteral, MinIntegerLiteral, MaxIntegerLiteral
from prompto.literal.ListLiteral import ListLiteral
from prompto.literal.NullLiteral import NullLiteral
from prompto.literal.PeriodLiteral import PeriodLiteral
from prompto.literal.RangeLiteral import RangeLiteral
from prompto.literal.SetLiteral import SetLiteral
from prompto.literal.TextLiteral import TextLiteral
from prompto.literal.TimeLiteral import TimeLiteral
from prompto.literal.TupleLiteral import TupleLiteral
from prompto.literal.UUIDLiteral import UUIDLiteral
from prompto.literal.VersionLiteral import VersionLiteral
from prompto.parser.Dialect import Dialect
from prompto.jsx.JsxSelfClosing import JsxSelfClosing
from prompto.jsx.JsxElement import JsxElement
from prompto.jsx.JsxProperty import JsxProperty
from prompto.jsx.JsxLiteral import JsxLiteral
from prompto.jsx.JsxText import JsxText
from prompto.jsx.JsxExpression import JsxExpression
from prompto.jsx.JsxCode import JsxCode
from prompto.parser import ParserUtils
from prompto.parser.OParser import OParser
from prompto.parser.OParserListener import OParserListener
from prompto.parser.Section import Section
from prompto.python.PythonArgument import PythonNamedArgument, PythonNamedArgumentList, PythonOrdinalArgumentList
from prompto.python.PythonBooleanLiteral import PythonBooleanLiteral
from prompto.python.PythonCharacterLiteral import PythonCharacterLiteral
from prompto.python.PythonDecimalLiteral import PythonDecimalLiteral
from prompto.python.PythonIdentifierExpression import PythonIdentifierExpression
from prompto.python.PythonIntegerLiteral import PythonIntegerLiteral
from prompto.python.PythonMethodExpression import PythonMethodExpression
from prompto.python.PythonModule import PythonModule
from prompto.python.PythonNativeCall import PythonNativeCall, Python2NativeCall, Python3NativeCall
from prompto.python.PythonNativeCategoryBinding import PythonNativeCategoryBinding, Python2NativeCategoryBinding, Python3NativeCategoryBinding
from prompto.python.PythonSelfExpression import PythonSelfExpression
from prompto.python.PythonStatement import PythonStatement
from prompto.python.PythonTextLiteral import PythonTextLiteral
from prompto.statement.AssignInstanceStatement import AssignInstanceStatement
from prompto.statement.AssignTupleStatement import AssignTupleStatement
from prompto.statement.AssignVariableStatement import AssignVariableStatement
from prompto.statement.RemoteCall import RemoteCall
from prompto.statement.AtomicSwitchCase import AtomicSwitchCase
from prompto.statement.BreakStatement import BreakStatement
from prompto.statement.CollectionSwitchCase import CollectionSwitchCase
from prompto.statement.CommentStatement import CommentStatement
from prompto.statement.DeclarationStatement import DeclarationStatement
from prompto.statement.DoWhileStatement import DoWhileStatement
from prompto.statement.FetchManyStatement import FetchManyStatement
from prompto.statement.FetchOneStatement import FetchOneStatement
from prompto.statement.FlushStatement import FlushStatement
from prompto.statement.ForEachStatement import ForEachStatement
from prompto.statement.IfStatement import IfElement, IfStatement, IfElementList
from prompto.statement.RaiseStatement import RaiseStatement
from prompto.statement.ReturnStatement import ReturnStatement
from prompto.statement.StatementList import StatementList
from prompto.statement.StoreStatement import StoreStatement
from prompto.statement.SwitchCase import SwitchCaseList
from prompto.statement.SwitchErrorStatement import SwitchErrorStatement
from prompto.statement.SwitchStatement import SwitchStatement
from prompto.statement.UnresolvedCall import UnresolvedCall
from prompto.statement.WhileStatement import WhileStatement
from prompto.statement.WithResourceStatement import WithResourceStatement
from prompto.statement.WithSingletonStatement import WithSingletonStatement
from prompto.statement.WriteStatement import WriteStatement
from prompto.type.AnyType import AnyType
from prompto.type.BlobType import BlobType
from prompto.type.BooleanType import BooleanType
from prompto.type.CategoryType import CategoryType
from prompto.type.CharacterType import CharacterType
from prompto.type.CodeType import CodeType
from prompto.type.CssType import CssType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.DictType import DictType
from prompto.type.DocumentType import DocumentType
from prompto.type.HtmlType import HtmlType
from prompto.type.IntegerType import IntegerType
from prompto.type.IteratorType import IteratorType
from prompto.type.ListType import ListType
from prompto.type.PeriodType import PeriodType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType

# need forward declaration
from prompto.type.UUIDType import UUIDType
from prompto.type.VersionType import VersionType

OCleverParser = None

class OPromptoBuilder(OParserListener):

    def __init__(self, parser:OCleverParser):
        self.input = parser.getTokenStream()
        self.path = parser.path
        self.nodeValues = dict()

    def getNodeValue(self, node:ParseTree):
        return self.nodeValues.get(node, None)

    def setNodeValue(self, node:ParseTree, value:object):
        self.nodeValues[node] = value
        if isinstance(value, Section):
            self.buildSection(node, value)

    def buildSection(self, node:ParserRuleContext, section:Section):
        first = self.findFirstValidToken(node.start.tokenIndex)
        last = self.findLastValidToken(node.stop.tokenIndex)
        section.setFrom(self.path, first, last, Dialect.O)

    def findFirstValidToken(self, idx:int):
        if idx==-1: # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx<len(self.input.tokens):
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx += 1
        return None

    def findLastValidToken(self, idx:int):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx >= 0:
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx -= 1
        return None

    def readValidToken(self, idx:int):
        token = self.input.tokens[idx]
        text = token.text
        if text is not None and len(text) > 0 and not text[0].isspace():
            return token
        else:
            return None
 

    def getHiddenTokensBefore(self, node):
        return self.getHiddenTokens(node, self.input.getHiddenTokensToLeft)


    def getHiddenTokensAfter(self, node):
        return self.getHiddenTokens(node, self.input.getHiddenTokensToRight)


    def getHiddenTokens(self, node, fetcher):
        token = node if isinstance(node, Token) else node.symbol
        hidden = fetcher(token.tokenIndex)
        if hidden is None or len(hidden) == 0:
            return None
        return "".join([token.text for token in hidden])


    def readAnnotations(self, contexts):
        return [ self.getNodeValue(ctx_) for ctx_ in contexts ]


    def readComments(self, contexts):
        return [ self.getNodeValue(ctx_) for ctx_ in contexts ]


    def exitTypeIdentifier(self, ctx:OParser.TypeIdentifierContext):
        name = self.getNodeValue(ctx.type_identifier())
        self.setNodeValue(ctx, UnresolvedIdentifier(name, Dialect.O))
    

    
    def exitMethod_expression(self, ctx:OParser.Method_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitAn_expression(self, ctx:OParser.An_expressionContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, typ)


    
    def exitBlob_expression(self, ctx:OParser.Blob_expressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, BlobExpression(exp))


    def exitBlobType(self, ctx:OParser.BlobTypeContext):
        self.setNodeValue(ctx, BlobType.instance)


    def exitBooleanLiteral(self, ctx:OParser.BooleanLiteralContext):
        self.setNodeValue(ctx, BooleanLiteral(ctx.getText()))
    

    
    def exitBreakStatement(self, ctx:OParser.BreakStatementContext):
        self.setNodeValue(ctx, BreakStatement())



    def exitMinIntegerLiteral(self, ctx:OParser.MinIntegerLiteralContext):
        self.setNodeValue(ctx, MinIntegerLiteral())
    

    
    def exitMaxIntegerLiteral(self, ctx:OParser.MaxIntegerLiteralContext):
        self.setNodeValue(ctx, MaxIntegerLiteral())
    

    
    def exitIntegerLiteral(self, ctx:OParser.IntegerLiteralContext):
        self.setNodeValue(ctx, IntegerLiteral(ctx.getText()))
    

    
    def exitDecimalLiteral(self, ctx:OParser.DecimalLiteralContext):
        self.setNodeValue(ctx, DecimalLiteral(ctx.getText()))
    

    
    def exitHexadecimalLiteral(self, ctx:OParser.HexadecimalLiteralContext):
        self.setNodeValue(ctx, HexaLiteral(ctx.getText()))
    

    
    def exitCharacterLiteral(self, ctx:OParser.CharacterLiteralContext):
        self.setNodeValue(ctx, CharacterLiteral(ctx.getText()))
    

    
    def exitDateLiteral(self, ctx:OParser.DateLiteralContext):
        self.setNodeValue(ctx, DateLiteral(ctx.getText()))
    

    
    def exitDateTimeLiteral(self, ctx:OParser.DateTimeLiteralContext):
        self.setNodeValue(ctx, DateTimeLiteral(ctx.getText()))
    


    def exitTernaryExpression(self, ctx:OParser.TernaryExpressionContext):
        condition = self.getNodeValue(ctx.test)
        ifTrue = self.getNodeValue(ctx.ifTrue)
        ifFalse = self.getNodeValue(ctx.ifFalse)
        exp = TernaryExpression(condition, ifTrue, ifFalse)
        self.setNodeValue(ctx, exp)

    
    def exitTest_method_declaration(self, ctx:OParser.Test_method_declarationContext):
        name = ctx.name.text
        stmts = self.getNodeValue(ctx.stmts)
        exps = self.getNodeValue(ctx.exps)
        errorName = self.getNodeValue(ctx.error)
        error = None if errorName is None else SymbolExpression(errorName)
        self.setNodeValue(ctx, TestMethodDeclaration(name, stmts, exps, error))



    def exitTextLiteral(self, ctx:OParser.TextLiteralContext):
        self.setNodeValue(ctx, TextLiteral(ctx.getText()))
    

    
    def exitTimeLiteral(self, ctx:OParser.TimeLiteralContext):
        self.setNodeValue(ctx, TimeLiteral(ctx.getText()))
    

    
    def exitPeriodLiteral(self, ctx:OParser.PeriodLiteralContext):
        self.setNodeValue(ctx, PeriodLiteral(ctx.getText()))



    def exitPeriodType(self, ctx: OParser.PeriodTypeContext):
        self.setNodeValue(ctx, PeriodType.instance)



    def exitVersionLiteral(self, ctx: OParser.VersionLiteralContext):
        self.setNodeValue(ctx, VersionLiteral(ctx.getText()))



    def exitVersionType(self, ctx: OParser.VersionTypeContext):
        self.setNodeValue(ctx, VersionType.instance)



    def exitAttribute_identifier(self, ctx:OParser.Attribute_identifierContext):
        self.setNodeValue(ctx, ctx.getText())



    def exitVariable_identifier(self, ctx:OParser.Variable_identifierContext):
        self.setNodeValue(ctx, ctx.getText())
    

    
    def exitList_literal(self, ctx:OParser.List_literalContext):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.expression_list())
        items = items if items is not None else []
        value = ListLiteral(items, mutable=mutable)
        self.setNodeValue(ctx, value)
    

    
    def exitDict_literal(self, ctx:OParser.Dict_literalContext):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.dict_entry_list())
        value = DictLiteral(mutable, items)
        self.setNodeValue(ctx, value)
    

    
    def exitTuple_literal(self, ctx:OParser.Tuple_literalContext):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.expression_tuple())
        items = items if items is not None else []
        value = TupleLiteral(mutable, items)
        self.setNodeValue(ctx, value)

    

    def exitSet_literal(self, ctx:OParser.Set_literalContext):
        items = self.getNodeValue(ctx.expression_list())
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    
    def exitRange_literal(self, ctx:OParser.Range_literalContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))
    


    def exitDict_entry(self, ctx:OParser.Dict_entryContext):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DictEntry(key, value)
        self.setNodeValue(ctx, entry)


    def exitDict_entry_list(self, ctx: OParser.Dict_entry_listContext):
        items = DictEntryList()
        for rule in ctx.dict_entry():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitDictKeyIdentifier(self, ctx:OParser.DictKeyIdentifierContext):
        name = ctx.name.getText()
        self.setNodeValue(ctx, DictIdentifierKey(name))


    def exitDictKeyText(self, ctx:OParser.DictKeyTextContext):
        name = ctx.name.text
        self.setNodeValue(ctx, DictTextKey(name))


    def exitLiteral_expression(self, ctx:OParser.Literal_expressionContext):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)



    def exitLiteralExpression(self, ctx:OParser.LiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    


    def exitIdentifierExpression(self, ctx:OParser.IdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitVariableIdentifier(self, ctx:OParser.VariableIdentifierContext):
        name = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, InstanceExpression(name))
    

    
    def exitSymbol_identifier(self, ctx:OParser.Symbol_identifierContext):
        self.setNodeValue(ctx, ctx.getText())
    

    
    def exitNative_symbol(self, ctx:OParser.Native_symbolContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NativeSymbol(name, exp))
    

    
    def exitSymbolIdentifier(self, ctx:OParser.SymbolIdentifierContext):
        name = self.getNodeValue(ctx.symbol_identifier())
        self.setNodeValue(ctx, SymbolExpression(name))
    

    
    def exitBooleanType(self, ctx:OParser.BooleanTypeContext):
        self.setNodeValue(ctx, BooleanType.instance)
    

    
    def exitCharacterType(self, ctx:OParser.CharacterTypeContext):
        self.setNodeValue(ctx, CharacterType.instance)
    

    
    def exitTextType(self, ctx:OParser.TextTypeContext):
        self.setNodeValue(ctx, TextType.instance)



    def exitHtmlType(self, ctx:OParser.HtmlTypeContext):
        self.setNodeValue(ctx, HtmlType.instance)



    def exitThisExpression(self, ctx:OParser.ThisExpressionContext):
        self.setNodeValue(ctx, ThisExpression())


    
    def exitIntegerType(self, ctx:OParser.IntegerTypeContext):
        self.setNodeValue(ctx, IntegerType.instance)
    

    
    def exitDecimalType(self, ctx:OParser.DecimalTypeContext):
        self.setNodeValue(ctx, DecimalType.instance)
    

    
    def exitDateType(self, ctx:OParser.DateTypeContext):
        self.setNodeValue(ctx, DateType.instance)
    

    
    def exitDateTimeType(self, ctx:OParser.DateTimeTypeContext):
        self.setNodeValue(ctx, DateTimeType.instance)
    

    
    def exitTimeType(self, ctx:OParser.TimeTypeContext):
        self.setNodeValue(ctx, TimeType.instance)
    

    
    def exitCodeType(self, ctx:OParser.CodeTypeContext):
        self.setNodeValue(ctx, CodeType.instance)
    

    def exitPrimaryType(self, ctx:OParser.PrimaryTypeContext):
        typ = self.getNodeValue(ctx.p)
        self.setNodeValue(ctx, typ)
    

    def exitAttribute_declaration(self, ctx:OParser.Attribute_declarationContext):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        match = self.getNodeValue(getattr(ctx, "match", None))
        indices = None if ctx.INDEX() is None else IdentifierList()
        if ctx.indices is not None:
            indices.extend(self.getNodeValue(ctx.indices))
        decl = AttributeDeclaration(name, typ, match, indices)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)
    

    def exitNativeType(self, ctx:OParser.NativeTypeContext):
        typ = self.getNodeValue(ctx.n)
        self.setNodeValue(ctx, typ)
    

    def exitCategoryType(self, ctx:OParser.CategoryTypeContext):
        typ = self.getNodeValue(ctx.c)
        self.setNodeValue(ctx, typ)
    

    def exitCategory_type(self, ctx:OParser.Category_typeContext):
        name = ctx.getText()
        self.setNodeValue(ctx, CategoryType(name))
    

    def exitListType(self, ctx:OParser.ListTypeContext):
        typ = self.getNodeValue(ctx.l)
        self.setNodeValue(ctx, ListType(typ))
    

    def exitDictType(self, ctx:OParser.DictTypeContext):
        typ = self.getNodeValue(ctx.d)
        self.setNodeValue(ctx, DictType(typ))
    

    
    def exitAttribute_identifier_list(self, ctx:OParser.Attribute_identifier_listContext):
        items = IdentifierList()
        for c in ctx.attribute_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitVariable_identifier_list(self, ctx:OParser.Variable_identifier_listContext):
        items = IdentifierList()
        for c in ctx.variable_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitDerivedList(self, ctx:OParser.DerivedListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))



    def exitDerivedListItem(self, ctx:OParser.DerivedListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)



    def exitConcrete_category_declaration(self, ctx:OParser.Concrete_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        derived = self.getNodeValue(ctx.derived)
        methods = self.getNodeValue(ctx.methods)
        ccd = ConcreteCategoryDeclaration(name)
        ccd.storable = ctx.STORABLE() is not None
        ccd.setAttributes(attrs)
        ccd.setDerivedFrom(derived)
        ccd.setMethods(methods)
        self.setNodeValue(ctx, ccd)



    def exitConcrete_widget_declaration(self, ctx:OParser.Concrete_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        derived = self.getNodeValue(ctx.derived)
        methods = self.getNodeValue(ctx.methods)
        ccd = ConcreteWidgetDeclaration(name, derived, methods)
        self.setNodeValue(ctx, ccd)



    def exitConcreteCategoryDeclaration(self, ctx:OParser.ConcreteCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitConcreteWidgetDeclaration(self, ctx:OParser.ConcreteWidgetDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitNativeWidgetDeclaration(self, ctx:OParser.NativeWidgetDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)



    def exitType_identifier(self, ctx:OParser.Type_identifierContext):
        self.setNodeValue(ctx, ctx.getText())



    def exitType_identifier_list(self, ctx:OParser.Type_identifier_listContext):
        items = IdentifierList()
        for rule in ctx.type_identifier():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitTypeLiteral(self, ctx:OParser.TypeLiteralContext):
        typ = self.getNodeValue(ctx.type_literal())
        self.setNodeValue(ctx, typ)


    def exitType_literal(self, ctx:OParser.Type_literalContext):
        typ = self.getNodeValue(ctx.category_or_any_type())
        self.setNodeValue(ctx, TypeLiteral(typ))



    def exitInstanceExpression(self, ctx:OParser.InstanceExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitSelectableExpression(self, ctx:OParser.SelectableExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        self.setNodeValue(ctx, parent)
    

    
    def exitSelectorExpression(self, ctx:OParser.SelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)
    

    
    def exitMemberSelector(self, ctx:OParser.MemberSelectorContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))



    def exitIsAnExpression(self, ctx:OParser.IsAnExpressionContext):
        left = self.getNodeValue(ctx.left)
        typ = self.getNodeValue(ctx.right)
        right = TypeExpression(typ)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS_A, right))



    def exitIsNotAnExpression(self, ctx:OParser.IsNotAnExpressionContext):
        left = self.getNodeValue(ctx.left)
        typ = self.getNodeValue(ctx.right)
        right = TypeExpression(typ)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS_NOT_A, right))



    def exitIsExpression(self, ctx:OParser.IsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS, right))



    def exitIsNotExpression(self, ctx:OParser.IsNotExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.IS_NOT, right))


    
    def exitItemSelector(self, ctx:OParser.ItemSelectorContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))
    

    
    def exitSliceSelector(self, ctx:OParser.SliceSelectorContext):
        slice = self.getNodeValue(ctx.xslice)
        self.setNodeValue(ctx, slice)
    

    def exitTyped_argument(self, ctx:OParser.Typed_argumentContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        exp = self.getNodeValue(ctx.value)
        arg = CategoryParameter(typ, name) if attrs is None else ExtendedParameter(typ, name, attrs)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitCodeArgument(self, ctx:OParser.CodeArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)
    

    def exitArgument_list(self, ctx:OParser.Argument_listContext):
        items = ParameterList()
        for rule in ctx.argument():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)
    

    def exitMethod_call_expression(self, ctx:OParser.Method_call_expressionContext):
        name = self.getNodeValue(ctx.name)
        caller = UnresolvedIdentifier(name, Dialect.O)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, UnresolvedCall(caller, args))



    def exitMethod_call_statement(self, ctx:OParser.Method_call_statementContext):
        parent = self.getNodeValue(ctx.parent)
        call = self.getNodeValue(ctx.method)
        call.setParent(parent)
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        if name is not None or stmts is not None:
            self.setNodeValue(ctx, RemoteCall(call.caller, call.arguments, name, stmts))
        else:
            self.setNodeValue(ctx, call)


    def exitMethod_declaration(self, ctx:OParser.Method_declarationContext):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)


    def exitMethod_identifier(self, ctx:OParser.Method_identifierContext):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitArgument_assignment(self, ctx:OParser.Argument_assignmentContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = UnresolvedParameter(name)
        self.setNodeValue(ctx, Argument(arg, exp))


    def exitExpressionAssignmentList(self, ctx:OParser.ExpressionAssignmentListContext):
        exp = self.getNodeValue(ctx.exp)
        items = ArgumentList()
        items.insert(0, Argument(None, exp))
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentList(self, ctx:OParser.ArgumentAssignmentListContext):
        item = self.getNodeValue(ctx.item)
        items = ArgumentList(items=[item])
        self.setNodeValue(ctx, items)
    

    def exitArgumentAssignmentListItem(self, ctx:OParser.ArgumentAssignmentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitArrow_prefix(self, ctx:OParser.Arrow_prefixContext):
        args = self.getNodeValue (ctx.arrow_args())
        argsSuite = self.getHiddenTokensBefore(ctx.EGT())
        arrowSuite = self.getHiddenTokensAfter(ctx.EGT())
        self.setNodeValue(ctx, ArrowExpression(args, argsSuite, arrowSuite))


    def exitArrowExpression(self, ctx:OParser.ArrowExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitArrowExpressionBody(self, ctx:OParser.ArrowExpressionBodyContext):
        arrow = self.getNodeValue(ctx.arrow_prefix())
        exp = self.getNodeValue(ctx.expression())
        arrow.setExpression(exp)
        self.setNodeValue(ctx, arrow)


    def exitArrowListArg(self, ctx:OParser.ArrowListArgContext):
        list = self.getNodeValue(ctx.variable_identifier_list())
        self.setNodeValue(ctx, list)


    def exitArrowSingleArg(self, ctx:OParser.ArrowSingleArgContext):
        arg = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, IdentifierList(arg))


    def exitArrowStatementsBody(self, ctx:OParser.ArrowStatementsBodyContext):
        arrow = self.getNodeValue(ctx.arrow_prefix())
        stmts = self.getNodeValue(ctx.statement_list())
        arrow.statements = stmts
        self.setNodeValue(ctx, arrow)


    def exitAddExpression(self, ctx:OParser.AddExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        exp = PlusExpression(left, right) if ctx.op.type == OParser.PLUS else SubtractExpression(left, right)
        self.setNodeValue(ctx, exp)



    def exitNative_member_method_declaration(self, ctx:OParser.Native_member_method_declarationContext):
        decl = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, decl)



    def exitNative_member_method_declaration_list(self, ctx:OParser.Native_member_method_declaration_listContext):
        items = MethodDeclarationList()
        for rule in ctx.native_member_method_declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitCurlyCategoryMethodList(self, ctx:OParser.CurlyCategoryMethodListContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitCurlyStatementList(self, ctx:OParser.CurlyStatementListContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)



    def exitMember_method_declaration_list(self, ctx:OParser.Member_method_declaration_listContext):
        items = MethodDeclarationList()
        for rule in ctx.member_method_declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitSetter_method_declaration(self, ctx:OParser.Setter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, SetterMethodDeclaration(name, stmts))
    

    def exitGetter_method_declaration(self, ctx:OParser.Getter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, GetterMethodDeclaration(name, stmts))
    

    def exitNative_setter_declaration(self, ctx:OParser.Native_setter_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeSetterMethodDeclaration(name, stmts))



    def exitNative_getter_declaration(self, ctx:OParser.Native_getter_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeGetterMethodDeclaration(name, stmts))

    def exitMember_method_declaration(self, ctx:OParser.Member_method_declarationContext):
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount()-1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)


    def exitStatement_list(self, ctx:OParser.Statement_listContext):
        items = StatementList()
        for rule in ctx.statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)

    
    def exitAbstract_method_declaration(self, ctx:OParser.Abstract_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, typ))
    

    
    def exitConcrete_method_declaration(self, ctx:OParser.Concrete_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ConcreteMethodDeclaration(name, args, typ, stmts))



    def exitSingleStatement(self, ctx:OParser.SingleStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, StatementList(stmt))



    def exitMethodCallStatement(self, ctx:OParser.MethodCallStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    def exitConstructorFrom(self, ctx: OParser.ConstructorFromContext):
        typ = self.getNodeValue(ctx.typ)
        copyFrom = self.getNodeValue(ctx.copyExp)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(typ, copyFrom, args, True))


    def exitConstructorNoFrom(self, ctx: OParser.ConstructorNoFromContext):
        typ = self.getNodeValue(ctx.typ)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(typ, None, args, True))


    def exitCopy_from(self, ctx:OParser.Copy_fromContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitAssertion(self, ctx:OParser.AssertionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAssertion_list(self, ctx:OParser.Assertion_listContext):
        items = []
        for rule in ctx.assertion():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitAssign_instance_statement(self, ctx:OParser.Assign_instance_statementContext):
        inst = self.getNodeValue(ctx.inst)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignInstanceStatement(inst, exp))
    

    
    def exitAssignInstanceStatement(self, ctx:OParser.AssignInstanceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    
    def exitAssign_variable_statement(self, ctx:OParser.Assign_variable_statementContext):
        name = self.getNodeValue(ctx.variable_identifier())
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, AssignVariableStatement(name, exp))



    def exitAssign_tuple_statement(self, ctx:OParser.Assign_tuple_statementContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmt = AssignTupleStatement(items)
        stmt.setExpression(exp)
        self.setNodeValue(ctx, stmt)



    def exitRootInstance(self, ctx:OParser.RootInstanceContext):
        name = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, VariableInstance(name))



    def exitRoughlyEqualsExpression(self, ctx:OParser.RoughlyEqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.ROUGHLY, right))



    def exitChildInstance(self, ctx:OParser.ChildInstanceContext):
        parent = self.getNodeValue(ctx.assignable_instance())
        child = self.getNodeValue(ctx.child_instance())
        child.setParent(parent)
        self.setNodeValue(ctx, child)



    def exitMemberInstance(self, ctx:OParser.MemberInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberInstance(None, name))



    def exitItemInstance(self, ctx:OParser.ItemInstanceContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemInstance(None, exp))



    def exitMethodExpression(self, ctx:OParser.MethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitMethodSelector(self, ctx:OParser.MethodSelectorContext):
        call = self.getNodeValue(ctx.method)
        if isinstance(call.caller, UnresolvedIdentifier):
            name = call.caller.name
            call.caller = UnresolvedSelector(name)
        self.setNodeValue(ctx, call)


    def exitNative_statement_list(self, ctx:OParser.Native_statement_listContext):
        items = StatementList()
        for rule in ctx.native_statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitJava_identifier(self, ctx:OParser.Java_identifierContext):
        self.setNodeValue(ctx, ctx.getText())



    def exitCSharpChildIdentifier(self, ctx:OParser.CSharpChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = CSharpIdentifierExpression(parent, name)
        self.setNodeValue(ctx, child)



    def exitCsharp_identifier(self, ctx:OParser.Csharp_identifierContext):
        self.setNodeValue(ctx, ctx.getText())

    def exitCsharp_method_expression(self, ctx:OParser.Csharp_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CSharpMethodExpression(name, args))

    def exitCSharpMethodExpression(self, ctx:OParser.CSharpMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitCSharpSelectorExpression(self, ctx:OParser.CSharpSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)

    def exitCSharpArgumentList(self,  ctx:OParser.CSharpArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CSharpExpressionList(item))

    def exitCSharpArgumentListItem(self, ctx:OParser.CSharpArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitPython_identifier(self, ctx:OParser.Python_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)

    def exitPythonNamedArgumentList(self, ctx:OParser.PythonNamedArgumentListContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonNamedArgumentList(PythonNamedArgument(name, exp)))

    def exitPythonNamedArgumentListItem(self, ctx:OParser.PythonNamedArgumentListItemContext):
        items = self.getNodeValue(ctx.items)
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        items.append(PythonNamedArgument(name, exp))
        self.setNodeValue(ctx, items)

    def exitPythonNamedOnlyArgumentList(self, ctx:OParser.PythonNamedOnlyArgumentListContext):
        items = self.getNodeValue(ctx.named)
        self.setNodeValue(ctx, items)

    def exitPythonOrdinalArgumentList(self, ctx:OParser.PythonOrdinalArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, PythonOrdinalArgumentList(item))

    def exitPythonOrdinalArgumentListItem(self, ctx:OParser.PythonOrdinalArgumentListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitPythonOrdinalOnlyArgumentList(self, ctx:OParser.PythonOrdinalOnlyArgumentListContext):
        ordinal = self.getNodeValue(ctx.ordinal)
        self.setNodeValue(ctx, ordinal)

    def exitPython_method_expression(self, ctx:OParser.Python_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, PythonMethodExpression(name, args))


    def exitPythonMethodExpression(self, ctx:OParser.PythonMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonGlobalMethodExpression(self, ctx:OParser.PythonGlobalMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonSelectorExpression(self, ctx:OParser.PythonSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitPythonSelfExpression(self, ctx: OParser.PythonSelfExpressionContext):
        self.setNodeValue(ctx, PythonSelfExpression())


    def exitCSharpIdentifier(self, ctx:OParser.CSharpIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))


    def exitPythonIdentifier(self, ctx:OParser.PythonIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, PythonIdentifierExpression(name))
    
    def exitPythonPromptoIdentifier(self, ctx:OParser.PythonPromptoIdentifierContext):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, PythonIdentifierExpression(name))

    def exitPythonPrimaryExpression(self, ctx:OParser.PythonPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIdentifierExpression(self, ctx:OParser.PythonIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitCsharp_primary_expression(self, ctx:OParser.Csharp_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)

    def exitCsharp_this_expression(self, ctx:OParser.Csharp_this_expressionContext):
        self.setNodeValue(ctx, CSharpThisExpression())

    def exitPythonChildIdentifier(self, ctx:OParser.PythonChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = PythonIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)
    

    def exitJavaIdentifier(self, ctx:OParser.JavaIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaIdentifierExpression(name))

    
    def exitJava_primary_expression(self, ctx:OParser.Java_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)

    def exitJavaChildIdentifier(self, ctx:OParser.JavaChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = JavaIdentifierExpression(name, parent=parent)
        self.setNodeValue(ctx, child)

    def exitJavaClassIdentifier(self, ctx:OParser.JavaClassIdentifierContext):
        klass = self.getNodeValue(ctx.klass)
        self.setNodeValue(ctx, klass)


    def exitJavaChildClassIdentifier(self, ctx:OParser.JavaChildClassIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        child = JavaIdentifierExpression(parent, ctx.name.getText())
        self.setNodeValue(ctx, child)


    def exitJavaPrimaryExpression(self, ctx:OParser.JavaPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    
    def exitJavaSelectorExpression(self, ctx:OParser.JavaSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitJava_item_expression(self, ctx:OParser.Java_item_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaItemExpression(exp))


    def exitJavaItemExpression(self, ctx:OParser.JavaItemExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaStatement(self, ctx:OParser.JavaStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, False))
    
    def exitJavaReturnStatement(self, ctx:OParser.JavaReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, True))

    def exitCSharpPromptoIdentifier(self, ctx:OParser.CSharpPromptoIdentifierContext):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))

    def exitCSharpPrimaryExpression(self, ctx:OParser.CSharpPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpStatement(self, ctx:OParser.CSharpStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, False))
    

    def exitPythonStatement(self, ctx:OParser.PythonStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, False))
    
    def exitPython_native_statement(self, ctx:OParser.Python_native_statementContext):
        stmt = self.getNodeValue(ctx.python_statement())
        module = self.getNodeValue(ctx.python_module())
        self.setNodeValue(ctx, PythonNativeCall(stmt, module))

    def exitPython_module(self, ctx:OParser.Python_moduleContext):
        ids = [c.getText() for c in ctx.python_identifier()]
        module = PythonModule(ids)
        self.setNodeValue(ctx, module)

    def exitCSharpReturnStatement(self, ctx:OParser.CSharpReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, True))


    def exitPythonReturnStatement(self, ctx:OParser.PythonReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, True))


    def exitJavaNativeStatement(self, ctx:OParser.JavaNativeStatementContext):
        stmt = self.getNodeValue(ctx.java_statement())
        self.setNodeValue(ctx, JavaNativeCall(stmt))


    def exitCSharpNativeStatement(self, ctx:OParser.CSharpNativeStatementContext):
        stmt = self.getNodeValue(ctx.csharp_statement())
        self.setNodeValue(ctx, CSharpNativeCall(stmt))


    def exitPython2NativeStatement(self, ctx:OParser.Python2NativeStatementContext):
        call = self.getNodeValue(ctx.python_native_statement())
        self.setNodeValue(ctx, Python2NativeCall(call.statement, call.module))


    def exitPython3NativeStatement(self, ctx:OParser.Python3NativeStatementContext):
        call = self.getNodeValue(ctx.python_native_statement())
        self.setNodeValue(ctx, Python3NativeCall(call.statement, call.module))
    

    def exitNative_method_declaration(self, ctx:OParser.Native_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeMethodDeclaration(name, args, typ, stmts))

    
    def exitJavaArgumentList(self, ctx:OParser.JavaArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, JavaExpressionList(item))
    

    
    def exitJavaArgumentListItem(self, ctx:OParser.JavaArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitJava_method_expression(self, ctx:OParser.Java_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, JavaMethodExpression(name, args))
    

    
    def exitJavaMethodExpression(self, ctx:OParser.JavaMethodExpressionContext):
        exp = self.getNodeValue(ctx.java_method_expression())
        self.setNodeValue(ctx, exp)



    def exitFlush_statement(self, ctx: OParser.Flush_statementContext):
        self.setNodeValue(ctx, FlushStatement())



    def exitFlushStatement(self, ctx: OParser.FlushStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))



    def exitFullDeclarationList(self, ctx:OParser.FullDeclarationListContext):
        items = self.getNodeValue(ctx.declarations())
        if items is None:
            items = DeclarationList()
        self.setNodeValue(ctx, items)
    

    def exitDeclaration(self, ctx:OParser.DeclarationContext):
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount()-1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)



    def exitDeclarations(self, ctx: OParser.DeclarationsContext):
        items = DeclarationList()
        for rule in ctx.declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitJavaBooleanLiteral(self, ctx:OParser.JavaBooleanLiteralContext):
        self.setNodeValue(ctx, JavaBooleanLiteral(ctx.getText()))
    

    
    def exitJavaIntegerLiteral(self, ctx:OParser.JavaIntegerLiteralContext):
        self.setNodeValue(ctx, JavaIntegerLiteral(ctx.getText()))
    

    
    def exitJavaDecimalLiteral(self, ctx:OParser.JavaDecimalLiteralContext):
        self.setNodeValue(ctx, JavaDecimalLiteral(ctx.getText()))
    

    
    def exitJavaCharacterLiteral(self, ctx:OParser.JavaCharacterLiteralContext):
        self.setNodeValue(ctx, JavaCharacterLiteral(ctx.getText()))
    

    
    def exitJavaTextLiteral(self, ctx:OParser.JavaTextLiteralContext):
        self.setNodeValue(ctx, JavaTextLiteral(ctx.getText()))
    

    
    def exitCSharpBooleanLiteral(self, ctx:OParser.CSharpBooleanLiteralContext):
        self.setNodeValue(ctx, CSharpBooleanLiteral(ctx.getText()))
    

    
    def exitCSharpIntegerLiteral(self, ctx:OParser.CSharpIntegerLiteralContext):
        self.setNodeValue(ctx, CSharpIntegerLiteral(ctx.getText()))
    

    
    def exitCSharpDecimalLiteral(self, ctx:OParser.CSharpDecimalLiteralContext):
        self.setNodeValue(ctx, CSharpDecimalLiteral(ctx.getText()))
    

    
    def exitCSharpCharacterLiteral(self, ctx:OParser.CSharpCharacterLiteralContext):
        self.setNodeValue(ctx, CSharpCharacterLiteral(ctx.getText()))
    

    
    def exitCSharpTextLiteral(self, ctx:OParser.CSharpTextLiteralContext):
        self.setNodeValue(ctx, CSharpTextLiteral(ctx.getText()))
    

    
    def exitPythonBooleanLiteral(self, ctx:OParser.PythonBooleanLiteralContext):
        self.setNodeValue(ctx, PythonBooleanLiteral(ctx.getText()))
    

    def exitPythonCharacterLiteral(self, ctx:OParser.PythonCharacterLiteralContext):
        self.setNodeValue(ctx, PythonCharacterLiteral(ctx.getText()))


    def exitPythonIntegerLiteral(self, ctx:OParser.PythonIntegerLiteralContext):
        self.setNodeValue(ctx, PythonIntegerLiteral(ctx.getText()))
    

    
    def exitPythonDecimalLiteral(self, ctx:OParser.PythonDecimalLiteralContext):
        self.setNodeValue(ctx, PythonDecimalLiteral(ctx.getText()))
    

    
    def exitPythonTextLiteral(self, ctx:OParser.PythonTextLiteralContext):
        self.setNodeValue(ctx, PythonTextLiteral(ctx.getText()))
    


    def exitJava_this_expression(self, ctx:OParser.Java_this_expressionContext):
        self.setNodeValue(ctx, JavaThisExpression())



    def exitPythonLiteralExpression(self, ctx:OParser.PythonLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)



    def exitJavaCategoryBinding(self, ctx:OParser.JavaCategoryBindingContext):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, JavaNativeCategoryBinding(binding))
    

    
    def exitCSharpCategoryBinding(self, ctx:OParser.CSharpCategoryBindingContext):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, CSharpNativeCategoryBinding(binding))
    


    def exitPython_category_binding(self, ctx:OParser.Python_category_bindingContext):
        id_ = ctx.identifier().getText()
        module = self.getNodeValue(ctx.python_module())
        self.setNodeValue(ctx, PythonNativeCategoryBinding(id_, module))



    def exitPython2CategoryBinding(self, ctx:OParser.Python2CategoryBindingContext):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python2NativeCategoryBinding(binding.identifier, binding.module))
    

    
    def exitPython3CategoryBinding(self, ctx:OParser.Python3CategoryBindingContext):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python3NativeCategoryBinding(binding.identifier, binding.module))
    

    
    def exitNativeCategoryBindingList(self, ctx:OParser.NativeCategoryBindingListContext):
        item = self.getNodeValue(ctx.item)
        items = NativeCategoryBindingList(item)
        self.setNodeValue(ctx, items)
    

    
    def exitNativeCategoryBindingListItem(self, ctx:OParser.NativeCategoryBindingListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitNative_category_bindings(self, ctx:OParser.Native_category_bindingsContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)
    

    
    def exitNative_category_declaration(self, ctx:OParser.Native_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeCategoryDeclaration(name, attrs, bindings, None, methods)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)
    


    def exitNative_widget_declaration(self, ctx:OParser.Native_widget_declarationContext):
        name = self.getNodeValue(ctx.name)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeWidgetDeclaration(name, bindings, methods)
        self.setNodeValue(ctx, decl)



    def exitNativeCategoryDeclaration(self, ctx:OParser.NativeCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitNative_resource_declaration(self, ctx:OParser.Native_resource_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeResourceDeclaration(name, attrs, bindings, None, methods)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)
    

    
    def exitResource_declaration(self, ctx:OParser.Resource_declarationContext):
        decl = self.getNodeValue(ctx.native_resource_declaration())
        self.setNodeValue(ctx, decl)
    


    def exitParenthesis_expression(self, ctx:OParser.Parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, ParenthesisExpression(exp))
    

    
    def exitParenthesisExpression(self, ctx:OParser.ParenthesisExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitNative_symbol_list(self, ctx:OParser.Native_symbol_listContext):
        items = NativeSymbolList()
        for rule in ctx.native_symbol():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitEnum_native_declaration(self, ctx:OParser.Enum_native_declarationContext):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        symbols = self.getNodeValue(ctx.symbols)
        self.setNodeValue(ctx, EnumeratedNativeDeclaration(name, typ, symbols))
    

    
    def exitFor_each_statement(self, ctx:OParser.For_each_statementContext):
        name1 = self.getNodeValue(ctx.name1)
        name2 = self.getNodeValue(ctx.name2)
        source = self.getNodeValue(ctx.source)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ForEachStatement(name1, name2, source, stmts))
    

    
    def exitForEachStatement(self, ctx:OParser.ForEachStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitSymbols_token(self, ctx:OParser.Symbols_tokenContext):
        self.setNodeValue(ctx, ctx.getText())
    

    
    def exitKey_token(self, ctx:OParser.Key_tokenContext):
        self.setNodeValue(ctx, ctx.getText())
    


    def exitUUIDType(self, ctx:OParser.UUIDTypeContext):
        self.setNodeValue(ctx, UUIDType.instance)



    def exitUUIDLiteral(self, ctx:OParser.UUIDLiteralContext):
        self.setNodeValue(ctx, UUIDLiteral(ctx.getText()))


    
    def exitValue_token(self, ctx:OParser.Value_tokenContext):
        self.setNodeValue(ctx, ctx.getText())
    

    
    def exitNamed_argument(self, ctx:OParser.Named_argumentContext):
        name = self.getNodeValue(ctx.variable_identifier())
        arg = UnresolvedParameter(name)
        exp = self.getNodeValue(ctx.literal_expression())
        arg.defaultValue = exp
        self.setNodeValue(ctx, arg)
    

    
    def exitClosureStatement(self, ctx:OParser.ClosureStatementContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, DeclarationStatement(decl))
    

    
    def exitReturn_statement(self, ctx:OParser.Return_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ReturnStatement(exp))
    

    
    def exitReturnStatement(self, ctx:OParser.ReturnStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitClosureExpression(self, ctx:OParser.ClosureExpressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodExpression(name))
    

    
    def exitIf_statement(self, ctx:OParser.If_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elseIfs = self.getNodeValue(ctx.elseIfs)
        elseStmts = self.getNodeValue(ctx.elseStmts)
        stmt = IfStatement(exp, stmts)
        if elseIfs is not None:
            stmt.addAdditionals(elseIfs)
        if elseStmts is not None:
            stmt.setFinal(elseStmts)
        self.setNodeValue(ctx, stmt)
    

    
    def exitElseIfStatementList(self, ctx:OParser.ElseIfStatementListContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        self.setNodeValue(ctx, IfElementList(elem))
    

    
    def exitElseIfStatementListItem(self, ctx:OParser.ElseIfStatementListItemContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        items.add(elem)
        self.setNodeValue(ctx, items)
    

    
    def exitIfStatement(self, ctx:OParser.IfStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitSwitchStatement(self, ctx:OParser.SwitchStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitAssignTupleStatement(self, ctx:OParser.AssignTupleStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitRaiseStatement(self, ctx:OParser.RaiseStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitWriteStatement(self, ctx:OParser.WriteStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitWithResourceStatement(self, ctx:OParser.WithResourceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitWhileStatement(self, ctx:OParser.WhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitDoWhileStatement(self, ctx:OParser.DoWhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitTryStatement(self, ctx:OParser.TryStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    
    def exitEqualsExpression(self, ctx:OParser.EqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.EQUALS, right))
    

    
    def exitNotEqualsExpression(self, ctx:OParser.NotEqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.NOT_EQUALS, right))
    

    
    def exitGreaterThanExpression(self, ctx:OParser.GreaterThanExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GT, right))
    

    
    def exitGreaterThanOrEqualExpression(self, ctx:OParser.GreaterThanOrEqualExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GTE, right))
    

    
    def exitLessThanExpression(self, ctx:OParser.LessThanExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LT, right))
    

    
    def exitLessThanOrEqualExpression(self, ctx:OParser.LessThanOrEqualExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LTE, right))
    

    
    def exitAtomicSwitchCase(self, ctx:OParser.AtomicSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(exp, stmts))
    

    
    def exitCollection_literal(self, ctx:OParser.Collection_literalContext):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)



    def exitCollectionSwitchCase(self, ctx:OParser.CollectionSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))
    

    def exitCommentStatement(self, ctx:OParser.CommentStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.comment_statement()))


    def exitComment_statement(self, ctx:OParser.Comment_statementContext):
        self.setNodeValue(ctx, CommentStatement(ctx.getText()))



    def exitCursorType(self, ctx: OParser.CursorTypeContext):
        raise Exception("not implemented")



    def exitSwitch_case_statement_list(self, ctx:OParser.Switch_case_statement_listContext):
        items = SwitchCaseList()
        for rule in ctx.switch_case_statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitSwitch_statement(self, ctx:OParser.Switch_statementContext):
        exp = self.getNodeValue(ctx.exp)
        cases = self.getNodeValue(ctx.cases)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = SwitchStatement(exp)
        stmt.setSwitchCases(cases)
        stmt.setDefaultCase(stmts)
        self.setNodeValue(ctx, stmt)
    

    
    def exitLiteralRangeLiteral(self, ctx:OParser.LiteralRangeLiteralContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))
    


    def exitLiteralSetLiteral(self, ctx:OParser.LiteralSetLiteralContext):
        items = self.getNodeValue(ctx.literal_list_literal())
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)



    def exitLiteralListLiteral(self, ctx:OParser.LiteralListLiteralContext):
        items = self.getNodeValue(ctx.literal_list_literal())
        items = items if items is not None else []
        value = ListLiteral(items)
        self.setNodeValue(ctx, value)



    def exitLiteral_list_literal(self, ctx:OParser.Literal_list_literalContext):
        items = []
        for rule in ctx.atomic_literal():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitInExpression(self, ctx:OParser.InExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.IN, right))
    

    def exitNotInExpression(self, ctx:OParser.NotInExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_IN, right))


    def exitCssType(self, ctx:OParser.CssTypeContext):
        self.setNodeValue(ctx, CssType.instance)


    def exitHasExpression(self, ctx: OParser.HasExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.HAS, right))


    def exitNotHasExpression(self, ctx: OParser.NotHasExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_HAS, right))


    def exitHasAllExpression(self, ctx: OParser.HasAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.HAS_ALL, right))


    def exitNotHasAllExpression(self, ctx: OParser.NotHasAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_HAS_ALL, right))


    def exitHasAnyExpression(self, ctx: OParser.HasAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.HAS_ANY, right))



    def exitNotHasAnyExpression(self, ctx: OParser.NotHasAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_HAS_ANY, right))


    def exitContainsExpression(self, ctx: OParser.ContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.CONTAINS, right))


    def exitNotContainsExpression(self, ctx: OParser.NotContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.NOT_CONTAINS, right))


    def exitDivideExpression(self, ctx:OParser.DivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, DivideExpression(left, right))
    

    def exitIntDivideExpression(self, ctx:OParser.IntDivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, IntDivideExpression(left, right))
    

    def exitModuloExpression(self, ctx:OParser.ModuloExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ModuloExpression(left, right))


    def exitAnnotation_constructor(self, ctx:OParser.Annotation_constructorContext):
        name = self.getNodeValue(ctx.name)
        args = DictEntryList()
        exp = self.getNodeValue(ctx.exp)
        if exp is not None:
            args.append(DictEntry(None, exp))
        for argCtx in ctx.annotation_argument():
            arg = self.getNodeValue(argCtx)
            args.append(arg)
        self.setNodeValue(ctx, Annotation(name, args))


    def exitAnnotation_argument(self, ctx:OParser.Annotation_argumentContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, DictEntry(name, exp))


    def exitAnnotation_identifier(self, ctx:OParser.Annotation_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitAnnotation_argument_name(self, ctx:OParser.Annotation_argument_nameContext):
       self.setNodeValue(ctx, ctx.getText())


    def exitAnnotationLiteralValue(self, ctx:OParser.AnnotationLiteralValueContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAnnotationTypeValue(self, ctx:OParser.AnnotationTypeValueContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, TypeExpression(typ))


    def exitAndExpression(self, ctx:OParser.AndExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, AndExpression(left, right))
    

    def exitNullLiteral(self, ctx:OParser.NullLiteralContext):
        self.setNodeValue(ctx, NullLiteral.instance)



    def exitOperator_argument(self, ctx:OParser.Operator_argumentContext):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)



    def exitOperatorArgument(self, ctx:OParser.OperatorArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        arg.mutable = ctx.MUTABLE() is not None
        self.setNodeValue(ctx, arg)


    def exitOperatorPlus(self, ctx:OParser.OperatorPlusContext):
        self.setNodeValue(ctx, Operator.PLUS)


    def exitOperatorMinus(self, ctx:OParser.OperatorMinusContext):
        self.setNodeValue(ctx, Operator.MINUS)


    def exitOperatorMultiply(self, ctx:OParser.OperatorMultiplyContext):
        self.setNodeValue(ctx, Operator.MULTIPLY)


    def exitOperatorDivide(self, ctx:OParser.OperatorDivideContext):
        self.setNodeValue(ctx, Operator.DIVIDE)


    def exitOperatorIDivide(self, ctx:OParser.OperatorIDivideContext):
        self.setNodeValue(ctx, Operator.IDIVIDE)


    def exitOperatorModulo(self, ctx:OParser.OperatorModuloContext):
        self.setNodeValue(ctx, Operator.MODULO)


    def exitOperator_method_declaration(self, ctx:OParser.Operator_method_declarationContext):
        op = self.getNodeValue(ctx.op)
        arg = self.getNodeValue(ctx.arg)
        typ = self.getNodeValue(ctx.typ)
        stmts = self.getNodeValue(ctx.stmts)
        decl = OperatorMethodDeclaration(op, arg, typ, stmts)
        self.setNodeValue(ctx, decl)


    def exitOrder_by(self, ctx:OParser.Order_byContext):
        names = IdentifierList()
        for ctx_ in ctx.variable_identifier():
            names.append(self.getNodeValue(ctx_))
        clause = OrderByClause(names, ctx.DESC() is not None)
        self.setNodeValue(ctx, clause)


    def exitOrder_by_list(self, ctx:OParser.Order_by_listContext):
        list_ = OrderByClauseList()
        for ctx_ in ctx.order_by():
            list_.append(self.getNodeValue(ctx_))
        self.setNodeValue(ctx, list_)


    def exitOrExpression(self, ctx:OParser.OrExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, OrExpression(left, right))
    

    
    def exitMultiplyExpression(self, ctx:OParser.MultiplyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, MultiplyExpression(left, right))
    

    def exitMutable_category_type(self, ctx):
        typ = self.getNodeValue(ctx.category_type())
        typ.mutable = ctx.MUTABLE() is not None
        self.setNodeValue(ctx, typ)


    def exitMutableInstanceExpression(self, ctx:OParser.MutableInstanceExpressionContext):
        source = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MutableExpression(source))


    def exitMutableSelectableExpression(self, ctx:OParser.MutableSelectableExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitMutableSelectorExpression(self, ctx:OParser.MutableSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.parent = parent
        self.setNodeValue(ctx, selector)


    def exitMinusExpression(self, ctx:OParser.MinusExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MinusExpression(exp))
    

    
    def exitNotExpression(self, ctx:OParser.NotExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NotExpression(exp))
    

    
    def exitWhile_statement(self, ctx:OParser.While_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WhileStatement(exp, stmts))
    

    
    def exitDo_while_statement(self, ctx:OParser.Do_while_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, DoWhileStatement(exp, stmts))
    

    def exitSingleton_category_declaration(self, ctx:OParser.Singleton_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        methods = self.getNodeValue(ctx.methods)
        self.setNodeValue(ctx, SingletonCategoryDeclaration(name, attrs, methods))

    def exitSingletonCategoryDeclaration(self, ctx:OParser.SingletonCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitSliceFirstAndLast(self, ctx:OParser.SliceFirstAndLastContext):
        first = self.getNodeValue(ctx.first)
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(first, last))
    

    
    def exitSliceFirstOnly(self, ctx:OParser.SliceFirstOnlyContext):
        first = self.getNodeValue(ctx.first)
        self.setNodeValue(ctx, SliceSelector(first, None))
    

    
    def exitSliceLastOnly(self, ctx:OParser.SliceLastOnlyContext):
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(None, last))
    

    def exitStoreStatement (self, ctx:OParser.StoreStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitStore_statement (self, ctx:OParser.Store_statementContext):
        to_del = self.getNodeValue(ctx.to_del)
        to_add = self.getNodeValue(ctx.to_add)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = StoreStatement(to_del, to_add, stmts)
        self.setNodeValue(ctx, stmt)


    def exitSorted_expression(self, ctx:OParser.Sorted_expressionContext):
        source = self.getNodeValue(ctx.source)
        desc = ctx.DESC() is not None
        key = self.getNodeValue(ctx.key)
        self.setNodeValue(ctx, SortedExpression(source, desc, key))


    def exitSorted_key(self, ctx:OParser.Sorted_keyContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitDocument_expression(self, ctx:OParser.Document_expressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, DocumentExpression(exp))
    

    
    def exitDocumentType(self, ctx:OParser.DocumentTypeContext):
        self.setNodeValue(ctx, DocumentType.instance)



    def exitDocument_literal(self, ctx:OParser.Document_literalContext):
        entries = self.getNodeValue(ctx.dict_entry_list())
        items = DocEntryList(entries=entries)
        self.setNodeValue(ctx, DocumentLiteral(items))


    def exitFetchStatement(self, ctx:OParser.FetchStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitFetchMany (self, ctx:OParser.FetchManyContext):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        orderBy = self.getNodeValue(ctx.orderby)
        self.setNodeValue(ctx, FetchManyExpression(category, predicate, start, stop, orderBy))


    def exitFetchManyAsync(self, ctx:OParser.FetchManyAsyncContext):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        orderBy = self.getNodeValue(ctx.orderby)
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, FetchManyStatement(category, predicate, start, stop, orderBy, name, stmts))


    def exitFetchOne (self, ctx:OParser.FetchOneContext):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        self.setNodeValue(ctx, FetchOneExpression(category, predicate))


    def exitFetchOneAsync(self, ctx:OParser.FetchOneAsyncContext):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, FetchOneStatement(category, predicate, name, stmts))


    def exitFiltered_list_expression(self, ctx:OParser.Filtered_list_expressionContext):
        itemName = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        predicate = self.getNodeValue(ctx.predicate)
        self.setNodeValue(ctx, FilteredExpression(itemName, source, predicate))



    def exitClosure_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodExpression(name))


    def exitCode_type(self, ctx:OParser.Code_typeContext):
        self.setNodeValue(ctx, CodeType.instance)
    

    
    def exitExecuteExpression(self, ctx:OParser.ExecuteExpressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, ExecuteExpression(name))



    def exitExpression_list(self, ctx: OParser.expression_list):
        items = []
        for rule in ctx.expression():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitExpression_tuple(self, ctx: OParser.expression_tuple):
        items = []
        for rule in ctx.expression():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitCodeExpression(self, ctx:OParser.CodeExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CodeExpression(exp))
    

    
    def exitCode_argument(self, ctx:OParser.Code_argumentContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CodeParameter(name))



    def exitCategory_or_any_type(self, ctx:OParser.Category_or_any_typeContext):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)



    def exitCategory_symbol(self, ctx:OParser.Category_symbolContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CategorySymbol(name, args))



    def exitCategory_symbol_list(self, ctx:OParser.Category_symbol_listContext):
        items = CategorySymbolList()
        for rule in ctx.category_symbol():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    
    def exitEnum_category_declaration(self, ctx:OParser.Enum_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        parent = self.getNodeValue(ctx.derived)
        derived = None if parent is None else IdentifierList(parent)
        symbols = self.getNodeValue(ctx.symbols)
        ecd = EnumeratedCategoryDeclaration(name)
        ecd.setAttributes(attrs)
        ecd.setDerivedFrom(derived)
        ecd.setSymbols(symbols)
        self.setNodeValue(ctx, ecd)



    def exitEnum_declaration(self, ctx: OParser.Enum_declarationContext):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)



    def exitRead_all_expression(self, ctx:OParser.Read_all_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadAllExpression(source))



    def exitRead_one_expression(self, ctx: OParser.Read_one_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadOneExpression(source))



    def exitWrite_statement(self, ctx:OParser.Write_statementContext):
        what = self.getNodeValue(ctx.what)
        target = self.getNodeValue(ctx.target)
        self.setNodeValue(ctx, WriteStatement(what, target))
    


    def exitWith_singleton_statement(self, ctx:OParser.With_singleton_statementContext):
        name = self.getNodeValue(ctx.typ)
        typ = CategoryType(name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithSingletonStatement(typ, stmts))



    def exitWithSingletonStatement(self, ctx:OParser.WithSingletonStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_resource_statement(self, ctx:OParser.With_resource_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithResourceStatement(stmt, stmts))
    

    
    def exitAnyType(self, ctx:OParser.AnyTypeContext):
        self.setNodeValue(ctx, AnyType.instance)
    

    
    def exitAnyListType(self, ctx:OParser.AnyListTypeContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, ListType(typ))
    

    
    def exitAnyDictType(self, ctx:OParser.AnyDictTypeContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, DictType(typ))
    


    def exitCastExpression(self, ctx:OParser.CastExpressionContext):
        typ = self.getNodeValue(ctx.right)
        exp = self.getNodeValue(ctx.left)
        self.setNodeValue(ctx, CastExpression(exp, typ))



    def exitCatchAtomicStatement(self, ctx:OParser.CatchAtomicStatementContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(SymbolExpression(name), stmts))
    

    
    def exitCatchCollectionStatement(self, ctx:OParser.CatchCollectionStatementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))
    

    
    def exitCatch_statement_list(self, ctx:OParser.Catch_statement_listContext):
        items = SwitchCaseList()
        for rule in ctx.catch_statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitTry_statement(self, ctx:OParser.Try_statementContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        handlers = self.getNodeValue(ctx.handlers)
        anyStmts = self.getNodeValue(ctx.anyStmts)
        finalStmts = self.getNodeValue(ctx.finalStmts)
        stmt = SwitchErrorStatement(name, stmts)
        stmt.setSwitchCases(handlers)
        stmt.setDefaultCase(anyStmts)
        stmt.setAlwaysInstructions(finalStmts)
        self.setNodeValue(ctx, stmt)
    

    
    def exitRaise_statement(self, ctx:OParser.Raise_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, RaiseStatement(exp))



    def exitMatchingList(self, ctx:OParser.MatchingListContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingSet(self, ctx:OParser.MatchingSetContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingRange(self, ctx:OParser.MatchingRangeContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))



    def exitMatchingExpression(self, ctx:OParser.MatchingExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MatchingExpressionConstraint(exp))


    def exitMatchingPattern(self, ctx:OParser.MatchingPatternContext):
        self.setNodeValue(ctx, MatchingPatternConstraint(TextLiteral(ctx.text.text)))


    def exitIteratorExpression(self, ctx:OParser.IteratorExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        name = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, IteratorExpression(name, source, exp))


    def exitIteratorType(self, ctx:OParser.IteratorTypeContext):
        typ = self.getNodeValue(ctx.i)
        self.setNodeValue(ctx, IteratorType(typ))


    def exitJavascriptBooleanLiteral(self, ctx:OParser.JavascriptBooleanLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptBooleanLiteral(text))


    def exitJavascript_category_binding(self, ctx:OParser.Javascript_category_bindingContext):
        identifier = ".".join([cx.getText() for cx in ctx.javascript_identifier()])
        module = self.getNodeValue(ctx.javascript_module())
        map = JavaScriptNativeCategoryBinding(identifier, module)
        self.setNodeValue(ctx, map)

    def exitJavascriptCharacterLiteral(self, ctx:OParser.JavascriptCharacterLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptCharacterLiteral(text))


    def exitJavascript_identifier(self, ctx:OParser.Javascript_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJavascript_this_expression(self, ctx:OParser.Javascript_this_expressionContext):
        self.setNodeValue(ctx, JavaScriptThisExpression())


    def exitJavascript_method_expression(self, ctx:OParser.Javascript_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        method = JavaScriptMethodExpression(name)
        args = self.getNodeValue(ctx.args)
        method.arguments = args
        self.setNodeValue(ctx, method)


    def exitJavascript_module(self, ctx:OParser.Javascript_moduleContext):
        ids = []
        for ic in ctx.javascript_identifier():
            ids.append(ic.getText())
        module = JavaScriptModule(ids)
        self.setNodeValue(ctx, module)


    def exitJavascript_native_statement(self, ctx:OParser.Javascript_native_statementContext):
        stmt = self.getNodeValue(ctx.javascript_statement())
        module = self.getNodeValue(ctx.javascript_module())
        stmt.module = module
        self.setNodeValue(ctx, stmt)


    def exitJavascript_new_expression(self, ctx:OParser.Javascript_new_expressionContext):
        method = self.getNodeValue(ctx.javascript_method_expression())
        new = JavaScriptNewExpression(method)
        self.setNodeValue(ctx, new)


    def exitJavascriptArgumentList(self, ctx:OParser.JavascriptArgumentListContext):
        exp = self.getNodeValue(ctx.item)
        list = JavaScriptExpressionList(exp)
        self.setNodeValue(ctx, list)

    def exitJavascriptArgumentListItem(self, ctx:OParser.JavascriptArgumentListItemContext):
        exp = self.getNodeValue(ctx.item)
        list = self.getNodeValue(ctx.items)
        list.append(exp)
        self.setNodeValue(ctx, list)

    def exitJavaScriptCategoryBinding(self, ctx:OParser.JavaScriptCategoryBindingContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.binding))


    def exitJavascript_identifier_expression(self, ctx:OParser.Javascript_identifier_expressionContext):
        name = self.getNodeValue(ctx.name)
        exp = JavaScriptIdentifierExpression(None, name)
        self.setNodeValue(ctx, exp)


    def exitJavascriptDecimalLiteral(self, ctx:OParser.JavascriptDecimalLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptDecimalLiteral(text))

    def exitJavascriptIntegerLiteral(self, ctx:OParser.JavascriptIntegerLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptIntegerLiteral(text))


    def exitJavaScriptMethodExpression(self, ctx:OParser.JavaScriptMethodExpressionContext):
        method = self.getNodeValue(ctx.method)
        self.setNodeValue(ctx, method)


    def exitJavaScriptNativeStatement(self, ctx:OParser.JavaScriptNativeStatementContext):
        stmt = self.getNodeValue(ctx.javascript_native_statement())
        self.setNodeValue(ctx, JavaScriptNativeCall(stmt))

    def exitJavascriptPrimaryExpression(self, ctx:OParser.JavascriptPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitJavascriptReturnStatement(self, ctx:OParser.JavascriptReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, True))

    def exitJavascriptSelectorExpression(self, ctx:OParser.JavascriptSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)

    def exitJavaScriptMemberExpression(self, ctx:OParser.JavaScriptMemberExpressionContext):
        name = ctx.name.getText()
        self.setNodeValue(ctx, JavaScriptMemberExpression(name))

    def exitJavascript_primary_expression(self, ctx:OParser.Java_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitJavascriptStatement(self, ctx:OParser.JavascriptStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, False))


    def exitJavascriptTextLiteral(self, ctx:OParser.JavascriptTextLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptTextLiteral(text))


    def exitJsxChild(self, ctx: OParser.JsxChildContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.jsx))


    def exitJsxCode(self, ctx: OParser.JsxCodeContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JsxCode(exp))


    def exitJsxExpression(self, ctx: OParser.JsxExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitJsxElement(self, ctx: OParser.JsxElementContext):
        elem = self.getNodeValue(ctx.opening)
        closing = self.getNodeValue(ctx.closing)
        elem.setClosing(closing)
        children = self.getNodeValue(ctx.children_)
        elem.setChildren(children)
        self.setNodeValue(ctx, elem)


    def exitJsxSelfClosing(self, ctx: OParser.JsxSelfClosingContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.jsx))


    def exitJsxText(self, ctx: OParser.JsxTextContext):
        text = ParserUtils.getFullText(ctx.text)
        self.setNodeValue(ctx, JsxText(text))


    def exitJsxValue(self, ctx: OParser.JsxValueContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JsxExpression(exp))


    def exitJsx_attribute(self, ctx: OParser.Jsx_attributeContext):
        name = self.getNodeValue(ctx.name)
        value = self.getNodeValue(ctx.value)
        stop = ctx.value.stop if value is not None else ctx.name.stop
        suite = None if value is None else self.getHiddenTokensAfter(stop)
        self.setNodeValue(ctx, JsxProperty(name, value, suite))


    def exitJsx_children(self, ctx: OParser.Jsx_childrenContext):
        expressions = [self.getNodeValue(cx) for cx in ctx.jsx_child()]
        self.setNodeValue(ctx, expressions)


    def exitJsx_element_name(self, ctx: OParser.Jsx_element_nameContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJsx_expression(self, ctx: OParser.Jsx_expressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.getChild(0)))


    def exitJsx_identifier(self, ctx: OParser.Jsx_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJsxLiteral(self, ctx: OParser.JsxLiteralContext):
        text = ctx.getText()
        self.setNodeValue(ctx, JsxLiteral(text))


    def exitJsx_opening(self, ctx: OParser.Jsx_openingContext):
        name = self.getNodeValue(ctx.name)
        nameSuite = self.getHiddenTokensAfter(ctx.name.stop)
        attributes = [ self.getNodeValue(cx) for cx in ctx.jsx_attribute() ]
        openingSuite = self.getHiddenTokensAfter(ctx.GT())
        self.setNodeValue(ctx, JsxElement(name, nameSuite, attributes, openingSuite))


    def exitJsx_closing(self, ctx):
        name = self.getNodeValue(ctx.name)
        suite = self.getHiddenTokensAfter(ctx.GT())
        self.setNodeValue(ctx, JsxClosing(name, suite))


    def exitJsx_self_closing(self, ctx: OParser.Jsx_self_closingContext):
        name = self.getNodeValue(ctx.name)
        nameSuite = self.getHiddenTokensAfter(ctx.name.stop)
        attributes = [ self.getNodeValue(cx) for cx in ctx.jsx_attribute() ]
        openingSuite = self.getHiddenTokensAfter(ctx.GT())
        self.setNodeValue(ctx, JsxSelfClosing(name, nameSuite, attributes, openingSuite))


    def exitCssExpression(self, ctx: OParser.CssExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitCss_expression(self, ctx: OParser.Css_expressionContext):
        exp = CssExpression()
        [ exp.addField(self.getNodeValue(cx)) for cx in ctx.css_field() ]
        self.setNodeValue(ctx, exp)


    def exitCss_field(self, ctx: OParser.Css_fieldContext):
        name = ctx.name.getText()
        value = self.getNodeValue(ctx.value)
        self.setNodeValue(ctx, CssField(name, value))


    def exitCssText(self, ctx: OParser.CssTextContext):
        text = ctx.text.getText()
        self.setNodeValue(ctx, CssText(text))


    def exitCssValue(self, ctx: OParser.CssValueContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CssCode(exp))

