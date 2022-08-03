from itertools import groupby


df_livingroom = pd.read_csv('split_sensor_int_livingroom_motion.csv')
df_kitchen = pd.read_csv('split_sensor_int_kitchen_motion.csv')
df_corridor = pd.read_csv('split_sensor_int_corridor_motion.csv')
df_bathroom = pd.read_csv('split_sensor_int_bathroom_motion.csv')
df_bedroom = pd.read_csv('split_sensor_int_bedroom_motion.csv')
df_fridge_contact = pd.read_csv('split_sensor_int_fridge_contact.csv')
df_balcon_contact = pd.read_csv('split_sensor_int_balcon_contact.csv')
df_entrance_contact = pd.read_csv('split_sensor_int_entrance_door_contact.csv')


def inPlages(l, date):
  for i in range(int(len(l)/2)):
    if ( date >= l[2*i] and date <= l[2*i+1] ):
      return True
  return False


def get_motion_times(df):
  l = []
  for i in range(len(df)):
    if ( df['value'][i] == 1 and not inPlages(sleep_times, df['timestamp'][i]) and not inPlages(couch_times, df['timestamp'][i])):
      l.append(df['timestamp'][i])
  return l


def get_start_times(l):
  start_times = [ l[0] ]

  for i in range(1,len(l)):
    if (datetime.strptime(l[i], '%Y-%m-%d %H:%M:%S.%f')-datetime.strptime(l[i-1], '%Y-%m-%d %H:%M:%S.%f') > timedelta(seconds=1)):
      start_times.append(l[i])

  return start_times


livingroom_times = get_start_times(get_motion_times(df_livingroom))
kitchen_times = get_start_times(get_motion_times(df_kitchen))
corridor_times = get_start_times(get_motion_times(df_corridor))
bedroom_times = get_start_times(get_motion_times(df_bedroom))
bathroom_times = get_start_times(get_motion_times(df_bathroom))
fridge_times = get_start_times(get_motion_times(df_fridge_contact))
balcon_times = get_start_times(get_motion_times(df_balcon_contact))
entrance_times = get_start_times(get_motion_times(df_entrance_contact))


tuple_list = []

# a : entrer dans la salle de bain
# b : entrer dans la livingroom
# c : entrer dans la cuisine
# d : entrer dans le couloir
# e : entrer dans la chambre
# f : ouvrir frigo
# g : ouvrir porte balcon
# h : ouvrir porte entrée
# i : dormir
# j : s'assoir sur le canapé
# k : regarder la télé
# l : cuisiner


for i in range(len(bathroom_times)):
  tuple_list.append((bathroom_times[i], 'a'))

for i in range(len(livingroom_times)):
  tuple_list.append((livingroom_times[i], 'b'))

for i in range(len(kitchen_times)):
  tuple_list.append((kitchen_times[i], 'c'))

for i in range(len(corridor_times)):
  tuple_list.append((corridor_times[i], 'd'))

for i in range(len(bedroom_times)):
  tuple_list.append((bedroom_times[i], 'e'))

for i in range(len(fridge_times)):
  tuple_list.append((fridge_times[i], 'f'))

for i in range(len(balcon_times)):
  tuple_list.append((balcon_times[i], 'g'))

for i in range(len(entrance_times)):
  tuple_list.append((entrance_times[i], 'h'))

for i in range(int(len(sleep_times)/2)):
  tuple_list.append((sleep_times[2*i], 'i'))

for i in range(int(len(couch_times)/2)):
  tuple_list.append((couch_times[2*i], 'j'))

for i in range(int(len(tv_times)/2)):
  tuple_list.append((tv_times[2*i], 'k'))

for i in range(int(len(stove_times)/2)):
  tuple_list.append((stove_times[2*i], 'l'))



events = ""
l = sorted(tuple_list)
events += l[0][1]
for i in range(1,len(l)):
  if ( l[i][1] != l[i-1][1]):
    if ( l[i][0] != l[i-1][0]):
      events += ","
    events += l[i][1]
    
    
txt = events.split(',')

n = len(txt)

for i in range(n):
  if ( 'c' in txt[i] and ('f' in txt[i] or 'l' in txt[i] )):
    txt[i] = txt[i].replace('c','')
  if ( 'b' in txt[i] and ('k' in txt[i] or 'j' in txt[i] or 'g' in txt[i])):
    txt[i] = txt[i].replace('b','')
  if ( 'd' in txt[i] and 'h' in txt[i]):
    txt[i] = txt[i].replace('d','')

  
event_list = [key for key, _group in groupby(txt)]
events = ','.join(event_list)
events


