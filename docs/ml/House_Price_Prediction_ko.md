## 시각화

### 1. Predicted vs Actual (파란 점)
- 각 점은 테스트 데이터에 대한 **실제 주택 가격(Actual Values)**과 **모델이 예측한 가격(Predicted Values)**을 나타냅니다.
  - **X축**: 실제 값 (Actual)
  - **Y축**: 예측 값 (Predicted)
- 점이 **Ideal Line**에 가까울수록 모델의 예측이 실제 값과 일치함을 의미합니다.

### 2. Ideal Line (빨간 점선)
- 이 선은 \( y = x \) 형태의 선으로, **완벽한 예측**을 나타냅니다.
- 예측 값과 실제 값이 정확히 일치하는 경우 이 선 위에 위치합니다.
- 점이 Ideal Line에서 멀어질수록 오차가 크다는 것을 의미합니다.

## 평가 지표

### Mean Absolute Error (MAE)
- 예측값과 실제값의 **절대 오차**의 평균.

### Mean Squared Error (MSE)
- 예측값과 실제값의 **제곱 오차**의 평균.

### R² Score
- 모델이 데이터의 변동성을 얼마나 설명하는지 나타내는 지표.

### 선형 회귀(Linear Regression)
- 선형 회귀(Linear Regression)는 가장 기본적인 회귀 분석 방법으로, 종속 변수(y)와 하나 이상의 독립 변수(X) 간의 관계를 선형 방정식으로 모델링하는 기법입니다.

``` python
# 3. 선형 회귀 모델링
X = data_cleaned.drop(columns=['MEDV']) # 특성
y = data_cleaned['MEDV'] # 타겟

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 선형 회귀 모델 초기화 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression Performance:")
print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R2 Score: {r2}")

# 예측 결과 시각화
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', label='Ideal Line')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.title('Linear Regression Predictions')
plt.show()
```

## Graph
![House Price Prediction Graph](docs/images/Linear_Regression.png)


## 의사결정나무(Decision Tree)
- **의사결정나무**는 데이터를 **트리 형태**로 분할하여 예측하는 지도 학습 알고리즘입니다.
- 데이터의 특징(Feature)을 기준으로 데이터를 분할해 나가며, 분할이 더 이상 불가능하거나 조건을 만족할 때 예측 값을 도출합니다.

### 의사결정나무의 특징
- **직관적**: 트리 형태로 데이터가 분할되므로 시각화가 쉽습니다.
- **과적합(Overfitting)**: 깊은 트리를 생성할 경우 학습 데이터에 과적합되기 쉽습니다.
- **비선형 데이터 처리**: 복잡한 비선형 관계를 잘 모델링할 수 있습니다.
- **빠른 학습 속도**: 연산이 빠르고 해석이 용이합니다.

``` python
# 의사 결정 나무 모델 초기화 및 학습
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)

# 예측 및 평가 (의사 결정 나무)
y_pred_tree = decision_tree_model.predict(X_test)
mae_tree = mean_absolute_error(y_test, y_pred_tree)
mse_tree = mean_squared_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

print("Decision Tree Performance:")
print(f"MAE: {mae_tree}")
print(f"MSE: {mse_tree}")
print(f"R2 Score: {r2_tree}")

print("Decision Tree Performance:")
print(f"MAE: {mae_tree}")
print(f"MSE: {mse_tree}")
print(f"R2 Score: {r2_tree}")

# 예측 결과 시각화
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_tree, color='green', label='Decision Tree Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', label='Ideal Line')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.title('Decision Tree Predictions')
plt.show()
```

## Graph
![House Price Prediction Graph](docs/images/Decision_Tree.png)

## 랜덤 포레스트(Random Forest)
- **랜덤 포레스트**는 **여러 개의 의사결정나무(Decision Tree)를 앙상블(Ensemble)하여 예측**하는 알고리즘입니다.
- 각 트리는 **무작위로 샘플링**된 데이터와 특징을 사용해 독립적으로 학습됩니다.
- 최종 예측은 개별 트리의 결과를 **평균(회귀)** 또는 **다수결(분류)** 방식으로 결합합니다.

