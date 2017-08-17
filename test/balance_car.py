#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time


#define the PID controller
class pid_set(object):
	
	def __init__(self,
				SetData = 0, ActualData = 0,
				err = 0, err_integrate = 0, err_tmp = 0,
				Kp = 5, Ki = 0.1, Kd = 5):
		self.SetData = SetData
		self.ActualData = ActualData
		self.err = err
		self.err_integrate = err_integrate
		self.err_tmp = err_tmp
		self.Kp = Kp
		self.Ki = Ki
		self.Kd = Kd

	def get_SetData(self, s):
		self.SetData = s

	def get_ActualData(self, a):
		self.ActualData = a

	def pid_realize(self):
		self.err = self.SetData - self.ActualData
		index = 0
		"""if abs(self.err) >= (1/4 * self.SetData):"""
		if abs(self.err) >= 10:
			pass
		else:
			index = 1
			self.err_integrate += self.err
		TmpData = self.Kp * self.err + index * self.Ki * self.err_integrate + self.Kd * (self.err - self.err_tmp)
		self.err_tmp = self.err
		return TmpData

	
#get the path of every file
dir_path = os.path.join(os.path.abspath('.'), "../../../../sys/class/tacho-motor")

#the file path of motor1
dir_path1, dir_path2 = os.listdir(dir_path)
dir_path1 = os.path.join(dir_path, dir_path1)
dir_path1_command = os.path.join(dir_path1, "command")
dir_path1_dutycyclesp = os.path.join(dir_path1, "duty_cycle_sp")
dir_path1_position = os.path.join(dir_path1, "position")

#the file path of motor2
dir_path2 = os.path.join(dir_path, dir_path2)
dir_path2_command = os.path.join(dir_path2, "command")
dir_path2_dutycyclesp = os.path.join(dir_path2, "duty_cycle_sp")
dir_path2_position = os.path.join(dir_path2, "position")

#the file path of gyro sensor
dir_path3 = os.path.join(os.path.abspath('.'), "../../../../sys/class/lego-sensor/")
dir_path3_name = os.listdir(dir_path3)
dir_path3 = os.path.join(dir_path3, dir_path3_name[1])
dir_path3_mode = os.path.join(dir_path3, "mode")
dir_path3_value0 = os.path.join(dir_path3, "value0")
dir_path3_value1 = os.path.join(dir_path3, "value1")


if __name__ == "__main__":

	#open the files of gyro sensor
	f_mod = open(dir_path3_mode, 'r+')
	f_val_0 = open(dir_path3_value0, 'r')
	f_val_1 = open(dir_path3_value1, 'r')
	
	#get the initial value of rotation speed
	f_mod.truncate(0)
	f_mod.write('GYRO-G&A')
	f_mod.flush()

	f_val_0.seek(0)
	init_speed = int(f_val_0.readline())

	#get the initial value of angle
	f_val_1.seek(0)
	init_angle = int(f_val_1.readline())

	#open the files of motor1
	f_com1 = open(dir_path1_command, 'w')
	f_pos1 = open(dir_path1_position, 'r+')
	f_duty1 = open(dir_path1_dutycyclesp, 'w')

	#open the files of motor2
	f_com2 = open(dir_path2_command, 'w')
	f_pos2 = open(dir_path2_position, 'r+')
	f_duty2 = open(dir_path2_dutycyclesp, 'w')

	#run motors
	print("ready to go!")
	f_com1.truncate(0)
	f_com1.write("run-direct")
	f_com1.flush()
	f_com2.truncate(0)
	f_com2.write("run-direct")
	f_com2.flush()

	#invoking PID class
	pid_motor1 = pid_set()
	pid_motor2 = pid_set()
	pid_angle = pid_set()

	while True:
		#make sure the initial position is 0
		f_pos1.truncate(0)
		f_pos1.write('0')
		f_pos1.flush()
		f_pos2.truncate(0)
		f_pos2.write('0')
		f_pos2.flush()

		#get the actual angle of motor1 and motor2
		f_pos1.seek(0)
		th_motor1 = int(f_pos1.readline())
		f_pos2.seek(0)
		th_motor2 = int(f_pos2.readline())
		
		#set the angle of the car
		pid_angle.get_SetData(init_angle)
		f_val_1.seek(0)
		actual_angle = int(f_val_1.readline())
		if actual_angle >= 10:
			tmp = 100
		elif actual_angle <= -10:
			tmp = -100
		
		print("angle = ", actual_angle)

		pid_angle.get_ActualData(actual_angle)

		tmp = int(pid_angle.pid_realize())

		if tmp > 100:
			tmp = 100
		elif tmp < -100:
			tmp = -100

		print(-tmp)

		f_duty1.truncate(0)
		f_duty1.write(str(-tmp))
		f_duty1.flush()

		f_duty2.truncate(0)
		f_duty2.write(str(-tmp))
		f_duty1.flush()


	f_com1.close()
	f_com2.close()
	f_pos1.close()
	f_pos2.close()
	f_duty1.close()
	f_duty2.close()
	#f_mod.close()
	f_val.close()



		


























 





