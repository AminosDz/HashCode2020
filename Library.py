class Library:
    def __init__(self,nb_books,signup_time,speed,books,all_books):
        self.nb_books = nb_books
        self.signup_time = signup_time
        self.speed = speed
        self.books = books
        self.awards_sum = sum([all_books[i] for i in books])
        self.factor = 