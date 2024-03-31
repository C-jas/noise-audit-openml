import openml

#Dieses Programm hat herausgefunden wieviele verschiedene RMSE, 
#   und damit wieviele unterschiedliche Runs es von einem Flow auf einer Task gab
#Das Programm wurde mehrfach ausgeführt, jeweils mit einer Flow und Task Kombination, 
#   die von regression_flow_finder produziert wurde.

task_id = 2280
flow_id = 364
metric = "root_mean_squared_error"

#Sucht alle Runs, beziehungsweise je den RMSE von diesen
evaluations = openml.evaluations.list_evaluations(
    function=metric, tasks=[task_id],flows=[flow_id], output_format="dataframe"
)


measures = []
measures_counter = []

#zählt, wie häufig die jeweiligen RMSE vorkommen.
for runrow in evaluations.iterrows():
    measure = runrow[1]['value']
    if measure not in measures:
        measures.append(measure)
        measures_counter.append(1)
    else:
        index = measures.index(measure)
        measures_counter[index] += 1

measuresandcounters = []

#verknüpft die measure und die counterliste
for i in range(len(measures)):
    measuresandcounters.append([measures[i],measures_counter[i]])

print(measuresandcounters)