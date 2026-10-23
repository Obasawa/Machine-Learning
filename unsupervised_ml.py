from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#Prepare data
customers = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4]  
]

scaler=StandardScaler()
scaled_data=scaler.fit_transform(customers)

#Create model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

#Train model
model.fit(scaled_data)

labels = model.labels_
for i in range(len(labels)):
    print("Customer", i + 1, "belongs to Cluster", labels[i])
    
list(labels).count(0)    
for cluster in range(3):
    total = list(labels).count(cluster)
    print("Cluster", cluster, "has", total, "customers")
    
    
spending = []
visits = []

for row in customers:
    spending.append(row[0])
    visits.append(row[1])
    
 
 #Visualization   
plt.scatter(spending, visits, c=labels)
plt.show()