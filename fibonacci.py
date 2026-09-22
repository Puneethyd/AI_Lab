
def func(numdigits):
    if(numdigits<=2):
        if(numdigits==0):
            return error
        elif(numdigits==1):
            return 1
        else:
            return [0,1]

    else:
        i=[0,1]
        a=0
        b=1
        c=0
        sum=a+b
        while(numdigits>2):
            a=b
            b=sum
            sum=a+b
            i.append(sum)
            numdigits=numdigits-1

        for j in i:
            print(j)

n=int(input("Enter number of terms of fibonacci you want: "))
func(n)
            
            
            
        
