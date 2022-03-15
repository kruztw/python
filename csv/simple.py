import csv

with open('output.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, quotechar="\'", quoting=csv.QUOTE_NONE)

  writer.writerow(['name', 'age', 'weight'])
  writer.writerow(['cat', '', '{NTHASH}bVjyDsBbUYvcSXa0LQMi5A==', '6d58f20ec05b518bdc4976b42d0322e4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '"AdministratorsUserstg"']) 
  writer.writerow(['pikachu', 5, 60])
  writer.writerow(['"Squirtle"', 3, 50])


with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
