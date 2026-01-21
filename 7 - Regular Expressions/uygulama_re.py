import re

text = "BTK Akademi ile Python kurs tarihleri 15-May-2025 15.May.2025 15/May/2025 15.05.2025. Telefon numaralarımız +90-530-999-9999 +90 530 999 9999. Mail adreslerimiz abc@gmail.com abc@gmail.co.tr abc@hotmail.com"

# Tarihleri verir:
# pattern = r"\d\d-[a-zA-Z][a-zA-Z][a-zA-Z]-\d\d\d\d" # 15-May-2025

# pattern = r"\d{2}-[a-zA-Z]{3}-\d{4}" # 15-May-2025
  
# pattern = r"\d{2}[-./][a-zA-Z0-9]{2,3}[-./]\d{4}" # 15-May-2025 , 15/May/2025, 15.May.2025, 15.05.2025, 30-999-9999

# pattern = r"\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}" # 15-May-2025 , 15/May/2025, 15.May.2025, 15.05.2025


# Mailleri verir:
# pattern = r"\w+@[a-z]+(\.[a-z]{2,3})+" 


# Telefon numaralarını verir:
pattern = r"\+\d{2}[-\s]\d{3}[-\s]\d{3}[-\s]\d{4}" 

matches = re.finditer(pattern, text)

for match in matches:
    print(match)