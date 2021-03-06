# Importing the libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the SVM model on the Training set
# - Regularization: With a smaller C value, we obtain hyperplane of small margin and with a larger C value,
# we obtain hyperplane of larger value.

# - Gamma: With a lower value of Gamma will create a loose fit of the training dataset. On the contrary, a high value
# of gamma will allow the model to get fit more appropriately. A low value of gamma only provides consideration to
# the nearby points for the calculation of a separate plane whereas the high value of gamma will consider all
# the data-points to calculate the final separation line

classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting a new result
print(classifier.predict(sc.transform([[30,87000]])))

# Predicting the Test set results
y_pred = classifier.predict(X_test)
#print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Making the Confusion Matrix
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
