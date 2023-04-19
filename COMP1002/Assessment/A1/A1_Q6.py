a = int(input("Please enter length of the first side of a triangle:"))
b = int(input("Please enter length of the second side of a triangle:"))
c = int(input("Please enter length of the third side of a triangle:"))

s = ( a + b + c ) / 2
area = pow ( s * ( s - a ) * ( s - b ) * ( s - c ), 0.5 )

if area > 0 :
    print("The triangle area using Heron's formula is ", area)
else:
    print("There's some error of entered values.")