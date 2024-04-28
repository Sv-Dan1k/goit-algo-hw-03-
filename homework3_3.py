import re


def normalize_phone(phone_number):
    for numbers in phone_number:
        numbers = re.sub(r'\D', '', phone_number)
        if not numbers.startswith('+'):
            if numbers.startswith('380'):
                numbers = '+' + numbers
            else:
                numbers = '+38' + numbers
    return numbers


list_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]



cleaned_numbers = [normalize_phone(phone_number) for phone_number in list_numbers]
print("Normalized phone numbers for SMS sending: ", cleaned_numbers)

