# Declare Integer variable
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
if a < b and c < b:
    print ("b is greater")
elif c < a and b < a:
    print("a is greater")
elif a < c and  b < c:
    print("c is greater ") 