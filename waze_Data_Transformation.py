import pandas as pd
# import numpy as np

file_path = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\data\\waze_app_dataset.csv"
df = pd.read_csv(file_path)
# df['label'].replace('', np.nan, inplace=True)
# df = df.dropna(axis=0)
# df['label'] = df['label'].map({'retained': int(1), 'churn': int(0)})
# print(df['label'].isnull().sum())
# # df['label'] = df['label'].astype(int)
# df['device'] = df['device'].map({'Android': int(0), 'iPhone': int(1)})
# # df['device'] = df['device'].astype(int)

df.dropna(inplace=True)

df['label'] = df['label'].map({'retained': 1, 'churned': 0})

df['device'] = df['device'].map({'Android': 0, 'iPhone': 1})

print(df.head())
print(df.info())
output_file_path = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\data\\waze_app_dataset_transformed.csv"
df.to_csv(output_file_path, index=False)
