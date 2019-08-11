from prompto.error.PromptoError import PromptoError
from prompto.runtime.Score import Score
from prompto.type.CategoryType import CategoryType
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

    def findMethod(self, checkInstance):
        candidates = self.methodCall.selector.getCandidates(self.context, checkInstance)
        if len(candidates) == 0:
            raise SyntaxError("No method found for:" + str(self.methodCall))
        compatibles = self.filterCompatible(candidates, checkInstance)
        if len(compatibles) == 0:
            raise SyntaxError("No matching prototype for:" + str(self.methodCall))
        elif len(compatibles) == 1:
            return compatibles.pop()
        else:
            return self.findMostSpecific(compatibles, checkInstance)


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
            d1.registerArguments(s1)
            s2 = self.context.newLocalContext()
            d2.registerArguments(s2)
            las1 = self.methodCall.makeArguments(self.context, d1)
            las2 = self.methodCall.makeArguments(self.context, d2)
            for as1, as2 in itertools.zip_longest(las1, las2):
                ar1 = d1.getArguments().find(as1.getName())
                ar2 = d2.getArguments().find(as2.getName())
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
