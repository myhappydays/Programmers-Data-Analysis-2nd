import pandas as pd
import matplotlib.pyplot as plt

file_path = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\data\\Preprocessed_BankChurners.csv"
data = pd.read_csv(file_path)

for column in data.columns:
    plt.figure(figsize=(8, 6))
    plt.hist(data[column], color='skyblue')
    try:
        mean_value = data[column].mean()
        median_value = data[column].median()
        std_dev = data[column].std()
        plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {mean_value:.2f}')
        plt.axvline(median_value, color='green', linestyle='dashed', linewidth=1.5, label=f'Median: {median_value:.2f}')
        plt.axvline(mean_value + std_dev, color='orange', linestyle='dashed', linewidth=1.5, label=f'Std Dev: {std_dev:.2f}')
        plt.axvline(mean_value - std_dev, color='orange', linestyle='dashed', linewidth=1.5)
    except:
        True
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
