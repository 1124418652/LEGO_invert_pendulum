#! /bin/bash
MC=~/../../sys/class/tacho-motor/motor4
echo 50 > $MC/duty_cycle_sp
cat $MC/duty_cycle_sp
echo run-direct > $MC/command
