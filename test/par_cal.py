#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import csv
import string
import numpy as np
import pylab as pl
from scipy import optimize


duty_cycle = []
speed= []

with open("test2_res.csv",'r+') as f:
	f.readline()
	reader = csv.reader(f)
	for line in reader:
		d = string.atof(line[0])
		w = string.atof(line[1])
		duty_cycle.append(d)
		speed.append(w)
			
duty_cycle = np.array(duty_cycle)
speed = np.array(speed)
j = 0
avg_speed = []
for i in range(10, 90, 1):
	sum_w = 0
	num = 0
	for x in duty_cycle:
		if x == i:
			sum_w = sum_w + speed[j]
			num = num + 1
			j = j + 1
	print("%r:%r"%(sum_w, num))
	avg_speed.append(sum_w/num)
			
def func(x, p):
	k, b = p
	return k * x + b

def residuals(p, x, y):
	return y - func(x, p)
	
plsq = optimize.leastsq(residuals, [1, 1], args = (duty_cycle, speed))
print("拟合参数为：%r" %(plsq[0]))

pl.plot(duty_cycle, speed)
pl.plot(duty_cycle, func(duty_cycle, plsq[0]))
pl.plot(range(10, 90, 1), avg_speed)
pl.legend()
pl.show()













