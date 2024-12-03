# Crime Occurrence Pivot Analysis

This code processes a dataset containing crime occurrence and detection statistics, calculates detection rates, and organizes the data into a pivot table for easier analysis.

## Steps in the Code
1. **Data Import and Prepartion**
- Use 'pandas' to load crime occurrence data from an Excel file.
- Use a mapping dictionary to map police station names ('관서명') to district names ('구별').
- Add a new colum '구별' to DataFrame, assigning '구 없음' for unmapped values.

2. **Pivot Table Creation**
- Aggregate specific columns related to crime statistics ('colums_to_pivot') by district using 'pivot_talbe'
- Remove districts labeled as '구 없음' from the pivot table.

3. **Detection Rate Calculation**
- Calculate detection rates for vaious crimes, including rape, robbery, murder, theft, and violence using the formula
Detection Rate (%) = (Cases Detected / Cases Occurred) * 100

4. **Colum Cleanup**
- Use 'del' to remove the original detection and occurrence colums (e.g. , '강간(검거)', '강간(발생)').

5. **Column Renaming**
- Rename colums for clarity.

## Purpose
This transformation simplifies the analysis of crime data by district, enabling better interpretation and visualization of detection rates across different crime categories.

# 범죄 발생 피벗 분석
이 코드는 범죄 발생 및 검거 통계가 포함된 데이터셋을 처리하여, 검거율을 계산하고 피벗 테이블로 정리하여 더 쉽게 분석할 수 있도록 합니다.

## 코드 단계
1. **데이터 가져오기 및 준비**
- pandas를 사용하여 엑셀 파일에서 범죄 발생 데이터를 불러옵니다.
- 경찰서 이름(관서명)을 구 이름(구별)로 매핑하기 위해 매핑 딕셔너리를 사용합니다.
- 새로운 열 구별을 데이터프레임에 추가하며, 매핑되지 않은 값은 구 없음으로 대체합니다.

2. **피벗 테이블 생성**
- 범죄 통계와 관련된 특정 열(colums_to_pivot)을 pivot_talbe로 사용해 구별로 집계합니다.
- 구 없음 으로 표시된 구는 피벗 테이블에서 제거합니다.

3. **검거율 계산**
- 강간, 강도, 살인, 절도, 폭력 등 여러 범죄에 대한 검거율을 다음과 같이 계산합니다.
Detection Rate (%) = (Cases Detected / Cases Occurred) * 100

4. **컴럼 정리**
- del을 사용해 원래의 검거 및 발생 열(강간(검거), 강간(발생))을 삭제합니다.

5. **컬럼 이름 변경**
- 컬럼 이름을 더 명확하게 변경합니다.

## 목적
구별로 범되 데이터를 분석하기 쉽게 만들어, 범죄 카테고리별 검거율을 보다 쉽게 해석하고 시각화할 수 있도록 합니다.

## Source Code

```` python
import numpy as np
import pandas as pd

# 관서별 5대범죄 발생 및 검거 엑셀 파일 경로
crime_occurrence_file_path = 'data/crime_occurrence.xlsx'
# 구별 데이터 csv 파일 경로
district_data_file_path = 'data/district_data.csv'

# 엑셀 파일을 데이터프레임으로 변환
crime_occurrence_df = pd.read_excel(crime_occurrence_file_path, engine='openpyxl')
# print(crime_occurrence_df)

# 경찰서와 구 이름 매핑 딕셔너리
mapping = {
    '서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
    '서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
    '혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
    '마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
    '광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
    '강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구',
    '구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구',
    '방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'
}

# '구별' 컬럼 생성
crime_occurrence_df['구별'] = crime_occurrence_df['관서명'].map(mapping).fillna('구 없음')
# print(crime_occurrence_df)

# 죄종

columns_to_pivot = [
    '강간(검거)', '강간(발생)', '강도(검거)', '강도(발생)', '살인(검거)', '살인(발생)',
    '소계(검거)', '소계(발생)', '절도(검거)', '절도(발생)', '폭력(검거)', '폭력(발생)'
]

crime_occurrence_pivot = crime_occurrence_df.pivot_table(index='구별', values=columns_to_pivot, aggfunc='sum')
crime_occurrence_pivot.drop('구 없음', inplace=True)

# 각 항목별 검거율 추가
crime_occurrence_pivot['강간검거율'] = crime_occurrence_pivot['강간(검거)'] / crime_occurrence_pivot['강간(발생)'] * 100
crime_occurrence_pivot['강도검거율'] = crime_occurrence_pivot['강도(검거)'] / crime_occurrence_pivot['강도(발생)'] * 100
crime_occurrence_pivot['살인검거율'] = crime_occurrence_pivot['살인(검거)'] / crime_occurrence_pivot['살인(발생)'] * 100
crime_occurrence_pivot['절도검거율'] = crime_occurrence_pivot['절도(검거)'] / crime_occurrence_pivot['절도(발생)'] * 100
crime_occurrence_pivot['폭력검거율'] = crime_occurrence_pivot['폭력(검거)'] / crime_occurrence_pivot['폭력(발생)'] * 100

del_colum_list = ['강간(검거)', '강간(발생)', '강도(검거)', '강도(발생)', '살인(검거)', '살인(발생)', '절도(검거)', '절도(발생)', '폭력(검거)', '폭력(발생)']
for del_column in del_colum_list:
    del crime_occurrence_pivot[del_column]

rename_dic = {
    '소계(검거)': '검거율', '소계(발생)': '발생율', '강간검거율': '강간', '강도검거율': '강도', '살인검거율': '살인', '절도검거율': '절도', '폭력검거율': '폭력'
}
crime_occurrence_pivot.rename(columns=rename_dic, inplace=True)

print(crime_occurrence_pivot)
````
