# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# CodeGrade step1
df_boston = pd.read_sql("""
SELECT e.firstName, e.lastName, e.jobTitle
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = 'Boston'
""", conn)

# CodeGrade step2
df_zero_emp = pd.read_sql("""
SELECT o.*
FROM offices o
LEFT JOIN employees e ON o.officeCode = e.officeCode
WHERE e.employeeNumber IS NULL
""", conn)
df_zero_emp

# CodeGrade step3
df_employee = pd.read_sql("""
SELECT e.firstName, e.lastName, o.city, o.state
FROM employees e
LEFT JOIN offices o ON e.officeCode = o.officeCode
ORDER BY e.firstName, e.lastName
""", conn)
df_employee

# CodeGrade step4
df_contacts = pd.read_sql("""
SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber
WHERE o.orderNumber IS NULL
ORDER BY c.contactLastName
""", conn)
df_contacts

# CodeGrade step5
df_payment = pd.read_sql("""
SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
ORDER BY CAST(p.amount AS REAL) DESC
""", conn)
df_payment

# CodeGrade step6
df_credit = pd.read_sql("""
SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) AS num_customers
FROM employees e
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY e.employeeNumber
HAVING AVG(c.creditLimit) > 90000
ORDER BY num_customers DESC
""", conn)
df_credit

# CodeGrade step7
df_product_sold = pd.read_sql("""
SELECT p.productName,
       COUNT(od.orderNumber) AS numorders,
       SUM(od.quantityOrdered) AS totalunits
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
GROUP BY p.productCode
ORDER BY totalunits DESC
""", conn)
df_product_sold

# CodeGrade step8
df_total_customers = pd.read_sql("""
SELECT p.productName, p.productCode,
       COUNT(DISTINCT o.customerNumber) AS numpurchasers
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON od.orderNumber = o.orderNumber
GROUP BY p.productCode
ORDER BY numpurchasers DESC
""", conn)
df_total_customers

# CodeGrade step9
df_customers = pd.read_sql("""
SELECT o.officeCode, o.city, COUNT(c.customerNumber) AS n_customers
FROM offices o
JOIN employees e ON o.officeCode = e.officeCode
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY o.officeCode
""", conn)
df_customers

# CodeGrade step10
df_boston = pd.read_sql("""
SELECT e.firstName, e.lastName, e.jobTitle
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = 'Boston'
""", conn)
df_boston

# Run this cell without changes

conn.close()

