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
adwentures_of_tom_sawer1 = adwentures_of_tom_sawer.replace("\n", " ")
print(f"\ntask_01 {adwentures_of_tom_sawer1}")
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer2 = adwentures_of_tom_sawer.replace("....", " ")
print(f"\ntask_02 {adwentures_of_tom_sawer2}")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer3 = " ".join(adwentures_of_tom_sawer.split())
print(f"\ntask_03 {adwentures_of_tom_sawer3}")
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print(f"\ntask_04 {count_h}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
capital_count = sum(1 for c in adwentures_of_tom_sawer if "A" <= c <= "Z")
print(f"\ntask_05 {capital_count}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first = adwentures_of_tom_sawer.find("Tom")
second = adwentures_of_tom_sawer.find("Tom", first + 1)
print(f"\ntask_06 {second}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(f"\ntask_07 {adwentures_of_tom_sawer_sentences}")
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(f"\ntask_08 {fourth_sentence}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
starts_with_BTT = any(s.strip().startswith("By the time") for s in adwentures_of_tom_sawer_sentences)
print(f"\ntask_09 {starts_with_BTT}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1].strip()
word_count = len(last_sentence.split())
print(f"\ntask_10 {word_count}")
