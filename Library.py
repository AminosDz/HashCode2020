class Library:
    def __init__(self,id,nb_books,signup_time,speed,books,all_books):
        self.id = id
        self.nb_books = nb_books
        self.signup_time = signup_time
        self.speed = speed
        self.books = books
        self.awards_sum = sum([all_books[i] for i in books])
        self.factor = ( self.awards_sum * self.speed ) / self.signup_time
    

    def __str__(self):
        return "Id " + str(self.id) + " Nb books : " + str(self.nb_books) + " Signup_time : " + str(self.signup_time) + " Speed " + str(self.speed) + " Factor " + str(self.factor) + " Sum : " + str(self.awards_sum) + " Books : " + str(self.books)