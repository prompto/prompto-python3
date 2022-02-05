from prompto.declaration.ArrowDeclaration import ArrowDeclaration
from prompto.declaration.ClosureDeclaration import ClosureDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.error.PromptoError import PromptoError
from prompto.runtime.Context import MethodDeclarationMap
from prompto.runtime.Score import Score
from prompto.type.CategoryType import CategoryType
from prompto.type.MethodType import MethodType
from prompto.value.ArrowValue import ArrowValue
from prompto.value.ClosureValue import ClosureValue
from prompto.value.IInstance import IInstance
from prompto.error.SyntaxError import SyntaxError
import itertools

class MethodFinder(object):

    def __init__(self, context, methodCall):
        super(MethodFinder, self).__init__()
        self.context = context
        self.methodCall = methodCall

    def __str__(self):
        return str(self.methodCall)

    def findBest(self, checkInstance):
        decl = self.findBestReference(checkInstance)
        if decl is None:
            decl = self.findBestMethod(checkInstance)
        if decl is None:
            raise SyntaxError("No such method: " + str(self.methodCall))
        else:
            return decl

    def findBestReference(self, checkInstance):
        candidate = self.findCandidateReference(checkInstance)
        if candidate is None:
            return None
        candidates = { candidate }
        compatibles = self.filterCompatible(candidates, checkInstance)
        return compatibles.pop() if len(compatibles) > 0 else None

    def findCandidateReference(self, checkInstance):
        selector = self.methodCall.selector
        if selector.parent is not None:
            return None
        if checkInstance:
            if self.context.hasValue(selector.name):
                value = self.context.getValue(selector.name)
                if isinstance(value, ClosureValue):
                    return self.getClosureDeclaration(self.context, value)
                elif isinstance(value, ArrowValue):
                    return self.getArrowDeclaration(value)
        else:
            named = self.context.getInstance(selector.name, False)
            if named is None:
                return None
            type = named.getType(self.context)
            if isinstance(type, MethodType):
                return type.method.asReference()
        return None

    def getArrowDeclaration(self, value):
        return ArrowDeclaration(value)


    def getClosureDeclaration(self, context, closure):
        decl = closure.itype.method
        if decl.memberOf is not None:
            # the closure references a member method (useful when a method reference is needed)
            # in which case we may simply want to return that method to avoid spilling context into method body
            # this is only true if the closure comes straight from the method's instance context
            # if the closure comes from an accessible context that is not the instance context
            # then it is a local variable that needs the closure context to be interpreted
            selector = self.methodCall.selector
            declaring = context.contextForValue(selector.name)
            if declaring is closure.context:
                return decl
        return ClosureDeclaration(closure)


    def findBestMethod(self, checkInstance):
        candidates = self.findCandidates(checkInstance)
        compatibles = self.filterCompatible(candidates, checkInstance)
        if len(compatibles) == 0:
            return None
        elif len(compatibles) == 1:
            return compatibles.pop()
        else:
            return self.findMostSpecific(compatibles, checkInstance)

    def findCandidates(self, checkInstance):
        candidates = set()
        candidates.update(self.findMemberCandidates(checkInstance))
        candidates.update(self.findGlobalCandidates(checkInstance))
        return candidates

    def findGlobalCandidates(self, checkInstance):
        selector = self.methodCall.selector
        if selector.parent is not None:
            return set()
        else:
            globals = self.context.getRegisteredDeclaration(MethodDeclarationMap, selector.name)
            return set() if globals is None else set(globals.values())

    def findMemberCandidates(self, checkInstance):
        selector = self.methodCall.selector
        if selector.parent is None:
            # if called from a member method, could be a member method called without this / self
            instance = self.context.getClosestInstanceContext()
            if instance is not None:
                type = instance.instanceType
                cd = self.context.getRegisteredDeclaration(ConcreteCategoryDeclaration, type.typeName)
                if cd is not None:
                    members = cd.getMemberMethods(self.context, selector.name)
                    if members is not None:
                        return set(members.values())
            return set()
        else:
            parentType = selector.checkParentType(self.context, checkInstance)
            return set() if parentType is None else set(parentType.getMemberMethods(self.context, selector.name))

    def findMostSpecific(self, candidates, checkInstance):
        candidate = None
        ambiguous = []
        for declaration in candidates:
            if candidate is None:
                candidate = declaration
            else:
                score = self.scoreMostSpecific(candidate, declaration, checkInstance)
                if score is Score.WORSE:
                    candidate = declaration
                    ambiguous = []
                elif score is Score.BETTER:
                    pass
                elif score is Score.SIMILAR:
                    ambiguous.append(declaration)
        if len(ambiguous) > 0:
            raise SyntaxError("Too many prototypes!")  # TODO refine
        return candidate


    def scoreMostSpecific(self, d1, d2, checkInstance):
        try:
            s1 = self.context.newLocalContext()
            d1.registerParameters(s1)
            s2 = self.context.newLocalContext()
            d2.registerParameters(s2)
            las1 = self.methodCall.makeArguments(self.context, d1)
            las2 = self.methodCall.makeArguments(self.context, d2)
            for as1, as2 in itertools.zip_longest(las1, las2):
                ar1 = d1.parameters.find(as1.getName())
                ar2 = d2.parameters.find(as2.getName())
                if as1.getName() == as2.getName():
                    # the general case with named arguments
                    t1 = ar1.getType(s1)
                    t2 = ar2.getType(s2)
                    # try resolving runtime type
                    if checkInstance and isinstance(t1, CategoryType) and isinstance(t2, CategoryType):
                        value = as1.getExpression().interpret(self.context)  # in the named case as1==as2, so only interpret 1
                        if isinstance(value, IInstance):
                            actualType = value.getType()
                            score = actualType.scoreMostSpecific(self.context, t1, t2)
                            if score != Score.SIMILAR:
                                return score
                    if t1.isMoreSpecificThan(s2, t2):
                        return Score.BETTER
                    if t2.isMoreSpecificThan(s1, t1):
                        return Score.WORSE
                else:
                    # specific case for single anonymous argument
                    sp1 = d1.computeSpecificity(s1, ar1, as1, checkInstance)
                    sp2 = d2.computeSpecificity(s2, ar2, as2, checkInstance)
                    if sp1.greaterThan(sp2):
                        return Score.BETTER
                    if sp2.greaterThan(sp1):
                        return Score.WORSE
        except PromptoError:
            pass
        return Score.SIMILAR


    def filterCompatible(self, candidates, checkInstance):
        compatibles = set()
        for declaration in candidates:
            try:
                args = self.methodCall.makeArguments(self.context, declaration)
                if declaration.isAssignableTo(self.context, args, checkInstance):
                    compatibles.add(declaration)
            except SyntaxError:
                # OK
                pass
        return compatibles
