class Author:
    def __init__(self, name):
        self.name = name
        self.books = []#books as an array
        #alternately, can do the following
        #self.books =set()  #books as a set, where duplicates are not allowed

    def __str__(self):
        titles = ', '.join(self.books) or 'no books'
        return f'{self.name} has published {titles}.'

    def publish(self,title):
        if title in self.books: # to avoid duplicates, check if title already in self.books aray
            print('That book is already linked to the author')
        else:
            self.books.append(title) #- use this if books is a list[]
            #self.books.add(title)  #use this if books is a set(); title will not be added to set if it is already in set

def main():
    christie = Author('Agatha Christie')
    christie.publish('Death on the Nile')
    christie.publish('The Murder of Roger Ackroyd')
    christie.publish('The ABC Murders')
    christie.publish('Death on the Nile') #need to avoid publishing this one
    print(christie) #print the object using the __str__  method

    tempas = Author('Sierra Tempas')
    print(tempas)

main()  #call main fx

#alt idea - change book list to a set, which doesn't allow duplicates