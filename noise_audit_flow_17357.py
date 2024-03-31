import openml
import numpy
import math
import pandas as pd

def printNoise (runpredictions, fold):
    
    
    variancelist = []
    sumsquareerrors = []

    bias_squared_list = []
    
    #wie in der Arbeit entspricht i hier dem Fall i
    for i in range(0, len(runpredictions[0].index)):
        
        #jeder Aufruf der Funktion soll nur die Fehlerkomponenten für einen einzelnen Fold berechnen
        if runpredictions[0].at[i, 'fold'] != fold:
            continue
        
        #Bildet den Mittelwert von Xi über alle Schätzpersonen/Runs
        mean = numpy.mean([x.at[i, 'prediction'] for x in runpredictions])

        #Bildet die Variance V(Xi) über alle Runs
        variance = numpy.var([x.at[i, 'prediction'] for x in runpredictions])
        variancelist.append(variance)

        #Bildet das Quadrat des Gesamtfehlers, das später in den Mean Squared Error Mean einfließt
        sumsquareerrors.append([pow(x.at[i, 'prediction'] - x.at[i,'truth'],2) for x in runpredictions])

        #Bildet das Quadrat des Bias(Xi,Yi)
        bias_squared_list.append(pow(mean - runpredictions[0].at[i,'truth'],2))



    #Bildet das Quadrat des System-Noise
    systemvariance = numpy.mean(variancelist)

    #Bildet den MSEM, der direkt aus allen Gesamtfehlern berechnet werden kann.
    MSEM = numpy.mean(sumsquareerrors)

    #Bildest das Quadrat des Mean-Bias
    meanbias_squared = numpy.mean(bias_squared_list)

    #Hier wird noch das Level-Noise berechnet
    predictionmeans = []
    #Es wird über die Schätzperson/Run j iteriert
    for prediction in runpredictions:
        #Es wird sichergestellt, dass nur die Schätzwerte eines Folds benutzt werden.
        onefoldprediction = prediction.loc[prediction['fold'] == fold]
        list = onefoldprediction['prediction'].to_numpy()

        #Bildet den Mittelwert von Xj
        mean = numpy.mean(list)
        predictionmeans.append(mean)

    #Bildet das Quadrat des Level-Noise
    levelvar = numpy.var(predictionmeans)

    #Bildet das Quadrat des Pattern-Noise
    patternvar = systemvariance - levelvar
    
    #Es wird die Wurzel der einzelnen Fehlerkomponenten gezogen und diese dann in Latex-Code für eine einzelne Zeile
    # einer Tabelle ausgegeben.
    results = "$" + str(fold) + "$ & "
    #Formatiert den RMSEM
    results += "{:.3e}}}$".format(math.sqrt(MSEM)) + " & " 
    #Formatiert das Mean-Bias
    results += "{:.3e}}}$".format(math.sqrt(meanbias_squared)) + " & "
    #Formatiert System-Noise
    results += "{:.3e}}}$".format(math.sqrt(systemvariance)) + " & " 
    #Formatiert Level und Pattern-Noise
    results += "{:.3e}}}$".format(math.sqrt(levelvar)) + " & " + "{:.3e}}}$".format(math.sqrt(patternvar)) 

    results += "\\\\ \\hline"

    formatedresults = results.replace("e+", "$ \cdot 10^{").replace(".", ",")

    print(formatedresults)





task_id = 2295
flow_id = 17357
metric = "root_mean_squared_error"

#sucht alle runs raus, die die gewünschte Task und den gewünschten Flow haben
evaluations = openml.evaluations.list_evaluations(
    function=metric, tasks=[task_id], flows=[flow_id],output_format="dataframe"
)
run_ids = evaluations.run_id.unique()
runs = openml.runs.get_runs(run_ids)

#Sucht die Schätzwerte, und die korrespondierenden echten Werte aller Runs raus
runpredictions = [x.predictions.apply(pd.to_numeric) for x in runs]

#Berechnet die Fehlerkomponenten für jeden einzelnen der 10 Folds, da die Task Kreuzvalidierung vorschreibt
for i in range(10):
    printNoise(runpredictions, i)

