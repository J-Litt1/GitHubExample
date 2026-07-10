import csv

try:
    with open("csv_files/user_details.csv") as c:
        csvread = csv.reader(c, delimiter=",")

        new_list = []
        for row in csvread:
            row.remove(row[0])
            row.remove(row[-2])
            new_list.append(row)

        print(new_list)

        c.close()

except FileNotFoundError:
    print("File doesn't exist")

try:
    new_file = open("csv_files/edited_user_details.csv", "a")
    for i in new_list:
        new_file.write(str(i) + "\n")
except NameError:
    print("Can't save list of lists - file doesn't exist")
# remove all titles and genders
# save new data as list
# print new data as list of lists
# bonus - write new l-o-l to new csv file + save. Try + except blocks required