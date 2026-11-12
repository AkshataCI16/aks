import re

with open("input.txt", "r") as file:
    text = file.read()

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

phone_pattern = r'(?:\+91[- ]?)?[6-9]\d{9}'

emails = re.findall(email_pattern, text)
phone_numbers = re.findall(phone_pattern, text)

print("--- Email Addresses ---")

for email in emails:
    print(email)

print("\n--- Phone Numbers ---")

for phone in phone_numbers:
    print(phone)
