from antlr4.tree.Tree import ParseTree
from antlr4.ParserRuleContext import ParserRuleContext
from presto.csharp.CSharpBooleanLiteral import CSharpBooleanLiteral
from presto.csharp.CSharpCharacterLiteral import CSharpCharacterLiteral
from presto.csharp.CSharpDecimalLiteral import CSharpDecimalLiteral
from presto.csharp.CSharpExpressionList import CSharpExpressionList
from presto.csharp.CSharpIdentifierExpression import CSharpIdentifierExpression
from presto.csharp.CSharpIntegerLiteral import CSharpIntegerLiteral
from presto.csharp.CSharpMethodExpression import CSharpMethodExpression
from presto.csharp.CSharpNativeCategoryMapping import CSharpNativeCategoryMapping
from presto.csharp.CSharpNativeCall import CSharpNativeCall
from presto.csharp.CSharpStatement import CSharpStatement
from presto.csharp.CSharpTextLiteral import CSharpTextLiteral
from presto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from presto.declaration.AttributeDeclaration import AttributeDeclaration
from presto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from presto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from presto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
from presto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from presto.declaration.GetterMethodDeclaration import GetterMethodDeclaration
from presto.declaration.OperatorMethodDeclaration import OperatorMethodDeclaration
from presto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from presto.declaration.NativeMethodDeclaration import NativeMethodDeclaration
from presto.declaration.TestMethodDeclaration import TestMethodDeclaration
from presto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration
from presto.declaration.NativeResourceDeclaration import NativeResourceDeclaration
from presto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from presto.expression.AddExpression import AddExpression
from presto.expression.AndExpression import AndExpression
from presto.expression.CastExpression import CastExpression
from presto.expression.CodeExpression import CodeExpression
from presto.expression.CompareExpression import CompareExpression
from presto.expression.ConstructorExpression import ConstructorExpression
from presto.expression.ContainsExpression import ContainsExpression
from presto.expression.DivideExpression import DivideExpression
from presto.expression.DocumentExpression import DocumentExpression
from presto.expression.EqualsExpression import EqualsExpression
from presto.expression.ExecuteExpression import ExecuteExpression
from presto.expression.FetchExpression import FetchExpression
from presto.expression.InstanceExpression import InstanceExpression
from presto.expression.IntDivideExpression import IntDivideExpression
from presto.expression.ItemSelector import ItemSelector
from presto.expression.MemberSelector import MemberSelector
from presto.expression.MethodExpression import MethodExpression
from presto.expression.MethodSelector import MethodSelector
from presto.expression.MinusExpression import MinusExpression
from presto.expression.ModuloExpression import ModuloExpression
from presto.expression.MultiplyExpression import MultiplyExpression
from presto.expression.NotExpression import NotExpression
from presto.expression.OrExpression import OrExpression
from presto.expression.ParenthesisExpression import ParenthesisExpression
from presto.expression.ReadExpression import ReadExpression
from presto.expression.SliceSelector import SliceSelector
from presto.expression.SortedExpression import SortedExpression
from presto.expression.SubtractExpression import SubtractExpression
from presto.expression.SymbolExpression import SymbolExpression
from presto.expression.TernaryExpression import TernaryExpression
from presto.expression.ThisExpression import ThisExpression
from presto.expression.TypeExpression import TypeExpression
from presto.grammar.ArgumentAssignment import ArgumentAssignment
from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from presto.grammar.ArgumentList import ArgumentList
from presto.grammar.CategoryArgument import CategoryArgument
from presto.grammar.CategoryMethodDeclarationList import CategoryMethodDeclarationList
from presto.grammar.CategorySymbol import CategorySymbol
from presto.grammar.CategorySymbolList import CategorySymbolList
from presto.grammar.CmpOp import CmpOp
from presto.grammar.CodeArgument import CodeArgument
from presto.grammar.ContOp import ContOp
from presto.grammar.DeclarationList import DeclarationList
from presto.grammar.EqOp import EqOp
from presto.grammar.IdentifierList import IdentifierList
from presto.grammar.ItemInstance import ItemInstance
from presto.grammar.MatchingCollectionConstraint import MatchingCollectionConstraint
from presto.grammar.MatchingExpressionConstraint import MatchingExpressionConstraint
from presto.grammar.MatchingPatternConstraint import MatchingPatternConstraint
from presto.grammar.MemberInstance import MemberInstance
from presto.grammar.NativeCategoryMappingList import NativeCategoryMappingList
from presto.grammar.NativeSymbol import NativeSymbol
from presto.grammar.NativeSymbolList import NativeSymbolList
from presto.grammar.Operator import Operator
from presto.grammar.UnresolvedArgument import UnresolvedArgument
from presto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
from presto.grammar.VariableInstance import VariableInstance
from presto.java.JavaBooleanLiteral import JavaBooleanLiteral
from presto.java.JavaCharacterLiteral import JavaCharacterLiteral
from presto.java.JavaDecimalLiteral import JavaDecimalLiteral
from presto.java.JavaExpressionList import JavaExpressionList
from presto.java.JavaIdentifierExpression import JavaIdentifierExpression
from presto.java.JavaIntegerLiteral import JavaIntegerLiteral
from presto.java.JavaItemExpression import JavaItemExpression
from presto.java.JavaMethodExpression import JavaMethodExpression
from presto.java.JavaNativeCategoryMapping import JavaNativeCategoryMapping
from presto.java.JavaNativeCall import JavaNativeCall
from presto.java.JavaStatement import JavaStatement
from presto.java.JavaTextLiteral import JavaTextLiteral
from presto.javascript.JavaScriptBooleanLiteral import JavaScriptBooleanLiteral
from presto.javascript.JavaScriptCharacterLiteral import JavaScriptCharacterLiteral
from presto.javascript.JavaScriptDecimalLiteral import JavaScriptDecimalLiteral
from presto.javascript.JavaScriptExpressionList import JavaScriptExpressionList
from presto.javascript.JavaScriptIdentifierExpression import JavaScriptIdentifierExpression
from presto.javascript.JavaScriptIntegerLiteral import JavaScriptIntegerLiteral
from presto.javascript.JavaScriptMethodExpression import JavaScriptMethodExpression
from presto.javascript.JavaScriptModule import JavaScriptModule
from presto.javascript.JavaScriptNativeCall import JavaScriptNativeCall
from presto.javascript.JavaScriptNativeCategoryMapping import JavaScriptNativeCategoryMapping
from presto.javascript.JavaScriptStatement import JavaScriptStatement
from presto.javascript.JavaScriptTextLiteral import JavaScriptTextLiteral
from presto.literal.BooleanLiteral import BooleanLiteral
from presto.literal.CharacterLiteral import CharacterLiteral
from presto.literal.DateLiteral import DateLiteral
from presto.literal.DateTimeLiteral import DateTimeLiteral
from presto.literal.DecimalLiteral import DecimalLiteral
from presto.literal.DictEntry import DictEntry
from presto.literal.DictEntryList import DictEntryList
from presto.literal.DictLiteral import DictLiteral
from presto.literal.HexaLiteral import HexaLiteral
from presto.literal.IntegerLiteral import IntegerLiteral, MinIntegerLiteral, MaxIntegerLiteral
from presto.literal.ListLiteral import ListLiteral
from presto.literal.NullLiteral import NullLiteral
from presto.literal.PeriodLiteral import PeriodLiteral
from presto.literal.RangeLiteral import RangeLiteral
from presto.literal.SetLiteral import SetLiteral
from presto.literal.TextLiteral import TextLiteral
from presto.literal.TimeLiteral import TimeLiteral
from presto.literal.TupleLiteral import TupleLiteral
from presto.parser.OParser import OParser
from presto.parser.OParserListener import OParserListener
from presto.parser.Section import Section
from presto.parser.Dialect import Dialect
from presto.python.PythonNativeCategoryMapping import PythonNativeCategoryMapping, Python2NativeCategoryMapping, Python3NativeCategoryMapping
from presto.python.PythonArgument import PythonNamedArgument, PythonNamedArgumentList, PythonOrdinalArgumentList
from presto.python.PythonBooleanLiteral import PythonBooleanLiteral
from presto.python.PythonCharacterLiteral import PythonCharacterLiteral
from presto.python.PythonDecimalLiteral import PythonDecimalLiteral
from presto.python.PythonIdentifierExpression import PythonIdentifierExpression
from presto.python.PythonIntegerLiteral import PythonIntegerLiteral
from presto.python.PythonMethodExpression import PythonMethodExpression
from presto.python.PythonNativeCall import PythonNativeCall, Python2NativeCall, Python3NativeCall
from presto.python.PythonStatement import PythonStatement
from presto.python.PythonTextLiteral import PythonTextLiteral
from presto.python.PythonModule import PythonModule
from presto.statement.AssignInstanceStatement import AssignInstanceStatement
from presto.statement.AssignTupleStatement import AssignTupleStatement
from presto.statement.AssignVariableStatement import AssignVariableStatement
from presto.statement.AtomicSwitchCase import AtomicSwitchCase
from presto.statement.CollectionSwitchCase import CollectionSwitchCase
from presto.statement.DeclarationInstruction import DeclarationInstruction
from presto.statement.DoWhileStatement import DoWhileStatement
from presto.statement.ForEachStatement import ForEachStatement
from presto.statement.IfStatement import IfElement, IfStatement, IfElementList
from presto.statement.UnresolvedCall import UnresolvedCall
from presto.statement.RaiseStatement import RaiseStatement
from presto.statement.ReturnStatement import ReturnStatement
from presto.statement.StatementList import StatementList
from presto.statement.SwitchCase import SwitchCaseList
from presto.statement.SwitchErrorStatement import SwitchErrorStatement
from presto.statement.SwitchStatement import SwitchStatement
from presto.statement.WhileStatement import WhileStatement
from presto.statement.WithResourceStatement import WithResourceStatement
from presto.statement.WithSingletonStatement import WithSingletonStatement
from presto.statement.WriteStatement import WriteStatement
from presto.type.AnyType import AnyType
from presto.type.BooleanType import BooleanType
from presto.type.CategoryType import CategoryType
from presto.type.CharacterType import CharacterType
from presto.type.CodeType import CodeType
from presto.type.DateType import DateType
from presto.type.DecimalType import DecimalType
from presto.type.DictType import DictType
from presto.type.DocumentType import DocumentType
from presto.type.IntegerType import IntegerType
from presto.type.ListType import ListType
from presto.type.TextType import TextType
from presto.type.TimeType import TimeType

