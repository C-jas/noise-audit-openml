import openml
import numpy
import pandas as pd

#Dieses Programm hat alle Flows auf einer Task gefunden, und angegeben, wieviele Runs er auf der Task hat. 
#Das Programm wurde mehrfach ausgeführt, jeweils mit einer anderen Task.

task_id = 211993
metric = "root_mean_squared_error"

#Sucht alle Runs und Flows auf der Task.
evaluations = openml.evaluations.list_evaluations(
    function=metric, tasks=[task_id], output_format="dataframe"
)
run_ids = evaluations.run_id.unique()
flow_ids = evaluations.flow_id.unique()

#Erstellt eine Liste von Countern pro Flow
flow_ids_counter = [[x,0] for x in flow_ids]

#Zählt die Anzahl an Runs pro Flow
for runrow in evaluations.iterrows():
    for flow_id_counter in flow_ids_counter:
        if runrow[1]['flow_id']== flow_id_counter[0]:
            flow_id_counter[1] += 1

#Wirft alle Flows raus, die einen oder weniger Runs auf der Task haben
unique_flow_ids_counter = []
for flow_id_counter in flow_ids_counter:
    if flow_id_counter[1] > 1:
        unique_flow_ids_counter.append(flow_id_counter)

print(unique_flow_ids_counter)

