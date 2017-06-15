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

###根据拉格朗日方程法对平衡车进行建模

**对速度进行分析**  

*车身的速度是由多个速度叠加得到的*  
<table>
	<tr>
		<td> </td><td>车身倾斜引起</td><td>车轮转动引起</td><td>车身旋转引起</td>
	</tr>
</table>
