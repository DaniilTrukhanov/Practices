import re
import json

with open(r"C:\Users\truha\Desktop\учёба\PP2\practice5\raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

#1
prices = re.findall(r'\d[\d\s]*,\d{2}', text)
prices = [float(price.replace(" ", "").replace(",", ".")) for price in prices]

#2
products = re.findall(r'\d+\.\n(.+?)\n\d+,\d{3} x', text)

#3
total_amount = sum(prices[i] for i in range(len(prices)))
total_match = re.search(r'ИТОГО:\s*\n([\d\s]+,\d{2})', text)
if total_match:
    total_amount = float(total_match.group(1).replace(" ", "").replace(",", "."))

#4
date_time = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})', text)
date_time = date_time.group(1) if date_time else None

#5
payment = re.search(r'(Банковская карта):', text)
payment_method = payment.group(1) if payment else None

#6
receipt = {
    "products": products,
    "prices": prices[:len(products)],
    "total_amount": total_amount,
    "date_time": date_time,
    "payment_method": payment_method
}
print(json.dumps(receipt, indent=4, ensure_ascii=False))