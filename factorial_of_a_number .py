#Factorial of a number

def fact(num):
    if(num <= 1):
        return num
    else:
        return num*fact(num-1)
num = int(input("Enter a positive integer :"))
print('Factorial of ',num, 'is',fact(num))
