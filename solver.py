
def get_books_from_library(chosen_book,library,all_books):
  
  #Get the list of the books which correpond to the selected library
  
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




