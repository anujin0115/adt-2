# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.


Stack = [""] * 8
TopOfStack = -1



def Push(Word):
    global Stack, TopOfStack
    if TopOfStack==7:
        return False
    TopOfStack+=1
    Stack[TopOfStack] = Word
    return True
def Pop():
    global Stack, TopOfStack
    if TopOfStack==-1:
        return ""
    TopOfStack-=1
    return Stack[TopOfStack+1]

def GetText():
    global Stack, TopOfStack
    copy=[]
    for i in range(TopOfStack+1):
        copy.append(Stack[i])
    return " ".join(copy)
# Exercise 2
def DecimalToBinary(Number):
    global Stack, TopOfStack
    if Number == 0:
        return "0"
    TopOfStack = -1
    while Number > 0:
        remainder = str(Number % 2)
        Push(remainder)
        Number = Number // 2
    binary_str = ""
    while TopOfStack != -1:
        binary_str += Pop()
    return binary_str

