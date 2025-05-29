#1
danhsach1 = [1. , 3.] 
danhsach2 = [5. , 7.] 
danhsach = danhsach1 + danhsach2
danhsach_gapdoi = 2 * danhsach 
print(danhsach)
print(danhsach_gapdoi)



mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1] 
diem_so = [10, 9, 8, 7] 
anh_xa = list(zip(thu_tu, mon_hoc, diem_so))
print(list(anh_xa))
tap_hop = set(anh_xa) 
print(list(tap_hop))
lay_TT, lay_monhoc , lay_diem = zip(*anh_xa)
print(list(zip(range(4), range(7, 12), reversed(range(11) ) ) ))

#2
from sympy import Symbol 
x = Symbol('x') 
f = x + x + x + 2 
print(f)
a = Symbol('Noi')
b = Symbol('Chim')
x = 3*b + 7*a
print(x)
a = Symbol('Noi') 
b = Symbol('Chim') 
a.name 
b.name
print(a.name)
print(b.name)

from sympy import Symbol 
x = Symbol('x') 
y = Symbol('y') 
s = x*y + y*x
print(s)
p = x*(x+2*x) 
print(p)
p = (x+2)*(y+3) 
print(p)
p = (x+2)*(y+3) + (x+2)*(x-3)
print(p)
p = x*(-x+2*x-x) 
print(p)
p = (x+2)*(y+3) 
p.expand()
print(p)

#2.1
from sympy import factor
bieuthuc = x**3 - y**3
print(factor(bieuthuc))

from sympy import expand
bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))

from sympy import Symbol 
x = Symbol('x') 
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)
giatri = bieuthuc.subs({x:3, y:2}) 
print(giatri)
print(x)
print(y)
giatri = bieuthuc.subs({x:3, y:x})
print(giatri)
giatri = bieuthuc.subs({x:y, y:3}) 
print(giatri)
giatri = bieuthuc.subs({y:x}).subs({x:3}) 
print(giatri)

from sympy import Symbol 
x = Symbol('x') 
y = Symbol('y') 
bieuthuc = x*x - x*y + y*y 
print(bieuthuc)
bieuthuc_moi = bieuthuc.subs({x:1-y})
print(bieuthuc_moi)

from sympy import simplify 
dongian = simplify(bieuthuc_moi) 
print(dongian)

from sympy import Symbol 
from sympy import sin, cos 
x = Symbol('x') 
bt = sin(x)*cos(y) + cos(x)*sin(y) 
bt_moi = simplify(bt) 
print(bt_moi)

#3.1
import numpy as np
from numpy import * 
vec1 = np.array([1., 3., 5.])
kq = vec1 * 2
print(kq)
kq = vec1 * vec1
print(kq)
vec1 /2 
print(vec1 + vec1) 
vec2 = array([2., 4., 8.]) 
kq = vec1 + vec2
print(kq)# lý do không thể cộng 2 vec khác kích thước vì vậy thêm số để bằng kích thước
vec3 = array([2., 4., 6.])
kq = vec1 + vec3
print(kq) 
kq = 2* vec1 + 5* vec3 
print(kq)
print(vec3[2]) 
vec4 = np.linspace(0, 20, 5) 
print(vec4) 
vec5 = np.zeros(5) 
print(vec5)
vec6 = np.ones(5)
print(vec6)
vec7 = np.empty(5) 
print(vec7)
vec8 = np.random.random(5)
print(vec8)

v = np.array([1., 3., 5.]) 
np.sum(v)
v.shape
v.transpose() 
v1 = v[:2]
print(v1)
v[0] = 5 
print(v)
print(v1) 
v1[:2] = [1., 2] 
print(v)
v3 = 2 * v[:2] + v1 * 3
print(v3)
v1 = [4, 6] 
print(v3)
print(v)
v + 10.0 
np.sqrt(v)
np.cos(v) 
np.sin(v)
print(np.dot(v1, v3)) 
print(v1.dot(v3))
print(v3.dot(v1))
