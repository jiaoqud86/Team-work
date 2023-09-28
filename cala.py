import fractions
#运算函数
def calculate(num1, num2, op):
    result = 0
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '÷':
        if num2 == 0 :
            return -1
        elif num1%num2!=0:
            return fractions.Fraction(num1,num2)
        result = int(num1 / num2)
    return result

#将传入的算式字符串分解为数字和运算符两份数组
def disassemble(ss):
    s=list(ss)
    num=[]
    op=[]
    for i in range(len(s)):
        if s[i] in "+-*÷()":
            op.append(s[i])
    ss = ss.replace(')+', '.')
    ss = ss.replace(')-', '.')
    ss = ss.replace(')*', '.')
    ss = ss.replace(')÷', '.')
    ss = ss.replace('+(', '.')
    ss = ss.replace('-(', '.')
    ss = ss.replace('*(', '.')
    ss = ss.replace('÷(', '.')
    ss = ss.replace('+' ,'.')
    ss = ss.replace('-', '.')
    ss = ss.replace('*', '.')
    ss = ss.replace('÷', '.')
    ss = ss.replace('(', '.')
    ss = ss.replace(')', '.')
    ss=ss.split('.')

    for i in range(len(ss)):
        if '/' in ss[i]:
            if "'" in ss[i]:
                mix=list(ss[i])
                n=fractions.Fraction(int(mix[0])*int(mix[4])+int(mix[2]),int(mix[4]))
            else:
                n=fractions.Fraction(ss[i])
        elif ss[i]=='(' or ss[i]==')' or ss[i]=='':
            continue
        else:
            n=int(ss[i])
        num.append(n)
    return num,op
def cala(ss):
    num, op = disassemble(ss)
    result = 0
    if '(' in op:
        i = op.index(('('))
        result += calculate(num[i], num[i + 1], op[i+1])
        op.pop(i + 1)
        op.remove('(')
        op.remove(')')
        num[i:i + 2] = []
        num.insert(i, result)
    while len(op) != 0:
        result = 0
        if '*' in op and ('+' or '-') in op:# 若算式中既有加法又有乘法，则要先算乘法
            i = op.index(('*'))
            result += calculate(num[i], num[i + 1], op[i])
            op.remove('*')
            num[i:i + 2] = []
            num.insert(i, result)
        elif '÷' in op and ('+' or '-') in op:
            i = op.index(('÷'))
            result += calculate(num[i], num[i + 1], op[i])
            op.remove('÷')
            num[i:i + 2] = []
            num.insert(i, result)
        else:
            result += calculate(num[0], num[1], op[0])
            op.remove(op[0])
            num[0:2] = []
            num.insert(0, result)
    return num[0]