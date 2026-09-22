name=input("Enter your name:")
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
	factorial *= i
print("your name is ",name,"Factorial of", num, "is", factorial)
