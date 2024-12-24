## Visualization

### 1. Predicted vs Actual (Blue Dots)
- Each dot represents the **actual house price (Actual Values)** and the **model-predicted price (Predicted Values)** for the test data.
  - **X-Axis**: Actual Values
  - **Y-Axis**: Predicted Values
- The closer the points are to the **Ideal Line**, the better the model's predictions match the actual values.

### 2. Ideal Line (Red Dashed Line)
- This line represents the equation \( y = x \), indicating **perfect predictions**.
- Points on this line indicate the predicted values match the actual values exactly.
- The farther the points are from the Ideal Line, the larger the prediction error.

## Evaluation Metrics

### Mean Absolute Error (MAE)
- The average of the **absolute differences** between predicted and actual values.

### Mean Squared Error (MSE)
- The average of the **squared differences** between predicted and actual values.

### R² Score
- A metric indicating how well the model explains the variability in the data.

### Linear Regression
- Linear Regression is a basic regression method that models the relationship between a dependent variable (y) and one or more independent variables (X) using a linear equation.

```python
# 3. Linear Regression Modeling
X = data_cleaned.drop(columns=['MEDV'])  # Features
y = data_cleaned['MEDV']  # Target

# Data Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression Performance:")
print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R2 Score: {r2}")

# Visualization of Predictions
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
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/Linear_Regression.png)

## Decision Tree
- Decision Trees predict outcomes by splitting data into branches based on feature values.
- They split the data recursively until the stopping criteria are met, generating predictions at the leaf nodes.

### Features of Decision Trees
- Intuitive: Easy to visualize as a tree structure.
- Overfitting: Deep trees can lead to overfitting on training data.
- Handles Non-linearity: Capable of modeling complex non-linear relationships.
- Fast Training: Computationally efficient and easy to interpret.

```python
# Initialize and Train Decision Tree Model
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)

# Predictions and Evaluation (Decision Tree)
y_pred_tree = decision_tree_model.predict(X_test)
mae_tree = mean_absolute_error(y_test, y_pred_tree)
mse_tree = mean_squared_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

print("Decision Tree Performance:")
print(f"MAE: {mae_tree}")
print(f"MSE: {mse_tree}")
print(f"R2 Score: {r2_tree}")

# Visualization of Predictions
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
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/Decision_Tree.png)

## Random Forest
- Random Forest is an ensemble algorithm combining multiple Decision Trees.
- Each tree is trained on a random subset of data and features.
- Predictions are aggregated using averaging (regression) or majority voting (classification).

### Features of Random Forest
- Reduces Overfitting: Combines multiple trees to prevent overfitting.
- Stable Performance: Robust to noisy data.
- Higher Accuracy: Provides more accurate predictions than a single tree.
- Parallelizable: Trees can be trained independently, enabling parallel processing.

```python
# Initialize and Train Random Forest Model
random_forest_model = RandomForestRegressor(random_state=42)
random_forest_model.fit(X_train, y_train)

# Predictions and Evaluation (Random Forest)
y_pred_forest = random_forest_model.predict(X_test)
mae_forest = mean_absolute_error(y_test, y_pred_forest)
mse_forest = mean_squared_error(y_test, y_pred_forest)
r2_forest = r2_score(y_test, y_pred_forest)

print("Random Forest Performance:")
print(f"MAE: {mae_forest}")
print(f"MSE: {mse_forest}")
print(f"R2 Score: {r2_forest}")

# Visualization of Predictions
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
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/Random_Forest.png)

## Comparison
| Feature                    | Decision Tree                           | Random Forest                        |
|----------------------------|-----------------------------------------|---------------------------------------|
| **Structure**              | Single Tree                             | Ensemble of Multiple Trees            |
| **Overfitting**            | High Potential                         | Prevents Overfitting                  |
| **Training Speed**         | Fast                                    | Slow (Requires Training Multiple Trees) |
| **Prediction Accuracy**    | Low                                     | High                                  |
| **Noise Sensitivity**      | Sensitive                               | Stable                                |
| **Interpretability**       | Intuitive, Easy to Visualize            | Difficult to Interpret but High Performance |

## Full Source Code
```python
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load Data
file_path = 'data/housingdata.csv'
data = pd.read_csv(file_path)

# Handle Missing Values using KNN Imputation
imputer = KNNImputer(n_neighbors=5)
data_knn_filled = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# 2. Handle Outliers
# Detect and Remove Outliers using IQR
Q1 = data_knn_filled.quantile(0.25)
Q3 = data_knn_filled.quantile(0.75)
IQR = Q3 - Q1

# Outlier Condition
outlier_condition = (data_knn_filled < (Q1 - 1.5 * IQR)) | (data_knn_filled > (Q3 + 1.5 * IQR))

# Remove Outliers
data_cleaned = data_knn_filled[~outlier_condition.any(axis=1)]

# 3. Train Linear Regression, Decision Tree, and Random Forest Models
X = data_cleaned.drop(columns=['MEDV'])  # Features
y = data_cleaned['MEDV']  # Target

# Split Data into Train and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Models
linear_model = LinearRegression()
decision_tree_model = DecisionTreeRegressor(random_state=42)
random_forest_model = RandomForestRegressor(random_state=42)

# Train Models
linear_model.fit(X_train, y_train)
decision_tree_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

# Make Predictions
y_pred_linear = linear_model.predict(X_test)
y_pred_tree = decision_tree_model.predict(X_test)
y_pred_forest = random_forest_model.predict(X_test)

# Evaluate Models
mae_linear = mean_absolute_error(y_test, y_pred_linear)
mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

mae_tree = mean_absolute_error(y_test, y_pred_tree)
mse_tree = mean_squared_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

mae_forest = mean_absolute_error(y_test, y_pred_forest)
mse_forest = mean_squared_error(y_test, y_pred_forest)
r2_forest = r2_score(y_test, y_pred_forest)

# Visualize Model Performance
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
![](https://github.com/eungyukm/TeamPythonRun/blob/main/docs/images/metrics.png)
