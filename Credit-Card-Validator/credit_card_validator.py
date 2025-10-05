sum_of_odd_digits = 0
sum_of_even_digits = 0
total = 0

card_num = input("Enter a credit card #: ")
card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")
card_num = card_num[::-1]

for x in card_num[::2]:
    sum_of_even_digits += int(x)

for x in card_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_of_even_digits += (1 + (x % 10))
    else:
        sum_of_even_digits += x

total = sum_of_odd_digits + sum_of_even_digits

if total % 10 == 0:
    print("VALID")

else:
    print("INVALED")
    