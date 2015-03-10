__author__ = 'HCDN\mbataglia.dgis'
# Import the pandas package, then use the "read_csv" function to read
# the labeled training data
import pandas as pd
train = pd.read_csv("labeledTrainData.tsv", header=0, \
                    delimiter="\t", quoting=3)

num_reviews = train["review"].size
num_positive = 0
num_negative = 0
longitudMax = 0
longitudMin = 9999999
total = 0
cantidadAmazing = 0
lista  = []

for i in xrange( 0, num_reviews ):
    review = train["review"][i]
    review = review[1:-1]

    if train["sentiment"][i] == 1:
        num_positive = num_positive +1
    else:
        num_negative = num_negative +1
        if "amazing" in review:
              lista.append(train["review"][i])
              cantidadAmazing += 1

    if len(review) > longitudMax:
        longitudMax = len(review)
    if len(review) < longitudMin:
        longitudMin = len(review)

    total += len(review)



promedio = total / num_reviews

print "total: " + str(num_reviews)
print "positivos: " + str(num_positive)
print "negativos: " + str(num_negative)
print "promedio longitud review: " + str(promedio)
print "longitud maxima de review: " + str(longitudMax)
print "longitud minima de review: " + str(longitudMin)
print "cantidad de reviews negativos con la palabra amazing: " + str(cantidadAmazing)
print "listado de reviews negativos con la palabra amazing: "
print '\n------------------------------------------------------------------\n'.join(lista)
