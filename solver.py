from Library import Library
from random import randint

def get_books_from_library(chosen_books, library, all_books,scan_time):
  
  #Get the list of the books which correpond to the selected library
  books_list = list()
  for book in library.books: #Create the corresponding book list
    books_list.append([book,all_books[book]]) 
  
  books_list = sorted(books_list,key = lambda x:x[1],reverse = True)
  
  chosen_books_from_library = list()
  j = 0
  for i in range(scan_time):
    books_taken = 0
    while books_taken <= library.speed and j < len(books_list): 
        if books_list[j][0] not in chosen_books:
            chosen_books.append(books_list[j][0])
            chosen_books_from_library.append(books_list[j][0])
            books_taken += 1
        j+=1
    if (j>=len(books_list)):
        break

  return chosen_books_from_library,chosen_books

def library_solving(libraries_list,D,all_books):

  libraries_list = sorted(libraries_list,key=lambda x:x.factor,reverse=True)
  
  chosen_libraries = list()
  chosen_books = list()
  sum_days = 0
  j = 0
  while (sum_days < D) and (j < len(libraries_list)) :
    #Add the library to 
    while j < len(libraries_list):
      if (sum_days + libraries_list[j].signup_time) <= D:
         
        break
      else:
        j+=1
    
    if j != len(libraries_list): #A library was selected 
      #Choose the list of the books of the library 
      scan_time = D - (sum_days + libraries_list[j].signup_time)
      books_list,chosen_books = get_books_from_library(chosen_books,libraries_list[j],all_books,scan_time)
      if (len(books_list)!=0):
        chosen_libraries.append([libraries_list[j].id,books_list])
        sum_days+=libraries_list[j].signup_time
      j += 1
 
    else: #We can't choose a new library 
      sum_days = D

  return chosen_libraries

def grasp(libraries_list,D,all_books,x):

  libraries_list = sorted(libraries_list,key=lambda x:x.factor,reverse=True)
  
  chosen_libraries = list()
  chosen_books = list()
  sum_days = 0
  j = 0
  while (sum_days < D) and len(libraries_list)!=0 :
    if (len(libraries_list)>x):
      j = randint(0,x)
    else:
      j = randint(0,len(libraries_list)-1)  
    
    if (sum_days + libraries_list[j].signup_time) <= D: #A library was selected 
      #Choose the list of the books of the library 
      scan_time = D - (sum_days + libraries_list[j].signup_time)
      books_list,chosen_books = get_books_from_library(chosen_books,libraries_list[j],all_books,scan_time)
      chosen_libraries.append([libraries_list[j].id,books_list])
      sum_days+=libraries_list[j].signup_time
    del libraries_list[j]

  return chosen_libraries




