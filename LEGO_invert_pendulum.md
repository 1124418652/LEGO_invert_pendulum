# the analys of LEGO invert pendulum
### 乐高倒立摆的简化坐标图如下所示：
![](image/invert_pendulum.png)

Ψ：车体倾斜角度

R：车轮半径

Θ<sub>l,r</sub>：左右车轮转过的角度

Θm<sub>l,r</sub>：左右电机的转动角度

W：车轮间距

Φ：车体与x轴的夹角
### 各参数之间的相互关系

Θ = 1/2 * (Θ<sub>l</sub> + Θ<sub>r</sub>)

Φ = R/W * (Θ<sub>r</sub> - Θ<sub>l</sub>)

x'<sub>m</sub> = R * Θ' * cosΦ

y'<sub>m</sub> = R * Θ' * sinΦ

**各点在坐标系中的位置：**

x<sub>m</sub>: &int;x'<sub>m</sub>dt  
y<sub>m</sub>: &int;y'<sub>m</sub>dt  
z<sub>m</sub>: z<sub>m</sub>

x<sub>l</sub>: x<sub>m</sub> - W/2 * sinΦ  
y<sub>l</sub>: y<sub>m</sub> + W/2 * cosΦ  
z<sub>l</sub>: z<sub>m</sub>

x<sub>r</sub>: x<sub>m</sub> + W/2 * sinΦ  
y<sub>r</sub>: y<sub>m</sub> - W/2 * cosΦ  
z<sub>r</sub>: z<sub>m</sub>

x<sub>b</sub>: x<sub>m</sub> + L * sinΨ * cosΦ  
y<sub>b</sub>: y<sub>m</sub> + L * sinΨ * sinΦ  
z<sub>b</sub>: z<sub>m</sub> + L * sinΨ  

### 根据拉格朗日方程法对平衡车进行建模

**对速度进行分析**  

*车身的速度是由多个速度叠加得到的*  
<table>
	<tr>
		<td> </td> <td>车身倾斜引起</td> <td>车轮转动引起</td> <td>车身旋转引起</td>
	</tr>
	<tr>
		<td>x</td> <td>L*Ψ'*cosΨ*cosΦ</td> <td>(Θ'<sub>l</sub>+Θ'<sub>r</sub>)/2*R*cosΦ</td> 
		<td>-Φ'*L*sinΨ*sinΦ</td>
	</tr>
	<tr>
		<td>y</td> <td>L*Ψ'*cosΨ*sinΦ</td> <td>(Θ'<sub>l</sub>+Θ'<sub>r</sub>)/2*R*sinΦ</td>
		<td>Φ'*L*sinΨ*cosΦ</td>
	</tr>
	<tr>
		<td>z</td> <td>-L*Ψ'sinΨ</td> <td></td> <td></td>
	</tr>
</table>

*平衡车的总能量为车体的动能与两个车轮的动能之和*  
T=1/2*M*[(L*Ψ')<sup>2</sup>+(R*(Θ'<sub>l</sub>+Θ'<sub>r</sub>)/2)<sup>2</sup>+(R*L*(Θ'<sub>l</sub>-Θ'<sub>r</sub>)*sinΨ/W)<sup>2</sup>]  
		+1/2*J<sub>Ψ</sub>*Ψ'<sup>2</sup> -----------车体相对于电机轴转动的动能
		+1/2*J<sub>Ψ</sub>((Θ'<sub>l</sub>-Θ'<sub>r</sub>)*R/W)<sup>2</sup> -----------车体相对于Z轴的转动动能  
		+1/2*m*(Θ'<sub>l</sub>*R)<sup>2</sup>+1/2*m*(Θ'<sub>r</sub>*R)<sup>2</sup> -----------车轮的平动动能  
		+1/2*J<sub>w</sub>(Θ'<sub>l</sub><sup>2</sup>+Θ'<sub>r</sub><sup>2</sup>) -----------车轮相对于电机轴的转动动能  
		+m/4*((Θ'<sub>l</sub>-Θ'<sub>r</sub>)*R)<sup>2</sup> ----------车轮相对于Z轴的转动动能  
  

