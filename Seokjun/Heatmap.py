import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# 데이터 불러오기
file_path = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\Seokjun\\data\\Preprocessed_BankChurners.csv"
data = pd.read_csv(file_path)

# 결과를 저장할 디렉토리 생성
output_dir = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\Seokjun\\images\\Heatmaps"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

correlation_matrix = data.corr()

plt.figure(figsize=(15, 12))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, cmap='GnBu', fmt='.2f', linewidths=.5, mask=mask, annot_kws={"size": 10}, annot=True)
plt.title('Correlation Heatmap')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

output_file_path = os.path.join(output_dir, 'correlation_heatmap.png')
plt.savefig(output_file_path, bbox_inches='tight')
plt.show()

print("히트맵이 성공적으로 저장되었습니다.")
