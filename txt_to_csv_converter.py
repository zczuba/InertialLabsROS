import csv
import os
import sys
from datetime import datetime

time = datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')
csv_file_name = time + '.csv'

file_path = sys.argv[1]

if os.path.exists(file_path) == False:
	print('ERROR: Incorrect filepath argument')
	sys.exit()

myfile = open(file_path)
lines = myfile.readlines()
transList = []

while len(lines) > 0:
    temp = lines.pop(0)
    
    if True in [char.isdigit() for char in temp]:
        openQuotes = False

        for char in temp:
            if openQuotes == False:
                if not (char.isdigit() or char == '-' or char == '.'):
                    if char == '"':
                        openQuotes = True
                    else:
                        temp = temp.replace(char, '')

            if openQuotes == True:
                if char == '"':
                    openQuotes = False
        
        transList.append(temp)

fields = ['seq', 'stamp_secs', 'stamp_nsecs', 'frame_id', 'GPS_INS_Time', 'GPS_IMU_Time', 'GPS_mSOW_data', 
'LLH_x', 'LLH_y', 'LLH_z', 'YPR_x', 'YPR_y', 'YPR_z', 'OriQuat_x', 'OriQuat_y', 'OriQuat_z', 'OriQuat_w', 
'Vel_ENU_x', 'Vel_ENU_y', 'Vel_ENU_z', 'Solution_Status_data', 'Pos_STD_x', 'Pos_STD_y', 'Pos_STD_z', 
'Heading_STD', 'USW']

csv_list = []

while len(transList) > 0:
    csv_list.append(transList[:26])
    del transList[:26]

with open(csv_file_name, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(csv_list)
