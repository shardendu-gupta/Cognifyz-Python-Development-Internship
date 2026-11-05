
import pandas as pd
import plotly.express as px



data = pd.read_csv("data.csv")

print("Sales Dataset:")
print(data)
print("\nTotal Records:", len(data))


product_sales = data.groupby("Product")["Sales"].sum().reset_index()

bar_chart = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    title="Product Wise Total Sales",
    labels={
        "Product": "Product Name",
        "Sales": "Total Sales (Rs.)"
    }
)

bar_chart.show()
bar_chart.write_html("bar_chart.html")
monthly_sales = data.groupby("Month")["Sales"].sum().reset_index()

month_order = ["January", "February", "March", "April", "May"]

monthly_sales["Month"] = pd.Categorical(
    monthly_sales["Month"],
    categories=month_order,
    ordered=True
)

monthly_sales = monthly_sales.sort_values("Month")


# Create Line Chart
line_chart = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    title="Monthly Sales Report",
    markers=True,
    labels={
        "Month": "Month",
        "Sales": "Total Sales (Rs.)"
    }
)

line_chart.show()
line_chart.write_html("line_chart.html")
category_sales = data.groupby("Category")["Sales"].sum().reset_index()
pie_chart = px.pie(category_sales, names="Category", values="Sales", title="Category Wise Sales Distribution")
pie_chart.show()
pie_chart.write_html("pie_chart.html")



print("\nData Visualization Completed Successfully!")
print("\nProduct Wise Sales:")
print(product_sales)
print("\nMonthly Sales:")
print(monthly_sales)
print("\nCategory Wise Sales:")
print(category_sales)
print("\nAll charts saved successfully!")
