
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
columns = ["buying", "maint", "doors", "persons",
           "lug_boot", "safety", "class"]

data = pd.read_csv("archive (1)/car_evaluation.csv", names=columns)

print("Dataset Shape:", data.shape)
print("\nFirst 5 rows:")
print(data.head())

# Encode categorical values
encoder = LabelEncoder()

for column in data.columns:
    data[column] = encoder.fit_transform(data[column])

# Features and target
X = data.drop("safety", axis=1)
y = data["safety"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100, random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Results
print("\n===== RANDOM FOREST RESULTS =====")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Sample prediction
print("\n===== SAFETY PREDICTION =====")

for i, prediction in enumerate(model.predict(X_test.iloc[:5])):
    print("Car", i + 1, "Safety:", prediction)












# 1. Import required libraries
# import pandas as pdfrom sklearn.model_selection import train_test_splitfrom sklearn.ensemble import RandomForestClassifierfrom sklearn.preprocessing import LabelEncoderfrom sklearn.metrics import accuracy_score, confusion_matrix, classification_report



# - pandas: Used to load and handle the dataset.
# - train_test_split: Divides the dataset into training and testing data.
# - RandomForestClassifier: Implements the Random Forest classification algorithm.
# - LabelEncoder: Converts categorical text values into numerical values.
# - accuracy_score: Calculates the accuracy of the model.
# - confusion_matrix: Shows correct and incorrect predictions.
# - classification_report: Displays precision, recall, F1-score and support.
# 2. Load the dataset
# columns = ["buying", "maint", "doors", "persons",           "lug_boot", "safety", "class"]



# - Creates a list containing the column names of the Car Evaluation dataset.
# - These columns represent different car features and the target category.
# data = pd.read_csv("archive (1)/car_evaluation.csv", names=columns)



# - read_csv() loads the CSV dataset.
# - names=columns assigns the column names defined above.
# - The loaded dataset is stored in the variable data.
# The dataset contains these seven columns:
# Column	Meaning
# buying	Buying price of the car
# maint	Maintenance cost
# doors	Number of doors
# persons	Passenger capacity
# lug_boot	Luggage boot size
# safety	Safety level
# class	Overall car evaluation

# 3. Display dataset information
# print("Dataset Shape:", data.shape)print("\nFirst 5 rows:")print(data.head())



# - data.shape displays the number of rows and columns.
# - data.head() displays the first five records.
# - This helps us understand the structure of the dataset.
# 4. Convert categorical values into numerical values
# encoder = LabelEncoder()



# - Creates an object of the LabelEncoder class.
# - LabelEncoder converts text categories into numerical values.
# for column in data.columns:    data[column] = encoder.fit_transform(data[column])



# - The for loop processes every column in the dataset.
# - fit_transform() identifies the unique categories in each column and converts them into numerical labels.
# - The converted values are stored back in the same column.
# Example: Text categories such as low, medium and high are converted into numerical values.

# This conversion is necessary because the machine learning model works with numerical data.

# Important: The encoder is fitted separately for each column, so the numerical codes are specific to that column.
# 5. Separate features and target
# X = data.drop("safety", axis=1)y = data["safety"]



# - X contains the input features used for prediction.
# - drop("safety", axis=1) removes the safety column from the input data.
# - axis=1 indicates that we are removing a column.
# - y contains the safety column, which is the target/output.
# In simple words: The model uses the other car features to predict the safety category.

# Note: The class column is also included in X because this code drops only the safety column. So the model uses the overall car evaluation category as one of its input features.
# 6. Split the dataset
# X_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42)



# - Divides the dataset into training and testing sets.
# - X_train: Input features used for training.
# - X_test: Input features used for testing.
# - y_train: Actual safety labels used for training.
# - y_test: Actual safety labels used for testing.
# - test_size=0.2 means 80% data is used for training and 20% for testing.
# - random_state=42 ensures reproducible splitting.
# 7. Create the Random Forest model
# model = RandomForestClassifier(    n_estimators=100, random_state=42)



# - Creates a Random Forest classification model.
# - n_estimators=100 means the model uses 100 decision trees.
# - random_state=42 makes the results reproducible.
# In simple words: Random Forest creates multiple decision trees and combines their predictions to make the final classification.








# virtual-labs.github.io


# 8. Train the model
# model.fit(X_train, y_train)



# - Trains the Random Forest model using the training data.
# - The model learns patterns between the car features and their safety categories.
# - It builds multiple decision trees during training.
# 9. Predict the results
# y_pred = model.predict(X_test)



# - Uses the trained model to predict safety categories for the testing data.
# - Stores the predicted values in y_pred.
# 10. Display accuracy
# print("\n===== RANDOM FOREST RESULTS =====")print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")



# - accuracy_score() compares actual and predicted safety categories.
# - Multiplying by 100 converts accuracy into a percentage.
# - round(..., 2) rounds the result to two decimal places.
# 11. Display confusion matrix
# print("\nConfusion Matrix:")print(confusion_matrix(y_test, y_pred))



# - Displays the confusion matrix.
# - It shows the number of correct and incorrect predictions for each safety category.
# - Values on the diagonal represent correct predictions.
# 12. Display classification report
# print("\nClassification Report:")print(classification_report(y_test, y_pred))



# Displays the model's performance using:
# - Precision: How many predicted samples of a class were actually correct.
# - Recall: How many actual samples of a class were correctly identified.
# - F1-score: Balance between precision and recall.
# - Support: Number of actual samples in each class.
# 13. Display sample predictions
# print("\n===== SAFETY PREDICTION =====")for i, prediction in enumerate(model.predict(X_test.iloc[:5])):    print("Car", i + 1, "Safety:", prediction)



# - X_test.iloc[:5] selects the first five records from the testing dataset.
# - model.predict() predicts their safety categories.
# - enumerate() provides the index and predicted value.
# - The for loop displays the safety prediction for each car.