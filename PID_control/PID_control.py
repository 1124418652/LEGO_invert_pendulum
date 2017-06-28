# -*- coding:utf-8 -*-
import pylab as pl

class pid_set(object):

    def __init__(self, 
                SetAngle=0, ActualAngle=0, err=0, err_integrate = 0, err_tmp = 0, 
                err_last=0, Kp=0, Ki=0, Kd=0):
        self.SetAngle = SetAngle           #设定角度
        self.ActualAngle = ActualAngle     #实际角度
        self.err = err                     #角度偏差
        self.err_integrate = err_integrate #角度偏差的积累
        self.err_tmp = err_tmp             #t-1时刻的角度偏差值
        self.err_last = err_last           #t-2时刻的角度偏差值
        self.Kp = Kp                       #比例系数
        self.Ki = Ki                       #积分系数
        self.Kd = Kd                       #微分系数
        
    def set_start_value(self):
        start_value = []
        start_value = input("""依次输入SetAngle,ActualAngle,err,err_integrate,err_tmp,err_last,Kp,Ki,Kd的初始值:""")
        self.SetAngle, self.ActualAngle, self.err, self.err_integrate, self.err_tmp, self.err_last, self.Kp, self.Ki, self.Kd = start_value
        
    def pid_realize(self):
        #print(self.err,self.err_integrate,self.err_tmp,self.err_last)
        self.err = self.SetAngle - self.ActualAngle
        self.err_integrate += self.err
        diff_angle = self.Kp * (self.err - self.err_tmp) + self.Ki * self.err + self.Kd * (self.err - 2 * self.err_tmp + self.err_last)
        self.ActualAngle += diff_angle
        self.err_last = self.err_tmp
        self.err_tmp = self.err
        return self.ActualAngle
    
    
if __name__ == '__main__':
    pid1 = pid_set()
    pid1.set_start_value()
    angle = []
    for i in range(1000):
        angle.append(pid1.pid_realize())
        #print(pid1.err,pid1.err_integrate,pid1.err_tmp,pid1.err_last)
    x = range(1000)
    y = angle
    print(y)
    pl.plot(x,y)
    pl.show()
        
        
