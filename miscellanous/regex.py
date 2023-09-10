import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phone_num_regex.search('My number is 415-555-4242.')

print(f'Phone number found: {mo.group()}')

hero_regex = re.compile (r'Batman|Tina Fey')

mo1 = hero_regex.search('Batman and Tina Fey.')
mo1.group()
# 'Batman'

mo2 = hero_regex.search('Tina Fey and Batman.')
mo2.group()

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')

print(mo.group(0))
# 'Batmobile'

mo.group(1)
# 'mobile'

