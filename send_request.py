import requests

command = 'ADD PRODUCT "Product Name", SKU123, "Category", "Sub-Category"'
url = 'http://localhost:5000/command'
response = requests.post(url, data={'command': command})
print(response.text)
