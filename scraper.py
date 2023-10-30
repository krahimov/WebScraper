


import requests
from plyer import notification

headers = {
    'Authorization': 'Bearer c1c35625-8fcc-4da8-8339-e52617fac1ab',
    'Content-Type': 'application/json'
}

url = "https://api.brightdata.com/dca/dataset?id=j_lodbfbgymm9w17f4s"
response = requests.get(url, headers=headers)

data = response.json()

# Calculate the price difference for each item and store with the item
for item in data:
    item['price_difference'] = item['finalPrice']['value'] - item['initialPrice']['value']

# Sort the items by the price difference in descending order
sorted_data = sorted(data, key=lambda x: x['price_difference'], reverse=True)

# Get the item with the largest price difference
largest_difference_item = sorted_data[0]

# Notify about the item with the largest price difference
notification.notify(
    title=f"Item with Largest Price Difference: {largest_difference_item['title']}",
    message=f"Price Difference: {largest_difference_item['price_difference']}",
    timeout=10  # the notification will be visible for 10 seconds
)
