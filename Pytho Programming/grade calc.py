m=int(input("Marks in maths:"))
s=int(input("Marks in science:"))
e=int(input("Marks in english:"))
Total=m+s+e
Average=(Total/300)*100
grade=""
if Average >= 90:
    grade="A+"
elif Average >=80 and Average <90:
      grade="A"
elif Average >=70 and Average<80:
	grade="B"
else:
	grade="p"
print(f"Total Marks:{Total}")
print(f"Average :{Average}")
print(f"grade:{grade}")		