
# to square every digit of a number and concatenate them.


def square_digits(num):
    
    num=str(num)
    splt_word=list(num)
    strNem=[]
    
    for i in splt_word:
        k=str(int(i)**2)
        strNem.append(k)
        
    x=''.join(strNem)
    x=int(x)
    #print(type(x))
    return x

print(square_digits(81))
