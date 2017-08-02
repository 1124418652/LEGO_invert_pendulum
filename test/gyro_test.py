#! usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time


dir_path3 = os.path.join(os.path.abspath('.'), "../../../../sys/class/lego-sensor/")
dir_path3_name = os.listdir(dir_path3)
dir_path3 = os.path.join(dir_path3, dir_path3_name[1])
dir_path3_mode = os.path.join(dir_path3, "mode")
dir_path3_value0 = os.path.join(dir_path3, "value0")

f_mod = open(dir_path3_mode, 'r+')
f_val = open(dir_path3_value0, 'r')

f_mod.truncate(0)
f_mod.write('GYRO-RATE')
f_mod.flush()

f_val.seek(0)
init_speed = int(f_val.readline())

f_mod.truncate(0)
f_mod.write('GYRO-ANG')
f_mod.flush()

while True:
	start = time.perf_counter()
	f_val.seek(0)
	angle = int(f_val.readline()) - init_speed * (time.perf_counter() - start)
	print("angle = ", angle)


