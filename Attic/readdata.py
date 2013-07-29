
import pandas
dataFrame = pandas.read_csv('pyGaugeOutput_okay.csv')
print dataFrame

print dataFrame.describe()

print dataFrame['x']

print dataFrame[0:2]

for row_index, row in dataFrame.iterrows():
    print (row['x'] + row['y']) / 2.0
