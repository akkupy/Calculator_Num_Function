def calcul(a,b,c):
    if c == '+':
        result =str(a+b)
        traceback="{} + {} = {} ".format(a,b,result)
        return traceback
    elif c == '-':
        result =str(a-b)
        traceback="{} - {} = {} ".format(a,b,result)
        return traceback
    elif c== '*':
        result =str(a*b)
        traceback="{} x {} = {} ".format(a,b,result)
        return traceback
    else:
        result =str(a/b)
        traceback="{} / {} = {} ".format(a,b,result)
        return traceback
