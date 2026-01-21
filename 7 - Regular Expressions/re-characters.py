import re

text = "A34as ABC 123 XYZ 456 @&% 300 2 3434 123456 1_2 abc"


# pattern = r"\d\d\d" #pattern yazarken başa r yazmayı ihmal etme (ters slash için \)
# pattern = r"\d+" # bulacagımız sayıya gore d koymamıza gerek kalmaz en az 1 eşleşme olmalı
# pattern = r"\d*" # sayı olmaması durumunda da 
# pattern = r"\d{3}" # 3 basamaklı sayılar
# pattern = r"\d{3,5}" # min 3 basamaklı maks 5 basamaklı sayıları getirir
# pattern = r"\d{3,}" # min 3 bas
# pattern = r"\d{,5}" # maks 5 bas
# pattern = r"\d.\d" # 3 basamaklı olucak ortada da 1 karakter olucak
# pattern = r"\d|[a-z]"
# pattern = r"\d\w\w\w"
# pattern = r"^A\d\w\w\w" # ^yanındakinin özelliği ile başlayacak textin en başında olmalı 
pattern = r"A\d\w\w\w$" # textin en sonunda A ile başlayan araması için


# matches = re.search(pattern, text)

# matches = re.findall(pattern, text) # 123 456 300

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())
    # 123 456 300

print(matches)