import pdfplumber
from parse import split_data
import csv
import re

with open('data_temp.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile)
    with pdfplumber.open("full-1-100.pdf") as pdf:
        for idx, page in enumerate(pdf.pages):
            page = page.extract_table()
            print('-----')
            content = page[1]
            TNXDateCol = content[0]
            TNXDateCol = TNXDateCol.split('\n')
        
            creditCol = content[2]
            creditCol = creditCol.split('\n')
        
            detailsCol = content[4]
            detailsCol = split_data(detailsCol)
            # print("--date--")
            # print (TNXDateCol)
            # print("--credit--")
            # print (creditCol)
            # print("--detail--")
            # print (detailsCol)
            # print('---validate--')
            print(idx, len(TNXDateCol),len(creditCol),len(detailsCol))
            if len(creditCol) == len(detailsCol):
                # result.append(detailsCol)
                for index, item in enumerate(detailsCol):
                    # f.write(TNXDateCol[index*2] + ';' + creditCol[index] + ';' + item + '\n')
                    dataWriter.writerow([TNXDateCol[index*2], creditCol[index], re.sub("\n",' ',item)])
            else:
                print('---error--- ',idx)
                # print( content[4])