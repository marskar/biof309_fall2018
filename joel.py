# Demonstrate logistic regression
from sklearn.datasets import load_digits
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib import pyplot as plt

# load data
digits = load_digits()

digits

data = digits['data']

target = digits['target']

data.shape

# train-test-split
y_train, y_test = target[:1500], target[1500:]
x_train, x_test = data[:1500], data[1500:]

# Or this is better
#x_train, x_test, y_train, y_test = train_test_split(
#    data, target, train_size=1500/1797, random_state=42)


# model
model = LogisticRegression()
model.fit(x_train, y_train)
predicted = model.predict(x_test)

# evaluate the model
cm = confusion_matrix(y_test, predicted)
a = accuracy_score(y_test, predicted)

# plot the confusion matrix
fig, ax = plt.subplots()
colorbar = ax.matshow(cm)
fig.colorbar(colorbar)
fig.suptitle("Confusion Matrix")
fig.savefig('sklearn.png')

# In addition to saving the plot, you can show it
plt.show()

# Accuracy score
a

# 89% accurate!
# Logistic regression is pretty good...
# at handwritten digit recognition.
