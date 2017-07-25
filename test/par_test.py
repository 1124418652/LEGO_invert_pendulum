#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import os
import sys
import csv
import time


#get the path and names of every file
dir_path = os.path.join(os.path.abspath('.'), "../../../../sys/class/tacho-motor")
motor_name = [x for x in os.listdir(dir_path)]
dir_path = os.path.join(dir_path, motor_name[0])

file_path = {}
for y in [y for y in  os.listdir(dir_path)]:
	file_path[y] = os.path.join(dir_path, y)

data = []

with open(file_path["command"], 'w') as file2:
	file2.write("run-direct")

for duty_val in range(10, 90, 5):

	with open(file_path["duty_cycle_sp"], 'r+') as file1:
		file1.write(str(duty_val))
	time.sleep(0.5)
	start = time.perf_counter()
	while time.perf_counter()-start <= 5:
		with open(file_path["duty_cycle"], 'r') as f1:
			with open(file_path["speed"], 'r') as f2:
				data.append((f1.readline().strip(), f2.readline().strip()))

with open(file_path["command"], 'w') as f:
	f.write("stop")

with open("test_res.csv", 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["duty_cycle", "speed"])
	writer.writerows(data)


