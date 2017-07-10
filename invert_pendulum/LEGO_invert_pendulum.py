#! usr/bin/env python
# -*- coding:utf-8 -*-
from sympy import *
from sympy import Derivative as D


var("m_w m_b l R bm J_b J_w F_f T_w T_b th_w th_b MT t tmp tmp2 g")
"""
the physical meaning of each variable:
m_w:            the quality of each wheel
m_b:            the quality of the body
l:              the distance between the center of gravity of the vehicle and the axis of rotation
R:              the radius of the wheel
bm:             the friction coefficient between tire and ground
J_b:            body moment of inertia
J_w:            wheel moment of inertia
F_f:            the friction produced by wheel torque
T_w:            the torque of wheel produced by motor
T_b:            the torque of body produced by motor
th_w:           wheel rotate angle
th_b:           body rotate angle
"""


#calculate the rate of the wheel and the body
dth_b = diff(th_b(t), t)
dth_w = diff(th_w(t), t)
v_bx = l * cos(th_b(t)) * dth_b
v_by = -l * sin(th_b(t)) * dth_b
v_w = R * dth_w

#calculate the force in the direction of th_b and th_w
F_th_b = m_b * g * l * sin(th_b) - 2*T_b
F_th_w = 2*(T_b - F_f * R)


#calculate the lagrange value
L_b = m_b/2 * ((v_bx + v_w)**2 + v_by**2) + J_b/2 * dth_b**2
L_w = m_w * v_w**2 + J_w * dth_w**2
L = L_b + L_w

print("the lagrange value is:\n")
pprint(simplify(L))

#define the function which can calculate lagrange equations
def lagrange_equation(L, th):
    ddL_th = L.subs(D(th(t),t), tmp).diff(tmp, 1).subs(tmp, D(th(t), t))
    dL_th = L.subs(D(th(t),t), tmp).subs(th(t),tmp2).diff(tmp2,1).subs(tmp2,th(t)).subs(tmp,D(th(t),t))
    L_equ = ddL_th.diff(t,1) - dL_th
    #print("the lagrange equation of %r is:\n"%th)
    #pprint(simplify(L_equ))
    #print("\n")
    return L_equ
    
    
var("dth_b dth_w dw_w dw_b")
sublist = [
    (D(th_b(t),t,t), dw_b),
    (D(th_b(t),t), dth_b),
    (D(th_w(t),t,t), dw_w),
    (D(th_w(t),t), dth_w)    
    ]    
    
    
equ_th_b = expand(simplify(lagrange_equation(L, th_b) - F_th_b)).subs(sublist)
equ_th_w = expand(simplify(lagrange_equation(L, th_w) - F_th_w)).subs(sublist)

val = solve((equ_th_b, equ_th_w), (dw_b, dw_w))
dw_b, dw_w = val[dw_b], val[dw_w]

    
    
    
    


