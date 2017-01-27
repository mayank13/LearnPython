s = 'qA2'
is_alnum = False
is_alpha = False
is_digit = False
is_lower = False
is_upper = False
for letter in s:
    is_alnum = (letter.isalnum())
    is_alpha = (letter.isalpha())
    is_digit = (letter.isdigit())
    is_lower = (letter.islower())
    is_upper = (letter.isupper())
print(is_alnum)
print(is_alpha)
print(is_digit)
print(is_lower)
print(is_upper)