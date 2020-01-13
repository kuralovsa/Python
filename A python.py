import re
print("Введите выражение :")
a=re.compile(r"[\s,.]+")
a=a.split("2 + 4 = 6")
print(a)
