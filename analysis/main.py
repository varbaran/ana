import csv

countries = {
    "IR": [],
    "US": [],
    "SA": [],
    "GB": [],
}

with open("international-trade-december-2022-quarter/output_csv_full.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["country_code"] in countries:
            countries[row["country_code"]].append(row)

products = set()
accounts = set()
for country in countries.keys():
    for row in countries[country]:
        products.add(row["product_type"])
        accounts.add(row["account"])

plot_data = {
    "imports": {
        "goods": {
            "IR": [],
            "US": [],
            "SA": [],
            "GB": [],
        },
        "services": {
            "IR": [],
            "US": [],
            "SA": [],
            "GB": [],
        },
    },
    "exports": {
        "goods": {
            "IR": [],
            "US": [],
            "SA": [],
            "GB": [],
        },
        "services": {
            "IR": [],
            "US": [],
            "SA": [],
            "GB": [],
        }
    }
}
for country in countries.keys():
    for product in products:
        for account in accounts:
            v = []
            for row in countries[country]:
                if row["product_type"] == product and row["account"] == account:
                    try:
                        v.append(float(row["value"]))
                    except ValueError:
                        pass
            s = sum(v)
            print(country, product, account, s, s / len(v))
            plot_data[account.lower()][product.lower()][country].append(s)

from matplotlib import pyplot as plt

x = ["IR", "US", "SA", "GB"]
y1 = [plot_data["imports"]["goods"]["IR"][0], plot_data["imports"]["goods"]["US"][0],
      plot_data["imports"]["goods"]["SA"][0], plot_data["imports"]["goods"]["GB"][0]]
y2 = [plot_data["imports"]["services"]["IR"][0], plot_data["imports"]["services"]["US"][0],
      plot_data["imports"]["services"]["SA"][0], plot_data["imports"]["services"]["GB"][0]]
y3 = [plot_data["exports"]["goods"]["IR"][0], plot_data["exports"]["goods"]["US"][0],
      plot_data["exports"]["goods"]["SA"][0], plot_data["exports"]["goods"]["GB"][0]]
y4 = [plot_data["exports"]["services"]["IR"][0], plot_data["exports"]["services"]["US"][0],
      plot_data["exports"]["services"]["SA"][0], plot_data["exports"]["services"]["GB"][0]]
plt.bar(x, y1, color="red")
plt.bar(x, y2, bottom=y1, color="green")
plt.bar(x, y3, bottom=[y1[i] + y2[i] for i in range(len(y1))], color="blue")
plt.bar(x, y4, bottom=[y1[i] + y2[i] + y3[i] for i in range(len(y1))], color="yellow")
plt.show()
