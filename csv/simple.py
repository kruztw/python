import csv

with open('output.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, quotechar="\'", quoting=csv.QUOTE_NONE)

  writer.writerow(['name', 'age', 'weight'])
  
  writer.writerow(['pikachu', 5, 60])
  writer.writerow(['"Squirtle"', 3, 50])
