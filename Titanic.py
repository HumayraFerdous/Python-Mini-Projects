import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')
#print(data.head())

#print(data.isnull().sum()) # Age and Cabin column has 177 and 687 missing values
#print(data.duplicated())
#print(data.info())

#Check the categorical and numerical columns

cat_col = [col for col in data.columns if data[col].dtype == 'object']
print('Categorical columns: ',cat_col)
num_col = [col for col in data.columns if data[col].dtype!='object']
print('Numerical columns: ',num_col)

#Checking total number of unique columns
print(data[cat_col].nunique())

data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked']=data['Embarked'].fillna(data['Embarked'].mode()[0])
data.drop('Cabin',axis=1,inplace=True)
#print(data.info())

plt.boxplot(data['Age'],vert=False)
plt.title("Age Distribution")
plt.show()

Q1 = data['Age'].quantile(0.25)
Q3 = data['Age'].quantile(0.75)
IQR = Q3-Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
data = data[(data['Age']<lower_bound) | (data['Age']>upper_bound)]

plt.boxplot(data['Age'],vert=False)
plt.title("Age Distribution")
plt.show()

