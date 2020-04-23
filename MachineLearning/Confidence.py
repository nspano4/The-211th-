import csv

with open('testData.csv', 'r') as test:
    with open('results.csv', 'w') as results:
        with open('test1.csv', 'r') as test1:
            reader = csv.reader(test)
            writer = csv.writer(results)
            reader1 = csv.reader(test1)

            writer.writerow(next(reader) + ['WARNING'])
            next(reader1)

            for row in reader:
                predicted_val = row[1]
                for row1 in reader1:
                    exact = row1[1]
                    highG = float(exact) * 1.05
                    lowG = float(exact) * .95

                    highY = float(exact) * 1.15
                    lowY = float(exact) * .85

                    if lowG <= float(predicted_val) <= highG:
                        message = 'GREEN'
                    elif lowY <= float(predicted_val) <= highY:
                        message = 'YELLOW'
                    else:
                        message = 'RED'
                    writer.writerow(row + [message])
                    break
