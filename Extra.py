import csv

with open("books-en.csv") as f:
    books = list(row for row in csv.reader(f, delimiter = ';'))

    all_publishers = set()
    most_popular_books = []
    for row in books[1:]:
        ISBN, Book_Title, Book_Author, Year_Of_Publication, Publisher, Downloads, Price = row
        all_publishers.add(Publisher)
        most_popular_books.append([Book_Title, int(Downloads)])
    print(list(all_publishers))
    for i in sorted(most_popular_books, key=lambda f: f[1], reverse=True)[:20]:
        print(i[0])
