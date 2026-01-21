import re

text = "BTK Akademi Python Dersleri BTK"
pattern = "BTK"

match = re.search(pattern, text) # textteki patterni verir
sonuc = match

sonuc = match.start() # 0
sonuc = match.end()   # 3

match = re.findall(pattern,text) # tekrarlanan kelimelerin hepsini verir
sonuc = match

print(sonuc)
