
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Iris dataset
iris = load_iris()

# Petal length as input and petal width as output
X = iris.data[:, 2].reshape(-1, 1)
y = iris.data[:, 3]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict values
y_pred = model.predict(X_test)

# Display coefficients
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Display predictions
print("\nActual vs Predicted:")
for actual, predicted in zip(y_test, y_pred):
    print("Actual:", actual, "Predicted:", predicted)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)

# Plot regression line
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Linear Regression using Iris Dataset")
plt.show()














# //1. Import required libraries
# import numpy as npimport matplotlib.pyplot as plt



# - numpy: Used for numerical calculations and handling arrays.
# - matplotlib.pyplot: Used to create graphs and visualize the results.
# from sklearn.datasets import load_iris



# - Imports the built-in Iris dataset from Scikit-learn.
# - The dataset contains measurements of iris flowers.
# from sklearn.model_selection import train_test_split



# - Divides the dataset into training and testing parts.
# - Training data is used to teach the model.
# - Testing data is used to check its performance.
# from sklearn.linear_model import LinearRegression



# - Imports the Linear Regression algorithm.
# - It finds the relationship between input and output values.
# from sklearn.metrics import mean_squared_error, r2_score



# - mean_squared_error: Measures the average squared difference between actual and predicted values.
# - r2_score: Measures how well the model explains the variation in the output.
# 2. Load the Iris dataset
# iris = load_iris()



# - Loads the Iris dataset into the variable iris.
# - It contains 150 flower samples with four features:
#   - Sepal length
#   - Sepal width
#   - Petal length
#   - Petal width
# 3. Select input and output features
# X = iris.data[:, 2].reshape(-1, 1)y = iris.data[:, 3]



# - X represents the input feature, which is Petal Length.
# - iris.data[:, 2] selects the third column (Petal Length) from all rows.
# - reshape(-1, 1) converts the input into a 2D array because Scikit-learn expects input features in this format.
# - y represents the output feature, which is Petal Width.
# - iris.data[:, 3] selects the fourth column (Petal Width).
# In simple words: We use Petal Length to predict Petal Width.
# 4. Split the dataset
# X_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42)



# - Splits the dataset into training and testing data.
# - test_size=0.2 means 20% data is used for testing and 80% for training.
# - random_state=42 ensures that the same split is generated every time.
# - X_train and y_train are used for training.
# - X_test and y_test are used for testing.
# 5. Create the Linear Regression model
# model = LinearRegression()



# - Creates an object of the Linear Regression algorithm.
# - This model will learn the relationship between Petal Length and Petal Width.
# 6. Train the model
# model.fit(X_train, y_train)



# - Trains the model using the training dataset.
# - The model learns the best-fit straight line between input and output.
# - It calculates the slope and intercept of the line.
 

# \(\hat{y} = b_0 + b_1x\)

# \(\hat{y} = \text{8.49} - \text{0.54}x\)
# Estimated intercept · R-squared = 0.72

# Fit
# InterceptThrough origin




# Focus
# DataLinePredictionsResiduals






# Generate new data




# Drag a point to refit the line.
# 2468102468PredictorResponse





# Give feedback

# 7. Predict values
# y_pred = model.predict(X_test)



# - Uses the trained model to predict Petal Width.
# - It takes the testing input (X_test) and produces predicted output values (y_pred).
# 8. Display coefficients
# print("Slope:", model.coef_[0])print("Intercept:", model.intercept_)



# - model.coef_[0] gives the slope of the regression line.
# - model.intercept_ gives the intercept of the regression line.
# - These values define the equation of the regression line.
# The equation is:
# \[
# y = mx + c
# \]

# Where:
# - y = Predicted Petal Width
# - x = Petal Length
# - m = Slope
# - c = Intercept
# 9. Display actual and predicted values
# print("\nActual vs Predicted:")for actual, predicted in zip(y_test, y_pred):    print("Actual:", actual, "Predicted:", predicted)



# - Displays actual values alongside predicted values.
# - zip() combines the actual and predicted values one by one.
# - The for loop prints each pair.
# 10. Evaluate the model
# mse = mean_squared_error(y_test, y_pred)r2 = r2_score(y_test, y_pred)



# - Calculates Mean Squared Error (MSE).
# - Calculates the R² score to measure model performance.
# print("\nMean Squared Error:", mse)print("R2 Score:", r2)



# - Displays the evaluation results.
# - Lower MSE generally indicates better predictions.
# - An R² score closer to 1 indicates a better fit.
# 11. Plot the regression line
# plt.scatter(X_test, y_test)



# - Displays the actual testing values as individual points on a scatter plot.
# plt.plot(X_test, y_pred)



# - Draws the predicted regression line.
# plt.xlabel("Petal Length")plt.ylabel("Petal Width")plt.title("Linear Regression using Iris Dataset")plt.show()



# - Sets the X-axis label as Petal Length.
# - Sets the Y-axis label as Petal Width.
# - Adds a title to the graph.
# - plt.show() displays the graph.//