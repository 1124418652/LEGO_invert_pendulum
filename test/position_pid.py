#! usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import time
import os
import sys
import csv


#define PID controller
class pid_set(object):
	
	def __init__(self,
				SetData = 0, ActualData = 0,
				err = 0, err_integrate = 0, err_tmp = 0,
				Kp = 2, Ki = 0.02, Kd = 30):
		self.SetData = SetData
		self.ActualData = ActualData
		self.err = err
		self.err_integrate = err_integrate
		self.err_tmp = err_tmp
		self.Kp = Kp
		self.Ki = Ki
		self.Kd = Kd
		
	def set_pid_value(self):
		print("the values of Kp, Ki, Kd are:\t%r, %r, %r\n" %(self.Kp, self.Ki, self.Kd))
		ans = raw_input("If you want to change the value, please press Y, else press N:\n")
		try:
			if ans == 'N': pass
			elif ans == 'Y':
				self.Kp, self.Ki, self.Kd = input("please reset the value of Kp, Ki, Kd:\n")
		except ValueError as e:
			print('ValueError:',e)
		finally:
			print("the pid values have been set successfully!")
				
	def get_SetData(self, s):
		self.SetData = s
		
	def get_ActualData(self, a):
		self.ActualData = a
		
	def pid_realize(self):
		self.err = self.SetData - self.ActualData
		index = 0
		if abs(self.err) >= self.SetData:
			pass
		else:
			index = 1
			self.err_integrate += self.err
		TmpData = self.Kp * self.err + index * self.Ki * self.err_integrate + self.Kd * (self.err - self.err_tmp)
		self.err_tmp = self.err
		return TmpData
	

if __name__ == "__main__":
	#get the path and names of every file
	dir_path = os.path.join(os.path.abspath('.'), "../../../../sys/class/tacho-motor")
	motor_name = [x for x in os.listdir(dir_path)]
	dir_path = os.path.join(dir_path, motor_name[0])
	
	file_name = [y for y in os.listdir(dir_path)]
	file_path = {}
	for y in file_name:
		file_path[y] = os.path.join(dir_path, y)
		
	pid1 = pid_set()
	pid1.get_SetData(200)
	angle = []
	
	#make sure the initial angle is 0
	with open(file_path["position"], 'r+') as f1:
		f1.write('0')
		
	with open(file_path["command"], 'w') as f2:
		f2.write("run-direct")
	
	f3 = open(file_path['position'], 'r')
	f4 = open(file_path['duty_cycle_sp'], 'r+')

	start = time.perf_counter()
	while time.perf_counter() - start <= 20:
		t_start = time.perf_counter()
		f3.seek(0)
		val = int(f3.readline())
		pid1.get_ActualData(val)
		angle.append(val)
		
		tmp = int(pid1.pid_realize())
		if tmp > 90:
			tmp = 90
		elif tmp < -90:
			tmp = -90
		print(tmp)
		f4.truncate(0)
		f4.write(str(tmp))
		f4.flush()
		print(time.perf_counter() - t_start)

	f3.close()
	f4.close()
	
	with open(file_path["command"], 'w') as f5:
		f5.write("stop")
		
	print(angle)	

	with open("angle.csv",'w') as fa:
		writer = csv.writer(fa)
		writer.writerow(angle)
		
	

	
	
	
	
	
	
	
