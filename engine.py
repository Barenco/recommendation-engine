import pandas as pd
from tabulate import tabulate

def get_recommendations(id):
    orders = pd.read_csv("OrderProduct.csv")

    # Getting the orders with the givind id product
    orders_for_product = orders[orders.product_id == id].order_id.unique()
    relevant_orders = orders[orders.order_id.isin(orders_for_product)]

    # Getting the related order products and the count of them
    accompanying_products_by_order = relevant_orders[relevant_orders.product_id != id]
    num_instance_by_accompanying_product = accompanying_products_by_order.groupby("product_id")["product_id"].count().reset_index(name="count")
    
    # Creating a row for the frequence of the related products
    num_orders_for_product = orders_for_product.size
    product_instances = pd.DataFrame(num_instance_by_accompanying_product)
    product_instances["frequency"] = product_instances["count"]/num_orders_for_product

    # Ordering the products by frequence (top 3)
    recommended_products = pd.DataFrame(product_instances.sort_values("frequency", ascending=False).head(3))

    # Merge the csv filed to get the name of each product
    products = pd.read_csv("Product.csv")
    recommended_products = pd.merge(recommended_products, products, on="product_id")


    # Optional line for printing the products in the terminal
    print(tabulate(recommended_products, ["product_id", "count"], tablefmt="grid"))

    return recommended_products.to_json(orient="table")
