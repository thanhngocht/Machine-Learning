import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('HousePrice.csv')

x = data.iloc[:, 0]
y = data.iloc[:, 1]

x = (x - np.mean(x)) / np.std(x)
y = (y - np.mean(y)) / np.std(y)

def gradient_descent(x, y, learning_rate=0.001, tolerance=0.0001, max_iterations=1000):
    m_curr = b_curr = 0
    n = len(x)
    iterations = 0
    
    while iterations < max_iterations:
        y_predicted = m_curr * x + b_curr

        m_derivative = sum(x * (y_predicted - y))
        b_derivative = sum(y_predicted - y)

        m_curr = m_curr - learning_rate * m_derivative
        b_curr = b_curr - learning_rate * b_derivative
        
        if abs(m_derivative) < tolerance and abs(b_derivative) < tolerance:
            break
        
        iterations += 1
    
    return m_curr, b_curr

m, b = gradient_descent(x, y)
print(m,b)


y_predicted = m * x + b

# Vẽ biểu đồ
plt.scatter(x, y, color='blue', label='Original data') 
plt.plot(x, y_predicted, color='red', label='Fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()#Chú thích
plt.show()
