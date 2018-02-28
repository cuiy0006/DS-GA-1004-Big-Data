import re

line = '7499381109,"795J,S",5,14,2016-03-06'
matches = re.findall(r'\".*?\"', line)
lst = list(map(lambda s:s.replace(',','*'), matches))
for i, match in enumerate(matches):
    line = line.replace(match, lst[i])
entry = line.split(',')
if '"' in entry[1]:
    entry[1] = entry[1][1:-1].replace('*', ',')
print('{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}'.format(entry[0],entry[1],entry[2],entry[3],entry[4]))
print(entry)