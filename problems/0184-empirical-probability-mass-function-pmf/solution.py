import numpy as np
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    # 1. 前置防御：只有当样本为空时，才返回 []
    if not samples:
        return []
    
    data = np.array(samples)
    m = len(data)
    
    # 2. 统计唯一值与频次（np.unique 默认会自动按升序排序，满足题目要求）
    unique_elements, counts = np.unique(data, return_counts=True)
    
    # 3. 概率归一化
    probs = counts / m
    
    # 4. 用 zip 成对遍历打包成元组列表
    result = []
    for val, prob in zip(unique_elements, probs):
        # 注意：转成原生 Python 类型可避免部分严格评测系统的类型校验问题
        result.append((int(val), float(prob)))
        
    return result