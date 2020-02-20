
def get_books_from_library(chosen_books, library, all_books):
  
  #Get the list of the books which correpond to the selected library
  books_list = list()
  for book in library.books: #Create the corresponding book list
    books_list.append([book,all_books[book]]) 
  
  books_list = sorted(books_list,key = lambda x:x[1],reverse = True)
  
  chosen_books_from_library = list()
  j = 0
  while ( j < len(books_list)) and (len(chosen_books_from_library) < library.speed):
    if books_list[j][0] not in chosen_books:
       chosen_books_from_library.append(books_list[j])
    j+=1

  return 0

def library_solving(libraries_list,D,all_books):

  libraries_list = sorted(libraries_list,key=lambda x:x.factor,reverse=True)
  
  chosen_libraries = list()
  chosen_books = list()
  sum_days = 0
  while sum_days < D:
    #Add the library to 
    j = 0
    while j <  len(libraries_list):
      if (sum_days + libraries_list[j].signup_time) <= D:
        break
      else:
        j+=1
    
    if j != len(libraries_list): #A library was selected 
      #Choose the list of the books of the library 
      books_list = get_books_from_library(libraries_list[j],chosen_books,all_books)
     
    else: #We can't choose a new library 
      sum_days = D
     

  return 




