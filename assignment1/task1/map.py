import sys
import os

for line in sys.stdin:
    print('0\t1 2 3 4 5')
    continue
    # currfile = os.environ.get('mapreduce_map_input_file')
    # currfile = '1'
    # line = line.strip()
    # entry = line.split(",")

    # if 'open' in currfile:
    #     summon_number = entry[0]
    #     print('{0:s}\t{1:s}'.format(summon_number, '0'))
    # else:
    #     summon_number = entry[0]
    #     plate_id = entry[14]
    #     violation_precinct = entry[6]
    #     violation_code = entry[2]
    #     issue_date = entry[1]
    #     print('{0:s}\t{1:s} {2:s} {3:s} {4:s} {5:s}'.format(summon_number, '1', plate_id, violation_precinct, violation_code, issue_date))