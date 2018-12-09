# Apriori 

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, len(dataset)):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])
        
# Training Apriori on the dataset 
from apyori import apriori
# Products that are in 3 transactions a day 
min_support = 3*7/7500 
rules = apriori(transactions, min_support = min_support, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results 
results = list(rules)
results_list = pd.DataFrame(results)














