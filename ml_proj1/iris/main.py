import pandas
import matplotlib as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

names = ["sepal-length", "sepal-width", "petal-length","petal-width","class"]

print("downloading data etc")

dataset = pandas.read_csv(url,names = names)

print("the representation shows number of rows and cols in dataset")
print(dataset.shape)

print("at anu time we can have a look at dataset")

print(dataset.head(10))

print("min medium max values of dataset")

print(dataset.describe)


print("amount of data in dataset")

print("3 types of data in dataset")
print(dataset.groupby("class").size())

#getting values from dataset, returns data in data in list
array = dataset.values

#getting all values except classes
X = array[:,0:3]

#getting all class for the above data
Y = array[:,4]

#30 percent of data for validation
validation_size = 0.3



#seed is the number of iterations for  number of folds in data
seed = 7

#this method is returining training data as well as data for validation


X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y,test_size=validation_size, random_state=seed)


#at this point our syste, is divided to 70% train and 30% validation data

#this will classify the 70% dataset and train itself
knn = KNeighborsClassifier()

knn.fit(X_train, Y_train)
print("training finished, running predictions")
#makes a prediction on our validation data
predictions = knn.predict(X_validation)


print(predictions)
print("accuracy score:")
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))




