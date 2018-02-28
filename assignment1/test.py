import re

line = 'sadsad, "asd,dfdf,cvc", "erew,cv", zdfwer'
matches = re.findall(r'\".*?\"', line)
lst = list(map(lambda s:s.replace(',','*'), matches))
for i, match in enumerate(matches):
    line.replace(match, lst[i])
entry = line.split(',')
print(entry)