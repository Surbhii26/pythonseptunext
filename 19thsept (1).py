#!/usr/bin/env python
# coding: utf-8

# In[ ]:


languages = ['Java' , 'Python' , 'Javascript']
versions = [14,3,6]
result = zip(languages,versions)
print(list(result))


# In[ ]:


data = {'Name' :['tom','nick','krish','jack'], 'Age':[20,21,19,18]}
import pandas as pd
dfEmpl = pd.DataFrame(data)
print(dfEmpl)


# In[ ]:


seremplage = pd.Series(dfEmpl['Age'])
seremplage.head(3)


# In[ ]:


import numpy as np
array1= np.array ([1,3,5])
print("np.array():\n", array1)


# In[ ]:


array2= np.zeros((3,3))
print("\nnp.zeros():\n", array2)


# In[ ]:


array3= np.array([1,3,5,7,9,11])
array4= np.reshape(array3,(2,3))
array5= np.transpose(array4)
print("Original array:\n", array3)
print("Reshaped array:\n", array4)
print("Transposed array:\n", array5)


# In[ ]:


array1 = np.array([[1,3,5],[2,4,6]])
np.savetxt('data.txt',array1)
loaded_data = np.loadtxt('data.txt')
print(loaded_data)


# In[ ]:


a = np.array([[2,1],[4,-5]])
b = np.array([[5],[7]])
from scipy import linalg
x = linalg.solve(a,b)
print(a.dot(x) -b)


# In[1]:


products = []

customers = []

sales_orders = []


# Define a Product class to represent products

class Product:

    def __init__(self, name, price):

        self.name = name

        self.price = price


# Define a Customer class to represent customers

class Customer:

    def __init__(self, name, email):

        self.name = name

        self.email = email


# Define a SalesOrder class to represent sales orders

class SalesOrder:

    def __init__(self, customer, products):

        self.customer = customer

        self.products = products


# Function to add a new product

def add_product():

    name = input("Enter product name: ")

    price = float(input("Enter product price: "))

    product = Product(name, price)

    products.append(product)

    print(f"Product '{name}' added successfully.")


# Function to list all products

def list_products():

    if not products:

        print("No products found.")

    else:

        print("List of Products:")

        for i, product in enumerate(products, start=1):

            print(f"{i}. {product.name} - ${product.price}")


# Function to add a new customer

def add_customer():

    name = input("Enter customer name: ")

    email = input("Enter customer email: ")

    customer = Customer(name, email)

    customers.append(customer)

    print(f"Customer '{name}' added successfully.")


# Function to list all customers

def list_customers():

    if not customers:

        print("No customers found.")

    else:

        print("List of Customers:")

        for i, customer in enumerate(customers, start=1):

            print(f"{i}. {customer.name} - {customer.email}")


# Function to create a new sales order

def create_sales_order():

    if not customers:

        print("No customers found. Please add a customer first.")

        return


    if not products:

        print("No products found. Please add a product first.")

        return


    print("Select a customer:")

    for i, customer in enumerate(customers, start=1):

        print(f"{i}. {customer.name}")


    customer_choice = int(input("Enter the customer number: ")) - 1

    if customer_choice < 0 or customer_choice >= len(customers):

        print("Invalid customer choice.")

        return


    selected_customer = customers[customer_choice]


    selected_products = []

    while True:

        print("Select a product to add to the sales order (0 to finish):")

        for i, product in enumerate(products, start=1):

            print(f"{i}. {product.name} - ${product.price}")

        product_choice = int(input("Enter the product number: ")) - 1


        if product_choice == -1:

            break


        if product_choice < 0 or product_choice >= len(products):

            print("Invalid product choice.")

            continue


        selected_products.append(products[product_choice])


    if not selected_products:

        print("No products added to the sales order.")

        return


    sales_order = SalesOrder(selected_customer, selected_products)

    sales_orders.append(sales_order)

    print("Sales order created successfully.")


# Function to list all sales orders

def list_sales_orders():

    if not sales_orders:

        print("No sales orders found.")

    else:

        print("List of Sales Orders:")

        for i, order in enumerate(sales_orders, start=1):

            total_price = sum(product.price for product in order.products)

            print(f"{i}. Customer: {order.customer.name}, Total Price: ${total_price}")
while (True):

    print("\nSales Management System")

    print("1. Add a new product")

    print("2. List all products")

    print("3. Add a new customer")

    print("4. List all customers")

    print("5. Create a new sales order")

    print("6. List all sales orders")

    print("7. Quit")


    choice = input("Enter your choice: ")


    if choice == "1":

        add_product()

    elif choice == "2":

        list_products()

    elif choice == "3":

        add_customer()

    elif choice == "4":

        list_customers()

    elif choice == "5":

        create_sales_order()

    elif choice == "6":

        list_sales_orders()

    elif choice == "7":

        break

    else:

        print("Invalid choice. Please try again.")


# # MACACHINE LEARNING USING SCIKIT-LEARN
# 

# In[10]:


import sklearn 
from sklearn import tree
Bumpy = 1
Smooth =0
Orange = 0
Apple = 1
feature = [[140,Bumpy],[130,Bumpy],[150,Smooth],[170,Smooth]]
label = [Orange,Orange,Apple,Apple]

mlModel = tree.DecisionTreeClassifier()
mlModel = mlModel.fit(feature,label)
print(mlModel.predict([[160,Smooth]]))


# In[ ]:




