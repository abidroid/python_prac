x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

if x == 0 and y == 0:
    print('Origin')
elif x > 0 and y > 0:
    print('1st Quadrant')
elif x < 0 and y > 0:
    print('2nd Quadrant')
elif x < 0 and y < 0:
    print('3rd Quadrant')
elif x > 0 and y < 0:
    print('4th Quadrant')
elif x == 0:
    if y > 0:
        print('Positive Y Axis')
    else:
        print('Negative Y Axis')
elif y == 0:
    if x > 0:
        print('Positive X Axis')
    else:
        print('Negative X Axis')