
age = 18  # Ціле число (int)
name = "Stephen"  # Рядок (str)
is_student = True  # Булеве значення (bool)

"""
- ✅ Використовуйте **англійські** слова
- ✅ **Маленькі літери** з підкресленнями: `user_name`, `total_price`
- ✅ **Описові імена**: `age` замість `a`, `student_count` замість `sc`
- ❌ Не економте на довжині: `max_users_age` краще ніж `m_u_a`
- ❌ Не починайте з цифр і символів: `2name`, `$name` неправильно
- ❌ Не використовуйте спеціальні символи: `user-name` неправильно
"""
імя = 18
print(імя)
"""
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""

"""
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
"""
print(2**6, 3**4)

a = 5
b = 2
result = a / b
print(result)

a = 5
b = 2
result = a // b 
print(result)

a = 5
b = 2
result = a % b 
print(result)

a = True
b = False
result = a and b 
print(result)

a = True
b = False
result = a or b
print(result)

a = True
result = not a
print(result)
"""
(       )       [       ]       {       }
,       :       .       ;       @
"""
result = (2 + 3) * 4
print(result)

список = [1, 2, 3, 4]
елемент = список[0]

словник = {'ключ': 'значення', "key2": 'value2'}
множина = {1, 2, 3}

if True:
    pass # не роби нічого, я не придумав що тут треба

def function_name():
    pass # дії усередині функції

hello = "Привіт"
its_len = hello.__len__() # a
print(its_len)


print(len(hello)) # a

zminna_a = "a"; zminna_b = "b"

"""
@декоратор
def функція():
    pass  # Блок коду
"""

single_quotes = 'Це рядок з одинарними лапкми'
double_quotes = "Це рядок з звичайними, подвійими лапкми"
long_quotes = '''Це \
рядок з тикратним \
повторенням лапок'''

print(long_quotes)
# \ /

int # цілі числа

dec_00 = 0
dec_01 = 1

dec_09 = 9
dec_x = 10 

eh_07 = 7
eh_08 = 8
eh_09 = 10 # 9

print(0b0)
print(0b1)
print(0b10)
print(0b11)
print(0b100)
print(0b101)
print(0b110)
print(0b111)
print(0b1000)

x_09 = 0x9
x_10 = 0xa
x_11 = 0xb
x_12 = 0xc
x_13 = 0xd
x_14 = 0xe
x_15 = 0xf
x_16 = 0x10

"""
Обмеження цілих чисел у Python залежить від архітектури вашої системи. 
У зазвичай 32-бітних системах це може бути від 
-2,147,483,648 до 2,147,483,647, 
а на 64-бітних системах це може бути від 
-9,223,372,036,854,775,808 до 
9,223,372,036,854,775,807.
"""
float
"0,1"
0.1
10.01
100.01
100000000.000001
0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0E0 # Floating-point literals

a = 0.1 + 0.2
b = 0.3

print("a =", repr(a))
print("b =", repr(b))
print("a == b:", a == b)
print("Різниця (a - b):", a - b)

None  ## 

str
print("str")
print('I\'m')
print('п\'ять')
print("п\"ять")
print('A not very long string \
that spans two lines')

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""
print("a", "b", "c", sep=' ', end=' : ')
print("a", "b", "c", sep=' ', end=' : ')
print("a", "b", "c", sep=' ', )

year = 2016
event = 'Referendum'
print(f'Results of the {event} in {year}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
out = '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(out)

query_sting = "підказка, що буде виведена на екран і повинна пояснити,\
  що ми очікуємо від користувача: "
variable = input(query_sting)
print(f"You type: {variable}\nend of \tlesson")