### 랜덤 포레스트의 특징
- **과적합 방지**: 여러 개의 트리를 사용하여 데이터에 과적합되는 것을 방지합니다.
- **안정성**: 노이즈가 많은 데이터에서도 안정적인 성능을 보입니다.
- **높은 예측 정확도**: 개별 트리보다 일반적으로 더 높은 정확도를 제공합니다.
- **병렬 처리**: 각 트리가 독립적으로 학습되므로 병렬 처리가 용이합니다.

``` python
# 랜덤 포레스트 모델 초기화 및 학습
random_forest_model = RandomForestRegressor(random_state=42)
random_forest_model.fit(X_train, y_train)

# 예측 및 평가 (랜덤 포레스트)
y_pred_forest = random_forest_model.predict(X_test)
mae_forest = mean_absolute_error(y_test, y_pred_forest)
mse_forest = mean_squared_error(y_test, y_pred_forest)
r2_forest = r2_score(y_test, y_pred_forest)

print("Random Forest Performance:")
print(f"MAE: {mae_forest}")
print(f"MSE: {mse_forest}")
print(f"R2 Score: {r2_forest}")

# 예측 결과 시각화
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_forest, color='blue', label='Random Forest Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', label='Ideal Line')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.title('Random Forest Predictions')
plt.show()
```

## Graph
![House Price Prediction Graph](docs/images/Random_Forest.png)

## 차이점
| 항목                         | 의사결정나무                             | 랜덤 포레스트                          |
|----------------------------|-----------------------------------------|---------------------------------------|
| **구조**                   | 하나의 트리                              | 다수의 트리 앙상블                     |
| **과적합**                 | 과적합 가능성 큼                         | 과적합 방지                           |
| **학습 속도**              | 빠름                                    | 느림 (다수의 트리 학습 필요)           |
| **예측 정확도**            | 낮음                                    | 높음                                   |
| **노이즈에 대한 민감도**   | 민감                                    | 안정적                                 |
| **해석 가능성**            | 직관적, 시각화 용이                      | 해석이 어렵지만 성능이 뛰어남           |


## Full Source
``` python
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = 'data/housingdata.csv'
data = pd.read_csv(file_path)

imputer = KNNImputer(n_neighbors=5)
data_knn_filled = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# 2. 이상치 처리
# IQR을 이용한 이상치 탐지 및 제거
Q1 = data_knn_filled.quantile(0.25)
Q3 = data_knn_filled.quantile(0.75)
IQR = Q3 - Q1

# 이상치 탐지 조건 설정
outlier_condition = (data_knn_filled < (Q1 - 1.5 * IQR)) | (data_knn_filled > (Q3 + 1.5 * IQR))

# 이상치 제거 (상/하위 1% 데이터 제거)
data_cleaned = data_knn_filled[~outlier_condition.any(axis=1)]

# 3. 선형 회귀, 의사 결정 나무, 랜덤 포레스트 모델 구축 및 평가
X = data_cleaned.drop(columns=['MEDV'])  # 특성
y = data_cleaned['MEDV']  # 타겟

# 훈련 및 테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 모델 초기화
linear_model = LinearRegression()
decision_tree_model = DecisionTreeRegressor(random_state=42)
random_forest_model = RandomForestRegressor(random_state=42)

# 모델 학습
linear_model.fit(X_train, y_train)
decision_tree_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

# 예측
y_pred_linear = linear_model.predict(X_test)
y_pred_tree = decision_tree_model.predict(X_test)
y_pred_forest = random_forest_model.predict(X_test)

# 평가
mae_linear = mean_absolute_error(y_test, y_pred_linear)
mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

mae_tree = mean_absolute_error(y_test, y_pred_tree)
mse_tree = mean_squared_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

mae_forest = mean_absolute_error(y_test, y_pred_forest)
mse_forest = mean_squared_error(y_test, y_pred_forest)
r2_forest = r2_score(y_test, y_pred_forest)

# 성능 시각화
metrics = pd.DataFrame({
    'MAE': [mae_linear, mae_tree, mae_forest],
    'MSE': [mse_linear, mse_tree, mse_forest],
    'R2 Score': [r2_linear, r2_tree, r2_forest]
}, index=['Linear Regression', 'Decision Tree', 'Random Forest'])

metrics.plot(kind='bar', figsize=(10, 6))
plt.title('Model Performance Comparison')
plt.ylabel('Error / Score')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.show()
```

## Graph
![House Price Prediction Graph](docs/images/metrics.png)
