import random

cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

select_cards=random.sample(cards, 2)
print(select_cards)

new_cards=select_cards + random.sample(cards, 1)
print(new_cards)


#print(sum(select_cards))
