import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("my_expenditure.csv")
print(data.head())
data = data.dropna()
data['Date'] = pd.to_datetime(data['Date'])
data['Year']=data['Date'].dt.strftime('%Y')
data['Day']=data['Date'].dt.strftime('%d')
data['Day_Name']=data['Date'].dt.strftime('%A')
print(data.head())

day_wise_spent = data.pivot_table(index = "Day",values="Amount",aggfunc = 'sum')
day_wise_spent = day_wise_spent.reset_index()

x = day_wise_spent['Day']
y = day_wise_spent['Amount']

plt.figure(figsize=(16,8))
plt.title("Day wise Expenditure")
plt.xlabel("Day")
plt.ylabel("Amount")
plt.bar(x,y)
plt.xticks(rotation=45)
plt.show()

category_wise_spent = data.pivot_table(index = "Category",values="Amount",aggfunc = 'sum')
category_wise_spent = category_wise_spent.reset_index()
#print(category_wise_spent)
x = category_wise_spent['Category']
y = category_wise_spent['Amount']

plt.figure(figsize=(8,8))
plt.title("Category wise Expenditure")
plt.pie(y, labels = x, autopct ='%.1f%%')
plt.legend()
plt.show()

week_wise_spent = data.pivot_table(index = "Day_Name",values="Amount",aggfunc = 'sum')
week_wise_spent = week_wise_spent.reset_index()
#print(week_wise_spent)
x = week_wise_spent['Day_Name']
y = week_wise_spent['Amount']

plt.figure(figsize=(10,8))
plt.title("Week wise Expenditure")
sns.lineplot(x=x,y=y,data=week_wise_spent)
plt.show()