



## 模板
> 回溯算法模板为： 先写终止条件
```c++

结果result []
之间过程为temp 或者path []

void backtracking(参数) {
    if (终止条件) {
    
        # 这里要求增加一个新的 列表 
        result.append(path[:])
        存放结果;
        return result;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;path.append
        
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```