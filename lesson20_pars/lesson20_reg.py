import re
string = "Test1 Test2 Test3 Test4 Test5"
template=r"Test"
result = re.match(template, string) # begin
print(result)
print(result.group(0))

template=r"Test5"
result2 = re.search(template, string) # whoole, first end
print(result2)
print(result2.group(0))


template=r"Test"
result = re.findall(template, string) # whoole
print(result)

result = re.sub(r"T", "t", string)
print(result)

result = re.split(r"t", string)
print(result)

"." # Один будь-який символ, крім нового рядка \n
"?" # може бути чи ні
"*" # 0 і більше входжень шаблону зліва
"+" # 1 і більше входжень шаблону зліва
"\w" # Будь-яка цифра чи літера
"\d" # Будь-яка цифра [0-9]
"\s" # Будь-який символ пробілу + tab

tel_reg =r"\(\d{3}\)\s?\d{3}(\s|-)?\d{2}(\s|-)?\d{2}"

"{n,m}" # Від n до m входжень ({,m} — від 0 до m
"()" # Групує вираз, присв. йому індекс та повертає знайдений текст
# (==)(.*)(==)
# $2 # Зберегти другу групу (те що між "вусиками")

email = "user.marketing@example.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Email введено правильно.")
else:
    print("Некоректний формат email.")