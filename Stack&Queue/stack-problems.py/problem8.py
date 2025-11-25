

def infix_to_postfix(expr):
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack, res = [], ''
    for c in expr:
        if c.isalnum():
            res += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and prec.get(stack[-1], 0) >= prec[c]:
                res += stack.pop()
            stack.append(c)
    while stack:
        res += stack.pop()
    return res

expr = input()
print(infix_to_postfix(expr))
