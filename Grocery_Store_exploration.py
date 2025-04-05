import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("grocery_store.csv")

#Checking missing values
print(data.isnull().sum())
print(data.dtypes)
data['Age']=data['Age'].fillna(data['Age'].median())
data['PaymentMethod']=data['PaymentMethod'].fillna(data['PaymentMethod'].mode()[0])

#Dropping unnecessary data
data.drop('CustomerID',axis=1,inplace = True)

data['Date']=pd.to_datetime(data['Date'])
data['Member']=data['Member'].map({'Yes':1,'No':0})

#Data Engineering
data['TotalSpend']=data['Quantity']+data['Price']
data['DayOfWeek']=data['Date'].dt.day_name()

#Encode using hot encoder
data = pd.get_dummies(data,columns=['Gender','PaymentMethod'],drop_first=True)
#print(data.head())

avg_spend=data.groupby('Item')['TotalSpend'].mean().sort_values(ascending=False)
print("Average Total Spend by Item")
print(avg_spend)
sales_by_day=data.groupby('DayOfWeek')['TotalSpend'].sum().sort_values(ascending=False)
print("Total Sales by Day")
print(sales_by_day)
popular_item = data.groupby('Item')['Quantity'].sum().sort_values(ascending=False)
print("Most Popular Item (Quantity Sold):")
print(popular_item)
member_spend = data.groupby('Member')['TotalSpend'].mean()
print("Average Spend by Membership Status:")
print(member_spend)

data.groupby('Item')['TotalSpend'].sum().plot(kind='bar',color='skyblue')
plt.title("Total Revenue by Item")
plt.ylabel("Total Spend($)")
plt.show()

data['Age'].plot(kind='box',vert=False)
plt.title("Age Distribution of Customers")
plt.show()

print(data[['Age','TotalSpend']].corr())

