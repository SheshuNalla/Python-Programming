a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
d=((b**2)-4*a*c)
root1=(-b+(d**(0.5)))/2*a
root2=(-b-(d**(0.5)))/2*a
print("Roots:",(root1,root2,),sep=(""))
print(f"Roots:({root1},{root2})")