import pyodbc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import webbrowser

# Define connection parameters
server = 'localhost'  # Replace with your server address
database = 'students'  # Replace with your database name
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure this matches the installed driver

# Establish connection
try:
    connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
    )
    print("Connection successful")
except Exception as e:
    print("Error connecting to the database:", e)


# Assuming your connection is already established
sql_query = "SELECT * FROM students"  # Replace with your table name
df = pd.read_sql(sql_query, connection)

mean = 0
std_dev = 1
size = 1000

# Generate random data from a normal distribution
data = np.random.normal(mean, std_dev, size)

# Step 2: Plot the normal distribution using seaborn
sns.set(style="whitegrid")  # Optional: for better plot styling
plt.figure(figsize=(8, 6))

# Plot a histogram and fit a KDE to visualize the normal distribution
sns.histplot(df['grade'], kde=True, color="green", bins=1)

# Customize the plot
plt.title('Normal Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')

plot_path = "normal_distribution.png"
plt.savefig(plot_path, dpi=300, bbox_inches='tight')
plt.close()

# Generate HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Normal Distribution</title>
</head>
<body>
    <h1>Normal Distribution of Marks</h1>
    <img src="{plot_path}" alt="Normal Distribution" style="max-width:100%; height:auto;">
</body>
</html>
"""

# Save the HTML content to a file
html_file = "diagram.html"
with open(html_file, "w") as file:
    file.write(html_content)

print(f"HTML file created: {html_file}")

# Open the HTML file in a browser
webbrowser.open(html_file)
