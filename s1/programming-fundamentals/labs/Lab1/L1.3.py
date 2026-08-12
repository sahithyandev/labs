import math

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

delta = b*b - 4*a*c

if delta > 0:
    # minor optimization
    delta_sqrt = math.sqrt(delta)
    root1 = (-b - delta_sqrt) / (2*a)
    root2 = (-b + delta_sqrt) / (2*a)
    print("Roots are: ", root1, root2)
elif delta == 0:
    root = -b/(2*a)
    print("Roots are: ", root, root)
else:
    print("There are no real roots for the equation.")
