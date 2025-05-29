from sympy import Symbol, solve
x = Symbol('x') 
y = Symbol('y') 
pt1 = 2*x+3*y-12 
pt2 = 3*x-2*y-5 
solve((pt1, pt2), dict=True) 
nghiem = solve((pt1, pt2), dict=True) 
nghiem = nghiem[0] 
pt1 = pt1.subs({x:nghiem[x], y:nghiem[y]}) 
pt2 = pt2.subs({x:nghiem[x], y:nghiem[y]}) 
print(pt1)
print(pt2)