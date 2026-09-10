import operator
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = 0
        operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda a,b: math.trunc(a / b)
        }
        l = []
        for i in tokens:
            if i not in operators:
                l.append(int(i))
            else:
                v2 = l.pop()
                v1 = l.pop()
                op = operators.get(i)
                l.append(op(v1, v2))
        return l[-1]
                

        


