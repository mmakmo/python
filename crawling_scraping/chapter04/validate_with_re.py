import re


value = '3,000yen'
if not re.search(r'^[0-9,]+$', value):
    raise ValueError('Invalid price')
