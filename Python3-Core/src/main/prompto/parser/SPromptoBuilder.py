from curses.ascii import SP

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import ParseTree

from prompto.argument.CategoryArgument import CategoryArgument
from prompto.argument.CodeArgument import CodeArgument
from prompto.argument.UnresolvedArgument import UnresolvedArgument
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
from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.declaration.DeclarationList import DeclarationList
from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from prompto.declaration.GetterMethodDeclaration import GetterMethodDeclaration
from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from prompto.declaration.NativeGetterMethodDeclaration import NativeGetterMethodDeclaration
from prompto.declaration.NativeMethodDeclaration import NativeMethodDeclaration
from prompto.declaration.NativeResourceDeclaration import NativeResourceDeclaration
from prompto.declaration.NativeSetterMethodDeclaration import NativeSetterMethodDeclaration
from prompto.declaration.OperatorMethodDeclaration import OperatorMethodDeclaration
from prompto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration
from prompto.declaration.TestMethodDeclaration import TestMethodDeclaration
from prompto.expression.AddExpression import AddExpression
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
from prompto.expression.FetchAllExpression import FetchAllExpression
from prompto.expression.FetchExpression import FetchExpression
from prompto.expression.FetchOneExpression import FetchOneExpression
from prompto.expression.IntDivideExpression import IntDivideExpression
from prompto.expression.ItemSelector import ItemSelector
from prompto.expression.IteratorExpression import IteratorExpression
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.MethodExpression import MethodExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.expression.MinusExpression import MinusExpression
from prompto.expression.ModuloExpression import ModuloExpression
from prompto.expression.MultiplyExpression import MultiplyExpression
from prompto.expression.NativeSymbol import NativeSymbol
from prompto.expression.NotExpression import NotExpression
from prompto.expression.OrExpression import OrExpression
from prompto.expression.ParenthesisExpression import ParenthesisExpression
from prompto.expression.ReadExpression import ReadExpression
from prompto.expression.SliceSelector import SliceSelector
from prompto.expression.SortedExpression import SortedExpression
from prompto.expression.SubtractExpression import SubtractExpression
from prompto.expression.SymbolExpression import SymbolExpression
from prompto.expression.TernaryExpression import TernaryExpression
from prompto.expression.ThisExpression import ThisExpression
from prompto.expression.TypeExpression import TypeExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.grammar.ArgumentAssignment import ArgumentAssignment
from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from prompto.grammar.ArgumentList import ArgumentList
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
from prompto.literal.BooleanLiteral import BooleanLiteral
from prompto.literal.CharacterLiteral import CharacterLiteral
from prompto.literal.DateLiteral import DateLiteral
from prompto.literal.DateTimeLiteral import DateTimeLiteral
from prompto.literal.DecimalLiteral import DecimalLiteral
from prompto.literal.DictEntry import DictEntry
from prompto.literal.DictEntryList import DictEntryList
from prompto.literal.DictLiteral import DictLiteral
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
from prompto.parser.Dialect import Dialect
from prompto.parser.SParser import SParser
from prompto.parser.SParserListener import SParserListener
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
from prompto.python.PythonStatement import PythonStatement
from prompto.python.PythonTextLiteral import PythonTextLiteral
from prompto.statement.AssignInstanceStatement import AssignInstanceStatement
from prompto.statement.AssignTupleStatement import AssignTupleStatement
from prompto.statement.AssignVariableStatement import AssignVariableStatement
from prompto.statement.AtomicSwitchCase import AtomicSwitchCase
from prompto.statement.CollectionSwitchCase import CollectionSwitchCase
from prompto.statement.CommentStatement import CommentStatement
from prompto.statement.DeclarationStatement import DeclarationStatement
from prompto.statement.DoWhileStatement import DoWhileStatement
from prompto.statement.ForEachStatement import ForEachStatement
from prompto.statement.IfStatement import IfElement, IfElementList, IfStatement
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
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.DictType import DictType
from prompto.type.DocumentType import DocumentType
from prompto.type.IntegerType import IntegerType
from prompto.type.IteratorType import IteratorType
from prompto.type.ListType import ListType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType


