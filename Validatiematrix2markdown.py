#!/usr/bin/python3
#
# Auteur: w.quak@geonovum.nl

from datetime import datetime
import openpyxl
import sys


print("## De validatiematrix")
print("")
print("| id | omschrijving|");
print("|:---|:------------|");


wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb['Validatieregels']
for row in sheet.iter_rows():
    if row[1].value == 'Id' :
        continue

    id = str(row[1].value) 
    regel = row[2].value.replace('\n','') 
    print("|" + id + "|" + regel + "|")
