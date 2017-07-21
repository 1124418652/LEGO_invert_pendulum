#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import time
import os
import sys


#get the path and names of every file
dir_path = os.path.join(os.path.abspath('__FILE__'), "../../../../sys/class/tacho-motor")
motor_name = [x for x in os.listdir(dir_path)]
dir_path = os.path.join(dir_path, motor_name[0])

file_path = {}
for y in [y for y in  os.listdir(dir_path)]:
	file_path[y] = os.path.join(dir_path, y)



