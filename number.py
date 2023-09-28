import random
from memory_profiler import profile
class N_S:  # 数字结构体
    def __init__(self,min,max):
        self.number_sign = 0  # 数的类型
        self.numerator = 0  # 分子
        self.denominator = 1  # 分母
        self.min=min
        self.max=max

    def generate_number_sign(self):  # 随机生成数的类型，类型值为1时分母默认为1
        self.number_sign = random.randint(1, 2)
        if self.number_sign==1: # 生成数为整数
            self.generate_numerator(self.min,self.max)
            num=str(self.numerator)
        elif self.number_sign==2: # 生成数为分数
            self.generate_numerator(self.min,self.max)
            self.generate_denominator(self.min,self.max)
            if self.numerator>=self.denominator: # 当生成的分数为假分数时，将其转化为带分数
                m=int(self.numerator/self.denominator)
                self.numerator -= m * self.denominator
                if self.numerator!=0:
                    num=str(m)+"'"+str(self.numerator)+'/'+str(self.denominator)
                else:
                    num=str(m)
            else:
                num=str(self.numerator)+'/'+str(self.denominator)
        else:
            return 0
        return num

    def generate_numerator(self, min, max):  # 随机生成分子的大小
        self.numerator = random.randint(min, max)

    def generate_denominator(self, min, max):  # 随机生成分母的大小
        self.denominator = random.randint(min, max)
