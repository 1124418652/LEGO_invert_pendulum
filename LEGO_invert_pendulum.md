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

x'<sub>m</sub> = R * Θ' *cosΦ

y'<sub>m</sub> = R * Θ' *sinΦ

各点在坐标系中的位置：

x<sub>m</sub>: &int;x'<sub>m</sub>dt

