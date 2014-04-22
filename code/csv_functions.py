import csv


def export_tasks_to_csv(filename, tasks):
    with open(filename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in tasks:
            spamwriter.writerow(row)