import csv
from code.base import update_task_task, TUPLE_INDEX_TASK


def export_tasks_to_csv(filename, tasks):
    with open(filename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in tasks:
            spamwriter.writerow(update_task_task(row, row[TUPLE_INDEX_TASK].encode("utf8")))