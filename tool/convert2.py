import pdfplumber
import csv
import re

with open('data_temp.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile)
    with pdfplumber.open("full2.pdf") as pdf:
        for idx, page in enumerate(pdf.pages):
            page = page.extract_table()
            print('page: ',idx)
            content = page
            for row in content:
                # print(row[2])
                if row[0]=='STT':
                    continue
                dataWriter.writerow([row[1].split('\n')[0], row[3], re.sub("\n",' ',(row[4]+':'+row[2]))])