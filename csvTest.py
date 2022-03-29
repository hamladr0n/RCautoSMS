# import csv
# with open('AutomatedTexts.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

import csv

with open('AutomatedTexts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}') #Headers
            line_count += 1
        else:
            #Printing data within message
            print('Hi ' + f'{row[0]} this is Corbin from Jobot. I cam agross your profile for the {row[4]} role in {row[5]} that i have posted. Are you still open to oportunities? If so when do you have a few minutes to hop on a call call to tell you more about it')
            line_count += 1
    print(f'Processed {line_count} lines.')