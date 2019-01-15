import json
import re

output = []

with open('productList.json') as json_data:
    d = json.load(json_data)
#print(d["products"][0]["id"]);
for x in d["products"]:
	data = {
		"id": str(x["id"]),
		"title": str(x["title"].encode('utf-8')),
		"vendor": str(x["vendor"].encode('utf-8')),
		"product_type": str(x["product_type"].encode('utf-8')),
		"taxable": str(x["variants"][0]["taxable"]),
		"sku": str(x["variants"][0]["sku"].encode('utf-8')),
		"available": str(x["variants"][0]["available"]),
		"price": str(x["variants"][0]["price"].encode('utf-8')),
		"grams": str(x["variants"][0]["grams"])}
	output.append(data)
json = json.dumps(output)
print( json)

