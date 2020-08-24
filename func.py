'''
Title: give-three-point-get-twice-function
Author: zymzs
Date: 2020/08/23
License: GNU Ver.3
'''

from sympy import *

while True:
    
    # define
    a = symbols('a')
    b = symbols('b')
    c = symbols('c')
    
    
    # get coordinate of points as temp for further format
    p1t = input("Please enter Point 1(format like '(1,1)'):")
    p2t = input("Please enter Point 2(format like '(1,1)'):")
    p3t = input("Please enter Point 3(format like '(1,1)'):")
    
    # format the points
    p1x = float(p1t.split(',')[0][1:])
    p1y = float(p1t.split(',')[1][:-1])
     # print(p1x)
     # print(p1y)
    p2x = float(p2t.split(',')[0][1:])
    p2y = float(p2t.split(',')[1][:-1])
    p3x = float(p3t.split(',')[0][1:])
    p3y = float(p3t.split(',')[1][:-1])
    
    
    # Wrong! For you can only use ** but not ^ in python.
    '''
    # calculate
    result = solve([Eq(a*(p1x^2)+b*p1x+c, int(p1y)), \
                    Eq(a*(p2x^2)+b*p2x+c, int(p2y)), \
                    Eq(a*(p3x^2)+b*p3x+c, int(p3y))], [a, b, c])
    '''
    
    # calculate
    result = solve([Eq((p1x**2)*a+p1x*b+c, p1y), \
                    Eq((p2x**2)*a+p2x*b+c, p2y), \
                    Eq((p3x**2)*a+p3x*b+c, p3y)], [a, b, c])
        
    print(result)
    
    feedback = input("Continue? (Y/N):")
    if feedback.lower() == "y":
        continue
    else:
        break
