import csv

# id - i
# #domain -1
# custom_login -2
# stop -3
# verified_forum_id 8
# activity 11
# inactive_days - 12
# board_id -13
# board_found - 14

data = []
i = 1
with open('forums_old.csv') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        if row[3] == 'false':
            data.append([i, row[1], row[2], row[3], row[8], row[11], row[12], row[13], row[14]])
            i += 1

with open('forums.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        spamwriter.writerow(row)