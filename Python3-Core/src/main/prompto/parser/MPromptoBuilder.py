from antlr4 import ParserRuleContext, Token
from antlr4.tree.Tree import ParseTree, TerminalNode

from prompto.expression.ExplicitPredicateExpression import ExplicitPredicateExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.expression.PredicateExpression import PredicateExpression
from prompto.expression.ReadBlobExpression import ReadBlobExpression
from prompto.expression.SuperExpression import SuperExpression
from prompto.grammar.ThenWith import ThenWith
from prompto.javascript.JavaScriptItemExpression import JavaScriptItemExpression
from prompto.jsx.JsxFragment import JsxFragment
from prompto.literal.DocEntry import DocEntry
from prompto.literal.DocIdentifierKey import DocIdentifierKey
from prompto.literal.DocTextKey import DocTextKey
from prompto.literal.TypeLiteral import TypeLiteral
from prompto.param.CategoryParameter import CategoryParameter
from prompto.param.CodeParameter import CodeParameter
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
from prompto.expression.InstanceExpression import InstanceExpression
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

from prompto.jsx.JsxElement import JsxElement

from prompto.jsx.JsxLiteral import JsxLiteral

from prompto.jsx.JsxSelfClosing import JsxSelfClosing

from prompto.jsx.JsxProperty import JsxProperty

from prompto.jsx.JsxExpression import JsxExpression

from prompto.jsx.JsxText import JsxText

from prompto.jsx.JsxCode import JsxCode
from prompto.parser import ParserUtils
from prompto.parser.MLexer import MLexer
from prompto.parser.MParser import MParser
from prompto.parser.MParserListener import MParserListener
from prompto.parser.Section import Section
from prompto.python.PythonArgument import PythonNamedArgument, PythonOrdinalArgumentList, PythonNamedArgumentList
from prompto.python.PythonBooleanLiteral import PythonBooleanLiteral
from prompto.python.PythonCharacterLiteral import PythonCharacterLiteral
from prompto.python.PythonDecimalLiteral import PythonDecimalLiteral
from prompto.python.PythonIdentifierExpression import PythonIdentifierExpression
from prompto.python.PythonIntegerLiteral import PythonIntegerLiteral
from prompto.python.PythonMethodExpression import PythonMethodExpression
from prompto.python.PythonModule import PythonModule
from prompto.python.PythonNativeCall import Python2NativeCall, Python3NativeCall, PythonNativeCall
from prompto.python.PythonNativeCategoryBinding import PythonNativeCategoryBinding, Python2NativeCategoryBinding, \
    Python3NativeCategoryBinding
from prompto.python.PythonSelfExpression import PythonSelfExpression
from prompto.python.PythonStatement import PythonStatement
from prompto.python.PythonTextLiteral import PythonTextLiteral
from prompto.statement.AssignInstanceStatement import AssignInstanceStatement
from prompto.statement.AssignTupleStatement import AssignTupleStatement
from prompto.statement.AssignVariableStatement import AssignVariableStatement
from prompto.statement.ReadStatement import ReadStatement
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
from prompto.statement.IfStatement import IfElement, IfElementList, IfStatement
from prompto.statement.RaiseStatement import RaiseStatement
from prompto.statement.ReturnStatement import ReturnStatement
from prompto.statement.StatementList import StatementList
from prompto.statement.DeleteAndStoreStatement import DeleteAndStoreStatement
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
from prompto.type.DbIdType import DbIdType
from prompto.type.DecimalType import DecimalType
from prompto.type.DictType import DictType
from prompto.type.DocumentType import DocumentType
from prompto.type.HtmlType import HtmlType
from prompto.type.IntegerType import IntegerType
from prompto.type.IteratorType import IteratorType
from prompto.type.ListType import ListType
from prompto.type.PeriodType import PeriodType
from prompto.type.SetType import SetType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType
from prompto.type.TypeType import TypeType
from prompto.type.UUIDType import UUIDType
from prompto.type.VersionType import VersionType


