from sympy import solve , Symbol
x = Symbol('x')
ptb2 = x**2 + 9*x +8 
nghiem = solve(ptb2, dict = True) 
print(nghiem)