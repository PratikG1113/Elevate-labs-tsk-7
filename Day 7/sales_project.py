import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',        # or your MySQL server
    user='root',
    password='7225',
    database='sales_project'
)

# Create cursor and execute query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM 
    sales 
GROUP BY 
    product
"""

df = pd.read_sql(query, conn)
print(df)

# Plot revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Revenue by Product')
plt.ylabel('Revenue (USD)')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig("c:\\Users\\admin\\Elevate Labs\\Day 6\\sales_chart.png")
plt.show()

# Close connection
conn.close()
