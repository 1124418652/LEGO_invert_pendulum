#! usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import os
import csv
import time
import threading
from position_pid import *


#get the path and names of every file
dir_path = os.path.join(os.path.abspath('.'), "../../../../sys/class/tacho-motor")
dir_path1, dir_path2 = os.listdir(dir_path)
dir_path1 = os.path.join(dir_path, dir_path1)
dir_path2 = os.path.join(dir_path, dir_path2)
dir_path1_command = os.path.join(dir_path1, "command")
dir_path1_dutycyclesp = os.path.join(dir_path1, "duty_cycle_sp")
dir_path1_position = os.path.join(dir_path1, "position")
dir_path2_command = os.path.join(dir_path2, "command")
dir_path2_dutycyclesp = os.path.join(dir_path2, "duty_cycle_sp")
dir_path2_position = os.path.join(dir_path2, "position")


pid1 = pid_set()
pid2 = pid_set()

set_angle = range(100, 800, 100)

f_com1 = open(dir_path1_command, 'w')
f_com2 = open(dir_path2_command, 'w')
f_com1.write('run-direct')
f_com2.write('run-direct')

f_pos1 = open(dir_path1_position, 'r+')
f_pos2 = open(dir_path2_position, 'r+')
f_duty1 = open(dir_path1_dutycyclesp, 'w')
f_duty2 = open(dir_path2_dutycyclesp, 'w')

for i in set_angle:
	#make sure the initial position is 0
	f_pos1.truncate(0)
	f_pos1.write('0')
	f_pos1.flush()
	f_pos2.truncate(0)
	f_pos2.write('0')
	f_pos2.flush()

	pid1.get_SetData(i)
	pid2.get_SetData(i)

	start = time.perf_counter()
	while time.perf_counter() - start <= 20:
		f_pos1.seek(0)
		val1 = int(f_pos1.readline())
		f_pos2.seek(0)
		val2 = int(f_pos2.readline())
		print("angle1 = %r\tangle2 = %r" %(val1, val2))

		pid1.get_ActualData(val1)
		pid2.get_ActualData(val2)

		tmp1 = int(pid1.pid_realize())
		tmp2 = int(pid2.pid_realize())

		if tmp1 > 90:
			tmp1 = 100
		elif tmp1 < -90:
			tmp1 = -90

		if tmp2 > 90:
			tmp2 = 100
		elif tmp2 < -90:
			tmp2 = -90

		f_duty1.truncate(0)
		f_duty1.write(str(tmp1))
		f_duty1.flush()
		f_duty2.truncate(0)
		f_duty2.write(str(tmp2))
		f_duty2.flush()

f_com1.truncate(0)
f_com1.write('stop')
f_com1.flush()
f_com2.truncate(0)
f_com2.write('stop')
f_com2.flush()

f_duty1.close()
f_duty2.close()
f_pos1.close()
f_pos2.close()
f_com1.close()
f_com2.close()






	

