
cdef (list,list) get_books_from_library(list chosen_books, object library, list all_books,int scan_time):
  
  #Get the list of the books which correpond to the selected library
  cdef books_list, chosen_books_from_library
  cdef int j, i,books_taken

  books_list = list()
  chosen_books_from_library = list()

  for book in library.books: #Create the corresponding book list
    books_list.append([book,all_books[book]]) 
  
  books_list = SORT(books_list)
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

  return chosen_books_from_library, chosen_books

cdef list SORT(list list_):
    list_ = sorted(list_,key = lambda x:x[1],reverse = True)
    return list_


##########################################################################################################################
##########################################################################################################################
cdef list library_solving(list libraries_list,int D, list all_books):

  cdef list chosen_librairies, chosen_books
  cdef int sum_days,j,scan_time

  libraries_list =  sort_lib(libraries_list)
  
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
      chosen_libraries.append([libraries_list[j].id,books_list])
      sum_days+=libraries_list[j].signup_time
      j += 1
 
    else: #We can't choose a new library 
      sum_days = D

  return chosen_libraries


cdef list sort_lib(list list_):
    list_ = sorted(list_,key = lambda x:x.factor,reverse = True)
    return list_
