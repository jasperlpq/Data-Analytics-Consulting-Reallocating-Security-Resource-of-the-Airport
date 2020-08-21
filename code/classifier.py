from tkinter import *
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def line_predict():
    data = pd.read_csv("fd.csv")
    line = data.line_needed
    macid = data.Distinct_Macid
    X_train, X_test, y_train, y_test = train_test_split(macid, line, random_state=2, test_size=0.2)
    X_train_temp = X_train.values.reshape(-1,1)
    X_test_temp = X_test.values.reshape(-1,1)
    classification_tree = DecisionTreeClassifier(max_depth = 8,random_state = 0)
    classification_tree.fit(X_train_temp,y_train)
    input_x = int(entry1.get())
    
    result = classification_tree.predict(np.array([[input_x]]))
    asd = round(1/(float(input_x)/30),3)
    messagebox.showinfo(title="Output", message="You need "+str(result[0])+" line\n Arrival Rate: "+ str(asd))
    entry1.delete(0, END)
    
    return result[0]

myWindow = Tk()

myWindow.title('Line Prediction')

Label(myWindow, text="input").grid(row=0)

entry1=Entry(myWindow)

entry1.grid(row=0, column=1)

Button(myWindow, text='Quit', command=myWindow.quit).grid(row=2, column=0,sticky=W, padx=5, pady=5)
Button(myWindow, text='Run', command=line_predict).grid(row=2, column=1, sticky=W, padx=5, pady=5)
#
myWindow.mainloop()