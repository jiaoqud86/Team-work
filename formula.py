from number import *
from cala import *
class formula:
    def __init__(self,max,min):
        self.symbol_number = 0
        self.max=max
        self.min=min
        self.symbol_number=random.randint(1,3) # 生成运算符号数量

    def generate_formula(self):
        self.bracket_sign = random.randint(0, 1) #是否添加括号
        ns=N_S(self.min,self.max)
        op=[]
        tree=[]
        formula=''
        # 生成运算符号
        for i in range(self.symbol_number):
            op_count = random.randint(0, 3)
            operation = ['+', '-', '*', '÷']
            op.append(operation[op_count])
        if self.bracket_sign==1:
            if self.symbol_number==1:
                self.bracket_sign==0
            else:
                loc=random.randint(0,self.symbol_number-1)
                if loc != 0 and loc + 1 != self.symbol_number:
                    op[loc - 1] = op[loc - 1] + '('
                    op[loc + 1] = ')' + op[loc + 1]
                elif loc == 0:
                    op[loc + 1] = ')' + op[loc + 1]
                    op.insert(loc, '(')
                elif loc + 1 == self.symbol_number:
                    op[loc - 1] = op[loc - 1] + '('
                    op.insert(loc + 1, ')')
        # 生成算式
        if self.bracket_sign==1:
            for i in op:
                if i=='(':
                    formula=formula+i
                else:
                    nums=ns.generate_number_sign()
                    formula=formula+nums+i
            if i!=')':
                nums = ns.generate_number_sign()
                formula = formula + nums
        else:
            for i in op:
                nums = ns.generate_number_sign()
                formula = formula + nums + i
            nums = ns.generate_number_sign()
            formula = formula + nums
        if '+' and '*' in op: #判断生成的算式是否重复，若式子中的符号和数字都相同，则将其判断为重复式子
            num,op=disassemble(formula)
            if [num,op] in tree:
                return False
            else:
                tree.append([num,op])
        return formula