'''def smart(fun):
    def new():
        print("start")
        fun()
        print("end")
    return new
@smart
def skill():
    print("i am skill")
skill()'''
def smart(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner
@smart
def sub(a,b):
    return a-b
sub(3,4)



