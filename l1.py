import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,2,3,4,5])
Y = np.array([2,2.5,3,2.4,2.2])
iterations = 1000




#Building the model
m = 0

c = 0
n = float(len(X))

L = 0.001
for i in range(iterations):
    Y_pred=m*X + c
    D_m = (1/n)*sum(X*(Y_pred - Y))
    D_c = (1/n)*sum(Y-Y_pred)
    
    m = m - L*D_m
    c = c - L*D_c
print(m,c)

Y_pred = m*X + c

plt.scatter(X,Y,color ="blue")


plt.scatter(X,Y_pred, color ="red")
plt.show()