from datetime import datetime



df = pd.read_csv('split_sensor_int_bed_pressure.csv')
df[:172800].plot(x="timestamp", y="value", figsize = (15,10))

bed = [0] * 604800

for i in range(604800):
  if ( df['value'][i] > 630):
    bed[i] = 1

first_timestamp = 1582675200
bed_times = []
i = 0

while i < len(bed) - 1:
    n = bed[i]
    startIndex = i
    dt_object_start = datetime.fromtimestamp(first_timestamp+startIndex)
    while i < len(bed) - 1 and bed[i] == bed[i + 1]:
        i = i + 1

    endIndex = i
    dt_object_end = datetime.fromtimestamp(first_timestamp+endIndex)
    date_time_str_1 = dt_object_start.strftime("%y-%m-%d %H:%M:%S")
    date_time_str_2 = dt_object_end.strftime("%y-%m-%d %H:%M:%S")
    bed_times.append(date_time_str_1)
    bed_times.append(date_time_str_2)
    duree = endIndex - startIndex


    print("{0} >> {1}".format(n, [date_time_str_1, date_time_str_2, str(int(duree//3600))+"h-"+str(int((duree%3600)//60))+"min-"+str(int((duree%3600)%60))+"s"]))
    i = i + 1
    
        
 

## Find timestamp


date_time_str = '20-02-26 00:00:00'

date_time_obj = datetime.strptime(date_time_str, '%y-%m-%d %H:%M:%S')

timestamp = datetime.timestamp(date_time_obj)
print("timestamp =", timestamp)
