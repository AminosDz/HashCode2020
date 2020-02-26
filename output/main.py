from reader import read_file,write_output
from Library import Library
from solver import library_solving,grasp

input_path = "input/f_libraries_of_the_world.txt"
output_path = "output/f_libraries_of_the_world.out"

nb_days,all_books,libs = read_file(input_path)



for x in [5,10,30,50]:
    chosen_libs = grasp(libs,nb_days,all_books,x)
    write_output(output_path + str(x),chosen_libs)