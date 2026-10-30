import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\DELL\Downloads\retail_sales_dataset.csv")
print(df.head())
print(df.info())
print(df.dtypes)
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.dropna()
df[' Order_Date'] = pd.to_datetime(df['Order_Date'])
print(df.head())

total_sales = df['Total_Sales_INR'].sum()
print("Total Sales:", total_sales)

product_sales = df.groupby('Product')['Total_Sales_INR'].sum()
print(product_sales.idxmax())

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
monthly_sales  = df.groupby(df['Order_Date'].dt.month)['Total_Sales_INR'].sum()
print(monthly_sales)

sales_by_region = df.groupby('City')['Total_Sales_INR'].sum().sort_values(ascending=False)
print(sales_by_region)

sales_by_region.plot(kind='bar')
plt.title('Region-wise sales')
plt.xlabel('Region')
plt.ylabel('Total Sales (INR)')
plt.show()

monthly_sales.plot(kind='line',marker = 'o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales (INR)')
plt.show()

sales_by_region.plot(kind='pie',autopct='%1.1f%%')
plt.title('Sales Distribution by Region')
plt.ylabel('')
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['Total_Sales_INR'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Total Sales (INR)')
plt.ylabel('Frequency')
plt.title('Distribution of Total Sales')
plt.xlim(0,1000)
plt.show()