# need forward declaration
OCleverParser = None

class OPrestoBuilder(OParserListener):

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
        if idx==-1: # happens because input.index() is called before any other read operation (bug?)
            idx = 0
        while idx>=0:
            token = self.readValidToken(idx)
            if token is not None:
                return token
            idx -= 1
        return None

    def readValidToken(self, idx:int):
        token = self.input.tokens[idx]
        text = token.text
        if text is not None and len(text)>0 and not text[0].isspace():
            return token
        else:
            return None
 

    def exitTypeIdentifier(self, ctx:OParser.TypeIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))
    

    
    def exitMethodCallExpression(self, ctx:OParser.MethodCallExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    def exitAtomicLiteral(self, ctx:OParser.AtomicLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitCollectionLiteral(self, ctx:OParser.CollectionLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitListLiteral(self, ctx:OParser.ListLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitBooleanLiteral(self, ctx:OParser.BooleanLiteralContext):
        self.setNodeValue(ctx, BooleanLiteral(ctx.t.text))
    

    
    def exitMinIntegerLiteral(self, ctx:OParser.MinIntegerLiteralContext):
        self.setNodeValue(ctx, MinIntegerLiteral())
    

    
    def exitMaxIntegerLiteral(self, ctx:OParser.MaxIntegerLiteralContext):
        self.setNodeValue(ctx, MaxIntegerLiteral())
    

    
    def exitIntegerLiteral(self, ctx:OParser.IntegerLiteralContext):
        self.setNodeValue(ctx, IntegerLiteral(ctx.t.text))
    

    
    def exitDecimalLiteral(self, ctx:OParser.DecimalLiteralContext):
        self.setNodeValue(ctx, DecimalLiteral(ctx.t.text))
    

    
    def exitHexadecimalLiteral(self, ctx:OParser.HexadecimalLiteralContext):
        self.setNodeValue(ctx, HexaLiteral(ctx.t.text))
    

    
    def exitCharacterLiteral(self, ctx:OParser.CharacterLiteralContext):
        self.setNodeValue(ctx, CharacterLiteral(ctx.t.text))
    

    
    def exitDateLiteral(self, ctx:OParser.DateLiteralContext):
        self.setNodeValue(ctx, DateLiteral(ctx.t.text))
    

    
    def exitDateTimeLiteral(self, ctx:OParser.DateTimeLiteralContext):
        self.setNodeValue(ctx, DateTimeLiteral(ctx.t.text))
    

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


    def exitTestMethod(self, ctx:OParser.TestMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)

    def exitTextLiteral(self, ctx:OParser.TextLiteralContext):
        self.setNodeValue(ctx, TextLiteral(ctx.t.text))
    

    
    def exitTimeLiteral(self, ctx:OParser.TimeLiteralContext):
        self.setNodeValue(ctx, TimeLiteral(ctx.t.text))
    

    
    def exitPeriodLiteral(self, ctx:OParser.PeriodLiteralContext):
        self.setNodeValue(ctx, PeriodLiteral(ctx.t.text))
    

    
    def exitVariable_identifier(self, ctx:OParser.Variable_identifierContext):
        self.setNodeValue(ctx, ctx.getText())
    

    
    def exitList_literal(self, ctx:OParser.List_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = ListLiteral(items)
        self.setNodeValue(ctx, value)
    

    
    def exitDict_literal(self, ctx:OParser.Dict_literalContext):
        items = self.getNodeValue(ctx.items)
        value = DictLiteral(items)
        self.setNodeValue(ctx, value)
    

    
    def exitTuple_literal(self, ctx:OParser.Tuple_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = TupleLiteral(items)
        self.setNodeValue(ctx, value)

    
    def exitTupleLiteral(self, ctx:OParser.TupleLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    def exitSet_literal(self, ctx:OParser.Set_literalContext):
        items = self.getNodeValue(ctx.items)
        items = items if items is not None else []
        value = SetLiteral(items)
        self.setNodeValue(ctx, value)


    def exitSetLiteral(self, ctx:OParser.SetLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    
    def exitRange_literal(self, ctx:OParser.Range_literalContext):
        low = self.getNodeValue(ctx.low)
        high = self.getNodeValue(ctx.high)
        self.setNodeValue(ctx, RangeLiteral(low, high))
    

    
    def exitRangeLiteral(self, ctx:OParser.RangeLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitDictLiteral(self, ctx:OParser.DictLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitDictEntryList(self, ctx:OParser.DictEntryListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, DictEntryList(item))
    

    
    def exitDictEntryListItem(self, ctx:OParser.DictEntryListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitDict_entry(self, ctx:OParser.Dict_entryContext):
        key = self.getNodeValue(ctx.key)
        value = self.getNodeValue(ctx.value)
        entry = DictEntry(key, value)
        self.setNodeValue(ctx, entry)
    

    
    def exitLiteralExpression(self, ctx:OParser.LiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    def exitIdentifierExpression(self, ctx:OParser.IdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitVariableIdentifier(self, ctx:OParser.VariableIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, InstanceExpression(name))
    

    
    def exitValueList(self, ctx:OParser.ValueListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])
    

    
    def exitValueListItem(self, ctx:OParser.ValueListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitValueTuple(self, ctx:OParser.ValueTupleContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])
    

    
    def exitValueTupleItem(self, ctx:OParser.ValueTupleItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitSymbol_identifier(self, ctx:OParser.Symbol_identifierContext):
        self.setNodeValue(ctx, ctx.getText())
    

    
    def exitNative_symbol(self, ctx:OParser.Native_symbolContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, NativeSymbol(name, exp))
    

    
    def exitSymbolIdentifier(self, ctx:OParser.SymbolIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, SymbolExpression(name))
    

    
    def exitBooleanType(self, ctx:OParser.BooleanTypeContext):
        self.setNodeValue(ctx, BooleanType.instance)
    

    
    def exitCharacterType(self, ctx:OParser.CharacterTypeContext):
        self.setNodeValue(ctx, CharacterType.instance)
    

    
    def exitTextType(self, ctx:OParser.TextTypeContext):
        self.setNodeValue(ctx, TextType.instance)
    
    def exitThisExpression(self, ctx:OParser.ThisExpressionContext):
        self.setNodeValue(ctx, ThisExpression())


    
    def exitIntegerType(self, ctx:OParser.IntegerTypeContext):
        self.setNodeValue(ctx, IntegerType.instance)
    

    
    def exitDecimalType(self, ctx:OParser.DecimalTypeContext):
        self.setNodeValue(ctx, DecimalType.instance)
    

    
    def exitDateType(self, ctx:OParser.DateTypeContext):
        self.setNodeValue(ctx, DateType.instance)
    

    
    def exitDateTimeType(self, ctx:OParser.DateTimeTypeContext):
        self.setNodeValue(ctx, TextType.instance)
    

    
    def exitTimeType(self, ctx:OParser.TimeTypeContext):
        self.setNodeValue(ctx, TimeType.instance)
    

    
    def exitCodeType(self, ctx:OParser.CodeTypeContext):
        self.setNodeValue(ctx, CodeType.instance)
    

    
    def exitPrimaryType(self, ctx:OParser.PrimaryTypeContext):
        type = self.getNodeValue(ctx.p)
        self.setNodeValue(ctx, type)
    

    
    def exitAttribute_declaration(self, ctx:OParser.Attribute_declarationContext):
        name = self.getNodeValue(ctx.name)
        type = self.getNodeValue(ctx.typ)
        match = self.getNodeValue(getattr(ctx,"match",None))
        self.setNodeValue(ctx, AttributeDeclaration(name, type, match))
    

    
    def exitNativeType(self, ctx:OParser.NativeTypeContext):
        type = self.getNodeValue(ctx.n)
        self.setNodeValue(ctx, type)
    

    
    def exitCategoryType(self, ctx:OParser.CategoryTypeContext):
        type = self.getNodeValue(ctx.c)
        self.setNodeValue(ctx, type)
    

    
    def exitCategory_type(self, ctx:OParser.Category_typeContext):
        name = ctx.getText()
        self.setNodeValue(ctx, CategoryType(name))
    

    
    def exitListType(self, ctx:OParser.ListTypeContext):
        type = self.getNodeValue(ctx.l)
        self.setNodeValue(ctx, ListType(type))
    

    
    def exitDictType(self, ctx:OParser.DictTypeContext):
        type = self.getNodeValue(ctx.d)
        self.setNodeValue(ctx, DictType(type))
    

    
    def exitAttributeList(self, ctx:OParser.AttributeListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))
    

    
    def exitAttributeListItem(self, ctx:OParser.AttributeListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitVariableList(self, ctx:OParser.VariableListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))
    

    
    def exitVariableListItem(self, ctx:OParser.VariableListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
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
        ccd.setAttributes(attrs)
        ccd.setDerivedFrom(derived)
        ccd.setMethods(methods)
        self.setNodeValue(ctx, ccd)

    def exitConcreteCategoryDeclaration(self, ctx:OParser.ConcreteCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitType_identifier(self, ctx:OParser.Type_identifierContext):
        self.setNodeValue(ctx, ctx.getText())

    
    def exitTypeIdentifierList(self, ctx:OParser.TypeIdentifierListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, IdentifierList(item))
    

    
    def exitTypeIdentifierListItem(self, ctx:OParser.TypeIdentifierListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
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
    
    def exitIsATypeExpression(self, ctx:OParser.IsATypeExpressionContext):
        typ = self.getNodeValue(ctx.typ)
        exp = TypeExpression(typ)
        self.setNodeValue(ctx, exp)

    def exitIsOtherExpression(self, ctx:OParser.IsOtherExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitIsExpression(self, ctx:OParser.IsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        op = EqOp.IS_A if isinstance(right, TypeExpression) else EqOp.IS
        self.setNodeValue(ctx, EqualsExpression(left, op, right))

    def exitIsNotExpression(self, ctx:OParser.IsNotExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        op = EqOp.IS_NOT_A if isinstance(right, TypeExpression) else EqOp.IS_NOT
        self.setNodeValue(ctx, EqualsExpression(left, op, right))

    
    def exitItemSelector(self, ctx:OParser.ItemSelectorContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))
    

    
    def exitSliceSelector(self, ctx:OParser.SliceSelectorContext):
        slice = self.getNodeValue(ctx.xslice)
        self.setNodeValue(ctx, slice)
    

    
    def exitTyped_argument(self, ctx:OParser.Typed_argumentContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        exp = self.getNodeValue(ctx.value)
        arg = CategoryArgument(type, name, attrs)
        arg.defaultExpression = exp
        self.setNodeValue(ctx, arg)


    
    def exitTypedArgument(self, ctx:OParser.TypedArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)
    

    
    def exitNamedArgument(self, ctx:OParser.NamedArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)
    

    
    def exitCodeArgument(self, ctx:OParser.CodeArgumentContext):
        arg = self.getNodeValue(ctx.arg)
        self.setNodeValue(ctx, arg)
    

    
    def exitCategoryArgumentType(self, ctx:OParser.CategoryArgumentTypeContext):
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, type)
    

    
    def exitArgumentList(self, ctx:OParser.ArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, ArgumentList(item))
    

    
    def exitArgumentListItem(self, ctx:OParser.ArgumentListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitMethodTypeIdentifier(self, ctx:OParser.MethodTypeIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)
    
    def exitMethodName(self, ctx:OParser.MethodNameContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, UnresolvedIdentifier(name))

    def exitMethodParent(self, ctx:OParser.MethodParentContext):
        name = self.getNodeValue(ctx.name)
        parent = self.getNodeValue(ctx.parent)
        self.setNodeValue(ctx, MethodSelector(name, parent))


    def exitCallableMemberSelector(self, ctx:OParser.CallableMemberSelectorContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberSelector(name))

    def exitCallableItemSelector(self, ctx:OParser.CallableItemSelectorContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemSelector(exp))

    def exitCallableRoot(self, ctx:OParser.CallableRootContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)

    def exitCallableSelector(self, ctx:OParser.CallableSelectorContext):
        parent = self.getNodeValue(ctx.parent)
        select = self.getNodeValue(ctx.select)
        select.setParent(parent)
        self.setNodeValue(ctx, select)

    def exitMethodVariableIdentifier(self, ctx:OParser.MethodVariableIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, name)
    
    def exitMethod_call(self, ctx:OParser.Method_callContext):
        selector = self.getNodeValue(ctx.method)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, UnresolvedCall(selector, args))
    
    def exitArgument_assignment(self, ctx:OParser.Argument_assignmentContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        arg = UnresolvedArgument(name)
        self.setNodeValue(ctx, ArgumentAssignment(arg, exp))
    
    def exitExpressionAssignmentList(self, ctx:OParser.ExpressionAssignmentListContext):
        exp = self.getNodeValue(ctx.exp)
        items = ArgumentAssignmentList()
        items.insert(0, ArgumentAssignment(None, exp))
        self.setNodeValue(ctx, items)


    def exitArgumentAssignmentList(self, ctx:OParser.ArgumentAssignmentListContext):
        item = self.getNodeValue(ctx.item)
        items = ArgumentAssignmentList(item=item)
        self.setNodeValue(ctx, items)
    

    
    def exitArgumentAssignmentListItem(self, ctx:OParser.ArgumentAssignmentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitAddExpression(self, ctx:OParser.AddExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        exp = AddExpression(left, right) if ctx.op.type==OParser.PLUS else SubtractExpression(left, right)
        self.setNodeValue(ctx, exp)
    

    
    def exitCategoryMethodList(self, ctx:OParser.CategoryMethodListContext):
        item = self.getNodeValue(ctx.item)
        items = CategoryMethodDeclarationList(item)
        self.setNodeValue(ctx, items)
    
    def exitCurlyCategoryMethodList(self, ctx:OParser.CurlyCategoryMethodListContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)

    def exitCurlyStatementList(self, ctx:OParser.CurlyStatementListContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)

    def exitCategoryMethodListItem(self, ctx:OParser.CategoryMethodListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitMember_method_declaration(self, ctx:OParser.Member_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, MemberMethodDeclaration(name, args, type, stmts))
    

    
    def exitSetter_method_declaration(self, ctx:OParser.Setter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, SetterMethodDeclaration(name, stmts))
    

    
    def exitGetter_method_declaration(self, ctx:OParser.Getter_method_declarationContext):
        name = self.getNodeValue(ctx.name)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, GetterMethodDeclaration(name, stmts))
    

    
    def exitConcreteMemberMethod(self, ctx:OParser.ConcreteMemberMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    def exitAbstractMemberMethod(self, ctx:OParser.AbstractMemberMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitSetterMemberMethod(self, ctx:OParser.SetterMemberMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitGetterMemberMethod(self, ctx:OParser.GetterMemberMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitStatementList(self, ctx:OParser.StatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, StatementList(item))
    

    
    def exitStatementListItem(self, ctx:OParser.StatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitAbstract_method_declaration(self, ctx:OParser.Abstract_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, AbstractMethodDeclaration(name, args, type))
    

    
    def exitConcrete_method_declaration(self, ctx:OParser.Concrete_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, ConcreteMethodDeclaration(name, args, type, stmts))
    
    def exitSingleStatement(self, ctx:OParser.SingleStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, StatementList(stmt))
    
    def exitMethodCallStatement(self, ctx:OParser.MethodCallStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)
    

    def exitConstructor_expression(self, ctx:OParser.Constructor_expressionContext):
        mutable = ctx.MUTABLE() is not None
        type = self.getNodeValue(ctx.typ)
        args = self.getNodeValue(ctx.args)
        if args is None:
            args = ArgumentAssignmentList()
        self.setNodeValue(ctx, ConstructorExpression(type, mutable, args))
    

    def exitAssertion(self, ctx:OParser.AssertionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitAssertionList(self, ctx:OParser.AssertionListContext):
        item = self.getNodeValue(ctx.item)
        items = [ item ]
        self.setNodeValue(ctx, items)


    def exitAssertionListItem(self, ctx:OParser.AssertionListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.push(item)
        self.setNodeValue(ctx, items)

    
    def exitAssign_instance_statement(self, ctx:OParser.Assign_instance_statementContext):
        inst = self.getNodeValue(ctx.inst)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignInstanceStatement(inst, exp))
    

    
    def exitAssignInstanceStatement(self, ctx:OParser.AssignInstanceStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, stmt)


    
    def exitAssign_variable_statement(self, ctx:OParser.Assign_variable_statementContext):
        name = self.getNodeValue(ctx.name)
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, AssignVariableStatement(name, exp))

    def exitAssign_tuple_statement(self, ctx:OParser.Assign_tuple_statementContext):
        items = self.getNodeValue(ctx.items)
        exp = self.getNodeValue(ctx.exp)
        stmt = AssignTupleStatement(items)
        stmt.setExpression(exp)
        self.setNodeValue(ctx, stmt)

    def exitRootInstance(self, ctx:OParser.RootInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, VariableInstance(name))

    def exitRoughlyEqualsExpression(self, ctx):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, EqualsExpression(left, EqOp.ROUGHLY, right))

    def exitChildInstance(self, ctx:OParser.ChildInstanceContext):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.setParent(parent)
        self.setNodeValue(ctx, child)

    def exitMemberInstance(self, ctx:OParser.MemberInstanceContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MemberInstance(None, name))

    def exitItemInstance(self, ctx:OParser.ItemInstanceContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ItemInstance(None, exp))

    def exitConstructorExpression(self, ctx:OParser.ConstructorExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitMethodExpression(self, ctx:OParser.MethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitNativeStatementList(self, ctx:OParser.NativeStatementListContext):
        item = self.getNodeValue(ctx.item)
        items = StatementList(item)
        self.setNodeValue(ctx, items)

    def exitNativeStatementListItem(self, ctx:OParser.NativeStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitJava_identifier(self, ctx:OParser.Java_identifierContext):
        self.setNodeValue(ctx, ctx.getText())

    def exitCsharp_identifier(self, ctx:OParser.Csharp_identifierContext):
        self.setNodeValue(ctx, ctx.getText())

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


    def exitJavaIdentifier(self, ctx:OParser.JavaIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaIdentifierExpression(name))

    def exitCSharpIdentifier(self, ctx:OParser.CSharpIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CSharpIdentifierExpression(None, name))

    def exitCsharp_method_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CSharpMethodExpression(name, args))

    def exitCSharpMethodExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitCSharpSelectorExpression(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        child = self.getNodeValue(ctx.child)
        child.parent = parent
        self.setNodeValue(ctx, child)

    def exitCSharpArgumentList(self,  ctx):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CSharpExpressionList(item))

    def exitCSharpArgumentListItem(self, ctx):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)

    def exitPythonIdentifier(self, ctx:OParser.PythonIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, PythonIdentifierExpression(name))
    
    def exitPythonPrimaryExpression(self, ctx:OParser.PythonPrimaryExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitPythonIdentifierExpression(self, ctx:OParser.PythonIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitJavaIdentifierExpression(self, ctx:OParser.JavaIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)


    def exitCSharpIdentifierExpression(self, ctx):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitJavaChildIdentifier(self, ctx):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = JavaIdentifierExpression(name, parent=parent)
        self.setNodeValue(ctx, child)
    

    
    def exitCSharpChildIdentifier(self, ctx:OParser.CSharpChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = CSharpIdentifierExpression(parent, name)
        self.setNodeValue(ctx, child)
    

    
    def exitPythonChildIdentifier(self, ctx:OParser.PythonChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        child = PythonIdentifierExpression(name, parent)
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
    

    
    def exitCSharpPrimaryExpression(self, ctx:OParser.CSharpPrimaryExpressionContext):
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
        self.setNodeValue(ctx, JavaStatement(exp,False))
    

    
    def exitCSharpStatement(self, ctx:OParser.CSharpStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp,False))
    

    def exitPythonStatement(self, ctx:OParser.PythonStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp,False))
    
    def exitPython_native_statement(self, ctx:OParser.Python_native_statementContext):
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        self.setNodeValue(ctx, PythonNativeCall(stmt, module))

    def exitPython_module(self, ctx:OParser.Python_moduleContext):
        ids = [c.getText() for c in ctx.identifier()]
        module = PythonModule(ids)
        self.setNodeValue(ctx, module)

    
    def exitJavaReturnStatement(self, ctx:OParser.JavaReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaStatement(exp,True))
    

    
    def exitCSharpReturnStatement(self, ctx:OParser.CSharpReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CSharpStatement(exp,True))

    def exitPythonReturnStatement(self, ctx:OParser.PythonReturnStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, PythonStatement(exp,True))

    def exitJavaNativeStatement(self, ctx:OParser.JavaNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, JavaNativeCall(stmt))

    def exitCSharpNativeStatement(self, ctx:OParser.CSharpNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, CSharpNativeCall(stmt))

    def exitPython2NativeStatement(self, ctx:OParser.Python2NativeStatementContext):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python2NativeCall(call.statement, call.module))

    def exitPython3NativeStatement(self, ctx:OParser.Python3NativeStatementContext):
        call = self.getNodeValue(ctx.stmt)
        self.setNodeValue(ctx, Python3NativeCall(call.statement, call.module))
    

    
    def exitNative_method_declaration(self, ctx:OParser.Native_method_declarationContext):
        type = self.getNodeValue(ctx.typ)
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, NativeMethodDeclaration(name, args, type, stmts))
    

    
    def exitJavaArgumentList(self, ctx:OParser.JavaArgumentListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, JavaExpressionList(item))
    

    
    def exitJavaArgumentListItem(self, ctx:OParser.JavaArgumentListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
        self.setNodeValue(ctx, items)
    

    
    def exitJava_method_expression(self, ctx:OParser.Java_method_expressionContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, JavaMethodExpression(name, args))
    

    
    def exitJavaMethodExpression(self, ctx:OParser.JavaMethodExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitFullDeclarationList(self, ctx:OParser.FullDeclarationListContext):
        items = self.getNodeValue(ctx.items)
        if items is None:
            items = DeclarationList()
        self.setNodeValue(ctx, items)
    

    
    def exitDeclarationList(self, ctx:OParser.DeclarationListContext):
        item = self.getNodeValue(ctx.item)
        items = DeclarationList(item)
        self.setNodeValue(ctx, items)
    

    
    def exitDeclarationListItem(self, ctx:OParser.DeclarationListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitMethodDeclaration(self, ctx:OParser.MethodDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitNativeMethod(self, ctx:OParser.NativeMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitConcreteMethod(self, ctx:OParser.ConcreteMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitAbstractMethod(self, ctx:OParser.AbstractMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
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
    

    def exitPythonCharacterLiteral(self, ctx):
        self.setNodeValue(ctx, PythonCharacterLiteral(ctx.getText()))

    def exitPythonIntegerLiteral(self, ctx:OParser.PythonIntegerLiteralContext):
        self.setNodeValue(ctx, PythonIntegerLiteral(ctx.getText()))
    

    
    def exitPythonDecimalLiteral(self, ctx:OParser.PythonDecimalLiteralContext):
        self.setNodeValue(ctx, PythonDecimalLiteral(ctx.getText()))
    

    
    def exitPythonTextLiteral(self, ctx:OParser.PythonTextLiteralContext):
        self.setNodeValue(ctx, PythonTextLiteral(ctx.getText()))
    

    
    def exitJavaLiteralExpression(self, ctx:OParser.JavaLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    


    
    def exitCSharpLiteralExpression(self, ctx:OParser.CSharpLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitPythonLiteralExpression(self, ctx:OParser.PythonLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitJavaCategoryMapping(self, ctx:OParser.JavaCategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, JavaNativeCategoryMapping(map))
    

    
    def exitCSharpCategoryMapping(self, ctx:OParser.CSharpCategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, CSharpNativeCategoryMapping(map))
    

    def exitPython_category_mapping(self, ctx:OParser.Python_category_mappingContext):
        id_ = ctx.id_.getText()
        module = self.getNodeValue(ctx.module)
        self.setNodeValue(ctx, PythonNativeCategoryMapping(id_, module))

    
    def exitPython2CategoryMapping(self, ctx:OParser.Python2CategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, Python2NativeCategoryMapping(map.identifier, map.module))
    

    
    def exitPython3CategoryMapping(self, ctx:OParser.Python3CategoryMappingContext):
        map = self.getNodeValue(ctx.mapping)
        self.setNodeValue(ctx, Python3NativeCategoryMapping(map.identifier, map.module))
    

    
    def exitNativeCategoryMappingList(self, ctx:OParser.NativeCategoryMappingListContext):
        item = self.getNodeValue(ctx.item)
        items = NativeCategoryMappingList(item)
        self.setNodeValue(ctx, items)
    

    
    def exitNativeCategoryMappingListItem(self, ctx:OParser.NativeCategoryMappingListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitNative_category_mappings(self, ctx:OParser.Native_category_mappingsContext):
        items = self.getNodeValue(ctx.items)
        self.setNodeValue(ctx, items)
    

    
    def exitNative_category_declaration(self, ctx:OParser.Native_category_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        mappings = self.getNodeValue(ctx.mappings)
        self.setNodeValue(ctx, NativeCategoryDeclaration(name, attrs, mappings, None))
    

    
    def exitNativeCategoryDeclaration(self, ctx:OParser.NativeCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitNative_resource_declaration(self, ctx:OParser.Native_resource_declarationContext):
        name = self.getNodeValue(ctx.name)
        attrs = self.getNodeValue(ctx.attrs)
        mappings = self.getNodeValue(ctx.mappings)
        self.setNodeValue(ctx, NativeResourceDeclaration(name, attrs, mappings, None))
    

    
    def exitResource_declaration(self, ctx:OParser.Resource_declarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitResourceDeclaration(self, ctx:OParser.ResourceDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitCategoryDeclaration(self, ctx:OParser.CategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitAttributeDeclaration(self, ctx:OParser.AttributeDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitEnumCategoryDeclaration(self, ctx:OParser.EnumCategoryDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitEnumNativeDeclaration(self, ctx:OParser.EnumNativeDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitEnumDeclaration(self, ctx:OParser.EnumDeclarationContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)
    

    
    def exitParenthesis_expression(self, ctx:OParser.Parenthesis_expressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ParenthesisExpression(exp))
    

    
    def exitParenthesisExpression(self, ctx:OParser.ParenthesisExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitNativeSymbolList(self, ctx:OParser.NativeSymbolListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, NativeSymbolList(item))
    

    
    def exitNativeSymbolListItem(self, ctx:OParser.NativeSymbolListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.append(item)
        self.setNodeValue(ctx, items)
    

    
    def exitEnum_native_declaration(self, ctx:OParser.Enum_native_declarationContext):
        name = self.getNodeValue(ctx.name)
        type = self.getNodeValue(ctx.typ)
        symbols = self.getNodeValue(ctx.symbols)
        self.setNodeValue(ctx, EnumeratedNativeDeclaration(name, type, symbols))
    

    
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
    

    
    def exitValue_token(self, ctx:OParser.Value_tokenContext):
        self.setNodeValue(ctx, ctx.getText())
    

    
    def exitNamed_argument(self, ctx:OParser.Named_argumentContext):
        name = self.getNodeValue(ctx.name)
        arg = UnresolvedArgument(name)
        exp = self.getNodeValue(ctx.value)
        arg.defaultValue = exp
        self.setNodeValue(ctx, arg)
    

    
    def exitClosureStatement(self, ctx:OParser.ClosureStatementContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, DeclarationInstruction(decl))
    

    
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
    

    
    def exitCollectionSwitchCase(self, ctx:OParser.CollectionSwitchCaseContext):
        exp = self.getNodeValue(ctx.exp)
        stmts = self.getNodeValue(ctx.stmts)
        self.setNodeValue(ctx, CollectionSwitchCase(exp, stmts))
    

    
    def exitSwitchCaseStatementList(self, ctx:OParser.SwitchCaseStatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))
    

    
    def exitSwitchCaseStatementListItem(self, ctx:OParser.SwitchCaseStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
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
    

    
    def exitLiteralListLiteral(self, ctx:OParser.LiteralListLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, ListLiteral(exp))
    
    def exitLiteralSetLiteral(self, ctx:OParser.LiteralSetLiteralContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, SetLiteral(exp))


    
    def exitLiteralList(self, ctx:OParser.LiteralListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, [ item ])
    

    
    def exitLiteralListItem(self, ctx:OParser.LiteralListItemContext):
        items = self.getNodeValue(ctx.items)
        item = self.getNodeValue(ctx.item)
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
    

    
    def exitContainsAllExpression(self, ctx:OParser.ContainsAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ALL, right))
    

    
    def exitNotContainsAllExpression(self, ctx:OParser.NotContainsAllExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ALL, right))
    

    
    def exitContainsAnyExpression(self, ctx:OParser.ContainsAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS_ANY, right))
    

    
    def exitNotContainsAnyExpression(self, ctx:OParser.NotContainsAnyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS_ANY, right))
    

    
    def exitContainsExpression(self, ctx:OParser.ContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.CONTAINS, right))
    

    
    def exitNotContainsExpression(self, ctx:OParser.NotContainsExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, ContainsExpression(left, ContOp.NOT_CONTAINS, right))
    

    
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
    

    
    def exitAndExpression(self, ctx:OParser.AndExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, AndExpression(left, right))
    

    def exitNullLiteral(self, ctx:OParser.NullLiteralContext):
        self.setNodeValue(ctx, NullLiteral.instance)


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


    def exitOperatorMemberMethod(self, ctx:OParser.OperatorMemberMethodContext):
        decl = self.getNodeValue(ctx.decl)
        self.setNodeValue(ctx, decl)


    def exitOrExpression(self, ctx:OParser.OrExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, OrExpression(left, right))
    

    
    def exitMultiplyExpression(self, ctx:OParser.MultiplyExpressionContext):
        left = self.getNodeValue(ctx.left)
        right = self.getNodeValue(ctx.right)
        self.setNodeValue(ctx, MultiplyExpression(left, right))
    

    
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
    

    
    def exitSorted_expression(self, ctx:OParser.Sorted_expressionContext):
        source = self.getNodeValue(ctx.source)
        key = self.getNodeValue(ctx.key)
        self.setNodeValue(ctx, SortedExpression(source, key))
    

    
    def exitSortedExpression(self, ctx:OParser.SortedExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitDocumentExpression(self, ctx:OParser.DocumentExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitDocument_expression(self, ctx:OParser.Document_expressionContext):
        self.setNodeValue(ctx, DocumentExpression())
    

    
    def exitDocument_type(self, ctx:OParser.Document_typeContext):
        self.setNodeValue(ctx, DocumentType.instance)
    

    
    def exitFetchExpression(self, ctx:OParser.FetchExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
    def exitFetch_expression(self, ctx:OParser.Fetch_expressionContext):
        itemName = self.getNodeValue(ctx.name)
        source = self.getNodeValue(ctx.source)
        filter = self.getNodeValue(ctx.xfilter)
        self.setNodeValue(ctx, FetchExpression(itemName, source, filter))
    
    def exitClosure_expression(self, ctx):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, MethodExpression(name))


    def exitCode_type(self, ctx:OParser.Code_typeContext):
        self.setNodeValue(ctx, CodeType.instance)
    

    
    def exitExecuteExpression(self, ctx:OParser.ExecuteExpressionContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, ExecuteExpression(name))
    

    
    def exitCodeExpression(self, ctx:OParser.CodeExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, CodeExpression(exp))
    

    
    def exitCode_argument(self, ctx:OParser.Code_argumentContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, CodeArgument(name))

    def exitCategory_symbol(self, ctx:OParser.Category_symbolContext):
        name = self.getNodeValue(ctx.name)
        args = self.getNodeValue(ctx.args)
        self.setNodeValue(ctx, CategorySymbol(name, args))

    def exitCategorySymbolList(self, ctx:OParser.CategorySymbolListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, CategorySymbolList(item))
    

    
    def exitCategorySymbolListItem(self, ctx:OParser.CategorySymbolListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
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
    

    
    def exitRead_expression(self, ctx:OParser.Read_expressionContext):
        source = self.getNodeValue(ctx.source)
        self.setNodeValue(ctx, ReadExpression(source))
    

    
    def exitReadExpression(self, ctx:OParser.ReadExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)
    

    
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
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, ListType(type))
    

    
    def exitAnyDictType(self, ctx:OParser.AnyDictTypeContext):
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, DictType(type))
    

    
    def exitAnyArgumentType(self, ctx:OParser.AnyArgumentTypeContext):
        type = self.getNodeValue(ctx.typ)
        self.setNodeValue(ctx, type)
    
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
    

    
    def exitCatchStatementList(self, ctx:OParser.CatchStatementListContext):
        item = self.getNodeValue(ctx.item)
        self.setNodeValue(ctx, SwitchCaseList(item))
    

    
    def exitCatchStatementListItem(self, ctx:OParser.CatchStatementListItemContext):
        item = self.getNodeValue(ctx.item)
        items = self.getNodeValue(ctx.items)
        items.add(item)
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

    def exitJavascriptBooleanLiteral(self, ctx:OParser.JavascriptBooleanLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptBooleanLiteral(text))

    def exitJavascript_category_mapping(self, ctx:OParser.Javascript_category_mappingContext):
        identifier = ctx.identifier().getText()
        module = self.getNodeValue(ctx.javascript_module())
        map = JavaScriptNativeCategoryMapping(identifier, module)
        self.setNodeValue(ctx, map)

    def exitJavascriptCharacterLiteral(self, ctx):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptCharacterLiteral(text))

    def exitJavascript_identifier(self, ctx:OParser.Javascript_identifierContext):
        name = ctx.getText()
        self.setNodeValue(ctx, name)

    def exitJavascriptLiteralExpression(self, ctx:OParser.JavascriptLiteralExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

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
        stmt = self.getNodeValue(ctx.stmt)
        module = self.getNodeValue(ctx.module)
        stmt.module = module
        self.setNodeValue(ctx, stmt)

    def exitJavascriptArgumentList(self, ctx:OParser.JavascriptArgumentListContext):
        exp = self.getNodeValue(ctx.item)
        list = JavaScriptExpressionList(exp)
        self.setNodeValue(ctx, list)

    def exitJavascriptArgumentListItem(self, ctx:OParser.JavascriptArgumentListItemContext):
        exp = self.getNodeValue(ctx.item)
        list = self.getNodeValue(ctx.items)
        list.append(exp)
        self.setNodeValue(ctx, list)

    def exitJavaScriptCategoryMapping(self, ctx:OParser.JavaScriptCategoryMappingContext):
        self.setNodeValue(ctx, self.getNodeValue(ctx.mapping))

    def exitJavascriptChildIdentifier(self, ctx:OParser.JavascriptChildIdentifierContext):
        parent = self.getNodeValue(ctx.parent)
        name = self.getNodeValue(ctx.name)
        exp = JavaScriptIdentifierExpression(parent, name)
        self.setNodeValue(ctx, exp)

    def exitJavascriptDecimalLiteral(self, ctx:OParser.JavascriptDecimalLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptDecimalLiteral(text))

    def exitJavascriptIdentifier(self, ctx:OParser.JavascriptIdentifierContext):
        name = self.getNodeValue(ctx.name)
        self.setNodeValue(ctx, JavaScriptIdentifierExpression(None, name))

    def exitJavascriptIdentifierExpression(self, ctx:OParser.JavascriptIdentifierExpressionContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, exp)

    def exitJavascriptIntegerLiteral(self, ctx:OParser.JavascriptIntegerLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptIntegerLiteral(text))

    def exitJavascriptMethodExpression(self, ctx:OParser.JavascriptMethodExpressionContext):
        method = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, method)

    def exitJavaScriptNativeStatement(self, ctx:OParser.JavaScriptNativeStatementContext):
        stmt = self.getNodeValue(ctx.stmt)
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

    def exitJavascriptStatement(self, ctx:OParser.JavascriptStatementContext):
        exp = self.getNodeValue(ctx.exp)
        self.setNodeValue(ctx, JavaScriptStatement(exp, False))

    def exitJavascriptTextLiteral(self, ctx:OParser.JavascriptTextLiteralContext):
        text = ctx.t.text
        self.setNodeValue(ctx, JavaScriptTextLiteral(text))
