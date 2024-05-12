# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:45:08 2024

@author: Demiso
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Visualize churn distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Churn', data=data)
plt.title('Distribution of Churned Customers')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.show()

# Analyze demographic information
plt.figure(figsize=(12, 6))
sns.countplot(x='gender', hue='Churn', data=data)
plt.title('Churn by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='SeniorCitizen', hue='Churn', data=data)
plt.title('Churn by Senior Citizen Status')
plt.xlabel('Senior Citizen')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Partner', hue='Churn', data=data)
plt.title('Churn by Partner Status')
plt.xlabel('Partner')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Dependents', hue='Churn', data=data)
plt.title('Churn by Dependents Status')
plt.xlabel('Dependents')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

# Analyze service usage
plt.figure(figsize=(12, 6))
sns.countplot(x='PhoneService', hue='Churn', data=data)
plt.title('Churn by Phone Service Status')
plt.xlabel('Phone Service')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='InternetService', hue='Churn', data=data)
plt.title('Churn by Internet Service Type')
plt.xlabel('Internet Service')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='StreamingTV', hue='Churn', data=data)
plt.title('Churn by Streaming TV Status')
plt.xlabel('Streaming TV')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='StreamingMovies', hue='Churn', data=data)
plt.title('Churn by Streaming Movies Status')
plt.xlabel('Streaming Movies')
plt.ylabel('Count')
plt.legend(title='Churn', loc='upper right')
plt.show()

# Analyze tenure
plt.figure(figsize=(12, 6))
sns.boxplot(x='Churn', y='tenure', data=data)
plt.title('Churn by Tenure')
plt.xlabel('Churn')
plt.ylabel('Tenure')
plt.show()