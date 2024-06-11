import pandas as pd
import matplotlib.pyplot as plt
import os

# 데이터 불러오기
file_path = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\data\\Preprocessed_BankChurners.csv"
data = pd.read_csv(file_path)

# 결과를 저장할 디렉토리 생성
output_dir = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\images\\Histogram"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

unique_value_counts = data.nunique()

for column in data.columns:
    plt.figure(figsize=(8, 6))
    if unique_value_counts[column] <= 20:
        # 유니크한 값의 개수가 20 이하인 경우에는 해당 개수를 히스토그램의 bin 개수로 설정
        bins = unique_value_counts[column]
    else:
        bins = 30  # 유니크한 값의 개수가 20 초과인 경우에는 기본값으로 30개의 bin을 사용
    plt.hist(data[column], color='skyblue', bins=bins)
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
    output_file_path = os.path.join(output_dir, f'{column}_histogram.png')
    plt.savefig(output_file_path)
    plt.close()

print("히스토그램이 성공적으로 저장되었습니다.")
