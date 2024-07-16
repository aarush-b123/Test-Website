import matplotlib.pyplot as plt
import numpy as np



# Generate random stock prices
days = 100
prices = [50]  # Starting price

for _ in range(1, days):
    deviation = np.random.randint(-5, 6)  
    next_price = prices[-1] + deviation
    next_price = max(1, min(next_price, 100))  
    prices.append(next_price)


x = list(range(1, days + 1))



plt.plot(x, prices, label='Java Stock Price')
plt.xlabel('Day')
plt.ylabel('Price in Dollars')
plt.title('Stock Market Graph of Java')
plt.grid(True)
plt.show()
