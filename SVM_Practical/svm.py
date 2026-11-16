
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("archive/emails.csv")

# Display dataset information
print("Dataset Shape:", data.shape)
print("\nFirst 5 rows:")
print(data.head())

# Separate features and target
X = data.iloc[:, 1:-1]
y = data.iloc[:, -1]

# Display class distribution
print("\nClass Distribution:")
print(y.value_counts())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# Create SVM model
model = SVC(kernel="linear")

# Train the model
print("\nTraining SVM model...")
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n========== SVM RESULTS ==========")
print("Accuracy:", round(accuracy * 100, 2), "%")

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Normal", "Abnormal"]
))

# Display sample predictions
print("\n========== EMAIL PREDICTION ==========")

sample = X_test.iloc[:5]
predictions = model.predict(sample)

for i, prediction in enumerate(predictions):
    if prediction == 1:
        result = "Abnormal (Spam)"
    else:
        result = "Normal (Not Spam)"

    print("Email", i + 1, ":", result)






















# 1. Import required libraries
# import pandas as pdfrom sklearn.model_selection import train_test_splitfrom sklearn.svm import SVCfrom sklearn.metrics import accuracy_score, confusion_matrix, classification_report



# - pandas: Used to load and handle the dataset.
# - train_test_split: Divides the dataset into training and testing data.
# - SVC: Stands for Support Vector Classifier. It implements the SVM algorithm for classification.
# - accuracy_score: Calculates the accuracy of the model.
# - confusion_matrix: Shows correct and incorrect predictions.
# - classification_report: Displays precision, recall, F1-score and support.
# 2. Load the dataset
# data = pd.read_csv("archive/emails.csv")



# - read_csv() reads the email dataset from the CSV file.
# - The loaded dataset is stored in the variable data.
# - The dataset contains numerical features of emails and a target column that identifies whether an email is normal or abnormal.
# Important: The file path archive/emails.csv is relative to the folder from which you run the Python program. Make sure the archive folder is in the correct location.
# 3. Display dataset information
# print("Dataset Shape:", data.shape)



# - Displays the shape of the dataset.
# - data.shape returns the number of rows and columns.
# - Rows represent email records, and columns represent features and the target.
# print("\nFirst 5 rows:")print(data.head())



# - head() displays the first five rows of the dataset.
# - It helps us understand the structure and values of the dataset.
# 4. Separate features and target
# X = data.iloc[:, 1:-1]y = data.iloc[:, -1]



# - X contains the input features used for prediction.
# - y contains the target/output column.
# - iloc is used to select rows and columns by their numerical positions.
# - data.iloc[:, 1:-1] selects all rows and columns starting from the second column up to, but not including, the last column.
# - data.iloc[:, -1] selects the last column as the target.
# In simple words: We separate the information used to identify an email from the column that tells us whether it is normal or abnormal.
# 5. Display class distribution
# print("\nClass Distribution:")print(y.value_counts())



# - value_counts() counts how many times each target class appears.
# - It shows the number of normal and abnormal email records.
# - This helps us understand whether the dataset has balanced or imbalanced classes.
# 6. Split the dataset
# X_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42)



# - Divides the dataset into training and testing sets.
# - X_train contains input features for training.
# - X_test contains input features for testing.
# - y_train contains the correct training labels.
# - y_test contains the correct testing labels.
# - test_size=0.2 means 80% data is used for training and 20% for testing.
# - random_state=42 ensures the same random split each time.
# print("\nTraining Data:", X_train.shape)print("Testing Data:", X_test.shape)



# - Displays the number of rows and columns in the training and testing data.
# 7. Create the SVM model
# model = SVC(kernel="linear")



# - Creates an SVM classification model.
# - SVC means Support Vector Classifier.
# - kernel="linear" tells the model to use a linear decision boundary to separate the classes.
# In simple words: SVM tries to find the best possible boundary that separates normal emails from abnormal emails.
# 8. Train the model
# print("\nTraining SVM model...")model.fit(X_train, y_train)



# - Displays a training message.
# - fit() trains the SVM model using the training features and their correct labels.
# - The model learns how to distinguish between the two email categories.
# 9. Predict test data
# y_pred = model.predict(X_test)



# - Uses the trained model to predict the classes of the testing emails.
# - The predicted results are stored in y_pred.
# - The predictions can be compared with the actual labels in y_test.
# 10. Calculate accuracy
# accuracy = accuracy_score(y_test, y_pred)



# - Compares actual labels with predicted labels.
# - Calculates the percentage of correct predictions.
# print("\n========== SVM RESULTS ==========")print("Accuracy:", round(accuracy * 100, 2), "%")



# - Displays the model's accuracy.
# - accuracy * 100 converts the result into a percentage.
# - round(..., 2) rounds it to two decimal places.
# 11. Display confusion matrix
# print("\nConfusion Matrix:")print(confusion_matrix(y_test, y_pred))



# - Displays a confusion matrix.
# - It shows how many predictions were correct and incorrect for each class.
# For a binary classification problem, the matrix looks like this:
# 	Predicted Normal	Predicted Abnormal
# Actual Normal	True Normal	False Abnormal
# Actual Abnormal	False Normal	True Abnormal

# - Correct predictions appear on the diagonal.
# - Incorrect predictions appear outside the diagonal.
# 12. Display classification report
# print("\nClassification Report:")print(classification_report(    y_test,    y_pred,    target_names=["Normal", "Abnormal"]))



# - Displays a detailed performance report of the model.
# - target_names assigns readable names to the two classes.
# The report contains:
# - Precision: Out of all emails predicted as a particular class, how many were actually from that class?
# - Recall: Out of all actual emails belonging to a class, how many were correctly identified?
# - F1-score: Harmonic mean of precision and recall.
# - Support: Number of actual samples belonging to each class.
# 13. Display sample predictions
# print("\n========== EMAIL PREDICTION ==========")sample = X_test.iloc[:5]predictions = model.predict(sample)



# - X_test.iloc[:5] selects the first five emails from the testing dataset.
# - predict() predicts whether these emails are normal or abnormal.
# - The results are stored in predictions.
# for i, prediction in enumerate(predictions):    if prediction == 1:        result = "Abnormal (Spam)"    else:        result = "Normal (Not Spam)"    print("Email", i + 1, ":", result)



# - enumerate() provides the index and prediction for each email.
# - The if-else condition checks the predicted class.
# - If prediction is 1, it displays Abnormal (Spam).
# - If prediction is 0, it displays Normal (Not Spam).
# - Finally, it displays the prediction for each of the five emails.