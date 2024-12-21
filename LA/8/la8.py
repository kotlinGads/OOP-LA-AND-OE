print("LA #8")
class book:
    def __init__(self, title , author):
        self.title = title
        self.author = author
libro = book("kwentong daniel", "daniel")
libro1 = book("kwentong aron", "aron")
print(f"{libro.title}, {libro.author}")
del libro.author
#print(f"{libro.title}, {libro.author}")
print(f"{libro1.title}, {libro1.author}")