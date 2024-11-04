import csv
from random import randint
import xml.etree.cElementTree as ET



def count_len(length):
    global books
    count = 0
    for i in books:
        if len(i[1]) > length:
            count += 1
    return count

def condition(year):
    if int(year) < 1990:
        return True
    return False

with open("books-en.csv") as f:
    books = list(row for row in csv.reader(f, delimiter = ';'))
    amount_of_rows = len(books)

    print(count_len(30))


    information = dict.fromkeys(['Book-Author'])
    for row in books[1:]:
        ISBN, Book_Title, Book_Author, Year_Of_Publication, Publisher, Downloads, Price = row
        if Book_Author not in information.keys():
            information[Book_Author] = []
        if condition(Year_Of_Publication):
            information[Book_Author].append([ISBN, Book_Title, Year_Of_Publication, Downloads, Price])

    with open("Task_3.txt", 'w') as file:
         for i in range(20):
             line = randint(0, amount_of_rows)
             ISBN, Book_Title, Book_Author, Year_Of_Publication, Publisher, Downloads, Price = books[line]
             file.write("{} {}. {} - {}".format(line, Book_Author, Book_Title, Year_Of_Publication) + "\n")

tree = ET.parse('currency.xml')
root = tree.getroot()
names = []
for valutes in root.findall('Valute'):
    nominal = valutes.find('Nominal').text
    if nominal == '1':
        names.append(valutes.find('Name').text)
print(names)