from Library import Library
import string

def read_file(path):
    f = open(path,"r")
    lines = f.readlines()
    nb_books,nb_lib,nb_days = map(int,lines[0].replace("\n","").split(" "))
    all_books = list(map(int,lines[1].split(" ")))
    i = 2
    id = 0
    libs = []
    while (i<len(lines)-1):
        nb_book_lib, signup_time, speed = map(int,lines[i].split(" ")[0:3])
        books_lib = list(map(int,lines[i+1].split(" ")))
        library = Library(id,nb_book_lib,signup_time,speed,books_lib,all_books)
        libs.append(library)
        i += 2
        id += 1

    repet_all_books = []
    all_repet = 0
    for i, book in enumerate(all_books):
        counter = 0
        for j, lib in enumerate(libs):
            if i in lib.books:
                counter +=1
                all_repet += 1
        
        repet_all_books.append(counter)
    for i, book in enumerate(all_books):
        repet_all_books[i] /= all_repet
    
    print("Calc Freq")
    for j, lib in enumerate(libs):
        sum_freq = 0
        for book in lib.books:
            sum_freq += all_books[book] / repet_all_books[book]
        lib.factor = (sum_freq * lib.speed) / lib.signup_time


    print("Finished Reading")
    return nb_days,all_books,libs

def write_output(path,libs):
    f = open(path,"w")
    nb_libs = len(libs)
    f.write(str(nb_libs) + "\n")
    for i,element in enumerate(libs):
        id_lib = element[0]
        nb_books = len(element[1])
        if nb_books >0:
            f.write(str(id_lib) + " " + str(nb_books)+"\n")
            for i in range(len(element[1])):
                f.write(str(element[1][i]) + " ")
            f.write("\n")
    
