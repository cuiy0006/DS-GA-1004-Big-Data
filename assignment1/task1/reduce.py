import sys

openkey = None
parkingdic = {}
currentkey = None

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t', 1)
    entry = value.split(' ')

    if key == currentkey:
        if entry[0] == '0': #from open
            openkey = key
        else: #from parking
            parkingdic[key] = entry
    else:
        for k, v in parkingdic.items():
            if k != openkey:
                print('{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}'.format(k, v[1], v[2], v[3], v[4]))
        currentkey = key
        openkey = None
        parkingdic = {}
        if entry[0] == '0': #from open
            openkey = key
        else: #from parking
            parkingdic[key] = entry

if key == currentkey:
    for k, v in parkingdic.items():
        if k != openkey:
            print('{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}'.format(k, v[1], v[2], v[3], v[4]))