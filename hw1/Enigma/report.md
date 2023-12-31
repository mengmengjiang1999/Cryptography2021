# report
陈张萌 2017013678
- [report](#report)
  - [破解原理](#破解原理)
  - [注意事项](#注意事项)

## 破解原理

- 题目中所给的置换可以分解为若干个循环，Rejewski 证明了：插线板不影响循环的个数和长度。于是插线板的影响就被消除了。

- 固定Initial Position，遍历三个转轮的顺序，以及所有可能的Ring-Setting，得到所有可能产生的置换，求出其循环的个数和长度，并筛选出与已知的代换循环长度相同的那些。对于符合条件的暴力破解即可。

## 注意事项

查找资料可知，三个转轮进位的位置分别是Q，E，V，并不都是在A处进位。

https://en.wikipedia.org/wiki/Enigma_rotor_details