from Library import Library

def read_file(path):
    f = open(path,"r")
    lines = f.readlines()
    nb_books,nb_lib,nb_days = map(int,lines[0].split(" "))
    all_books = list(map(int,lines[1].split(" ")))
    i = 2
    id = 0
    libs = []
    while (i<len(lines)):
        nb_book_lib, signup_time, speed = map(int,lines[i].split(" "))
        books_lib = list(map(int,lines[i+1].split(" ")))
        library = Library(id,nb_book_lib,signup_time,speed,books_lib,all_books)
        libs.append(library)
        i += 2
        id += 1
    
    return nb_days,all_books,libs

def write_output(path):
    f = open(path,"w")
    