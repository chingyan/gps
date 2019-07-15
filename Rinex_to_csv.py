import numpy as np
import math 
import csv
from datetime import datetime as dt
import time as tm

gps_start_data = 723186

def read(data,sys_type):
    counter = 0
    counter1 = 0
    csv_counter = 0
    b = 0
    with open(data,'r') as count:
        a = count.readlines()
        for i in a:
            if i.find('END OF HEADER') != -1:
                break
            else:
                counter1 += 1
    csv1 = np.empty(((len(a) - counter1),17))
    with open(data,'r') as data:
        for i in data:
            
            counter += 1
            if i.find('END OF HEADER') == 60 or counter > 60 :
                if i.find('> 2019') == 0:
                    date = i.split()
                    year = date[1]
                    month = date[2]
                    day = date[3]
                    hour = date[4]
                    minutes = date[5]
                    second = date[6]
                    time = (year,month,day,hour,minutes,second)
                    temp = '-'.join(time[0:3])
                    timeArray = dt.strptime(temp, "%Y-%m-%d")                   
                    day_total = dt.toordinal(timeArray)
                    gps_start = dt.toordinal(dt(1980,1,6))
                    deltat = day_total - gps_start
                    gps_week = math.floor(deltat/7)
                    gps_dow = math.floor(deltat - gps_week * 7)
                    gps_sow = (deltat - gps_week * 7) * 86400
                    gps_sow = int(gps_sow) + int(hour) * 3600 + int(minutes) * 60 + float(second)
                elif i[0] == 'G' or i[0] =='J' or i[0] == 'R' or i[0] == 'C':            
                    csv1[csv_counter][0] = int(gps_week) 
                    csv1[csv_counter][1] = int(gps_sow)
                    csv1[csv_counter][3] = i[1:3]
                    if i[0] == "G":
                        csv1[csv_counter][2] = 1
                    elif i[0] == 'J':
                        csv1[csv_counter][2] = 5
                    elif i[0] == 'C':
                        csv1[csv_counter][2] = 2
                    elif i[0] == 'R':
                        csv1[csv_counter][2] = 3
                    try:
                        csv1[csv_counter][4] = i[5:16]
                    except:
                        csv1[csv_counter][4] = "NaN"
                    try:                        
                        csv1[csv_counter][5] = i[21:32]
                    except:
                        csv1[csv_counter][5] = "NaN"
                    try:
                        csv1[csv_counter][6] = i[37:48]
                    except:
                        csv1[csv_counter][6] = "NaN"
                    try:
                        csv1[csv_counter][7] = i[52:64]
                    except:
                        csv1[csv_counter][7] = "NaN"
                    try:
                        csv1[csv_counter][8] = i[68:80]
                    except:
                        csv1[csv_counter][8] = "NaN"
                    try:
                        csv1[csv_counter][9] = i[84:96]
                    except:
                        csv1[csv_counter][9] = "NaN"
                    try:
                        csv1[csv_counter][10] = i[100:112]
                    except:
                        csv1[csv_counter][10] = "NaN"
                    try:
                        csv1[csv_counter][11] = i[116:128]                    
                    except:
                        csv1[csv_counter][11] = "NaN"
                    try:
                        csv1[csv_counter][12] = i[132:144]
                    except:
                        csv1[csv_counter][12] = "NaN"
                    try:
                        csv1[csv_counter][13] = i[149:160]
                    except:
                        csv1[csv_counter][13] = "NaN"
                    try:
                        csv1[csv_counter][14] = i[162:176]
                    except:
                        csv1[csv_counter][14] = "NaN"
                    try:
                        csv1[csv_counter][15] = i[178:192]
                    except:
                        csv1[csv_counter][15] = "NaN"
                    try:
                        csv1[csv_counter][16] = i[194:208]
                    except:
                        csv1[csv_counter][16] = "NaN"
                    csv_counter = csv_counter + 1
                    
                
                
                
            
                





    return csv1

    # obs_filename='Data/0...0201904221000.19o'
    # data = read(obs_filename,'G')
    # print(data)