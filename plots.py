import plotly.express as px

df = []

for i in range(int(len(bed_times)/2)):
  df.append(dict(Task="Lit", Start=bed_times[2*i], Finish=bed_times[2*i+1]))

for i in range(int(len(couch_times)/2)):
  df.append(dict(Task="Canapé", Start=couch_times[2*i], Finish=couch_times[2*i+1]))

for i in range(int(len(tv_times)/2)):
  df.append(dict(Task="TV", Start=tv_times[2*i], Finish=tv_times[2*i+1]))

for i in range(int(len(stove_times)/2)):
  df.append(dict(Task="Four", Start=stove_times[2*i], Finish=stove_times[2*i+1]))


fig = px.timeline(df, x_start='Start', x_end='Finish', y = 'Task', color='Task')
fig.show()
