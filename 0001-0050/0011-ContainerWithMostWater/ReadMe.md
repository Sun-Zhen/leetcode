### 题目
* 给定 n 个正整数 a1，a2，...，an，其中每个点的坐标用（i, ai）表示。 
* 画 n 条直线，使得线 i 的两个端点处于（i，ai）和（i，0）处。
* 请找出其中的两条直线，使得他们与 X 轴形成的容器能够装最多的水。
* 注意：你不能倾斜容器，n 至少是2。

#### 提示
* 其实是求最大的面积
* 也就是求(i-j)*min(a<sub>i</sub>,a<sub>j</sub>)的最大值