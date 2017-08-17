#! usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import csv


dir_path3 = os.path.join(os.path.abspath('.'), "../../../../sys/class/lego-sensor/")
dir_path3_name = os.listdir(dir_path3)
dir_path3 = os.path.join(dir_path3, dir_path3_name[1])
dir_path3_mode = os.path.join(dir_path3, "mode")
dir_path3_value0 = os.path.join(dir_path3, "value0")
dir_path3_value1 = os.path.join(dir_path3, "value1")

f_mod = open(dir_path3_mode, 'r+')
f_val_0 = open(dir_path3_value0, 'r')
f_val_1 = open(dir_path3_value1, 'r')


f_mod.truncate(0)
f_mod.write('GYRO-G&A')
f_mod.flush()

f_val_0.seek(0)
init_speed = int(f_val_1.readline())
f_val_1.seek(0)
init_angle = int(f_val_0.readline())

print("init speed = %r\tinit angle = %r " %(init_speed, init_angle))

f_gyrotest = open("gyrotest.csv", 'w')
writer = csv.writer(f_gyrotest)
writer.writerow(("speed", "angle"))
start = time.perf_counter()
while time.perf_counter() - start < 10:
	f_val_0.seek(0)
	speed = int(f_val_1.readline())
	f_val_1.seek(0)
	angle = int(f_val_0.readline())
	print("speed = %r\tangle = %r" %(speed, angle))
	writer.writerow((speed, angle))
	

f_mod.close()
f_val_0.close()
f_val_1.close()

