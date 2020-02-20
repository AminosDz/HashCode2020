from reader import read_file
from Library import Library

path = "input/a_example.txt"

nb_days,all_books,libs = read_file(path)

print(nb_days,all_books,"\n",libs[0],"\n",libs[1])