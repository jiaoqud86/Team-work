def save_answer(formula):
    f=open('answer.txt','w')
    f.write(formula)
    f.close()
def save_question(formula):
    f = open('question.txt', 'w', encoding='utf-8')
    f.write(formula)
    f.close()
def check():
    f1=open('answer.txt','r')
    f2=open('grade.txt','r')
    line1=f1.readlines()
    line2=f2.readlines()
    correct=[]
    count_corrent=0
    count_wrong=0
    wrong=[]
    for i in range(len(line1)):
        if line2[i]==line1[i]:
            correct.append(i+1)
            count_corrent+=1
        else:
            wrong.append(i+1)
            count_wrong+=1
    correct=str(correct)
    wrong=str(wrong)
    return correct,wrong,count_corrent,count_wrong

check()