class SPromptoBuilder(SParserListener):

    def __init__(self, parser:SParser):
        self.input = parser.getTokenStream()
        self.path = parser.path
        self.nodeValues = dict()

    def getNodeValue(self, node:ParseTree) -> object:
        return self.nodeValues.get(node, None)

    def setNodeValue(self, node:ParseTree, value:object):
        self.nodeValues[node] = value
        if isinstance(value, Section):
            self.buildSection(node, value)

    def buildSection(self, node:ParserRuleContext, section:Section):
        first = self.findFirstValidToken(node.start.tokenIndex)
        last = self.findLastValidToken(node.stop.tokenIndex)
        section.setFrom(self.path, first, last, Dialect.S)

    def findFirstValidToken(self, idx:int):
        if idx == -1:  # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx < len(self.input.tokens):
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


    def exitAbstract_method_declaration(self, ctx:SParser.Abstract_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, typ))


    def exitAbstractMethod(self, ctx:SParser.AbstractMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitAddExpression(self, ctx:SParser.AddExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        exp = AddExpression(left, right) if ctx.op.type == SParser.PLUS else SubtractExpression(left, right)
        self.setNodeValue(ctx, exp)


    def exitAndExpression(self, ctx:SParser.AndExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, AndExpression(left, right))


    def exitAnyArgumentType(self, ctx:SParser.AnyArgumentTypeContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, typ)


    def exitAnyDictType(self, ctx:SParser.AnyDictTypeContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, DictType(typ))


    def exitAnyListType(self, ctx:SParser.AnyListTypeContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, ListType(typ))


    def exitAnyType(self, ctx:SParser.AnyTypeContext):
        self.setNodeValue(ctx, AnyType.instance)


    def exitArgument_assignment(self, ctx:SParser.Argument_assignmentContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = UnresolvedArgument(name)
        item = ArgumentAssignment(arg, exp)
        self.setNodeValue(ctx, item)


    def exitArgumentAssignmentList(self, ctx:SParser.ArgumentAssignmentListContext):
        item = self.getNodeValue(ctx.item)
        items = ArgumentAssignmentList(item=item)
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentListItem(self, ctx:SParser.ArgumentAssignmentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitArgumentList(self, ctx:SParser.ArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, ArgumentList(item))


    def exitArgumentListItem(self, ctx:SParser.ArgumentListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitAssertion(self, ctx:SParser.AssertionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAssertionList(self, ctx:SParser.AssertionListContext):
        item = self.getNodeValue(ctx.item)
        items = [ item ]
        self.setNodeValue(ctx, items)


    def exitAssertionListItem(self, ctx:SParser.AssertionListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitAssign_instance_statement(self, ctx:SParser.Assign_instance_statementContext):
        inst = self.getNodeValue(ctx.inst)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignInstanceStatement(inst, exp))


    def exitAssign_tuple_statement(self, ctx:SParser.Assign_tuple_statementContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmt = AssignTupleStatement(items)
        stmt.setExpression(exp)
        self.setNodeValue(ctx, stmt)


    def exitAssign_variable_statement(self, ctx:SParser.Assign_variable_statementContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignVariableStatement(name, exp))


    def exitAssignInstanceStatement(self, ctx:SParser.AssignInstanceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitAssignTupleStatement(self, ctx:SParser.AssignTupleStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitAtomicLiteral(self, ctx:SParser.AtomicLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAtomicSwitchCase(self, ctx:SParser.AtomicSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(exp, stmts))


    def exitAttribute_declaration(self, ctx:SParser.Attribute_declarationContext):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        match = self.getNodeValue(ctx.match)
        decl = AttributeDeclaration(name, typ, match)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)



    def exitBlobExpression(self, ctx:SParser.BlobExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitBlob_expression(self, ctx:SParser.Blob_expressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, BlobExpression(exp))


    def exitBlobType(self, ctx:SParser.BlobTypeContext):
        self.setNodeValue(ctx, BlobType.instance)


    def exitBooleanLiteral(self, ctx:SParser.BooleanLiteralContext):
        self.setNodeValue(ctx, BooleanLiteral(ctx.t.text))


    def exitBooleanType(self, ctx:SParser.BooleanTypeContext):
        self.setNodeValue(ctx, BooleanType.instance)


    def exitCallableRoot(self, ctx:SParser.CallableRootContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))


    def exitCastExpression(self, ctx:SParser.CastExpressionContext):
        typ = self.getNodeValue(ctx.right)
        exp = self.getNodeValue(ctx.left)
        self.setNodeValue(ctx, CastExpression(exp, typ))


    def exitCatchAtomicStatement(self, ctx:SParser.CatchAtomicStatementContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, AtomicSwitchCase(SymbolExpression(name), stmts))


    def exitCatchCollectionStatement(self, ctx:SParser.CatchCollectionStatementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCatchStatementList(self, ctx:SParser.CatchStatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))


    def exitCatchStatementListItem(self, ctx:SParser.CatchStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)


    def exitCategory_symbol(self, ctx:SParser.Category_symbolContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CategorySymbol(name, args))


    def exitCategory_type(self, ctx:SParser.Category_typeContext):
        name = ctx.getText()
        self.setNodeValue(ctx, CategoryType(name))


    def exitCategoryArgumentType(self, ctx:SParser.CategoryArgumentTypeContext):
        typ = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, typ)


    def exitNative_member_method_declaration(self, ctx:SParser.Native_member_method_declarationContext):
        decl = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, decl)


    def exitNativeCategoryMethodList(self, ctx:SParser.NativeCategoryMethodListContext):
        item = self.getNodeValue(ctx.item)
        items = MethodDeclarationList(item)
        self.setNodeValue(ctx, items)


    def exitNativeCategoryMethodListItem(self, ctx:SParser.NativeCategoryMethodListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitMember_method_declaration(self, ctx:SParser.Member_method_declarationContext):
        decl = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, decl)


    def exitCategoryMethodList(self, ctx:SParser.CategoryMethodListContext):
        item = self.getNodeValue(ctx.item)
        items = MethodDeclarationList(item)
        self.setNodeValue(ctx, items)


    def exitCategoryMethodListItem(self, ctx:SParser.CategoryMethodListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitCategorySymbolList(self, ctx:SParser.CategorySymbolListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CategorySymbolList(item))


    def exitCategorySymbolListItem(self, ctx:SParser.CategorySymbolListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitCategoryType(self, ctx:SParser.CategoryTypeContext):
        typ = self.getNodeValue(ctx.c)
        self.setNodeValue(ctx, typ)


    def exitCharacterLiteral(self, ctx:SParser.CharacterLiteralContext):
        self.setNodeValue(ctx, CharacterLiteral(ctx.t.text))


    def exitCharacterType(self, ctx:SParser.CharacterTypeContext):
        self.setNodeValue(ctx, CharacterType.instance)


    def exitChildInstance(self, ctx:SParser.ChildInstanceContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitClosure_expression(self, ctx:SParser.Closure_expressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodExpression(name))


    def exitClosureExpression(self, ctx:SParser.ClosureExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitClosureStatement(self, ctx:SParser.ClosureStatementContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, DeclarationStatement(decl))


    def exitCode_argument(self, ctx:SParser.Code_argumentContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CodeArgument(name))


    def exitCode_type(self, ctx:SParser.Code_typeContext):
        self.setNodeValue(ctx, CodeType.instance)


    def exitCodeArgument(self, ctx:SParser.CodeArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitCodeExpression(self, ctx:SParser.CodeExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CodeExpression(exp))


    def exitCodeType(self, ctx:SParser.CodeTypeContext):
        self.setNodeValue(ctx, CodeType.instance)


    def exitCollectionLiteral(self, ctx:SParser.CollectionLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCollectionSwitchCase(self, ctx:SParser.CollectionSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))


    def exitCommentStatement(self, ctx:SParser.CommentStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.comment_statement()))


    def exitComment_statement(self, ctx:SParser.Comment_statementContext):
        self.setNodeValue(ctx, CommentStatement(ctx.getText()))


    def exitConcrete_category_declaration(self, ctx:SParser.Concrete_category_declarationContext):
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


    def exitConcrete_method_declaration(self, ctx:SParser.Concrete_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ConcreteMethodDeclaration(name, args, typ, stmts))


    def exitConcreteCategoryDeclaration(self, ctx:SParser.ConcreteCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitConcreteMethod(self, ctx:SParser.ConcreteMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitConstructor_expression(self, ctx:SParser.Constructor_expressionContext):
        typ = self.getNodeValue(ctx.typ)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, ConstructorExpression(typ, args))


    def exitConstructorExpression(self, ctx:SParser.ConstructorExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitContainsAllExpression(self, ctx:SParser.ContainsAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ALL, right))


    def exitContainsAnyExpression(self, ctx:SParser.ContainsAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ANY, right))


    def exitContainsExpression(self, ctx:SParser.ContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS, right))

    def exitCsharp_primary_expression(self, ctx:SParser.Csharp_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)


    def exitCsharp_identifier(self, ctx:SParser.Csharp_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitCsharp_method_expression(self, ctx:SParser.Csharp_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CSharpMethodExpression(name, args))


    def exitCSharpArgumentList(self, ctx:SParser.CSharpArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CSharpExpressionList(item))


    def exitCSharpArgumentListItem(self, ctx:SParser.CSharpArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)


    def exitCSharpBooleanLiteral(self, ctx:SParser.CSharpBooleanLiteralContext):
        self.setNodeValue(ctx, CSharpBooleanLiteral(ctx.getText()))


    def exitCSharpCategoryBinding(self, ctx:SParser.CSharpCategoryBindingContext):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, CSharpNativeCategoryBinding(map))


    def exitCSharpCharacterLiteral(self, ctx:SParser.CSharpCharacterLiteralContext):
        self.setNodeValue(ctx, CSharpCharacterLiteral(ctx.getText()))


    def exitCSharpChildIdentifier(self, ctx:SParser.CSharpChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = CSharpIdentifierExpression(parent, name)
        self.setNodeValue(ctx, child)

    def exitCsharp_this_expression(self, ctx:SParser.Csharp_this_expressionContext):
        self.setNodeValue(ctx, CSharpThisExpression())

    def exitCSharpDecimalLiteral(self, ctx:SParser.CSharpDecimalLiteralContext):
        self.setNodeValue(ctx, CSharpDecimalLiteral(ctx.getText()))


    def exitCSharpIdentifier(self, ctx:SParser.CSharpIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))


    def exitCSharpIntegerLiteral(self, ctx:SParser.CSharpIntegerLiteralContext):
        self.setNodeValue(ctx, CSharpIntegerLiteral(ctx.getText()))


    def exitCSharpMethodExpression(self, ctx:SParser.CSharpMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpNativeStatement(self, ctx:SParser.CSharpNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, CSharpNativeCall(stmt))


    def exitCSharpPromptoIdentifier(self, ctx:SParser.CSharpPromptoIdentifierContext):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))


    def exitCSharpPrimaryExpression(self, ctx:SParser.CSharpPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpReturnStatement(self, ctx:SParser.CSharpReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, True))


    def exitCSharpSelectorExpression(self, ctx:SParser.CSharpSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitCSharpStatement(self, ctx:SParser.CSharpStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp, False))


    def exitCSharpTextLiteral(self, ctx:SParser.CSharpTextLiteralContext):
        self.setNodeValue(ctx, CSharpTextLiteral(ctx.getText()))


    def exitDateLiteral(self, ctx:SParser.DateLiteralContext):
        self.setNodeValue(ctx, DateLiteral(ctx.t.text))


    def exitDateTimeLiteral(self, ctx:SParser.DateTimeLiteralContext):
        self.setNodeValue(ctx, DateTimeLiteral(ctx.t.text))


    def exitDateTimeType(self, ctx:SParser.DateTimeTypeContext):
        self.setNodeValue(ctx, DateTimeType.instance)


    def exitDateType(self, ctx:SParser.DateTypeContext):
        self.setNodeValue(ctx, DateType.instance)


    def exitDecimalLiteral(self, ctx:SParser.DecimalLiteralContext):
        self.setNodeValue(ctx, DecimalLiteral(ctx.t.text))


    def exitDecimalType(self, ctx:SParser.DecimalTypeContext):
        self.setNodeValue(ctx, DecimalType.instance)


    def exitDeclaration(self, ctx:SParser.DeclarationContext):
        stmts = None
        if ctx.comment_statement() is not None:
            stmts = [ self.getNodeValue(ctx_) for ctx_ in ctx.comment_statement() ]
        ctx_ = ctx.attribute_declaration()
        if ctx_ is None:
            ctx_ = ctx.category_declaration()
        if ctx_ is None:
            ctx_ = ctx.enum_declaration()
        if ctx_ is None:
            ctx_ = ctx.method_declaration()
        if ctx_ is None:
            ctx_ = ctx.resource_declaration()
        decl = self.getNodeValue(ctx_)
        if decl is not None:
            decl.comments = stmts
            self.setNodeValue(ctx, decl)


    def exitDeclarationList(self, ctx:SParser.DeclarationListContext):
        item = self.getNodeValue(ctx.item)
        items = DeclarationList(item)
        self.setNodeValue(ctx, items)


    def exitDeclarationListItem(self, ctx:SParser.DeclarationListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitDerived_list(self, ctx:SParser.Derived_listContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitDict_entry(self, ctx:SParser.Dict_entryContext):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DictEntry(key, value)
        self.setNodeValue(ctx, entry)


    def exitDict_literal(self, ctx:SParser.Dict_literalContext):
        items = self.getNodeValue(ctx.items)
        value = DictLiteral(items)
        self.setNodeValue(ctx, value)


    def exitDictEntryList(self, ctx:SParser.DictEntryListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, DictEntryList(item))


    def exitDictEntryListItem(self, ctx:SParser.DictEntryListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitDictLiteral(self, ctx:SParser.DictLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitDictType(self, ctx:SParser.DictTypeContext):
        typ = self.getNodeValue(ctx.d)
        self.setNodeValue(ctx, DictType(typ))


    def exitDivideExpression(self, ctx:SParser.DivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, DivideExpression(left, right))


    def exitDo_while_statement(self, ctx:SParser.Do_while_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, DoWhileStatement(exp, stmts))


    def exitDocument_expression(self, ctx:SParser.Document_expressionContext):
        exp = self.getNodeValue(ctx.expression())
        self.setNodeValue(ctx, DocumentExpression(exp))


    def exitDocumentType(self, ctx:SParser.DocumentTypeContext):
        self.setNodeValue(ctx, DocumentType.instance)


    def exitDocumentExpression(self, ctx:SParser.DocumentExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitDoWhileStatement(self, ctx:SParser.DoWhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitElseIfStatementList(self, ctx:SParser.ElseIfStatementListContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        self.setNodeValue(ctx, IfElementList(elem))


    def exitElseIfStatementListItem(self, ctx:SParser.ElseIfStatementListItemContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        elem = IfElement(exp, stmts)
        items.add(elem)
        self.setNodeValue(ctx, items)


    def exitEnum_category_declaration(self, ctx:SParser.Enum_category_declarationContext):
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


    def exitEnum_native_declaration(self, ctx:SParser.Enum_native_declarationContext):
        name = self.getNodeValue(ctx.name)
        typ = self.getNodeValue(ctx.typ)
        symbols = self.getNodeValue(ctx.symbols)
        self.setNodeValue(ctx, EnumeratedNativeDeclaration(name, typ, symbols))


    def exitEnumCategoryDeclaration(self, ctx:SParser.EnumCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitEnumNativeDeclaration(self, ctx:SParser.EnumNativeDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitEqualsExpression(self, ctx:SParser.EqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.EQUALS, right))


    def exitExecuteExpression(self, ctx:SParser.ExecuteExpressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, ExecuteExpression(name))


    def exitExpressionAssignmentList(self, ctx:SParser.ExpressionAssignmentListContext):
        exp = self.getNodeValue(ctx.exp)
        items = ArgumentAssignmentList()
        items.append(ArgumentAssignment(None, exp))
        self.setNodeValue(ctx, items)


    def exitFetchExpression(self, ctx:SParser.FetchExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitFetchList(self, ctx:SParser.FetchListContext):
        itemName = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        filter = self.getNodeValue(ctx.xfilter)
        self.setNodeValue(ctx, FetchExpression(itemName, source, filter))


    def exitFetchOne (self, ctx:SParser.FetchOneContext):
        category = self.getNodeValue(ctx.typ)
        xfilter = self.getNodeValue(ctx.xfilter)
        self.setNodeValue(ctx, FetchOneExpression(category, xfilter))


    def exitFetchAll (self, ctx:SParser.FetchAllContext):
        category = self.getNodeValue(ctx.typ)
        xfilter = self.getNodeValue(ctx.xfilter)
        start = self.getNodeValue(ctx.xstart)
        stop = self.getNodeValue(ctx.xstop)
        orderBy = self.getNodeValue(ctx.xorder)
        self.setNodeValue(ctx, FetchAllExpression(category, xfilter, start, stop, orderBy))

    def exitFor_each_statement(self, ctx:SParser.For_each_statementContext):
        name1 = self.getNodeValue(ctx.name1)
        name2 = self.getNodeValue(ctx.name2)
        source = self.getNodeValue(ctx.source)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ForEachStatement(name1, name2, source, stmts))


    def exitForEachStatement(self, ctx:SParser.ForEachStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitFullDeclarationList(self, ctx:SParser.FullDeclarationListContext):
        items = self.getNodeValue(ctx.items)
        if items is None:
            items = DeclarationList()
        self.setNodeValue(ctx, items)


    def exitGetter_method_declaration(self, ctx:SParser.Getter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, GetterMethodDeclaration(name, stmts))


    def exitNative_setter_declaration(self, ctx:SParser.Native_setter_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeSetterMethodDeclaration(name, stmts))



    def exitNative_getter_declaration(self, ctx:SParser.Native_getter_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeGetterMethodDeclaration(name, stmts))


    def exitGreaterThanExpression(self, ctx:SParser.GreaterThanExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GT, right))


    def exitGreaterThanOrEqualExpression(self, ctx:SParser.GreaterThanOrEqualExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.GTE, right))


    def exitHexadecimalLiteral(self, ctx:SParser.HexadecimalLiteralContext):
        self.setNodeValue(ctx, HexaLiteral(ctx.t.text))


    def exitIdentifierExpression(self, ctx:SParser.IdentifierExpressionContext):
        name = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))


    def exitIf_statement(self, ctx:SParser.If_statementContext):
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


    def exitIfStatement(self, ctx:SParser.IfStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitInExpression(self, ctx:SParser.InExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.IN, right))


    def exitInstanceExpression(self, ctx:SParser.InstanceExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitIntDivideExpression(self, ctx:SParser.IntDivideExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, IntDivideExpression(left, right))


    def exitIntegerLiteral(self, ctx:SParser.IntegerLiteralContext):
        self.setNodeValue(ctx, IntegerLiteral(ctx.t.text))


    def exitIntegerType(self, ctx:SParser.IntegerTypeContext):
        self.setNodeValue(ctx, IntegerType.instance)


    def exitIsATypeExpression(self, ctx:SParser.IsATypeExpressionContext):
        typ = self.getNodeValue(ctx.typ)
        exp = TypeExpression(typ)
        self.setNodeValue(ctx, exp)

    def exitIsOtherExpression(self, ctx:SParser.IsOtherExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitIsExpression(self, ctx:SParser.IsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        op = EqOp.IS_A if isinstance(right, TypeExpression) else EqOp.IS
        self.setNodeValue(ctx, EqualsExpression(left, op, right))


    def exitIsNotExpression(self, ctx:SParser.IsNotExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        op = EqOp.IS_NOT_A if isinstance(right, TypeExpression) else EqOp.IS_NOT
        self.setNodeValue(ctx, EqualsExpression(left, op, right))


    def exitItemInstance(self, ctx:SParser.ItemInstanceContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemInstance(None, exp))


    def exitItemSelector(self, ctx:SParser.ItemSelectorContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))


    def exitIteratorExpression(self, ctx:SParser.IteratorExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        name = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, IteratorExpression(name, source, exp))


    def exitIteratorType(self, ctx:SParser.IteratorTypeContext):
        typ = self.getNodeValue(ctx.i)
        self.setNodeValue(ctx, IteratorType(typ))


    def exitJava_identifier(self, ctx:SParser.Java_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitJava_item_expression(self, ctx:SParser.Java_item_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaItemExpression(exp))


    def exitJava_method_expression(self, ctx:SParser.Java_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, JavaMethodExpression(name, args))


    def exitJava_parenthesis_expression(self, ctx:SParser.Java_parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaArgumentList(self, ctx:SParser.JavaArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, JavaExpressionList(item))


    def exitJavaArgumentListItem(self, ctx:SParser.JavaArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)


    def exitJavaBooleanLiteral(self, ctx:SParser.JavaBooleanLiteralContext):
        self.setNodeValue(ctx, JavaBooleanLiteral(ctx.getText()))


    def exitJavaCategoryBinding(self, ctx:SParser.JavaCategoryBindingContext):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, JavaNativeCategoryBinding(map))


    def exitJavaCharacterLiteral(self, ctx:SParser.JavaCharacterLiteralContext):
        self.setNodeValue(ctx, JavaCharacterLiteral(ctx.getText()))


    def exitJavaChildClassIdentifier(self, ctx:SParser.JavaChildClassIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        child = JavaIdentifierExpression(parent, ctx.name.getText())
        self.setNodeValue(ctx, child)

    def exitJava_primary_expression(self, ctx:SParser.Java_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)

    def exitJavaChildIdentifier(self, ctx:SParser.JavaChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = JavaIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)


    def exitJavaClassIdentifier(self, ctx:SParser.JavaClassIdentifierContext):
        klass = self.getNodeValue(ctx.klass)
        self.setNodeValue(ctx, klass)


    def exitJavaDecimalLiteral(self, ctx:SParser.JavaDecimalLiteralContext):
        self.setNodeValue(ctx, JavaDecimalLiteral(ctx.getText()))


    def exitJavaIdentifier(self, ctx:SParser.JavaIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaIdentifierExpression(name))


    def exitJavaIntegerLiteral(self, ctx:SParser.JavaIntegerLiteralContext):
        self.setNodeValue(ctx, JavaIntegerLiteral(ctx.getText()))


    def exitJavaItemExpression(self, ctx:SParser.JavaItemExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaMethodExpression(self, ctx:SParser.JavaMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitJava_this_expression(self, ctx:SParser.Java_this_expressionContext):
        self.setNodeValue(ctx, JavaThisExpression())


    def exitJavaNativeStatement(self, ctx:SParser.JavaNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, JavaNativeCall(stmt))


    def exitJavaPrimaryExpression(self, ctx:SParser.JavaPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaReturnStatement(self, ctx:SParser.JavaReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, True))


    def exitJavascriptBooleanLiteral(self, ctx:SParser.JavascriptBooleanLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptBooleanLiteral(text))


    def exitJavascript_category_binding(self, ctx:SParser.Javascript_category_bindingContext):
        identifier = ctx.identifier().getText()
        module = self.getNodeValue(ctx.javascript_module())
        map = JavaScriptNativeCategoryBinding(identifier, module)
        self.setNodeValue(ctx, map)


    def exitJavascriptCharacterLiteral(self, ctx:SParser.JavascriptCharacterLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptCharacterLiteral(text))


    def exitJavascript_identifier(self, ctx:SParser.Javascript_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)


    def exitJavascript_this_expression(self, ctx:SParser.Javascript_this_expressionContext):
        self.setNodeValue(ctx, JavaScriptThisExpression())


    def exitJavascript_method_expression(self, ctx:SParser.Javascript_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        method = JavaScriptMethodExpression(name)
        args = self.getNodeValue(ctx.args)
        method.arguments = args
        self.setNodeValue(ctx, method)


    def exitJavascript_module(self, ctx:SParser.Javascript_moduleContext):
        ids = []
        for ic in ctx.javascript_identifier():
            ids.append(ic.getText())
        module = JavaScriptModule(ids)
        self.setNodeValue(ctx, module)


    def exitJavascript_native_statement(self, ctx:SParser.Javascript_native_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        stmt.module = module
        self.setNodeValue(ctx, stmt)


    def exitJavascript_new_expression(self, ctx:SParser.Javascript_new_expressionContext):
        method = self.getNodeValue(ctx.javascript_method_expression())
        new = JavaScriptNewExpression(method)
        self.setNodeValue(ctx, new)


    def exitJavascriptArgumentList(self, ctx:SParser.JavascriptArgumentListContext):
        exp = self.getNodeValue(ctx.item)
        list = JavaScriptExpressionList(exp)
        self.setNodeValue(ctx, list)


    def exitJavascriptArgumentListItem(self, ctx:SParser.JavascriptArgumentListItemContext):
        exp = self.getNodeValue(ctx.item)
        list = self.getNodeValue(ctx.items)
        list.add(exp)
        self.setNodeValue(ctx, list)


    def exitJavaScriptCategoryBinding(self, ctx:SParser.JavaScriptCategoryBindingContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.binding))


    def exitJavascript_identifier_expression(self, ctx:SParser.Javascript_identifier_expressionContext):
        name = self.getNodeValue(ctx.name)
        exp = JavaScriptIdentifierExpression(None, name)
        self.setNodeValue(ctx, exp)


    def exitJavascriptDecimalLiteral(self, ctx:SParser.JavascriptDecimalLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptDecimalLiteral(text))


    def exitJavascriptIntegerLiteral(self, ctx:SParser.JavascriptIntegerLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptIntegerLiteral(text))


    def exitJavaScriptMethodExpression(self, ctx:SParser.JavaScriptMethodExpressionContext):
        method = self.getNodeValue(ctx.method)
        self.setNodeValue(ctx, method)


    def exitJavaScriptNativeStatement(self, ctx:SParser.JavaScriptNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, JavaScriptNativeCall(stmt))


    def exitJavaScriptMemberExpression(self, ctx:SParser.JavaScriptMemberExpressionContext):
        name = ctx.name.getText()
        self.setNodeValue(ctx, JavaScriptMemberExpression(name))

    def exitJavascript_primary_expression(self, ctx:SParser.Java_primary_expressionContext):
        exp = self.getNodeValue(ctx.getChild(0))
        self.setNodeValue(ctx, exp)

    def exitJavascriptPrimaryExpression(self, ctx:SParser.JavascriptPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavascriptReturnStatement(self, ctx:SParser.JavascriptReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, True))


    def exitJavascriptSelectorExpression(self, ctx:SParser.JavascriptSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)


    def exitJavascriptStatement(self, ctx:SParser.JavascriptStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, False))

    def exitJavascriptTextLiteral(self, ctx:SParser.JavascriptTextLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptTextLiteral(text))


    def exitJavaSelectorExpression(self, ctx:SParser.JavaSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)


    def exitJavaStatement(self, ctx:SParser.JavaStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp, False))


    def exitJavaTextLiteral(self, ctx:SParser.JavaTextLiteralContext):
        self.setNodeValue(ctx, JavaTextLiteral(ctx.getText()))


    def exitKey_token(self, ctx:SParser.Key_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitLessThanExpression(self, ctx:SParser.LessThanExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LT, right))


    def exitLessThanOrEqualExpression(self, ctx:SParser.LessThanOrEqualExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, CompareExpression(left, CmpOp.LTE, right))


    def exitList_literal(self, ctx:SParser.List_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = ListLiteral(items)
        self.setNodeValue(ctx, value)


    def exitListLiteral(self, ctx:SParser.ListLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitListType(self, ctx:SParser.ListTypeContext):
        typ = self.getNodeValue(ctx.l)
        self.setNodeValue(ctx, ListType(typ))


    def exitLiteralExpression(self, ctx:SParser.LiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitLiteralList(self, ctx:SParser.LiteralListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])


    def exitLiteralListItem(self, ctx:SParser.LiteralListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitLiteralListLiteral(self, ctx:SParser.LiteralListLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ListLiteral(exp))


    def exitLiteralRangeLiteral(self, ctx:SParser.LiteralRangeLiteralContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))

    def exitLiteralSetLiteral(self, ctx:SParser.LiteralSetLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, SetLiteral(exp))

    def exitMatchingExpression(self, ctx:SParser.MatchingExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MatchingExpressionConstraint(exp))


    def exitMatchingList(self, ctx:SParser.MatchingListContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMatchingPattern(self, ctx:SParser.MatchingPatternContext):
        self.setNodeValue(ctx, MatchingPatternConstraint(TextLiteral(ctx.text.text)))


    def exitMatchingRange(self, ctx:SParser.MatchingRangeContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))

    def exitMatchingSet(self, ctx:SParser.MatchingSetContext):
        exp = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, MatchingCollectionConstraint(exp))


    def exitMaxIntegerLiteral(self, ctx:SParser.MaxIntegerLiteralContext):
        self.setNodeValue(ctx, MaxIntegerLiteral())


    def exitMemberInstance(self, ctx:SParser.MemberInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberInstance(None, name))


    def exitMemberSelector(self, ctx:SParser.MemberSelectorContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))


    def exitMethod_call(self, ctx:SParser.Method_callContext):
        method = self.getNodeValue(ctx.method)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, UnresolvedCall(method, args))


    def exitMethodCallExpression(self, ctx:SParser.MethodCallExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitMethodCallStatement(self, ctx:SParser.MethodCallStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitMethodExpression(self, ctx:SParser.MethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitMethodName(self, ctx:SParser.MethodNameContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))


    def exitMethodParent(self, ctx:SParser.MethodParentContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodSelector(name, parent))


    def exitMethodTypeIdentifier(self, ctx:SParser.MethodTypeIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitMethodVariableIdentifier(self, ctx:SParser.MethodVariableIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitMinIntegerLiteral(self, ctx:SParser.MinIntegerLiteralContext):
        self.setNodeValue(ctx, MinIntegerLiteral())


    def exitMinusExpression(self, ctx:SParser.MinusExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, MinusExpression(exp))


    def exitModuloExpression(self, ctx:SParser.ModuloExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ModuloExpression(left, right))


    def exitMultiplyExpression(self, ctx:SParser.MultiplyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, MultiplyExpression(left, right))


    def exitMutable_category_type(self, ctx):
        typ = self.getNodeValue(ctx.category_type())
        typ.mutable = ctx.MUTABLE() is not None
        self.setNodeValue(ctx, typ)


    def exitNamed_argument(self, ctx:SParser.Named_argumentContext):
        name = self.getNodeValue(ctx.name)
        arg = UnresolvedArgument(name)
        exp = self.getNodeValue(ctx.value)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitNamedArgument(self, ctx:SParser.NamedArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitNative_category_declaration(self, ctx:SParser.Native_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        decl = NativeCategoryDeclaration(name, attrs, bindings, None, methods)
        decl.storable = ctx.STORABLE() is not None
        self.setNodeValue(ctx, decl)


    def exitNative_category_bindings(self, ctx:SParser.Native_category_bindingsContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)


    def exitNative_method_declaration(self, ctx:SParser.Native_method_declarationContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeMethodDeclaration(name, args, typ, stmts))


    def exitNative_resource_declaration(self, ctx:SParser.Native_resource_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        bindings = self.getNodeValue(ctx.bindings)
        methods = self.getNodeValue(ctx.methods)
        self.setNodeValue(ctx, NativeResourceDeclaration(name, attrs, bindings, None, methods))


    def exitNative_symbol(self, ctx:SParser.Native_symbolContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NativeSymbol(name, exp))


    def exitNativeCategoryDeclaration(self, ctx:SParser.NativeCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNativeCategoryBindingList(self, ctx:SParser.NativeCategoryBindingListContext):
        item = self.getNodeValue(ctx.item)
        items = NativeCategoryBindingList(item)
        self.setNodeValue(ctx, items)


    def exitNativeCategoryBindingListItem(self, ctx:SParser.NativeCategoryBindingListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeMethod(self, ctx:SParser.NativeMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitNativeStatementList(self, ctx:SParser.NativeStatementListContext):
        item = self.getNodeValue(ctx.item)
        items = StatementList(item)
        self.setNodeValue(ctx, items)


    def exitNativeStatementListItem(self, ctx:SParser.NativeStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeSymbolList(self, ctx:SParser.NativeSymbolListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, NativeSymbolList(item))


    def exitNativeSymbolListItem(self, ctx:SParser.NativeSymbolListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitNativeType(self, ctx:SParser.NativeTypeContext):
        typ = self.getNodeValue(ctx.n)
        self.setNodeValue(ctx, typ)


    def exitNotContainsAllExpression(self, ctx:SParser.NotContainsAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ALL, right))


    def exitNotContainsAnyExpression(self, ctx:SParser.NotContainsAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ANY, right))


    def exitNotContainsExpression(self, ctx:SParser.NotContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS, right))


    def exitNotEqualsExpression(self, ctx:SParser.NotEqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.NOT_EQUALS, right))


    def exitNotExpression(self, ctx:SParser.NotExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NotExpression(exp))


    def exitNotInExpression(self, ctx:SParser.NotInExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_IN, right))


    def exitNullLiteral(self, ctx:SParser.NullLiteralContext):
        self.setNodeValue(ctx, NullLiteral.instance)


    def exitOperatorArgument(self, ctx:SParser.OperatorArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        arg.mutable = ctx.MUTABLE() is not None
        self.setNodeValue(ctx, arg)


    def exitOperatorPlus(self, ctx:SParser.OperatorPlusContext):
        self.setNodeValue(ctx, Operator.PLUS)


    def exitOperatorMinus(self, ctx:SParser.OperatorMinusContext):
        self.setNodeValue(ctx, Operator.MINUS)


    def exitOperatorMultiply(self, ctx:SParser.OperatorMultiplyContext):
        self.setNodeValue(ctx, Operator.MULTIPLY)


    def exitOperatorDivide(self, ctx:SParser.OperatorDivideContext):
        self.setNodeValue(ctx, Operator.DIVIDE)


    def exitOperatorIDivide(self, ctx:SParser.OperatorIDivideContext):
        self.setNodeValue(ctx, Operator.IDIVIDE)


    def exitOperatorModulo(self, ctx:SParser.OperatorModuloContext):
        self.setNodeValue(ctx, Operator.MODULO)


    def exitOperator_method_declaration(self, ctx:SParser.Operator_method_declarationContext):
        op = self.getNodeValue(ctx.op)
        arg = self.getNodeValue(ctx.arg)
        typ = self.getNodeValue(ctx.typ)
        stmts = self.getNodeValue(ctx.stmts)
        decl = OperatorMethodDeclaration(op, arg, typ, stmts)
        self.setNodeValue(ctx, decl)


    def exitOrder_by(self, ctx:SParser.Order_byContext):
        names = IdentifierList()
        for ctx_ in ctx.variable_identifier():
            names.append(self.getNodeValue(ctx_))
        clause = OrderByClause(names, ctx.DESC() is not None)
        self.setNodeValue(ctx, clause)

    def exitOrder_by_list(self, ctx:SParser.Order_by_listContext):
        list_ = OrderByClauseList()
        for ctx_ in ctx.order_by():
            list_.append(self.getNodeValue(ctx_))
        self.setNodeValue(ctx, list_)

    def exitOrExpression(self, ctx:SParser.OrExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, OrExpression(left, right))


    def exitParenthesis_expression(self, ctx:SParser.Parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ParenthesisExpression(exp))


    def exitParenthesisExpression(self, ctx:SParser.ParenthesisExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPeriodLiteral(self, ctx:SParser.PeriodLiteralContext):
        self.setNodeValue(ctx, PeriodLiteral(ctx.t.text))


    def exitPrimaryType(self, ctx:SParser.PrimaryTypeContext):
        typ = self.getNodeValue(ctx.p)
        self.setNodeValue(ctx, typ)


    def exitPython_category_binding(self, ctx:SParser.Python_category_bindingContext):
        identifier = ctx.identifier().getText()
        module = self.getNodeValue(ctx.python_module())
        map = PythonNativeCategoryBinding(identifier, module)
        self.setNodeValue(ctx, map)


    def exitPython_identifier(self, ctx:SParser.Python_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitPython_method_expression(self, ctx:SParser.Python_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        method = PythonMethodExpression(name, args)
        self.setNodeValue(ctx, method)


    def exitPython_module(self, ctx:SParser.Python_moduleContext):
        ids = []
        for ic in ctx.identifier():
            ids.append(ic.getText())
        module = PythonModule(ids)
        self.setNodeValue(ctx, module)


    def exitPython_native_statement(self, ctx:SParser.Python_native_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        self.setNodeValue(ctx, PythonNativeCall(stmt, module))


    def exitPython2CategoryBinding(self, ctx:SParser.Python2CategoryBindingContext):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python2NativeCategoryBinding(map.identifier, map.module))


    def exitPython2NativeStatement(self, ctx:SParser.Python2NativeStatementContext):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python2NativeCall(call.statement, call.module))


    def exitPython3CategoryBinding(self, ctx:SParser.Python3CategoryBindingContext):
        map = self.getNodeValue(ctx.binding)
        self.setNodeValue(ctx, Python3NativeCategoryBinding(map.identifier, map.module))


    def exitPython3NativeStatement(self, ctx:SParser.Python3NativeStatementContext):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python3NativeCall(call.statement, call.module))


    def exitPythonArgumentList(self, ctx:SParser.PythonArgumentListContext):
        ordinal = self.getNodeValue(ctx.ordinal)
        named = self.getNodeValue(ctx.named)
        ordinal.addAll(named)
        self.setNodeValue(ctx, ordinal)


    def exitPythonBooleanLiteral(self, ctx:SParser.PythonBooleanLiteralContext):
        self.setNodeValue(ctx, PythonBooleanLiteral(ctx.getText()))


    def exitPythonCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, PythonCharacterLiteral(ctx.getText()))


    def exitPythonChildIdentifier(self, ctx:SParser.PythonChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = PythonIdentifierExpression(name, parent)
        self.setNodeValue(ctx, child)


    def exitPythonDecimalLiteral(self, ctx:SParser.PythonDecimalLiteralContext):
        self.setNodeValue(ctx, PythonDecimalLiteral(ctx.getText()))


    def exitPythonGlobalMethodExpression(self, ctx:SParser.PythonGlobalMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIdentifier(self, ctx:SParser.PythonIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, PythonIdentifierExpression(name))


    def exitPythonIdentifierExpression(self, ctx:SParser.PythonIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonIntegerLiteral(self, ctx:SParser.PythonIntegerLiteralContext):
        self.setNodeValue(ctx, PythonIntegerLiteral(ctx.getText()))


    def exitPythonLiteralExpression(self, ctx:SParser.PythonLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonMethodExpression(self, ctx:SParser.PythonMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonNamedArgumentList(self, ctx:SParser.PythonNamedArgumentListContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = PythonNamedArgument(name, exp)
        arglist = PythonNamedArgumentList()
        arglist.append(arg)
        self.setNodeValue(ctx, arglist)


    def exitPythonNamedArgumentListItem(self, ctx:SParser.PythonNamedArgumentListItemContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        item = PythonNamedArgument(name, exp)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitPythonNamedOnlyArgumentList(self, ctx:SParser.PythonNamedOnlyArgumentListContext):
        named = self.getNodeValue(ctx.named)
        self.setNodeValue(ctx, named)


    def exitPythonOrdinalArgumentList(self, ctx:SParser.PythonOrdinalArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, PythonOrdinalArgumentList(item))

    def exitPythonOrdinalArgumentListItem(self, ctx:SParser.PythonOrdinalArgumentListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitPythonOrdinalOnlyArgumentList(self, ctx:SParser.PythonOrdinalOnlyArgumentListContext):
        ordinal = self.getNodeValue(ctx.ordinal)
        self.setNodeValue(ctx, ordinal)

    def exitPythonPromptoIdentifier(self, ctx:SParser.PythonPromptoIdentifierContext):
        name = ctx.DOLLAR_IDENTIFIER().getText()
        self.setNodeValue(ctx, PythonIdentifierExpression(name))


    def exitPythonPrimaryExpression(self, ctx:SParser.PythonPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitPythonReturnStatement(self, ctx:SParser.PythonReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, True))


    def exitPythonSelectorExpression(self, ctx:SParser.PythonSelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.child)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)


    def exitPythonStatement(self, ctx:SParser.PythonStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp, False))


    def exitPythonTextLiteral(self, ctx:SParser.PythonTextLiteralContext):
        self.setNodeValue(ctx, PythonTextLiteral(ctx.getText()))


    def exitRaise_statement(self, ctx:SParser.Raise_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, RaiseStatement(exp))


    def exitRaiseStatement(self, ctx:SParser.RaiseStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitRange_literal(self, ctx:SParser.Range_literalContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))


    def exitRangeLiteral(self, ctx:SParser.RangeLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitRead_expression(self, ctx:SParser.Read_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadExpression(source))


    def exitReadExpression(self, ctx:SParser.ReadExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitResource_declaration(self, ctx:SParser.Resource_declarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitReturn_statement(self, ctx:SParser.Return_statementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ReturnStatement(exp))


    def exitReturnStatement(self, ctx:SParser.ReturnStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitRootInstance(self, ctx:SParser.RootInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, VariableInstance(name))


    def exitRoughlyEqualsExpression(self, ctx:SParser.RoughlyEqualsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.ROUGHLY, right))


    def exitSelectableExpression(self, ctx:SParser.SelectableExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        self.setNodeValue(ctx, parent)


    def exitSelectorExpression(self, ctx:SParser.SelectorExpressionContext):
        parent = self.getNodeValue(ctx.parent)
        selector = self.getNodeValue(ctx.selector)
        selector.setParent(parent)
        self.setNodeValue(ctx, selector)


    def exitSetter_method_declaration(self, ctx:SParser.Setter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, SetterMethodDeclaration(name, stmts))


    def exitSingleton_category_declaration(self, ctx:SParser.Singleton_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        methods = self.getNodeValue(ctx.methods)
        self.setNodeValue(ctx, SingletonCategoryDeclaration(name, attrs, methods))


    def exitSingletonCategoryDeclaration(self, ctx:SParser.SingletonCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitSliceFirstAndLast(self, ctx:SParser.SliceFirstAndLastContext):
        first = self.getNodeValue(ctx.first)
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(first, last))


    def exitSliceFirstOnly(self, ctx:SParser.SliceFirstOnlyContext):
        first = self.getNodeValue(ctx.first)
        self.setNodeValue(ctx, SliceSelector(first, None))


    def exitSliceLastOnly(self, ctx:SParser.SliceLastOnlyContext):
        last = self.getNodeValue(ctx.last)
        self.setNodeValue(ctx, SliceSelector(None, last))


    def exitSliceSelector(self, ctx:SParser.SliceSelectorContext):
        slice = self.getNodeValue(ctx.xslice)
        self.setNodeValue(ctx, slice)


    def exitStoreStatement (self, ctx:SParser.StoreStatementContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.stmt))


    def exitStore_statement (self, ctx:SParser.Store_statementContext):
        to_del = self.getNodeValue(ctx.to_del)
        to_add = self.getNodeValue(ctx.to_add)
        stmt = StoreStatement(to_del, to_add)
        self.setNodeValue(ctx, stmt)


    def exitSorted_expression(self, ctx:SParser.Sorted_expressionContext):
        source = self.getNodeValue(ctx.source)
        key = self.getNodeValue(ctx.key)
        self.setNodeValue(ctx, SortedExpression(source, key))


    def exitSortedExpression(self, ctx:SParser.SortedExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitStatementList(self, ctx:SParser.StatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, StatementList(item))


    def exitStatementListItem(self, ctx:SParser.StatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitSwitch_statement(self, ctx:SParser.Switch_statementContext):
        exp = self.getNodeValue(ctx.exp)
        cases = self.getNodeValue(ctx.cases)
        stmts = self.getNodeValue(ctx.stmts)
        stmt = SwitchStatement(exp)
        stmt.setSwitchCases(cases)
        stmt.setDefaultCase(stmts)
        self.setNodeValue(ctx, stmt)


    def exitSwitchCaseStatementList(self, ctx:SParser.SwitchCaseStatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))


    def exitSwitchCaseStatementListItem(self, ctx:SParser.SwitchCaseStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitSwitchStatement(self, ctx:SParser.SwitchStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitSymbol_identifier(self, ctx:SParser.Symbol_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitSymbolIdentifier(self, ctx:SParser.SymbolIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitSymbols_token(self, ctx:SParser.Symbols_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitTernaryExpression(self, ctx):
        condition = self.getNodeValue(ctx.test)
        ifTrue = self.getNodeValue(ctx.ifTrue)
        ifFalse = self.getNodeValue(ctx.ifFalse)
        exp = TernaryExpression(condition, ifTrue, ifFalse)
        self.setNodeValue(ctx, exp)

    def exitTextLiteral(self, ctx:SParser.TextLiteralContext):
        self.setNodeValue(ctx, TextLiteral(ctx.t.text))

    def exitTest_method_declaration(self, ctx:SParser.Test_method_declarationContext):
        name = ctx.name.text
        stmts = self.getNodeValue(ctx.stmts)
        exps = self.getNodeValue(ctx.exps)
        errorName = self.getNodeValue(ctx.error)
        error = None if errorName is None else SymbolExpression(errorName)
        self.setNodeValue(ctx, TestMethodDeclaration(name, stmts, exps, error))


    def exitTestMethod(self, ctx:SParser.TestMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)

    def exitTextType(self, ctx:SParser.TextTypeContext):
        self.setNodeValue(ctx, TextType.instance)

    def exitThisExpression(self, ctx:SParser.ThisExpressionContext):
        self.setNodeValue(ctx, ThisExpression())


    def exitTimeLiteral(self, ctx:SParser.TimeLiteralContext):
        self.setNodeValue(ctx, TimeLiteral(ctx.t.text))


    def exitTimeType(self, ctx:SParser.TimeTypeContext):
        self.setNodeValue(ctx, TimeType.instance)


    def exitTry_statement(self, ctx:SParser.Try_statementContext):
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


    def exitTryStatement(self, ctx:SParser.TryStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitTuple_literal(self, ctx:SParser.Tuple_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = TupleLiteral(items)
        self.setNodeValue(ctx, value)


    def exitTupleLiteral(self, ctx:SParser.TupleLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitSet_literal(self, ctx:SParser.Set_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    def exitSetLiteral(self, ctx:SParser.SetLiteralContext):
        items = self.getNodeValue(ctx.exp)
        items = items if items is not None else []
        self.setNodeValue(ctx, items)


    def exitType_identifier(self, ctx:SParser.Type_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitTyped_argument(self, ctx:SParser.Typed_argumentContext):
        typ = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        exp = self.getNodeValue(ctx.value)
        from prompto.argument.ExtendedArgument import ExtendedArgument
        arg = CategoryArgument(typ, name) if attrs is None else ExtendedArgument(typ, name, attrs)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    def exitTypedArgument(self, ctx:SParser.TypedArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)


    def exitTypeIdentifier(self, ctx:SParser.TypeIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)


    def exitTypeIdentifierList(self, ctx:SParser.TypeIdentifierListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))


    def exitTypeIdentifierListItem(self, ctx:SParser.TypeIdentifierListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitValue_token(self, ctx:SParser.Value_tokenContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitValueList(self, ctx:SParser.ValueListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])


    def exitValueListItem(self, ctx:SParser.ValueListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitValueTuple(self, ctx:SParser.ValueTupleContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])


    def exitValueTupleItem(self, ctx:SParser.ValueTupleItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)


    def exitAttribute_identifier(self, ctx:SParser.Attribute_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitVariable_identifier(self, ctx:SParser.Variable_identifierContext):
        self.setNodeValue(ctx, ctx.getText())


    def exitVariableIdentifier(self, ctx:SParser.VariableIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)



    def exitAttribute_identifier_list(self, ctx:SParser.Attribute_identifier_listContext):
        items = IdentifierList()
        for c in ctx.attribute_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)


    def exitVariable_identifier_list(self, ctx:SParser.Variable_identifier_listContext):
        items = IdentifierList()
        for c in ctx.variable_identifier():
            item = self.getNodeValue(c)
            items.append(item)
        self.setNodeValue(ctx, items)



    def exitWhile_statement(self, ctx:SParser.While_statementContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WhileStatement(exp, stmts))


    def exitWhileStatement(self, ctx:SParser.WhileStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_singleton_statement(self, ctx:SParser.With_singleton_statementContext):
        name = self.getNodeValue(ctx.typ)
        typ = CategoryType(name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithSingletonStatement(typ, stmts))


    def exitWithSingletonStatement(self, ctx:SParser.WithSingletonStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWith_resource_statement(self, ctx:SParser.With_resource_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, WithResourceStatement(stmt, stmts))


    def exitWithResourceStatement(self, ctx:SParser.WithResourceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    def exitWrite_statement(self, ctx:SParser.Write_statementContext):
        what = self.getNodeValue(ctx.what)
        target = self.getNodeValue(ctx.target)
        self.setNodeValue(ctx, WriteStatement(what, target))


    def exitWriteStatement(self, ctx:SParser.WriteStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)

