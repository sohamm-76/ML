
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# AdaBoost Classifier
ada = AdaBoostClassifier(n_estimators=50)
ada.fit(X_train, y_train)
y_pred_ada = ada.predict(X_test)

# Gradient Boosting Classifier
gb = GradientBoostingClassifier(n_estimators=100)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)

# XGBoost Classifier
xgb = XGBClassifier(
    use_label_encoder=False,
    eval_metric='mlogloss'
)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)

# Compare accuracy
print("AdaBoost Accuracy:", accuracy_score(y_test, y_pred_ada))
print("Gradient Boosting Accuracy:", accuracy_score(y_test, y_pred_gb))
print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))
























# . Import required libraries
# from sklearn.datasets import load_irisfrom sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifierfrom xgboost import XGBClassifierfrom sklearn.model_selection import train_test_splitfrom sklearn.metrics import accuracy_score, classification_report



# - load_iris: Loads the built-in Iris flower dataset.
# - AdaBoostClassifier: Implements the AdaBoost classification algorithm.
# - GradientBoostingClassifier: Implements the Gradient Boosting algorithm.
# - XGBClassifier: Implements the XGBoost classification algorithm.
# - train_test_split: Divides the dataset into training and testing data.
# - accuracy_score: Calculates the accuracy of the models.
# - classification_report: Generates a detailed classification report containing precision, recall and F1-score. Note: It is imported here but not used in the given code.
# 2. Load the Iris dataset
# iris = load_iris()X, y = iris.data, iris.target



# - load_iris() loads the Iris dataset.
# - The dataset contains 150 flower samples.
# - Each flower has four features:
#   1. Sepal length
#   2. Sepal width
#   3. Petal length
#   4. Petal width
# - X stores the input features.
# - y stores the target labels (flower species).
# The dataset contains three flower classes:
# - Setosa
# - Versicolor
# - Virginica
# In simple words: We use flower measurements to predict which species the flower belongs to.
# 3. Split the dataset
# X_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42)



# - Divides the dataset into training and testing data.
# - X_train: Input features used for training.
# - X_test: Input features used for testing.
# - y_train: Actual labels used for training.
# - y_test: Actual labels used for testing.
# - test_size=0.2 means 80% data is used for training and 20% for testing.
# - random_state=42 ensures the same split every time.
# 4. Implement AdaBoost Classifier
# ada = AdaBoostClassifier(n_estimators=50)ada.fit(X_train, y_train)y_pred_ada = ada.predict(X_test)



# - AdaBoostClassifier() creates an AdaBoost classification model.
# - n_estimators=50 means the model uses 50 boosting estimators (weak learners).
# - fit() trains the model using the training data.
# - predict() predicts the flower species for the testing data.
# - The predictions are stored in y_pred_ada.
# How AdaBoost works:
# - It trains weak learners one after another.
# - It gives more importance to incorrectly classified samples.
# - Each new learner tries to correct the mistakes made by previous learners.
# - Finally, it combines their predictions to produce the result.








# arunp77.github.io


# 5. Implement Gradient Boosting Classifier
# gb = GradientBoostingClassifier(n_estimators=100)gb.fit(X_train, y_train)y_pred_gb = gb.predict(X_test)



# - GradientBoostingClassifier() creates a Gradient Boosting model.
# - n_estimators=100 means the model builds 100 boosting stages.
# - fit() trains the model using the training data.
# - predict() predicts the flower species for the testing data.
# - The predicted values are stored in y_pred_gb.
# How Gradient Boosting works:
# - It builds decision trees one after another.
# - Each new tree tries to correct the errors made by the previous trees.
# - It uses gradient descent to minimize the prediction error.
# - Finally, all the trees are combined to make the prediction.
# 6. Implement XGBoost Classifier
# xgb = XGBClassifier(    use_label_encoder=False,    eval_metric='mlogloss')



# - XGBClassifier() creates an XGBoost classification model.
# - XGBoost stands for Extreme Gradient Boosting.
# - use_label_encoder=False is an older XGBoost parameter that disables its built-in label encoder.
# - eval_metric='mlogloss' sets the evaluation metric to Multiclass Log Loss.
# xgb.fit(X_train, y_train)y_pred_xgb = xgb.predict(X_test)



# - fit() trains the XGBoost model.
# - predict() predicts the flower species for the testing data.
# - The predicted values are stored in y_pred_xgb.
# How XGBoost works:
# - It builds decision trees sequentially.
# - Each new tree tries to improve the previous predictions.
# - It uses regularization to reduce overfitting.
# - It is designed to be efficient and powerful.
# 7. Compare the accuracy of all three models
# print("AdaBoost Accuracy:", accuracy_score(y_test, y_pred_ada))print("Gradient Boosting Accuracy:", accuracy_score(y_test, y_pred_gb))print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))



# - accuracy_score() compares actual labels with predicted labels.
# - It calculates how many predictions are correct.
# - The accuracy of AdaBoost is displayed.
# - The accuracy of Gradient Boosting is displayed.
# - The accuracy of XGBoost is displayed.
# In simple words: We compare the three algorithms to find out which model performs better on the testing dataset.