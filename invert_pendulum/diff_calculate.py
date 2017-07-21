#! usr/bin/env python
# -*- coding: utf-8 -*-
from math import *
from scipy.integrate import odeint
from LEGO_invert_pendulum import *


class InvertPendulum(object):
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

	def __init__(self, m_w=1.0, m_b=1.0, l=1.0, R=1.0, bm=0.1, J_b=1.0, J_w=1.0, T_b=1.0, g=9.8):
		self.m_w, self.m_b, self.l, self.R, self.bm, self.J_b, self.J_w, self.T_b, self.g = m_w, m_b, l, R, bm, J_b, J_w, T_b, g
		self.init_status = [0.0, 0.0, 0.0, 0.0]
	
	def get_invertpendulum_parameters(self):
		ans = raw_input("the initial value of m_w, m_b, l, R, bm, J_b, J_w, T_b are 1, 1, 1, 1, 0.1, 1, 1, 1, if you want to change the value,\n"
        "please press Y, else press N:\n")
		if ans == 'Y':
			par = []
        	par = raw_input("please input the value of m_w, m_b, l, R, bm, J_b, J_w, T_b:")
        	self.m_w, self.m_b, self.l, self.R, self.bm, self.J_b, self.J_w, self.T_b = par
        	print("the initial parameters have been set successfully!\n")
        
        
        
        
        
        
        
        