class MPromptoBuilder(MParserListener):

    def __init__(self, parser: MParser):
        self.input = parser.getTokenStream()
        self.path = parser.path
        self.nodeValues = dict()


    def getNodeValue(self, node: ParseTree) -> object:
        return self.nodeValues.get(node, None)


    def setNodeValue(self, node: ParseTree, value: object):
        self.nodeValues[node] = value
        if isinstance(value, Section):
            self.buildSection(node, value)


    def buildSection(self, node: ParserRuleContext, section: Section):
        first = self.findFirstValidToken(node.start.tokenIndex)
        last = self.findLastValidToken(node.stop.tokenIndex)
        section.setFrom(self.path, first, last, Dialect.M)


    def findFirstValidToken(self, idx: int):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx < len(self.input.tokens):
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx += 1
        return None


    def findLastValidToken(self, idx: int):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx >= 0:
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx -= 1
        return None


    def readValidToken(self, idx: int):
        token = self.input.tokens[idx]
        text = token.text
        if text is not None and len(text) > 0 and not text[0].isspace():
            return token
        else:
            return None


    def getHiddenTokensBefore(self, node):
        token = node if isinstance(node, Token) else node.symbol
        hidden = self.input.getHiddenTokensToLeft(token.tokenIndex)
        return self.getHiddenTokensText(hidden)


    def getHiddenTokensAfter(self, node):
        token = node if isinstance(node, Token) else node.symbol
        hidden = self.input.getHiddenTokensToRight(token.tokenIndex)
        return self.getHiddenTokensText(hidden)


    # noinspection PyMethodMayBeStatic
    def getHiddenTokensText(self, hidden):
        if hidden is None or len(hidden) == 0:
            return None
        return "".join([token.text for token in hidden])


    def getWhiteSpacePlus(self, ctx):
        if ctx.children is None:
            return None
        within = "".join([child.getText() for child in filter(self.isNotIndent, ctx.children)])
        if within is None:
            return None
        before = self.getHiddenTokensBefore(ctx.start)
        if before is not None:
            within = before + within
        after = self.getHiddenTokensAfter(ctx.stop)
        if after is not None:
            within = within + after
        return within


    # noinspection PyUnresolvedReferences,PyMethodMayBeStatic
    def isNotIndent(self, tree):
        return (not isinstance(tree, TerminalNode)) or tree.symbol.type != MLexer.INDENT

    def readAnnotations(self, contexts):
        return [self.getNodeValue(ctx_) for ctx_ in contexts]

    def readComments(self, contexts):
        return [self.getNodeValue(ctx_) for ctx_ in contexts]

    def exitAbstract_global_method_declaration(self, ctx: MParser.Abstract_global_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        if isinstance(typ, CategoryType):
            typ.mutable = ctx.MUTABLE() is not None
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, typ))

    def exitAbstract_member_method_declaration(self, ctx: MParser.Abstract_member_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        if isinstance(typ, CategoryType):
            typ.mutable = ctx.MUTABLE() is not None
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, typ))

    def exitArrow_prefix(self, ctx: MParser.Arrow_prefixContext):
        args = self.getNodeValue(ctx.arrow_args())
        argsSuite = self.getHiddenTokensBefore(ctx.EGT())
        arrowSuite = self.getHiddenTokensAfter(ctx.EGT())
        self.setNodeValue(ctx, ArrowExpression(args, argsSuite, arrowSuite))

    def exitArrowExpression(self, ctx: MParser.ArrowExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitArrowExpressionBody(self, ctx: MParser.ArrowExpressionBodyContext):
        arrow = self.getNodeValue(ctx.arrow_prefix())
        exp = self.getNodeValue(ctx.expression())
        arrow.setExpression(exp)
        self.setNodeValue(ctx, arrow)


    def exitArrowListArg(self, ctx: MParser.ArrowListArgContext):
        xlist = self.getNodeValue(ctx.variable_identifier_list())
        self.setNodeValue(ctx, xlist)


    def exitArrowSingleArg(self, ctx: MParser.ArrowSingleArgContext):
        arg = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, IdentifierList(arg))


    def exitArrowStatementsBody(self, ctx: MParser.ArrowStatementsBodyContext):
        arrow = self.getNodeValue(ctx.arrow_prefix())
        stmts = self.getNodeValue(ctx.statement_list())
        arrow.statements = stmts
        self.setNodeValue(ctx, arrow)


    def exitAddExpression(self, ctx: MParser.AddExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        exp = PlusExpression(left, right) if ctx.op.type == MParser.PLUS else SubtractExpression(left, right)
        self.setNodeValue(ctx, exp)


    def exitAnnotation_constructor(self, ctx: MParser.Annotation_constructorContext):
        name = self.getNodeValue(ctx.name)
        args = DocEntryList()
        exp = self.getNodeValue(ctx.exp)
        if exp is not None:
            args.append(DocEntry(None, exp))
        for argCtx in ctx.annotation_argument():
            arg = self.getNodeValue(argCtx)
            args.append(arg)
        self.setNodeValue(ctx, Annotation(name, args))


    def exitAnnotation_argument(self, ctx: MParser.Annotation_argumentContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, DocEntry(name, exp))


    def exitAnnotation_identifier(self, ctx: MParser.Annotation_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitAnnotation_argument_name(self, ctx: MParser.Annotation_argument_nameContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitAnnotationLiteralValue(self, ctx: MParser.AnnotationLiteralValueContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAnnotationTypeValue(self, ctx: MParser.AnnotationTypeValueContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, TypeExpression(typ))


    def exitAndExpression(self, ctx: MParser.AndExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, AndExpression(left, right))


    def exitAnyDictType(self, ctx: MParser.AnyDictTypeContext):
        typ = self.getNodeValue(ctx.any_type())
        self.setNodeValue(ctx, DictType(typ))


    def exitAnyListType(self, ctx: MParser.AnyListTypeContext):
        typ = self.getNodeValue(ctx.any_type())
        self.setNodeValue(ctx, ListType(typ))


    def exitAnyType(self, ctx: MParser.AnyTypeContext):
        self.setNodeValue(ctx, AnyType.instance)


    def exitArgument_assignment(self, ctx: MParser.Argument_assignmentContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = UnresolvedParameter(name)
        item = Argument(arg, exp)
        self.setNodeValue(ctx, item)


    def exitArgumentAssignmentList(self, ctx: MParser.ArgumentAssignmentListContext):
        item = self.getNodeValue(ctx.item)
        items = ArgumentList(items=[item])
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentListItem(self, ctx: MParser.ArgumentAssignmentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitArgument_list(self, ctx: MParser.Argument_listContext):
        items = ParameterList()
        for rule in ctx.argument():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitAssertion(self, ctx: MParser.AssertionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAssertion_list(self, ctx: MParser.Assertion_listContext):
        items = []
        for rule in ctx.assertion():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitAssign_instance_statement(self, ctx: MParser.Assign_instance_statementContext):
        inst = self.getNodeValue(ctx.inst)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignInstanceStatement(inst, exp))


    def exitAssign_tuple_statement(self, ctx: MParser.Assign_tuple_statementContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmt = AssignTupleStatement(items)
        stmt.setExpression(exp)
        self.setNodeValue(ctx, stmt)


    def exitAssign_variable_statement(self, ctx: MParser.Assign_variable_statementContext):
        name = self.getNodeValue(ctx.variable_identifier())
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, AssignVariableStatement(name, exp))


    def exitAssignInstanceStatement(self, ctx: MParser.AssignInstanceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitAssignTupleStatement(self, ctx: MParser.AssignTupleStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitAtomicSwitchCase(self, ctx: MParser.AtomicSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(exp, stmts))


    def exitAttribute_declaration(self, ctx: MParser.Attribute_declarationContext):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        match = self.getNodeValue(ctx.match)
        indices = None if ctx.index_clause() is None else self.getNodeValue(ctx.index_clause())
        decl = AttributeDeclaration(name, typ, match, indices)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)


    def exitIndex_clause(self, ctx: MParser.Index_clauseContext):
        indices = IdentifierList() if ctx.indices is None else self.getNodeValue(ctx.indices)
        self.setNodeValue(ctx, indices)


    def exitInclude_list(self, ctx:MParser.Include_listContext):
        include = [ self.getNodeValue(c) for c in ctx.variable_identifier()]
        self.setNodeValue(ctx, include)


    def exitBlob_expression(self, ctx: MParser.Blob_expressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, BlobExpression(exp))


    def exitBlobType(self, ctx: MParser.BlobTypeContext):
        self.setNodeValue(ctx, BlobType.instance)


    def exitBooleanLiteral(self, ctx: MParser.BooleanLiteralContext):
        self.setNodeValue(ctx, BooleanLiteral(ctx.getText()))


    def exitBooleanType(self, ctx: MParser.BooleanTypeContext):
        self.setNodeValue(ctx, BooleanType.instance)


    def exitBreakStatement(self, ctx: MParser.BreakStatementContext):
        self.setNodeValue(ctx, BreakStatement())


    def exitCastExpression(self, ctx: MParser.CastExpressionContext):
        typ = self.getNodeValue(ctx.right)
        exp = self.getNodeValue(ctx.left)
        self.setNodeValue(ctx, CastExpression(exp, typ, ctx.MUTABLE() is not None))


    def exitCatchAtomicStatement(self, ctx: MParser.CatchAtomicStatementContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(SymbolExpression(name), stmts))


    def exitCatchCollectionStatement(self, ctx: MParser.CatchCollectionStatementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCatch_statement_list(self, ctx: MParser.Catch_statement_listContext):
        items = SwitchCaseList()
        for rule in ctx.catch_statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitCategory_or_any_type(self, ctx: MParser.Category_or_any_typeContext):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitCategory_symbol(self, ctx: MParser.Category_symbolContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CategorySymbol(name, args))


    def exitCategory_type(self, ctx: MParser.Category_typeContext):
        name = ctx.getText()
        self.setNodeValue(ctx, CategoryType(name))


    def exitNative_member_method_declaration(self, ctx: MParser.Native_member_method_declarationContext):
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount() - 1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)


    def exitNative_member_method_declaration_list(self, ctx: MParser.Native_member_method_declaration_listContext):
        items = MethodDeclarationList()
        for rule in ctx.native_member_method_declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitMember_method_declaration(self, ctx: MParser.Member_method_declarationContext):
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount() - 1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)


    def exitCategory_symbol_list(self, ctx: MParser.Category_symbol_listContext):
        items = CategorySymbolList()
        for rule in ctx.category_symbol():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitCategoryType(self, ctx: MParser.CategoryTypeContext):
        typ = self.getNodeValue(ctx.c)
        self.setNodeValue(ctx, typ)


    def exitCharacterLiteral(self, ctx: MParser.CharacterLiteralContext):
        self.setNodeValue(ctx, CharacterLiteral(ctx.getText()))


    def exitCharacterType(self, ctx: MParser.CharacterTypeContext):
        self.setNodeValue(ctx, CharacterType.instance)


    def exitChildInstance(self, ctx: MParser.ChildInstanceContext):
        parent = self.getNodeValue(ctx.assignable_instance())
        child = self.getNodeValue(ctx.child_instance())
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitType_expression(self, ctx: MParser.Type_expressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, TypeExpression(CategoryType(name)))


    def exitTypeExpression(self, ctx: MParser.TypeExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitClosureStatement(self, ctx: MParser.ClosureStatementContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, DeclarationStatement(decl))


    def exitCode_argument(self, ctx: MParser.Code_argumentContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CodeParameter(name))


    def exitCode_type(self, ctx: MParser.Code_typeContext):
        self.setNodeValue(ctx, CodeType.instance)


    def exitCodeArgument(self, ctx: MParser.CodeArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitCodeExpression(self, ctx: MParser.CodeExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CodeExpression(exp))


    def exitCodeType(self, ctx: MParser.CodeTypeContext):
        self.setNodeValue(ctx, CodeType.instance)


    def exitCollection_literal(self, ctx: MParser.Collection_literalContext):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitCollectionSwitchCase(self, ctx: MParser.CollectionSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCommentStatement(self, ctx: MParser.CommentStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.comment_statement()))


    def exitComment_statement(self, ctx: MParser.Comment_statementContext):
        self.setNodeValue(ctx, CommentStatement(ctx.getText()))


    def exitCursorType(self, ctx: MParser.CursorTypeContext):
        raise SyntaxError("not implemented")


    def exitConcrete_category_declaration(self, ctx: MParser.Concrete_category_declarationContext):
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


    def exitConcrete_method_declaration(self, ctx: MParser.Concrete_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        if isinstance(typ, CategoryType):
            typ.mutable = ctx.MUTABLE() is not None
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ConcreteMethodDeclaration(name, args, typ, stmts))


    def exitConcrete_widget_declaration(self, ctx: MParser.Concrete_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        derived = self.getNodeValue(ctx.derived)
        methods = self.getNodeValue(ctx.methods)
        ccd = ConcreteWidgetDeclaration(name, derived, methods)
        self.setNodeValue(ctx, ccd)


    def exitConcreteCategoryDeclaration(self, ctx: MParser.ConcreteCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitConcreteWidgetDeclaration(self, ctx: MParser.ConcreteWidgetDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNativeWidgetDeclaration(self, ctx: MParser.NativeWidgetDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitConstructorFrom(self, ctx: MParser.ConstructorFromContext):
        typ = self.getNodeValue(ctx.typ)
        copyFrom = self.getNodeValue(ctx.copyExp)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(typ, copyFrom, args))


    def exitConstructorNoFrom(self, ctx: MParser.ConstructorNoFromContext):
        typ = self.getNodeValue(ctx.typ)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(typ, None, args))


    def exitCopy_from(self, ctx: MParser.Copy_fromContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitCsharp_primary_expression(self, ctx: MParser.Csharp_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitCsharp_identifier(self, ctx: MParser.Csharp_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitCsharp_method_expression(self, ctx: MParser.Csharp_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CSharpMethodExpression(name, args))


    def exitCSharpArgumentList(self, ctx: MParser.CSharpArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CSharpExpressionList(item))


    def exitCSharpArgumentListItem(self, ctx: MParser.CSharpArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitCSharpBooleanLiteral(self, ctx: MParser.CSharpBooleanLiteralContext):
        self.setNodeValue(ctx, CSharpBooleanLiteral(ctx.getText()))


    def exitCSharpCategoryBinding(self, ctx: MParser.CSharpCategoryBindingContext):
        xmap = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, CSharpNativeCategoryBinding(xmap))


    def exitCSharpCharacterLiteral(self, ctx: MParser.CSharpCharacterLiteralContext):
        self.setNodeValue(ctx, CSharpCharacterLiteral(ctx.getText()))


    def exitCSharpChildIdentifier(self, ctx: MParser.CSharpChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = CSharpIdentifierExpression(parent, name)
        self.setNodeValue(ctx, child)


    def exitCsharp_this_expression(self, ctx: MParser.Csharp_this_expressionContext):
        self.setNodeValue(ctx, CSharpThisExpression())


    def exitCSharpDecimalLiteral(self, ctx: MParser.CSharpDecimalLiteralContext):
        self.setNodeValue(ctx, CSharpDecimalLiteral(ctx.getText()))


    def exitCSharpIdentifier(self, ctx: MParser.CSharpIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))


    def exitCSharpIntegerLiteral(self, ctx: MParser.CSharpIntegerLiteralContext):
        self.setNodeValue(ctx, CSharpIntegerLiteral(ctx.getText()))


    def exitCSharpMethodExpression(self, ctx: MParser.CSharpMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpNativeStatement(self, ctx: MParser.CSharpNativeStatementContext):
        stmt = self.getNodeValue(ctx.csharp_statement())
        self.setNodeValue(ctx, CSharpNativeCall(stmt))


    def exitCSharpPromptoIdentifier(self, ctx: MParser.CSharpPromptoIdentifierContext):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))


    def exitCSharpPrimaryExpression(self, ctx: MParser.CSharpPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpReturnStatement(self, ctx: MParser.CSharpReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, True))


    def exitCSharpSelectorExpression(self, ctx: MParser.CSharpSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitCSharpStatement(self, ctx: MParser.CSharpStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, False))


    def exitCSharpTextLiteral(self, ctx: MParser.CSharpTextLiteralContext):
        self.setNodeValue(ctx, CSharpTextLiteral(ctx.getText()))


    def exitDateLiteral(self, ctx: MParser.DateLiteralContext):
        self.setNodeValue(ctx, DateLiteral(ctx.getText()))


    def exitDateTimeLiteral(self, ctx: MParser.DateTimeLiteralContext):
        self.setNodeValue(ctx, DateTimeLiteral(ctx.getText()))


    def exitDateTimeType(self, ctx: MParser.DateTimeTypeContext):
        self.setNodeValue(ctx, DateTimeType.instance)


    def exitDateType(self, ctx: MParser.DateTypeContext):
        self.setNodeValue(ctx, DateType.instance)


    def exitDbIdType(self, ctx: MParser.DbIdTypeContext):
        self.setNodeValue(ctx, DbIdType.instance)


    def exitDecimalLiteral(self, ctx: MParser.DecimalLiteralContext):
        self.setNodeValue(ctx, DecimalLiteral(ctx.getText()))


    def exitDecimalType(self, ctx: MParser.DecimalTypeContext):
        self.setNodeValue(ctx, DecimalType.instance)


    def exitDeclaration(self, ctx: MParser.DeclarationContext):
        comments = self.readComments(ctx.comment_statement())
        annotations = self.readAnnotations(ctx.annotation_constructor())
        ctx_ = ctx.children[ctx.getChildCount() - 1]
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = comments
            decl.annotations = annotations
            self.setNodeValue(ctx, decl)


    def exitDeclarations(self, ctx: MParser.DeclarationsContext):
        items = DeclarationList()
        for rule in ctx.declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitDerived_list(self, ctx: MParser.Derived_listContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitDict_entry(self, ctx: MParser.Dict_entryContext):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DictEntry(key, value)
        self.setNodeValue(ctx, entry)


    def exitDict_entry_list(self, ctx: MParser.Dict_entry_listContext):
        items = DictEntryList()
        for rule in ctx.dict_entry():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitDict_literal(self, ctx: MParser.Dict_literalContext):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.dict_entry_list())
        value = DictLiteral(mutable, items)
        self.setNodeValue(ctx, value)


    def exitDictType(self, ctx):
        typ = self.getNodeValue(ctx.d)
        self.setNodeValue(ctx, DictType(typ))


    def exitDictKeyIdentifier(self, ctx: MParser.DictKeyIdentifierContext):
        name = ctx.name.getText()
        self.setNodeValue(ctx, DictIdentifierKey(name))


    def exitDictKeyText(self, ctx: MParser.DictKeyTextContext):
        name = ctx.name.text
        self.setNodeValue(ctx, DictTextKey(name))


    def exitDoc_entry(self, ctx: MParser.Doc_entryContext):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DocEntry(key, value)
        self.setNodeValue(ctx, entry)


    def exitDoc_entry_list(self, ctx: MParser.Doc_entry_listContext):
        items = DocEntryList()
        for rule in ctx.doc_entry():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitDocKeyIdentifier(self, ctx: MParser.DocKeyIdentifierContext):
        name = ctx.name.getText()
        self.setNodeValue(ctx, DocIdentifierKey(name))


    def exitDocKeyText(self, ctx: MParser.DocKeyTextContext):
        name = ctx.name.text
        self.setNodeValue(ctx, DocTextKey(name))


    def exitDivideExpression(self, ctx: MParser.DivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, DivideExpression(left, right))


    def exitDo_while_statement(self, ctx: MParser.Do_while_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, DoWhileStatement(exp, stmts))


    def exitDocument_expression(self, ctx: MParser.Document_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, DocumentExpression(exp))


    def exitDocumentType(self, ctx: MParser.DocumentTypeContext):
        self.setNodeValue(ctx, DocumentType.instance)


    def exitDocument_literal(self, ctx: MParser.Document_literalContext):
        entries = self.getNodeValue(ctx.doc_entry_list())
        if entries is None:
            entries = DocEntryList()
        self.setNodeValue(ctx, DocumentLiteral(entries))


    def exitDoWhileStatement(self, ctx: MParser.DoWhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitElseIfStatementList(self, ctx: MParser.ElseIfStatementListContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        self.setNodeValue(ctx, IfElementList(elem))


    def exitElseIfStatementListItem(self, ctx: MParser.ElseIfStatementListItemContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        items.add(elem)
        self.setNodeValue(ctx, items)


    def exitEnum_category_declaration(self, ctx: MParser.Enum_category_declarationContext):
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


    def exitEnum_declaration(self, ctx: MParser.Enum_declarationContext):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)


    def exitEnum_native_declaration(self, ctx: MParser.Enum_native_declarationContext):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        symbols = self.getNodeValue(ctx.symbols)
        self.setNodeValue(ctx, EnumeratedNativeDeclaration(name, typ, symbols))


    def exitEqualsExpression(self, ctx: MParser.EqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        if ctx.op.type == MLexer.EQ2:
            eqOp = EqOp.EQUALS
        elif ctx.op.type == MLexer.XEQ:
            eqOp = EqOp.NOT_EQUALS
        elif ctx.op.type == MLexer.TEQ:
            eqOp = EqOp.ROUGHLY
        else:
            raise Exception("Operator " + ctx.op.type)
        self.setNodeValue(ctx, EqualsExpression(left, eqOp, right))


    def exitExecuteExpression(self, ctx: MParser.ExecuteExpressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, ExecuteExpression(name))


    def exitExpression_list(self, ctx: MParser.expression_list):
        items = []
        for rule in ctx.expression():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitExpression_tuple(self, ctx: MParser.expression_tuple):
        items = []
        for rule in ctx.expression():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitExpressionAssignmentList(self, ctx: MParser.ExpressionAssignmentListContext):
        exp = self.getNodeValue(ctx.exp)
        items = ArgumentList()
        items.append(Argument(None, exp))
        self.setNodeValue(ctx, items)


    def exitFetchMany(self, ctx: MParser.FetchManyContext):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        include = self.getNodeValue(ctx.include)
        orderBy = self.getNodeValue(ctx.orderby)
        self.setNodeValue(ctx, FetchManyExpression(category, predicate, start, stop, include, orderBy))


    def exitFetchManyAsync(self, ctx: MParser.FetchManyAsyncContext):
        category = self.getNodeValue(ctx.typ)
        predicate = self.getNodeValue(ctx.predicate)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        include = self.getNodeValue(ctx.include)
        orderBy = self.getNodeValue(ctx.orderby)
        thenWith = ThenWith.OrEmpty(self.getNodeValue(ctx.then()))
        self.setNodeValue(ctx, FetchManyStatement(category, predicate, start, stop, include, orderBy, thenWith))


    def exitThen(self, ctx:MParser.ThenContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ThenWith(name, stmts))


    def exitFetchStatement(self, ctx: MParser.FetchStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitFetchOne(self, ctx: MParser.FetchOneContext):
        category = self.getNodeValue(ctx.typ)
        include = self.getNodeValue(ctx.include)
        predicate = self.getNodeValue(ctx.predicate)
        self.setNodeValue(ctx, FetchOneExpression(category, predicate, include))


    def exitFetchOneAsync(self, ctx: MParser.FetchOneAsyncContext):
        category = self.getNodeValue(ctx.typ)
        include = self.getNodeValue(ctx.include)
        predicate = self.getNodeValue(ctx.predicate)
        thenWith = ThenWith.OrEmpty(self.getNodeValue(ctx.then()))
        self.setNodeValue(ctx, FetchOneStatement(category, predicate, include, thenWith))


    def exitFilteredListExpression(self, ctx: MParser.FilteredListExpressionContext):
        filtered = self.getNodeValue(ctx.filtered_list_suffix())
        filtered.source = self.getNodeValue(ctx.src)
        self.setNodeValue(ctx, filtered)


    def exitFiltered_list_suffix(self, ctx: MParser.Filtered_list_suffixContext):
        itemName = self.getNodeValue(ctx.name)
        predicate = self.getNodeValue(ctx.predicate)
        if itemName is not None:
            expression = ExplicitPredicateExpression(itemName, predicate)
        elif isinstance(predicate, PredicateExpression):
            expression = predicate
        else:
            raise Exception("What?")
        self.setNodeValue(ctx, FilteredExpression(itemName, expression))


    def exitArrowFilterExpression(self, ctx: MParser.ArrowFilterExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.arrow_expression()))


    def exitExplicitFilterExpression(self, ctx: MParser.ExplicitFilterExpressionContext):
        name = self.getNodeValue(ctx.variable_identifier())
        predicate = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, ExplicitPredicateExpression(name, predicate))


    def exitOtherFilterExpression(self, ctx: MParser.OtherFilterExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.expression()))


    def exitFlush_statement(self, ctx: MParser.Flush_statementContext):
        self.setNodeValue(ctx, FlushStatement())


    def exitFlushStatement(self, ctx: MParser.FlushStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitFor_each_statement(self, ctx: MParser.For_each_statementContext):
        name1 = self.getNodeValue(ctx.name1)
        name2 = self.getNodeValue(ctx.name2)
        source = self.getNodeValue(ctx.source)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ForEachStatement(name1, name2, source, stmts))


    def exitForEachStatement(self, ctx: MParser.ForEachStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitFullDeclarationList(self, ctx: MParser.FullDeclarationListContext):
        items = self.getNodeValue(ctx.declarations())
        if items is None:
            items = DeclarationList()
        self.setNodeValue(ctx, items)


    def exitGetter_method_declaration(self, ctx: MParser.Getter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, GetterMethodDeclaration(name, stmts))


    def exitNative_setter_declaration(self, ctx: MParser.Native_setter_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeSetterMethodDeclaration(name, stmts))


    def exitNative_getter_declaration(self, ctx: MParser.Native_getter_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeGetterMethodDeclaration(name, stmts))


    def exitCompareExpression(self, ctx: MParser.CompareExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        if ctx.op.type == MLexer.LT:
            cmpOp = CmpOp.LT
        elif ctx.op.type == MLexer.LTE:
            cmpOp = CmpOp.LTE
        elif ctx.op.type == MLexer.GT:
            cmpOp = CmpOp.GT
        elif ctx.op.type == MLexer.GTE:
            cmpOp = CmpOp.GTE
        else:
            raise Exception("Operator " + ctx.op.type)
        self.setNodeValue(ctx, CompareExpression(left, cmpOp, right))


    def exitHexadecimalLiteral(self, ctx: MParser.HexadecimalLiteralContext):
        self.setNodeValue(ctx, HexaLiteral(ctx.getText()))


    def exitIdentifierExpression(self, ctx: MParser.IdentifierExpressionContext):
        name = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, UnresolvedIdentifier(name, Dialect.M))


    def exitIf_statement(self, ctx: MParser.If_statementContext):
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


    def exitIfStatement(self, ctx: MParser.IfStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitInExpression(self, ctx: MParser.InExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.IN if ctx.NOT() is None else ContOp.NOT_IN
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitInstanceExpression(self, ctx: MParser.InstanceExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitIntDivideExpression(self, ctx: MParser.IntDivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, IntDivideExpression(left, right))


    def exitIntegerLiteral(self, ctx: MParser.IntegerLiteralContext):
        self.setNodeValue(ctx, IntegerLiteral(ctx.getText()))


    def exitIntegerType(self, ctx: MParser.IntegerTypeContext):
        self.setNodeValue(ctx, IntegerType.instance)


    def exitIsATypeExpression(self, ctx: MParser.IsATypeExpressionContext):
        typ = self.getNodeValue(ctx.category_or_any_type())
        exp = TypeExpression(typ)
        self.setNodeValue(ctx, exp)


    def exitIsOtherExpression(self, ctx: MParser.IsOtherExpressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, exp)


    def exitIsExpression(self, ctx: MParser.IsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        if ctx.NOT() is not None:
            op = EqOp.IS_NOT_A if isinstance(right, TypeExpression) else EqOp.IS_NOT
        else:
            op = EqOp.IS_A if isinstance(right, TypeExpression) else EqOp.IS
        self.setNodeValue(ctx, EqualsExpression(left, op, right))


    def exitItemInstance(self, ctx: MParser.ItemInstanceContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemInstance(None, exp))


    def exitItemSelector(self, ctx: MParser.ItemSelectorContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))


    def exitIteratorExpression(self, ctx: MParser.IteratorExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        name = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, IteratorExpression(name, source, exp))


    def exitIteratorType(self, ctx: MParser.IteratorTypeContext):
        typ = self.getNodeValue(ctx.i)
        self.setNodeValue(ctx, IteratorType(typ))


    def exitJava_identifier(self, ctx: MParser.Java_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitJava_item_expression(self, ctx: MParser.Java_item_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaItemExpression(exp))


    def exitJava_method_expression(self, ctx: MParser.Java_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, JavaMethodExpression(name, args))


    def exitJava_parenthesis_expression(self, ctx: MParser.Java_parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaArgumentList(self, ctx: MParser.JavaArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, JavaExpressionList(item))


    def exitJavaArgumentListItem(self, ctx: MParser.JavaArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitJavaBooleanLiteral(self, ctx: MParser.JavaBooleanLiteralContext):
        self.setNodeValue(ctx, JavaBooleanLiteral(ctx.getText()))


    def exitJavaCategoryBinding(self, ctx: MParser.JavaCategoryBindingContext):
        xmap = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, JavaNativeCategoryBinding(xmap))


    def exitJavaCharacterLiteral(self, ctx: MParser.JavaCharacterLiteralContext):
        self.setNodeValue(ctx, JavaCharacterLiteral(ctx.getText()))


    def exitJavaChildClassIdentifier(self, ctx: MParser.JavaChildClassIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        child = JavaIdentifierExpression(parent, ctx.name.getText())
        self.setNodeValue(ctx, child)


    def exitJava_primary_expression(self, ctx: MParser.Java_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitJavaChildIdentifier(self, ctx: MParser.JavaChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = JavaIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)


    def exitJavaClassIdentifier(self, ctx: MParser.JavaClassIdentifierContext):
        klass = self.getNodeValue(ctx.klass)
        self.setNodeValue(ctx, klass)


    def exitJavaDecimalLiteral(self, ctx: MParser.JavaDecimalLiteralContext):
        self.setNodeValue(ctx, JavaDecimalLiteral(ctx.getText()))


    def exitJavaIdentifier(self, ctx: MParser.JavaIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaIdentifierExpression(name))


    def exitJavaIntegerLiteral(self, ctx: MParser.JavaIntegerLiteralContext):
        self.setNodeValue(ctx, JavaIntegerLiteral(ctx.getText()))


    def exitJavaItemExpression(self, ctx: MParser.JavaItemExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaMethodExpression(self, ctx: MParser.JavaMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJava_this_expression(self, ctx: MParser.Java_this_expressionContext):
        self.setNodeValue(ctx, JavaThisExpression())


    def exitJavaNativeStatement(self, ctx: MParser.JavaNativeStatementContext):
        stmt = self.getNodeValue(ctx.java_statement())
        self.setNodeValue(ctx, JavaNativeCall(stmt))


    def exitJavaPrimaryExpression(self, ctx: MParser.JavaPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaReturnStatement(self, ctx: MParser.JavaReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, True))


    def exitJavascriptBooleanLiteral(self, ctx: MParser.JavascriptBooleanLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptBooleanLiteral(text))


    def exitJavascript_category_binding(self, ctx: MParser.Javascript_category_bindingContext):
        identifier = ".".join([cx.getText() for cx in ctx.javascript_identifier()])
        module = self.getNodeValue(ctx.javascript_module())
        xmap = JavaScriptNativeCategoryBinding(identifier, module)
        self.setNodeValue(ctx, xmap)


    def exitJavascriptCharacterLiteral(self, ctx: MParser.JavascriptCharacterLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptCharacterLiteral(text))


    def exitJavascript_identifier(self, ctx: MParser.Javascript_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJavascript_this_expression(self, ctx: MParser.Javascript_this_expressionContext):
        self.setNodeValue(ctx, JavaScriptThisExpression())


    def exitJavascript_item_expression(self, ctx: MParser.Javascript_item_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptItemExpression(exp))


    def exitJavascriptItemExpression(self, ctx:MParser.JavascriptItemExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitJavascript_method_expression(self, ctx: MParser.Javascript_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        method = JavaScriptMethodExpression(name)
        args = self.getNodeValue(ctx.args)
        method.arguments = args
        self.setNodeValue(ctx, method)


    def exitJavascript_module(self, ctx: MParser.Javascript_moduleContext):
        ids = []
        for ic in ctx.javascript_identifier():
            ids.append(ic.getText())
        module = JavaScriptModule(ids)
        self.setNodeValue(ctx, module)


    def exitJavascript_native_statement(self, ctx: MParser.Javascript_native_statementContext):
        stmt = self.getNodeValue(ctx.javascript_statement())
        module = self.getNodeValue(ctx.javascript_module())
        stmt.module = module
        self.setNodeValue(ctx, stmt)


    def exitJavascript_new_expression(self, ctx: MParser.Javascript_new_expressionContext):
        method = self.getNodeValue(ctx.javascript_method_expression())
        new = JavaScriptNewExpression(method)
        self.setNodeValue(ctx, new)


    def exitJavascriptArgumentList(self, ctx: MParser.JavascriptArgumentListContext):
        exp = self.getNodeValue(ctx.item)
        xlist = JavaScriptExpressionList(exp)
        self.setNodeValue(ctx, xlist)


    def exitJavascriptArgumentListItem(self, ctx: MParser.JavascriptArgumentListItemContext):
        exp = self.getNodeValue(ctx.item)
        xlist = self.getNodeValue(ctx.items)
        xlist.append(exp)
        self.setNodeValue(ctx, xlist)


    def exitJavascriptCategoryBinding(self, ctx: MParser.JavascriptCategoryBindingContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.binding))


    def exitJavascript_identifier_expression(self, ctx: MParser.Javascript_identifier_expressionContext):
        name = self.getNodeValue(ctx.name)
        exp = JavaScriptIdentifierExpression(None, name)
        self.setNodeValue(ctx, exp)


    def exitJavascriptDecimalLiteral(self, ctx: MParser.JavascriptDecimalLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptDecimalLiteral(text))


    def exitJavascriptIntegerLiteral(self, ctx: MParser.JavascriptIntegerLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptIntegerLiteral(text))


    def exitJavascriptMethodExpression(self, ctx: MParser.JavascriptMethodExpressionContext):
        method = self.getNodeValue(ctx.method)
        self.setNodeValue(ctx, method)


    def exitJavascriptNativeStatement(self, ctx: MParser.JavascriptNativeStatementContext):
        stmt = self.getNodeValue(ctx.javascript_native_statement())
        self.setNodeValue(ctx, JavaScriptNativeCall(stmt))


    def exitJavascriptMemberExpression(self, ctx: MParser.JavascriptMemberExpressionContext):
        name = ctx.name.getText()
        self.setNodeValue(ctx, JavaScriptMemberExpression(name))


    def exitJavascript_primary_expression(self, ctx: MParser.Java_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitJavascriptPrimaryExpression(self, ctx: MParser.JavascriptPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavascriptReturnStatement(self, ctx: MParser.JavascriptReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, True))


    def exitJavascriptSelectorExpression(self, ctx: MParser.JavascriptSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)


    def exitJavascriptStatement(self, ctx: MParser.JavascriptStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, False))


    def exitJavascriptTextLiteral(self, ctx: MParser.JavascriptTextLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptTextLiteral(text))


    def exitJavaSelectorExpression(self, ctx: MParser.JavaSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitJavaStatement(self, ctx: MParser.JavaStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, False))


    def exitJavaTextLiteral(self, ctx: MParser.JavaTextLiteralContext):
        self.setNodeValue(ctx, JavaTextLiteral(ctx.getText()))


    def exitKey_token(self, ctx: MParser.Key_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitList_literal(self, ctx: MParser.List_literalContext):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.expression_list())
        items = items if items is not None else []
        value = ListLiteral(items, mutable=mutable)
        self.setNodeValue(ctx, value)


    def exitListType(self, ctx: MParser.ListTypeContext):
        typ = self.getNodeValue(ctx.l)
        self.setNodeValue(ctx, ListType(typ, False))


    def exitLiteral_expression(self, ctx: MParser.Literal_expressionContext):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)


    def exitLiteralExpression(self, ctx: MParser.LiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitLiteral_list_literal(self, ctx: MParser.Literal_list_literalContext):
        items = []
        for rule in ctx.atomic_literal():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitLiteralListLiteral(self, ctx: MParser.LiteralListLiteralContext):
        exp = self.getNodeValue(ctx.literal_list_literal())
        self.setNodeValue(ctx, ListLiteral(exp))


    def exitLiteralRangeLiteral(self, ctx: MParser.LiteralRangeLiteralContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))


    def exitLiteralSetLiteral(self, ctx: MParser.LiteralSetLiteralContext):
        exp = self.getNodeValue(ctx.literal_list_literal())
        self.setNodeValue(ctx, SetLiteral(exp))


    def exitMatchingExpression(self, ctx: MParser.MatchingExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MatchingExpressionConstraint(exp))


    def exitMatchingList(self, ctx: MParser.MatchingListContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingPattern(self, ctx: MParser.MatchingPatternContext):
        self.setNodeValue(ctx, MatchingPatternConstraint(TextLiteral(ctx.text.text)))


    def exitMatchingRange(self, ctx: MParser.MatchingRangeContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingSet(self, ctx: MParser.MatchingSetContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMaxIntegerLiteral(self, ctx: MParser.MaxIntegerLiteralContext):
        self.setNodeValue(ctx, MaxIntegerLiteral())


    def exitMember_identifier(self, ctx: MParser.Member_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitMemberInstance(self, ctx: MParser.MemberInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberInstance(None, name))


    def exitMemberSelector(self, ctx: MParser.MemberSelectorContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))


    def exitMethod_call_expression(self, ctx: MParser.Method_call_expressionContext):
        name = self.getNodeValue(ctx.name)
        caller = UnresolvedIdentifier(name, Dialect.M)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, UnresolvedCall(caller, args))


    def exitMethod_call_statement(self, ctx: MParser.Method_call_statementContext):
        parent = self.getNodeValue(ctx.parent)
        call = self.getNodeValue(ctx.method)
        call.setParent(parent)
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        if name is not None or stmts is not None:
            self.setNodeValue(ctx, RemoteCall(call.caller, call.arguments, name, stmts))
        else:
            self.setNodeValue(ctx, call)


    def exitMethod_declaration(self, ctx: MParser.Method_declarationContext):
        value = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, value)


    def exitMethod_identifier(self, ctx: MParser.Method_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitMethod_expression(self, ctx: MParser.Method_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitMethodCallStatement(self, ctx: MParser.MethodCallStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitMethodExpression(self, ctx: MParser.MethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitMethodRefSelector(self, ctx: MParser.MethodRefSelectorContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodSelector(name))

    def exitMethodCallSelector(self, ctx: MParser.MethodCallSelectorContext):
        call = self.getNodeValue(ctx.method)
        if isinstance(call.caller, UnresolvedIdentifier):
            name = call.caller.name
            call.caller = UnresolvedSelector(name)
        self.setNodeValue(ctx, call)


    def exitMinIntegerLiteral(self, ctx: MParser.MinIntegerLiteralContext):
        self.setNodeValue(ctx, MinIntegerLiteral())


    def exitMinusExpression(self, ctx: MParser.MinusExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MinusExpression(exp))


    def exitModuloExpression(self, ctx: MParser.ModuloExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ModuloExpression(left, right))


    def exitMultiplyExpression(self, ctx: MParser.MultiplyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, MultiplyExpression(left, right))


    def exitMutable_category_type(self, ctx):
        typ = self.getNodeValue(ctx.category_type())
        typ.mutable = ctx.MUTABLE() is not None
        self.setNodeValue(ctx, typ)


    def exitMutableInstanceExpression(self, ctx: MParser.MutableInstanceExpressionContext):
        source = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MutableExpression(source))


    def exitMutableSelectableExpression(self, ctx: MParser.MutableSelectableExpressionContext):
        name = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, InstanceExpression(name))


    def exitMutableSelectorExpression(self, ctx: MParser.MutableSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.parent = parent
        self.setNodeValue(ctx, selector)


    def exitNamed_argument(self, ctx: MParser.Named_argumentContext):
        name = self.getNodeValue(ctx.variable_identifier())
        arg = UnresolvedParameter(name)
        exp = self.getNodeValue(ctx.literal_expression())
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitNative_category_declaration(self, ctx: MParser.Native_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeCategoryDeclaration(name, attrs, bindings, None, methods)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)


    def exitNative_widget_declaration(self, ctx: MParser.Native_widget_declarationContext):
        name = self.getNodeValue(ctx.name)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeWidgetDeclaration(name, bindings, methods)
        self.setNodeValue(ctx, decl)


    def exitNative_category_bindings(self, ctx: MParser.Native_category_bindingsContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitNative_method_declaration(self, ctx: MParser.Native_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeMethodDeclaration(name, args, typ, stmts))


    def exitNative_resource_declaration(self, ctx: MParser.Native_resource_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeResourceDeclaration(name, attrs, bindings, None, methods)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)


    def exitNative_symbol(self, ctx: MParser.Native_symbolContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NativeSymbol(name, exp))


    def exitNativeCategoryDeclaration(self, ctx: MParser.NativeCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNativeCategoryBindingList(self, ctx: MParser.NativeCategoryBindingListContext):
        item = self.getNodeValue(ctx.item)
        items = NativeCategoryBindingList(item)
        self.setNodeValue(ctx, items)


    def exitNativeCategoryBindingListItem(self, ctx: MParser.NativeCategoryBindingListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNative_statement_list(self, ctx: MParser.Native_statement_listContext):
        items = StatementList()
        for rule in ctx.native_statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitNative_symbol_list(self, ctx: MParser.Native_symbol_listContext):
        items = NativeSymbolList()
        for rule in ctx.native_symbol():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeType(self, ctx: MParser.NativeTypeContext):
        typ = self.getNodeValue(ctx.n)
        self.setNodeValue(ctx, typ)


    def exitNotExpression(self, ctx: MParser.NotExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NotExpression(exp))


    def exitCssType(self, ctx: MParser.CssTypeContext):
        self.setNodeValue(ctx, CssType.instance)


    def exitHasExpression(self, ctx: MParser.HasExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.HAS if ctx.NOT() is None else ContOp.NOT_HAS
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitHasAllExpression(self, ctx: MParser.HasAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.HAS_ALL if ctx.NOT() is None else ContOp.NOT_HAS_ALL
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitHasAnyExpression(self, ctx: MParser.HasAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        contOp = ContOp.HAS_ANY if ctx.NOT() is None else ContOp.NOT_HAS_ANY
        self.setNodeValue(ctx, ContainsExpression(left, contOp, right))


    def exitContainsExpression(self, ctx: MParser.ContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        eqOp = EqOp.CONTAINS if ctx.NOT() is None else EqOp.NOT_CONTAINS
        self.setNodeValue(ctx, EqualsExpression(left, eqOp, right))


    def exitNullLiteral(self, ctx: MParser.NullLiteralContext):
        self.setNodeValue(ctx, NullLiteral.instance)


    def exitOperator_argument(self, ctx: MParser.Operator_argumentContext):
        stmt = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, stmt)


    def exitOperatorArgument(self, ctx: MParser.OperatorArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        arg.setMutable(ctx.MUTABLE() is not None)
        self.setNodeValue(ctx, arg)


    def exitOperatorPlus(self, ctx: MParser.OperatorPlusContext):
        self.setNodeValue(ctx, Operator.PLUS)


    def exitOperatorMinus(self, ctx: MParser.OperatorMinusContext):
        self.setNodeValue(ctx, Operator.MINUS)


    def exitOperatorMultiply(self, ctx: MParser.OperatorMultiplyContext):
        self.setNodeValue(ctx, Operator.MULTIPLY)


    def exitOperatorDivide(self, ctx: MParser.OperatorDivideContext):
        self.setNodeValue(ctx, Operator.DIVIDE)


    def exitOperatorIDivide(self, ctx: MParser.OperatorIDivideContext):
        self.setNodeValue(ctx, Operator.IDIVIDE)


    def exitOperatorModulo(self, ctx: MParser.OperatorModuloContext):
        self.setNodeValue(ctx, Operator.MODULO)


    def exitOperator_method_declaration(self, ctx: MParser.Operator_method_declarationContext):
        op = self.getNodeValue(ctx.op)
        arg = self.getNodeValue(ctx.arg)
        typ = self.getNodeValue(ctx.typ)
        stmts = self.getNodeValue(ctx.stmts)
        decl = OperatorMethodDeclaration(op, arg, typ, stmts)
        self.setNodeValue(ctx, decl)


    def exitOrder_by(self, ctx: MParser.Order_byContext):
        names = IdentifierList()
        for ctx_ in ctx.variable_identifier():
            names.append(self.getNodeValue(ctx_))
        clause = OrderByClause(names, ctx.DESC() is not None)
        self.setNodeValue(ctx, clause)


    def exitOrder_by_list(self, ctx: MParser.Order_by_listContext):
        list_ = OrderByClauseList()
        for ctx_ in ctx.order_by():
            list_.append(self.getNodeValue(ctx_))
        self.setNodeValue(ctx, list_)


    def exitOrExpression(self, ctx: MParser.OrExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, OrExpression(left, right))


    def exitParenthesis_expression(self, ctx: MParser.Parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, ParenthesisExpression(exp))


    def exitParenthesisExpression(self, ctx: MParser.ParenthesisExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPeriodLiteral(self, ctx: MParser.PeriodLiteralContext):
        self.setNodeValue(ctx, PeriodLiteral(ctx.getText()))


    def exitPeriodType(self, ctx: MParser.PeriodTypeContext):
        self.setNodeValue(ctx, PeriodType.instance)


    def exitVersionLiteral(self, ctx: MParser.VersionLiteralContext):
        self.setNodeValue(ctx, VersionLiteral(ctx.getText()))


    def exitVersionType(self, ctx: MParser.VersionTypeContext):
        self.setNodeValue(ctx, VersionType.instance)


    def exitPrimaryType(self, ctx: MParser.PrimaryTypeContext):
        typ = self.getNodeValue(ctx.p)
        self.setNodeValue(ctx, typ)


    def exitPython_category_binding(self, ctx: MParser.Python_category_bindingContext):
        identifier = ctx.identifier().getText()
        module = self.getNodeValue(ctx.python_module())
        xmap = PythonNativeCategoryBinding(identifier, module)
        self.setNodeValue(ctx, xmap)


    def exitPython_identifier(self, ctx: MParser.Python_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitPython_method_expression(self, ctx: MParser.Python_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        method = PythonMethodExpression(name, args)
        self.setNodeValue(ctx, method)


    def exitPython_module(self, ctx: MParser.Python_moduleContext):
        ids = [c.getText() for c in ctx.python_identifier()]
        module = PythonModule(ids)
        self.setNodeValue(ctx, module)


    def exitPython_native_statement(self, ctx: MParser.Python_native_statementContext):
        stmt = self.getNodeValue(ctx.python_statement())
        module = self.getNodeValue(ctx.python_module())
        self.setNodeValue(ctx, PythonNativeCall(stmt, module))


    def exitPython2CategoryBinding(self, ctx: MParser.Python2CategoryBindingContext):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python2NativeCategoryBinding(binding.identifier, binding.module))


    def exitPython2NativeStatement(self, ctx: MParser.Python2NativeStatementContext):
        call = self.getNodeValue(ctx.python_native_statement())
        self.setNodeValue(ctx, Python2NativeCall(call.statement, call.module))


    def exitPython3CategoryBinding(self, ctx: MParser.Python3CategoryBindingContext):
        binding = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python3NativeCategoryBinding(binding.identifier, binding.module))


    def exitPython3NativeStatement(self, ctx: MParser.Python3NativeStatementContext):
        call = self.getNodeValue(ctx.python_native_statement())
        self.setNodeValue(ctx, Python3NativeCall(call.statement, call.module))


    def exitPythonArgumentList(self, ctx: MParser.PythonArgumentListContext):
        ordinal = self.getNodeValue(ctx.ordinal)
        named = self.getNodeValue(ctx.named)
        ordinal.addAll(named)
        self.setNodeValue(ctx, ordinal)


    def exitPythonBooleanLiteral(self, ctx: MParser.PythonBooleanLiteralContext):
        self.setNodeValue(ctx, PythonBooleanLiteral(ctx.getText()))


    def exitPythonCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, PythonCharacterLiteral(ctx.getText()))


    def exitPythonChildIdentifier(self, ctx: MParser.PythonChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = PythonIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)


    def exitPythonDecimalLiteral(self, ctx: MParser.PythonDecimalLiteralContext):
        self.setNodeValue(ctx, PythonDecimalLiteral(ctx.getText()))


    def exitPythonGlobalMethodExpression(self, ctx: MParser.PythonGlobalMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIdentifier(self, ctx: MParser.PythonIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, PythonIdentifierExpression(name))


    def exitPythonIdentifierExpression(self, ctx: MParser.PythonIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIntegerLiteral(self, ctx: MParser.PythonIntegerLiteralContext):
        self.setNodeValue(ctx, PythonIntegerLiteral(ctx.getText()))


    def exitPythonLiteralExpression(self, ctx: MParser.PythonLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonMethodExpression(self, ctx: MParser.PythonMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonNamedArgumentList(self, ctx: MParser.PythonNamedArgumentListContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = PythonNamedArgument(name, exp)
        arglist = PythonNamedArgumentList()
        arglist.append(arg)
        self.setNodeValue(ctx, arglist)


    def exitPythonNamedArgumentListItem(self, ctx: MParser.PythonNamedArgumentListItemContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        item = PythonNamedArgument(name, exp)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitPythonNamedOnlyArgumentList(self, ctx: MParser.PythonNamedOnlyArgumentListContext):
        named = self.getNodeValue(ctx.named)
        self.setNodeValue(ctx, named)


    def exitPythonOrdinalArgumentList(self, ctx: MParser.PythonOrdinalArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, PythonOrdinalArgumentList(item))


    def exitPythonOrdinalArgumentListItem(self, ctx: MParser.PythonOrdinalArgumentListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitPythonOrdinalOnlyArgumentList(self, ctx: MParser.PythonOrdinalOnlyArgumentListContext):
        ordinal = self.getNodeValue(ctx.ordinal)
        self.setNodeValue(ctx, ordinal)


    def exitPythonPromptoIdentifier(self, ctx: MParser.PythonPromptoIdentifierContext):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, PythonIdentifierExpression(name))


    def exitPythonPrimaryExpression(self, ctx: MParser.PythonPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonReturnStatement(self, ctx: MParser.PythonReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, True))


    def exitPythonSelectorExpression(self, ctx: MParser.PythonSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.child)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)


    def exitPythonSelfExpression(self, ctx: MParser.PythonSelfExpressionContext):
        self.setNodeValue(ctx, PythonSelfExpression())


    def exitPythonStatement(self, ctx: MParser.PythonStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, False))


    def exitPythonTextLiteral(self, ctx: MParser.PythonTextLiteralContext):
        self.setNodeValue(ctx, PythonTextLiteral(ctx.getText()))


    def exitRaise_statement(self, ctx: MParser.Raise_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, RaiseStatement(exp))


    def exitRaiseStatement(self, ctx: MParser.RaiseStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitRange_literal(self, ctx: MParser.Range_literalContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))


    def exitRead_all_expression(self, ctx: MParser.Read_all_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadAllExpression(source))


    def exitRead_blob_expression(self, ctx: MParser.Read_blob_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadBlobExpression(source))


    def exitRead_one_expression(self, ctx: MParser.Read_one_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadOneExpression(source))


    def exitRead_statement(self, ctx: MParser.Read_statementContext):
        source = self.getNodeValue(ctx.source)
        thenWith = ThenWith.OrEmpty(self.getNodeValue(ctx.then()))
        self.setNodeValue(ctx, ReadStatement(source, thenWith))


    def exitReadStatement(self, ctx: MParser.ReadStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitResource_declaration(self, ctx: MParser.Resource_declarationContext):
        decl = self.getNodeValue(ctx.native_resource_declaration())
        self.setNodeValue(ctx, decl)


    def exitReturn_statement(self, ctx: MParser.Return_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ReturnStatement(exp))


    def exitReturnStatement(self, ctx: MParser.ReturnStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitRootInstance(self, ctx: MParser.RootInstanceContext):
        name = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, VariableInstance(name))


    def exitSelectableExpression(self, ctx: MParser.SelectableExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        self.setNodeValue(ctx, parent)


    def exitSelectorExpression(self, ctx: MParser.SelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)


    def exitMember_method_declaration_list(self, ctx: MParser.Member_method_declaration_listContext):
        items = MethodDeclarationList()
        for rule in ctx.member_method_declaration():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitSetter_method_declaration(self, ctx: MParser.Setter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, SetterMethodDeclaration(name, stmts))


    def exitSetType(self, ctx: MParser.SetTypeContext):
        typ = self.getNodeValue(ctx.s)
        self.setNodeValue(ctx, SetType(typ))


    def exitSingleton_category_declaration(self, ctx: MParser.Singleton_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        methods = self.getNodeValue(ctx.methods)
        self.setNodeValue(ctx, SingletonCategoryDeclaration(name, attrs, methods))


    def exitSingletonCategoryDeclaration(self, ctx: MParser.SingletonCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitSliceFirstAndLast(self, ctx: MParser.SliceFirstAndLastContext):
        first = self.getNodeValue(ctx.first)
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(first, last))


    def exitSliceFirstOnly(self, ctx: MParser.SliceFirstOnlyContext):
        first = self.getNodeValue(ctx.first)
        self.setNodeValue(ctx, SliceSelector(first, None))


    def exitSliceLastOnly(self, ctx: MParser.SliceLastOnlyContext):
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(None, last))


    def exitSliceSelector(self, ctx: MParser.SliceSelectorContext):
        xslice = self.getNodeValue(ctx.xslice)
        self.setNodeValue(ctx, xslice)


    def exitStoreStatement(self, ctx: MParser.StoreStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitStore_statement(self, ctx: MParser.Store_statementContext):
        to_del = self.getNodeValue(ctx.to_del)
        to_add = self.getNodeValue(ctx.to_add)
        with_meta = self.getNodeValue(ctx.with_meta)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = DeleteAndStoreStatement(to_del, to_add, with_meta, stmts)
        self.setNodeValue(ctx, stmt)


    def exitSorted_expression(self, ctx: MParser.Sorted_expressionContext):
        source = self.getNodeValue(ctx.source)
        desc = ctx.DESC() is not None
        key = self.getNodeValue(ctx.key)
        self.setNodeValue(ctx, SortedExpression(source, desc, key))


    def exitSorted_key(self, ctx: MParser.Sorted_keyContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitStatement_list(self, ctx: MParser.Statement_listContext):
        items = StatementList()
        for rule in ctx.statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitSuperExpression(self, ctx: MParser.SuperExpressionContext):
        self.setNodeValue(ctx, SuperExpression())


    def exitSwitch_statement(self, ctx: MParser.Switch_statementContext):
        exp = self.getNodeValue(ctx.exp)
        cases = self.getNodeValue(ctx.cases)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = SwitchStatement(exp)
        stmt.setSwitchCases(cases)
        stmt.setDefaultCase(stmts)
        self.setNodeValue(ctx, stmt)


    def exitSwitch_case_statement_list(self, ctx: MParser.Switch_case_statement_listContext):
        items = SwitchCaseList()
        for rule in ctx.switch_case_statement():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitSwitchStatement(self, ctx: MParser.SwitchStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitSymbol_identifier(self, ctx: MParser.Symbol_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitSymbolIdentifier(self, ctx: MParser.SymbolIdentifierContext):
        name = self.getNodeValue(ctx.symbol_identifier())
        self.setNodeValue(ctx, name)


    def exitSymbolLiteral(self, ctx: MParser.SymbolLiteralContext):
        name = ctx.getText()
        self.setNodeValue(ctx, SymbolExpression(name))


    def exitSymbols_token(self, ctx: MParser.Symbols_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitTernaryExpression(self, ctx):
        condition = self.getNodeValue(ctx.test)
        ifTrue = self.getNodeValue(ctx.ifTrue)
        ifFalse = self.getNodeValue(ctx.ifFalse)
        exp = TernaryExpression(condition, ifTrue, ifFalse)
        self.setNodeValue(ctx, exp)


    def exitTextLiteral(self, ctx: MParser.TextLiteralContext):
        self.setNodeValue(ctx, TextLiteral(ctx.getText()))


    def exitTest_method_declaration(self, ctx: MParser.Test_method_declarationContext):
        name = ctx.name.text
        stmts = self.getNodeValue(ctx.stmts)
        exps = self.getNodeValue(ctx.exps)
        errorName = self.getNodeValue(ctx.error)
        error = None if errorName is None else SymbolExpression(errorName)
        self.setNodeValue(ctx, TestMethodDeclaration(name, stmts, exps, error))


    def exitTextType(self, ctx: MParser.TextTypeContext):
        self.setNodeValue(ctx, TextType.instance)


    def exitHtmlType(self, ctx: MParser.HtmlTypeContext):
        self.setNodeValue(ctx, HtmlType.instance)


    def exitThisExpression(self, ctx: MParser.ThisExpressionContext):
        self.setNodeValue(ctx, ThisExpression())


    def exitTimeLiteral(self, ctx: MParser.TimeLiteralContext):
        self.setNodeValue(ctx, TimeLiteral(ctx.getText()))


    def exitTimeType(self, ctx: MParser.TimeTypeContext):
        self.setNodeValue(ctx, TimeType.instance)


    def exitTry_statement(self, ctx: MParser.Try_statementContext):
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


    def exitTryStatement(self, ctx: MParser.TryStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitTuple_literal(self, ctx: MParser.Tuple_literalContext):
        mutable = ctx.MUTABLE() is not None
        items = self.getNodeValue(ctx.expression_tuple())
        items = items if items is not None else []
        value = TupleLiteral(mutable, items)
        self.setNodeValue(ctx, value)


    def exitSet_literal(self, ctx: MParser.Set_literalContext):
        items = self.getNodeValue(ctx.expression_list())
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    def exitType_identifier(self, ctx: MParser.Type_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitType_identifier_list(self, ctx: MParser.Type_identifier_listContext):
        items = IdentifierList()
        for rule in ctx.type_identifier():
            item = self.getNodeValue(rule)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitType_literal(self, ctx: MParser.Type_literalContext):
        typ = self.getNodeValue(ctx.category_or_any_type())
        self.setNodeValue(ctx, TypeLiteral(typ))


    def exitTypeIdentifier(self, ctx: MParser.TypeIdentifierContext):
        name = self.getNodeValue(ctx.type_identifier())
        self.setNodeValue(ctx, name)


    def exitTypeLiteral(self, ctx: MParser.TypeLiteralContext):
        typ = self.getNodeValue(ctx.type_literal())
        self.setNodeValue(ctx, typ)


    def exitTypeType(self, ctx:MParser.TypeTypeContext):
        typ = self.getNodeValue(ctx.t)
        self.setNodeValue(ctx, TypeType(typ))


    def exitTyped_argument(self, ctx: MParser.Typed_argumentContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        exp = self.getNodeValue(ctx.value)
        from prompto.param.ExtendedParameter import ExtendedParameter
        arg = CategoryParameter(typ, name) if attrs is None else ExtendedParameter(typ, name, attrs)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitUUIDType(self, ctx: MParser.UUIDTypeContext):
        self.setNodeValue(ctx, UUIDType.instance)


    def exitUUIDLiteral(self, ctx: MParser.UUIDLiteralContext):
        self.setNodeValue(ctx, UUIDLiteral(ctx.getText()))


    def exitValue_token(self, ctx: MParser.Value_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitAttribute_identifier(self, ctx: MParser.Attribute_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitVariable_identifier(self, ctx: MParser.Variable_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitVariableIdentifier(self, ctx: MParser.VariableIdentifierContext):
        name = self.getNodeValue(ctx.variable_identifier())
        self.setNodeValue(ctx, name)


    def exitAttribute_identifier_list(self, ctx: MParser.Attribute_identifier_listContext):
        items = IdentifierList()
        for c in ctx.attribute_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitVariable_identifier_list(self, ctx: MParser.Variable_identifier_listContext):
        items = IdentifierList()
        for c in ctx.variable_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitWhile_statement(self, ctx: MParser.While_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WhileStatement(exp, stmts))


    def exitWhileStatement(self, ctx: MParser.WhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_singleton_statement(self, ctx: MParser.With_singleton_statementContext):
        name = self.getNodeValue(ctx.typ)
        typ = CategoryType(name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithSingletonStatement(typ, stmts))


    def exitWithSingletonStatement(self, ctx: MParser.WithSingletonStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_resource_statement(self, ctx: MParser.With_resource_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithResourceStatement(stmt, stmts))


    def exitWithResourceStatement(self, ctx: MParser.WithResourceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWrite_statement(self, ctx: MParser.Write_statementContext):
        what = self.getNodeValue(ctx.what)
        target = self.getNodeValue(ctx.target)
        thenWith = self.getNodeValue(ctx.then())
        self.setNodeValue(ctx, WriteStatement(what, target, thenWith))


    def exitWriteStatement(self, ctx: MParser.WriteStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitJsxChild(self, ctx: MParser.JsxChildContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.jsx))


    def exitJsxCode(self, ctx: MParser.JsxCodeContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JsxCode(exp, None))


    def exitJsxExpression(self, ctx: MParser.JsxExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitJsxElement(self, ctx: MParser.JsxElementContext):
        elem = self.getNodeValue(ctx.opening)
        closing = self.getNodeValue(ctx.closing)
        elem.setClosing(closing)
        children = self.getNodeValue(ctx.children_)
        elem.setChildren(children)
        self.setNodeValue(ctx, elem)


    def exitJsxLiteral(self, ctx: MParser.JsxLiteralContext):
        text = ctx.getText()
        self.setNodeValue(ctx, JsxLiteral(text))


    def exitJsxSelfClosing(self, ctx: MParser.JsxSelfClosingContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.jsx))


    def exitJsxText(self, ctx: MParser.JsxTextContext):
        text = ParserUtils.getFullText(ctx.text)
        self.setNodeValue(ctx, JsxText(text))


    def exitJsxValue(self, ctx: MParser.JsxValueContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JsxExpression(exp))


    def exitJsx_attribute(self, ctx: MParser.Jsx_attributeContext):
        name = self.getNodeValue(ctx.name)
        value = self.getNodeValue(ctx.value)
        suite = self.getWhiteSpacePlus(ctx.ws_plus())
        self.setNodeValue(ctx, JsxProperty(name, value, suite))


    def exitJsx_children(self, ctx: MParser.Jsx_childrenContext):
        expressions = [self.getNodeValue(cx) for cx in ctx.jsx_child()]
        self.setNodeValue(ctx, expressions)


    def exitJsx_closing(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JsxClosing(name, None))


    def exitJsx_element_name(self, ctx: MParser.Jsx_element_nameContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJsx_expression(self, ctx: MParser.Jsx_expressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.getChild(0)))


    def exitJsx_fragment(self, ctx: MParser.Jsx_fragmentContext):
        suite = self.getWhiteSpacePlus(ctx.ws_plus(0))
        fragment = JsxFragment(suite)
        fragment.children = self.getNodeValue(ctx.children_)
        self.setNodeValue(ctx, fragment)


    def exitJsx_identifier(self, ctx: MParser.Jsx_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJsx_opening(self, ctx: MParser.Jsx_openingContext):
        name = self.getNodeValue(ctx.name)
        suite = self.getWhiteSpacePlus(ctx.ws_plus())
        attributes = [self.getNodeValue(cx) for cx in ctx.jsx_attribute()]
        self.setNodeValue(ctx, JsxElement(name, suite, attributes, None))


    def exitJsx_self_closing(self, ctx: MParser.Jsx_self_closingContext):
        name = self.getNodeValue(ctx.name)
        suite = self.getWhiteSpacePlus(ctx.ws_plus())
        attributes = [self.getNodeValue(cx) for cx in ctx.jsx_attribute()]
        self.setNodeValue(ctx, JsxSelfClosing(name, suite, attributes, None))


    def exitCssExpression(self, ctx: MParser.CssExpressionContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.exp))


    def exitCss_expression(self, ctx: MParser.Css_expressionContext):
        exp = CssExpression()
        [exp.addField(self.getNodeValue(cx)) for cx in ctx.css_field()]
        self.setNodeValue(ctx, exp)


    def exitCss_field(self, ctx: MParser.Css_fieldContext):
        name = ctx.name.getText()
        values = [self.getNodeValue(x) for x in ctx.css_value()]
        self.setNodeValue(ctx, CssField(name, values))


    def exitCssText(self, ctx: MParser.CssTextContext):
        text = self.input.getText(ctx.text.start, ctx.text.stop)
        self.setNodeValue(ctx, CssText(text))


    def exitCssValue(self, ctx: MParser.CssValueContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CssCode(exp))
