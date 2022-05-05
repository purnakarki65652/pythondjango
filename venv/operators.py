#membership Operators
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
    print("Line 1 - x is available in the given list")
else:
    print("Line 1 - x is not available in the given list")
if ( y not in list ):
    print("Line 2 - y is not available in the given list")
else:
    print("Line 2 - y is available in the given list")

#Identity Operator
x = 20
y = 20
if ( x is y ):
    print("x & y  SAME identity")
y=30
if ( x is not y ):
    print("x & y have DIFFERENT identity")
