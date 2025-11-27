adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f'Task 01. Замінено кінець абзацу на пробіл: {adwentures_of_tom_sawer}')

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f'Task 02. Замінено .... на пробіл: {adwentures_of_tom_sawer}')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f'Task 03. Зроблено, щоб у тексті було не більше одного пробілу між словами: {adwentures_of_tom_sawer}')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print(f'Task 04. Літера "h" зустрічається у тексті {count_h} разів')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
big_words = adwentures_of_tom_sawer.count("A") + adwentures_of_tom_sawer.count("B") + adwentures_of_tom_sawer.count("C") + adwentures_of_tom_sawer.count("D") + adwentures_of_tom_sawer.count("E") + adwentures_of_tom_sawer.count("F") + adwentures_of_tom_sawer.count("G") + adwentures_of_tom_sawer.count("H") + adwentures_of_tom_sawer.count("I") + adwentures_of_tom_sawer.count("J") + adwentures_of_tom_sawer.count("K") + adwentures_of_tom_sawer.count("L") + adwentures_of_tom_sawer.count("M") + adwentures_of_tom_sawer.count("N") + adwentures_of_tom_sawer.count("O") + adwentures_of_tom_sawer.count("P") + adwentures_of_tom_sawer.count("Q") + adwentures_of_tom_sawer.count("R") + adwentures_of_tom_sawer.count("S") + adwentures_of_tom_sawer.count("T") + adwentures_of_tom_sawer.count("U") + adwentures_of_tom_sawer.count("V") + adwentures_of_tom_sawer.count("W") + adwentures_of_tom_sawer.count("X") + adwentures_of_tom_sawer.count("Y") + adwentures_of_tom_sawer.count("Z")
print(f'Task 05. У тексті з великої літери починається {big_words} слів')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
word_tom = adwentures_of_tom_sawer.find("Tom", 2)
print(f'Task 06. Слово "Том" зустрічається в тексті вдруге на {word_tom} позиції')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
adwentures_of_tom_sawer_sentences = [s.strip() + '.' for s in adwentures_of_tom_sawer_sentences if s.strip()] 
# Прохання розказати як можна переписати цю строку на основі наявної у нас на цей час інформації з курсу
# Ця строка була відверто запозичена з Gemini, без неї: 
# Task 9 видавав False для 4 речення, де мало бути True, 
# Task 10 не приймав [-1], оскільки останній елемент в списку був " ".

print(f'Task 07. {adwentures_of_tom_sawer_sentences}')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentences_4 = adwentures_of_tom_sawer_sentences[3]
sentences_4_lower = sentences_4.lower()
print(f'Task 08. Четверте речення з adwentures_of_tom_sawer_sentences в нижньому регістрі: {sentences_4_lower}')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

check_sentences = adwentures_of_tom_sawer_sentences[3].startswith("By the time")
print(f'Task 09. Перевірка чи починається якесь речення з "By the time": {check_sentences}')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_in_last_sentence = last_sentence.split()
words_count = len(words_in_last_sentence)

print(f'Task 10. Кількість слів останнього речення з adwentures_of_tom_sawer_sentences: {words_count}')
