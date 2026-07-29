text = '''Dear Ben,
Thanks foe your email. I was glad to hear from you again. In your message you asked me some questions.

As for your first question, cats and dogs are the most popular pets among teenagers in Russia because they are cute.

Besides, I spend almost all day in a week taking care of my cat and playing with my cat every week.

Speaking about your third question, to my mind, people should protect stray animals in cities because in cities very dangerous space for them.

Well, I need to go now as I have to do my homework.

Write back soon.

Best wishes,
Yaroslav
'''


word = text.split()
list_word = list(text)

# Это нужно для понимания разницы между .split() и list()
#print(f"Обычный список из письма: \n{list_word}")
#print(f"\nСписок слов из письма: \n{word}\n")

print(f"Письмо: \n{text}")
print(f"Количество слов в письме: {len(word)}")

print(f'Количество символов в письме: {len(list_word)}')
print(f'Количество символов в письме (Без пробелов): {len(text.replace(" ", ""))}')
