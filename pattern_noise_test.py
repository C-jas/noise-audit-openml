import numpy
import random

table = []

#Dieses Program prüft die Richtigkeit der Formeln, die für Pattern-Noise aufgestellt wurden.

#Es wird eine Tabelle mit Schätzwerten aufgestellt mit Fall i und Schätzperson j
for i in range(99):
    table.append([])
    for j in range(79):
        table[i].append(random.randint(0, 1000))

#Es wird das Quadrat des System-Noise gebildet
variancelist = []
columnmeans = []
for j in range(len(table[0])):
    column = []
    for i in range(len(table)):
        column.append(table[i][j])
    columnmeans.append(numpy.mean(column))
    variancelist.append(numpy.var(column))
systemvariance = numpy.mean(variancelist)

#Es wird das Quadrat des Level-Noise gebildet
rowmeans = []
for i in range(len(table)):
    rowmeans.append(numpy.mean(table[i]))
levelvariance = numpy.var(rowmeans)

#Das Quadrat von Pattern-Noise wird auf die herkömliche Weise hergeleitet
pattern_noise_by_difference = systemvariance - levelvariance


#Pattern-Noise wird auf die neue Art hergeleitet als der Mittelwert aller V(Xij - Xi - Xj)
row_pattern_variance = []
for j in range(len(table[0])):
    patternerrors = []
    for i in range(len(table)):
        patternerror = table[i][j] - rowmeans[i] - columnmeans[j]
        patternerrors.append(patternerror)
    row_pattern_variance.append(numpy.var(patternerrors))
pattern_noise_by_hypothesis = numpy.mean(row_pattern_variance)


#Es wird getestet, ob und wie weit sich die beiden Herleitungen von Pattern-Noise unterscheiden
isTrue = (pattern_noise_by_difference == pattern_noise_by_hypothesis)
print(isTrue)
print("Difference: " + str(pattern_noise_by_difference) + ", Hypothesis: " + str(pattern_noise_by_hypothesis))



#Pattern-Error mit dem Mittelwert über die Kovarianz = 0 test:
meanofmeans = numpy.mean(rowmeans)
rowmeanserror = [x - meanofmeans for x in rowmeans]
covariances = []
for i in range(len(table)):
    patternerrors = []
    for j in range(len(table[0])):
        patternerror = table[i][j] - rowmeans[i] - columnmeans[j] + meanofmeans
        patternerrors.append(patternerror)
    #covariance1 = (numpy.cov(rowmeans, patternerrors))#[0][1]
    patternerrorserror = [x - numpy.mean(patternerrors) for x in patternerrors]
    rowtimespattern = list(map(lambda x, y: x * y, patternerrorserror, rowmeanserror))
    covariance = numpy.mean(rowtimespattern)
    covariances.append(covariance)

covmean = numpy.mean(covariances)

#Es handeln sich durch die Art wie floats in python berechnet werden manchmal kleinste Ungenauigkeiten ein, 
# die durch das Runden ausgeglichen werden
print(round(covmean,10))

