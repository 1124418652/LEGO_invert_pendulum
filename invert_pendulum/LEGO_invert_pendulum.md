## 构建倒立摆的拉格朗日微分方程组

##### 变量说明  
**m<sub>w</sub>**:单个车轮的质量  
**m<sub>b</sub>**:车身的质量  
**l**:车身重心与转动轴心的距离  
**R**:车轮半径  
**bm**:地面和车轮之间的摩擦系数  
**J<sub>b</sub>**:车身的转动惯量  
**J<sub>w</sub>**:车轮的转动惯量  
**F<sub>f</sub>**:车轮与地面之间的摩擦力  
**T<sub>w</sub>**:电机对车轮的转矩  
**T<sub>b</sub>**:电机对车身的转矩  
**th<sub>w</sub>**:车轮转动角度  
**th<sub>b</sub>**:车身转动角度  


### 受力分析
![平衡车受力分析图](../image/invert_pendulum1.jpg)  
* 为了简化分析过程，假设两侧车轮转速始终相同，即不具备转弯功能  

* **车轮转动方向的受力为:**F<sub>th<sub>w</sub></sub> = 2*(T<sub>b</sub> - F<sub>f</sub> * R)  
* **车身转动方向的受力为:**F<sub>th<sub>b</sub></sub> = m<sub>b</sub> * g * l * sin(th<sub>b</sub>) - 2*T<sub>b</sub>  
**拉格朗日方程**  
![拉格朗日方程](../image/lagrange_equation.jpg)  
<p>根据拉格朗日方程公式，即可写出该平衡车的拉格朗日微分方程组</p>










