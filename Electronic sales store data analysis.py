# Data Manipulation
import pandas as pd


# Data Visualization
import matplotlib
from matplotlib import pyplot as plt 


# Read in updated dataframe
sales_data=pd.read_excel(r"C:\Users\dksin\Dropbox\My PC (LAPTOP-E383CH2K)\Desktop\Electronic-store-sales-details.xls")
sales_data.head()

# Shape of Electronic store sale dataset (rows, columns)
sales_data.shape

# Concise summary for Electronic store sale dataset
sales_data.info()

# Gives columns in Electronic sales store dataset
sales_data.columns

# Checking for missing values
sales_data.isnull().values.all()

# Generates descriptive statistics summary
sales_data.describe()




# Adding 'Year' column to the existing dataset

def get_year(s):
    return s.split('-')[1]
sales_data['Year'] = sales_data['Order ID'].apply(lambda x: get_year(x))


sales_data.head(10)






# #  What was the best year for sales? How much was earned in that year?


# Grouping Year column and summing up all possible numerical columns in a dataset
result=sales_data.groupby(['Year']).sum()
result

# Graphical analysis
Year=range(2016,2020)
plt.bar(Year, result['Sales'], color=['red','black','green','orange'])
plt.xticks(Year)
plt.xlabel('Year', color='red')
plt.ylabel('Sales in USD ($)', color='red')
plt.show()






# # Which 5 cities had the highest number of sales?


# Grouping City column and summing up all possible numerical columns in a dataset
grouped_city=sales_data.groupby(['City']).sum()

# Sorting grouped_city dataframe by "Sales" column
sorted_res = grouped_city.sort_values(by="Sales", ascending = False)

df=sorted_res.head(5)['Sales']
df


# Graphical analysis
df.plot(kind= "line" ,y="Quantity", use_index= True, color="blue")
plt.show()






# # What products most often sold together?


# Creating new column ID
def get_ID(s):
    return s.split('-')[2]

sales_data['ID'] = sales_data['Order ID'].apply(lambda x: get_ID(x))


# This gives similar product id which sold together
df=sales_data[sales_data["ID"].duplicated(keep=False)]

print(df[["Order ID" , "Category"]].head(20))






# # Which top 4 products are sold the most?


# Grouping by Product name 
groupby_product_name=sales_data.groupby(['Product Name']).sum()

#Sorting by Quantity values 
sorted_res = groupby_product_name.sort_values(by="Quantity", ascending = False)

df1=sorted_res.head(6)[['Quantity', 'Sales']]
df1


# Graphical analysis
df1.plot(kind= "pie" ,y="Quantity", subplots= True, startangle=90, figsize=(8,8))      
plt.show()  






# # Customers who ordered more than a product?


# Getting unique customers id or dropping duplicate customer id's
unique_customerID=sales_data.drop_duplicates(subset=["Customer ID"], keep="last")

# cond stores the values which satisfies "where" condition
cond=unique_customerID.where(unique_customerID["Quantity"]>=2)[["Customer ID", "Customer Name", "Sub-Category", "Year","Quantity"]]

# Sorting cond dataframe by "Year" column
cond.sort_values(by="Year").head(10)






# # Total number of gadgets sold in all years

#Grouping Year and Category columns and also counting sub-category values
gadgets_count=sales_data.groupby(["Year","Category"])["Sub-Category"].value_counts()

gadgets_count





# # Which is most preferred ship mode?

# Plotting shipmode with Seaborn library
import seaborn as sns

# It counts ship mode count from the dataset
sns.countplot(sales_data["Ship Mode"])

plt.show()






# # What is the overall sales trend?

sales_data["Order Date"].min()

sales_data["Order Date"].max()

# Getting month and year from the dataset
sales_data["month_year"]= sales_data["Order Date"].apply(lambda x: x.strftime("%Y-%m"))

# Grouping month_year
sales_data_trend = sales_data.groupby("month_year").sum()["Sales"].reset_index()


# Graphical analysis
plt.figure(figsize=(16,7))
plt.xlabel('Month_Year', color='red')
plt.ylabel('Sales', color='red')
plt.plot(sales_data_trend["month_year"], sales_data_trend ["Sales"], color="green" )
plt.xticks(rotation="vertical", size=8, color="black")
plt.show()





# # Which are the top 10 sub-categoroies by sales?

# Grouping and sorting product sub-category column
prod_category_sales= sales_data.groupby("Sub-Category").sum()
prod_category_sales = prod_category_sales.sort_values(by=["Sales"], ascending=False)[["Sales", "Profit"]]
prod_category_sales



# Top 10 sub categorical products by sales
top_10_sub_category=prod_category_sales[:10]


#Graphical analysis
top_10_sub_category.plot(kind= "barh" ,y="Sales", color=['purple','green','blue','orange','black','lime','pink'])  
plt.ylabel('Sub-Category', color='red')
plt.xlabel('Sum of sales', color='red')
plt.show() 



# # Which are more profitable category and sub-category ?

# Grouping category and sub-category columns 
grouped_data=sales_data.groupby(["Category", "Sub-Category"]).sum()

# Sorting profit column
sorted_profit = grouped_data.sort_values(by=["Profit","Sub-Category","Category"], ascending=False)["Profit"]
sorted_profit

# Graphical analysis
 sorted_profit.plot(kind= "line" ,y="Profit", use_index= True, color="blue")
plt.xlabel('Categories & Sub-Categories', color='red')
plt.ylabel('Total Profits', color='red')
plt.xticks(rotation="vertical", size=8, color="black")
plt.show() 




