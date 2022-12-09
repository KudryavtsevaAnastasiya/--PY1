from pprint import pprint

dict_num = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]

pprint(dict_num)
# Последняя строка