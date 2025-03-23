import pandas as pd

__all__ = ["process_data"]


def process_data(data):
    parsed_data = []

    products = data["data"]["productsFilter"]["record"]["products"]
    for product in products:
        name = product["name"]
        brand = product["brand"]["name"]
        price = product["price"]["current"]
        if not price:
            price = "Out of stock"
        cpu_info = {"name": name, "brand": brand, "price": price}
        parsed_data.append(cpu_info)

    df = pd.DataFrame(parsed_data)
    df.to_csv("two/cpu.csv", index=False)
    print("Cpu data saved to csv file.")  # noqa
