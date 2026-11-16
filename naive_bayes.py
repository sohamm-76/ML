
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training dataset
texts = [
    "I love this movie",
    "This movie is excellent",
    "The movie was amazing",
    "I enjoyed this film",
    "This is a wonderful movie",
    "The acting was great",
    "I liked this movie",
    "This film was fantastic",
    "The story was interesting",
    "It was an excellent experience",
    "I hate this movie",
    "This movie is terrible",
    "The movie was boring",
    "I disliked this film",
    "This is a horrible movie",
    "The acting was bad",
    "I did not like this movie",
    "This film was disappointing",
    "The story was boring",
    "It was a terrible experience"
]

# Labels: 1 = Positive, 0 = Negative
labels = [1,1,1,1,1,1,1,1,1,1,
          0,0,0,0,0,0,0,0,0,0]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Create and train Naive Bayes classifier
model = MultinomialNB()
model.fit(X, labels)

# Test sentences
test_texts = [
    "I love this excellent film",
    "The movie was boring",
    "This is a fantastic movie",
    "I disliked this terrible movie",
    "The acting was great"
]

# Convert test sentences
X_test = vectorizer.transform(test_texts)

# Predict the class
predictions = model.predict(X_test)

print("===== NAIVE BAYES TEXT CLASSIFICATION =====")

# Display predictions
for text, prediction in zip(test_texts, predictions):
    result = "Positive" if prediction == 1 else "Negative"
    print("\nText:", text)
    print("Prediction:", result)

# Display probabilities
print("\n===== PREDICTION PROBABILITIES =====")

probabilities = model.predict_proba(X_test)

for text, probability in zip(test_texts, probabilities):
    print("\nText:", text)
    print("Positive:", round(probability[1], 3))
    print("Negative:", round(probability[0], 3))

# Display model information
print("\n===== MODEL INFORMATION =====")
print("Training sentences:", len(texts))
print("Vocabulary size:", len(vectorizer.vocabulary_))
print("\nVocabulary:")
print(vectorizer.get_feature_names_out())














# 1. Import required libraries
# from sklearn.feature_extraction.text import CountVectorizerfrom sklearn.naive_bayes import MultinomialNB



# - CountVectorizer: Converts text sentences into numerical values by counting how many times each word appears.
# - MultinomialNB: Implements the Multinomial Naive Bayes algorithm, which is commonly used for text classification.
# 2. Create the training dataset
# texts = [    "I love this movie",    "This movie is excellent",    "The movie was amazing",    ...]



# - texts contains the training sentences.
# - These sentences are examples that the model uses to learn positive and negative opinions.
# - The first 10 sentences express positive feelings.
# - The last 10 sentences express negative feelings.
# In simple words: We provide sample movie reviews so that the model can learn which words are commonly associated with positive and negative opinions.
# 3. Assign labels to the sentences
# labels = [1,1,1,1,1,1,1,1,1,1,          0,0,0,0,0,0,0,0,0,0]



# - Labels represent the category of each sentence.
# - 1 represents Positive.
# - 0 represents Negative.
# - The first 10 sentences have label 1.
# - The last 10 sentences have label 0.
# Each label corresponds to the sentence at the same position in the texts list.
# 4. Convert text into numerical features
# vectorizer = CountVectorizer()X = vectorizer.fit_transform(texts)



# - Creates an object of CountVectorizer.
# - fit_transform() performs two operations:
#   - fit(): Identifies all unique words in the training sentences and creates a vocabulary.
#   - transform(): Converts sentences into numerical word-count representations.
# - X stores the numerical representation of the training sentences.
# Example:

# Sentence: "I love this movie"

# The words are converted into counts based on the vocabulary created by the vectorizer.

# This is necessary because machine learning algorithms work with numerical data, not raw text.
# 5. Create and train the Naive Bayes classifier
# model = MultinomialNB()model.fit(X, labels)



# - MultinomialNB() creates a Naive Bayes classification model.
# - fit() trains the model using the numerical text data (X) and their corresponding labels.
# - The model learns the relationship between words and sentiment categories.
# In simple words: The model learns which words are more likely to appear in positive and negative reviews.
# 6. Create test sentences
# test_texts = [    "I love this excellent film",    "The movie was boring",    "This is a fantastic movie",    "I disliked this terrible movie",    "The acting was great"]



# - test_texts contains new sentences that the model has not seen during training.
# - We use these sentences to check whether the model can correctly identify positive and negative opinions.
# 7. Convert test sentences into numerical features
# X_test = vectorizer.transform(test_texts)



# - Converts the test sentences into numerical word counts.
# - We use transform() instead of fit_transform().
# - This ensures that the same vocabulary created from the training data is used for testing.
# 8. Predict the sentiment
# predictions = model.predict(X_test)



# - predict() uses the trained model to classify each test sentence.
# - It returns 1 for Positive or 0 for Negative.
# - The predicted results are stored in predictions.
# 9. Display the predictions
# print("===== NAIVE BAYES TEXT CLASSIFICATION =====")



# - Prints the heading for the classification results.
# for text, prediction in zip(test_texts, predictions):    result = "Positive" if prediction == 1 else "Negative"    print("\nText:", text)    print("Prediction:", result)



# - zip() combines each test sentence with its predicted label.
# - The for loop processes each sentence one by one.
# - The conditional expression checks the prediction:
#   - If prediction is 1, the result is Positive.
#   - Otherwise, the result is Negative.
# - Finally, it prints the sentence and its predicted sentiment.
# 10. Display prediction probabilities
# print("\n===== PREDICTION PROBABILITIES =====")probabilities = model.predict_proba(X_test)



# - predict_proba() calculates the probability of each sentence belonging to each class.
# - It returns two probabilities:
#   - Probability of Negative (class 0).
#   - Probability of Positive (class 1).
# - These probabilities are stored in probabilities.
# for text, probability in zip(test_texts, probabilities):    print("\nText:", text)    print("Positive:", round(probability[1], 3))    print("Negative:", round(probability[0], 3))



# - Displays the probability of each sentence being Positive or Negative.
# - probability[0] represents the Negative probability.
# - probability[1] represents the Positive probability.
# - round(value, 3) rounds the probability to three decimal places.
# Example: If the positive probability is 0.950, it means the model estimates a 95% probability that the sentence belongs to the Positive class.
# 11. Display model information
# print("\n===== MODEL INFORMATION =====")print("Training sentences:", len(texts))



# - Displays the total number of training sentences.
# - len(texts) returns the number of sentences in the training dataset, which is 20.
# print("Vocabulary size:", len(vectorizer.vocabulary_))



# - Displays the total number of unique words identified by CountVectorizer.
# - vocabulary_ stores the words and their corresponding numerical indices.
# print("\nVocabulary:")print(vectorizer.get_feature_names_out())



# - get_feature_names_out() returns all the unique words in the vocabulary.
# - Displays the words used by the model during training.