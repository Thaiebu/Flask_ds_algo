def catAndMouse(x, y, z):
    num1 =0
    num2=0
    if x > z:
        num1=x-z
    else:
        num1=z-x
    
    if y > z:
        num2=y-z
    else:
        num2=z-y
    print(num1,num2)
    
    if num1 == num2:
        print("Mouse C")
    elif num2 > num1:
        print("Cat A")
    elif num1>num2:
        print("Cat B")
catAndMouse(1,3,2)