# report

陈张萌 2017013678

- [report](#report)

1. 已知 $n,m$，则分组长度为 $nm$。我们发现对于每个分组，置换如下

$$
     \left(\begin{matrix}
     1 & 2 & 3 & \cdots & n & \cdots & (m-1)n + 1 & (m-1)n + 2 & (m-1)n + 3 & \cdots & mn \\
     1 & m + 1 & 2m + 1 & \cdots & (n-1)m + 1 & \cdots & m & 2m & 3m & \cdots & nm &
     \end{matrix}\right)
$$

使用其逆置换进行变换，即可获得明文。

2. 首先枚举分组长度 $l$，然后枚举 $n$ 满足 $n | l$，则 $m = n / l$。

再使用上述做法即可求出明文：($l = 6, n = 2, m = 3$)

```
Mary, Mary, quite contrary, how does your garden grow?
```