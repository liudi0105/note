# Bash

## 数组

```bash
# 定义数组
arr = (a b c d e)
arr[5] = f

# 打印第一个元素
echo ${arr[0]}  # a

# 打印所有元素
echo ${arr[*]}  # a b c d e f
echo ${arr[@]}  # a b c d e f

# 打印数组的长度
echo ${#arr[*]}  # 6


### 条件判断 ###

if [[  ]]
```
