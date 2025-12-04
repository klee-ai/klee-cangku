from numpy_utils import compute_stats

def main():
    print("数据统计分析")
    values = [10, 20, 30, 40, 50]
    stats = compute_stats(values)
    
    print(f"数据: {values}")
    print(f"均值: {stats['mean']:.2f}")
    print(f"标准差: {stats['std']:.2f}")
    print(f"范围: {stats['min']}~{stats['max']}")

if __name__ == "__main__":
    main()
