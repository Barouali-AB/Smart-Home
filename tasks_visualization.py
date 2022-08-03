
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px


df_couch = pd.read_csv('split_sensor_int_couch_pressure.csv')
df_stove = pd.read_csv('split_sensor_int_stove_light.csv')
df_bed = pd.read_csv('split_sensor_int_bed_pressure.csv')
df_tv = pd.read_csv('split_sensor_int_tv_light.csv')

df_couch["state"] = 0
df_stove["state"] = 0
df_bed["state"] = 0
df_tv["state"] = 0

df_bed.loc[df_bed["value"] > 630, "state"] = 1
df_couch.loc[df_couch["value"] > 305, "state"] = 1
df_stove.loc[df_stove["value"] < 150, "state"] = 1
df_tv.loc[df_tv["value"] < 20, "state"] = 1

def get_times(df):
  times = []
  i = 0

  while i < len(df) - 1:
      n = df["state"][i]
      if  ( n == 1 ): 
        startIndex = i
        while i < len(df) - 1 and df["state"][i] == df["state"][i + 1]:
            i = i + 1
        endIndex = i
        if (startIndex < endIndex):
          times.append(df['timestamp'][startIndex])
          times.append(df['timestamp'][endIndex])
          date_time_obj1 = datetime.strptime(df['timestamp'][startIndex], '%Y-%m-%d %H:%M:%S')
          date_time_obj2 = datetime.strptime(df['timestamp'][endIndex], '%Y-%m-%d %H:%M:%S')
          duree = str(date_time_obj2 - date_time_obj1)
        #print("{0} >> {1}".format(n, [df['timestamp'][startIndex], df['timestamp'][endIndex], duree]))
      i = i + 1
    
  return times
  
  
bed_times = get_times(df_bed)
couch_times = get_times(df_couch)
tv_times = get_times(df_tv)
stove_times = get_times(df_stove)

sleep_times = [bed_times[0]]

for i in range(1, int(len(bed_times)/2)):
  if (datetime.strptime(bed_times[2*i], '%Y-%m-%d %H:%M:%S')-datetime.strptime(bed_times[2*i-1], '%Y-%m-%d %H:%M:%S') > timedelta(minutes=5)):
    sleep_times.append(bed_times[2*i-1])
    sleep_times.append(bed_times[2*i])

sleep_times.append(bed_times[-1])


df = []

for i in range(int(len(bed_times)/2)):
  df.append(dict(Task="Lit", Start=bed_times[2*i], Finish=bed_times[2*i+1]))

for i in range(int(len(sleep_times)/2)):
  df.append(dict(Task="Dormir", Start=sleep_times[2*i], Finish=sleep_times[2*i+1]))

for i in range(int(len(couch_times)/2)):
  df.append(dict(Task="Canapé", Start=couch_times[2*i], Finish=couch_times[2*i+1]))

for i in range(int(len(tv_times)/2)):
  df.append(dict(Task="Télé", Start=tv_times[2*i], Finish=tv_times[2*i+1]))

for i in range(int(len(stove_times)/2)):
  df.append(dict(Task="Cuisinière", Start=stove_times[2*i], Finish=stove_times[2*i+1]))


fig = px.timeline(df, x_start='Start', x_end='Finish', y = 'Task', color='Task')
fig.show()

