from datetime import datetime
import os
import csv
HEADERS = ['ORDER_ID','ORDER_NUMBER']
with open('all-mm-orders.csv','r') as openFile:
    with open(str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '_mlogistics_' + '.csv','w', newline='') as csvFile:
        writer = csv.writer(csvFile, quotechar="'")#quotechar required for "" in columns (M)
        writer.writerow(HEADERS)
        seen = set()
        for line in openFile:
            if line in seen:
                csvFile.write(line)
                print(line)
            seen.add(line)
openFile.close()
csvFile.close()
