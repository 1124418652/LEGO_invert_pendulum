#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import time
import os,sys


#define PID controller
class pid_set(object):

	def __init__(self,
				SetSpeed = 0, ActualSpeed = 0, duty_cycle = 0,
				err = 0, err_integrate = 0, err_tmp = 0, err_last = 0,
				Kp = 0, Ki = 0, Kd = 0):
		self.SetSpeed = SetSpeed                    #the expected speed
		self.ActualSpeed = ActualSpeed              #the actual speed
		self.duty_cycle = duty_cycle                #the mark_space ratio
		self.err = err                              #the difference between SetSpeed and ActualSpeed
		self.err_integrate = self.integrate         #the accumualte of err
		self.err_tmp = err_tmp                      #the error in t-1
		self.err_last = err_last                    #the error in t-2
		self.Kp = Kp                                #the proportion of pid controller
		self.Ki = Ki                                #the integral coefficient of pid controller
		self.Kd = Kd	                            #the differential coefficient of pid controller

	def set_pid_value(self):
		print("The values of Kp, Ki, Kd are:\t%r, %r, %r\n" %(self.Kp, self.Ki, self.Kd))
		ans = raw_input("If you want to change the value, please press Y, else press N:\n")
		try:
			if ans == 'N':pass
			elif ans == 'Y':
				self.Kp, self.Ki, self.Kd = input("please reset the value of Kp, Ki, Kd:\t")
		except ValueError as e:
			print('ValueError:', e)
		finally:
			print("the pid values have been set successfully!")

	def get_SetSpeed(self, expect_w):
		self.SetSpeed = expect_w

	def get_ActualSpeed(self, actual_w):
		self.ActualSpeed = actual_w

	def pid_realize(self):
		self.err = self.SetSpeed - self.ActualSpeed
		index = 0
		if(abs(self.err) > self.SetSpeed):
			pass
		else:
			index = 1
			self.err_integrate += self.err_integrate
		speed = self.Kp * self.err + index * self.Ki * self.err_integrate + self.Kd * (self.err - self.err_tmp)
		self.err_tmp = self.err
		self.duty_cycle = 8.95 * speed - 53.94                #the value of k should be confirmed through the relationship between duty_cycle and speed
		return self.duty_cycle
		
			                    

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
	pid1.get_SetSpeed(100)
	start = time.perf_counter()
	while time.perf_counter() - start <= 5:
		with open(file_path['speed'], 'r') as f1:
			pid1.get_ActualSpeed(f1.readline())




