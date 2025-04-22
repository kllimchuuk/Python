#import os

#print(os.getcwd())



#os.chdir('C:\\Python33')

#print(os.getcwd())

#import os
#print(os.getcwd())
#C:listdir()
#['DLLs',
# 'Doc',
#'include',
#'Lib',
#'libs',
#'LICENSE.txt',
#'NEWS.txt',
#'python.exe',
#'pythonw.exe',
#'README.txt',
#'Scripts',
#'tcl',
#'Tools']

#os.mkdir("test")
#os.listdir()
#["test"]

#os.listdir()
#['test']

#os.rename('test', "new_one")

#os.listdir()
#['new_one']

#os.remove("myfile.txt")

#os.rmdir("mydir")

#shutil.rmtree("mydir")

#import csv
#
#with open('people.csv', 'r') as file:
#    reader = csv.reader(file)

#    for row in reader:
#        print(row)


#with open('protagonist.csv', 'w', newline='') as file:
#   writer = csv.writer(file)
#    writer.writerow(["SN", "Movie", "Protagonist"])
#    writer.writerow([1, "Low of the Rings", "Frodo Baggins"])
#    writer.writerow([2, "Harry Potter", "Harry Potter"])#
#    import pandas as pd
#    pd.read_csv("people.csv")


import pandas as pd

#df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])
#df.to_csv('person.csv')

import csv

#with open('innovators.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(row)


#with open('people.csv', 'r') as csvfile:
 #   reader = csv.reader(csvfile, skipinitialspace=True)
 #   for row in reader:
 #       print(row)


#with open('person.csv', 'r') as file:
#    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
#    for row in reader:
#        print(row)


#import csv
#with open('innovators.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(["SN", "Name", "Contribution"])
#    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
#    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
#    writer.writerow([3, "Guido van Rossum", "Python Programming"])


