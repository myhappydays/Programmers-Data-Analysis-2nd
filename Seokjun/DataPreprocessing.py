import pandas as pd

# 데이터 불러오기
file_path = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\Seokjun\\data\\BankChurners.csv"
data = pd.read_csv(file_path)

# Attrition_Flag 전처리
data['Attrition_Flag'] = data['Attrition_Flag'].map({'Existing Customer': 1, 'Attrited Customer': 0})

# Gender 전처리
data['Gender'] = data['Gender'].map({'M': 1, 'F': 0})

# Education_Level 전처리
education_map = {
    'Unknown': 0,
    'Uneducated': 1,
    'High School': 2,
    'College': 3,
    'Graduate': 4,
    'Post-Graduate': 5,
    'Doctorate': 6
}
data['Education_Level'] = data['Education_Level'].map(education_map)

# Marital_Status 전처리
marital_map = {
    'Unknown': 0,
    'Single': 1,
    'Married': 2,
    'Divorced': 3
}
data['Marital_Status'] = data['Marital_Status'].map(marital_map)

# Income_Category 전처리
income_map = {
    'Unknown': 0,
    'Less than $40K': 1,
    '$40K - $60K': 2,
    '$60K - $80K': 3,
    '$80K - $120K': 4,
    '$120K +': 5
}
data['Income_Category'] = data['Income_Category'].map(income_map)

# Card_Category 전처리
card_map = {
    'Blue': 0,
    'Silver': 1,
    'Gold': 2,
    'Platinum': 3
}
data['Card_Category'] = data['Card_Category'].map(card_map)

# Naive_Bayes 전처리
columns_to_drop = ['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
                   'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2']
data.drop(columns=columns_to_drop, inplace=True)

# 결과 확인
print(data.head())

if input("저장할래요? (Y / N) : ") == "Y":
    output_file_path = "E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\Seokjun\\data\\Preprocessed_BankChurners.csv"
    data.to_csv(output_file_path, index=False)