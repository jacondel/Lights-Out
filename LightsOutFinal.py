import random
import os


def getInput():
    while 1:
        try:
            ip=input("1-25: ")
            number=int(ip)
            if number>0 and number <26 or number==-1 or number==-25:
                return number
            continue
        except:
            #word=str(ip)
            #if(word=="answer"):
            #    return word
            #elif word=="hint":
            #    return word
            continue
        continue
def assignment():
    answers=[]
    L=[]
    for x in range(25):
        L.append("_")
    for x in range(25):
        rand=random.randint(0,1)
        if rand==0:
            L=togglechoose(L,x)  #gaurantees solution
            answers.append(x+1)
    return [L,answers]

def toggle(s):
    if s=="X":
        return "_"
    else:
        return "X"

def togglechoose(L,index):
    #left edge
    if index==5 or index==10 or index==15 or index==20:
        L[index]=toggle(L[index])            #itself
        if index+5<25:
            L[index+5]=toggle(L[index+5])        #above
        if index-5>-1:
            L[index-5]=toggle(L[index-5])        #below
        L[index+1]=toggle(L[index+1])        #right


    #right edge

    elif index==4 or index==9 or index==14 or index==19:
        L[index]=toggle(L[index])            #itself
        if index+5<25:
            L[index+5]=toggle(L[index+5])        #above
        if index-5>-1:
            L[index-5]=toggle(L[index-5])        #below
        L[index-1]=toggle(L[index-1])        #left


    #not left or right edge case
    else:
        L[index]=toggle(L[index])            #itself
        if not index==0:
            L[index-1]=toggle(L[index-1])   #left
        if not index==24:
            L[index+1]=toggle(L[index+1])   #right
        if not index<5:
             L[index-5]=toggle(L[index-5])   #above
        if not index>19:
             L[index+5]=toggle(L[index+5])   #below
    return L

def clear():
  os.system("cls")


def printit(L):
    for x in range(0,5):
        print('  '.join(L[x*5:5*(x+1)]))
    print("---------------------")
    correct=checkwin(L)
    print(str(25-correct) + " on")
    print(str(correct)+" off")
    print("---------------------")
    print("")

    return 0

def checkwin(L):
    count=0
    for x in range(len(L)):
        if L[x]=="_":
            count=count+1
    return count


def run():
    ret=assignment()
    B=ret[0]
    answers=ret[1]
    printit(B)

    while 1:

        ip=getInput()
        print("------------")
        number=ip
        if isinstance(ip,int):
            if number==-1:
                randomIndex= random.randint(0,len(answers)-1)
                print("hint: ",answers[randomIndex])
                continue
            if number == -25:
                print("answers: ",end='')
                print(answers)
                continue
            number=number-1
            B=togglechoose(B,number)
            if number+1 in answers:
                answers.remove(number+1)
            else:
                answers.append(number+1)
            answers.sort()
            if checkwin(B)==25:
                print("YOU WIN!")
                exit()
            else:
                printit(B)
        if isinstance(ip,str):
            if ip=="answer":
                print(answers)
            else:
                randomIndex= random.randint(0,len(answers))
                print(answers[randomIndex])


run()
