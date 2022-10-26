import pandas as pd
import csv

file1 = 'bright_stars.csv'
file2 = 'unitConverted.csv'   
d1 = []
d2 = []
with open(file1, 'r', encoding='utf8') as read1:
    csv1 = csv.reader(read1)

    for w1 in csv1:
        d1.append(w1)

with open(file2, 'r', encoding='utf8') as read2:
    csv2 = csv.reader(read2)

    for w2 in csv2:
        d2.append(w2)



h1 = d1[0]
h2 = d2[0]

more1 = d1[1:]
more2 = d2[1:]
left = []

h = h1+h2
for i in more1:
    left.append(i)

for m in more2:
    left.append(m)

with open('finalMergedData', 'w', encoding = 'utf8') as k :
    csvwriter = csv.writer(k)
    csvwriter.writerow(h)   
    csvwriter.writerows(left)



