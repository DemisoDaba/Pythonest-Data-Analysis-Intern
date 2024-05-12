# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:59:46 2024

@author: Demiso
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('data.csv')

# Descriptive statistics
print(data.describe())

# Distribution plots
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.histplot(data['Tenure'], kde=True, bins=20, color='skyblue')
plt.title('Distribution of Tenure')

plt.subplot(2, 2, 2)
sns.histplot(data['MonthlyCharges'], kde=True, bins=20, color='salmon')
plt.title('Distribution of Monthly Charges')

plt.subplot(2, 2, 3)
sns.histplot(data['TotalCharges'], kde=True, bins=20, color='green')
plt.title('Distribution of Total Charges')

plt.subplot(2, 2, 4)
sns.countplot(data=data, x='Churn', palette='pastel')
plt.title('Churn Count')

plt.tight_layout()
plt.show()

# Relationship between categorical variables and churn
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='SeniorCitizen', hue='Churn', palette='muted')
plt.title('Churn Count by Senior Citizen')
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


