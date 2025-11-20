num1=int(input("give 1st number:"))
num2=int(input("give 2nd number:"))
operator=input("operator:")

if operator=="+":
	print("Addition:",num1+num2,sep=(""))
elif operator=="-":
	print("Subtraction:",num1-num2,sep=(""))
elif operator=="*":
	print("Multiplication:",num1*num2,sep=(""))
elif operator=="/":
	print("Division:",num1/num2,sep=(""))
else:
	print("Invalid operator")				