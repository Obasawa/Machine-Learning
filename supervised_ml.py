from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Prepare the data, #Label data
hours=[
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
    ]
score=[30,40,45,55,65,70,80,85,90,95]

#Create model

model=LinearRegression()

#Train model

model.fit(hours, score)

user_hours=float(input("Enter study hours:"))


#Predict
prediction=model.predict([[user_hours]])
print(f"Predicted score for {user_hours} hours: {round(prediction[0], 1)}")


#Visualization

plt.scatter(hours, score)
plt.show()