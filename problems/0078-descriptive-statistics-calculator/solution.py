import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    # 1. 统一转换为一维 numpy 浮点数组并排序（排序对求中位数、分位数至关重要）
    arr = np.asarray(data, dtype=float).flatten()
    
    # 2. 均值、方差、标准差
    mean_val = float(np.mean(arr))
    variance_val = float(np.var(arr))          # 题目未特指无偏样本方差时，默认总体方差 ddof=0
    std_val = float(np.std(arr))
    
    # 3. 中位数 (如果允许用自带函数直接 np.median，否则对排序后的数组取中值)
    median_val = float(np.median(arr))
    
    # 4. 众数 (利用 np.unique 避免重复遍历)
    vals, counts = np.unique(arr, return_counts=True)
    mode_val = float(vals[np.argmax(counts)])
    
    # 5. 百分位数 (25%, 50%, 75%)
    p25 = float(np.percentile(arr, 25))
    p50 = float(np.percentile(arr, 50))
    p75 = float(np.percentile(arr, 75))
    
    # 6. 四分位距 (IQR)
    iqr_val = float(p75 - p25)
    
    # 7. 组装返回字典 (根据题目约定的 Key 命名，通常小写或下划线)
    return {
        'mean': mean_val,
        'median': median_val,
        'mode': mode_val,
        'variance': variance_val,
        'standard_deviation': std_val,
        '25th_percentile': p25, 
        '50th_percentile':p50, 
        '75th_percentile': p75, 
        'interquartile_range': iqr_val
    }