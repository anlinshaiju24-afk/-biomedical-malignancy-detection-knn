import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
df=pd.read_csv("data.csv")
df["diagnosis"]=df["diagnosis"].map({'M':0,'B':1})
df=df.fillna(0)
x=df.drop(["id","diagnosis"],axis=1)
y=df["diagnosis"]
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=KNeighborsClassifier()
model.fit(x_train,y_train)
pred=model.predict(x_test)
print(pred)
acc=accuracy_score(pred,y_test)
print(acc)
plt.bar(["KNeighborsClassifier"],acc)
plt.ylim(0,1)
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("KNeighborsClassifier")
plt.show()


