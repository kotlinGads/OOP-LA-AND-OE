print("LA14")

class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"{self.name}, {self.age}")
        
class Tobey(Spiderman):
      def __init__(self, name, age, movieTitle):
             super().__init__(name, age)
             self.movieTitle = movieTitle
        
class Andrew(Spiderman):
      def __init__(self, name, age, movieTitle):
             super().__init__(name, age)
             self.movieTitle = movieTitle
        
class Tom(Spiderman):
      def __init__(self, name, age, movieTitle):
             super().__init__(name, age)
             self.movieTitle = movieTitle

Tobey = Tobey("Tobey", 33, "Spiderman")

Andrew = Andrew("Andew", 33, "The amazing spiderman")

Tom = Tom("Tom", 33, "Homecoming")

print(f" name: {Tobey.name.upper()},  Movie: {Tobey.movieTitle}")
print(f" name: {Andrew.name.upper()},  Movie: {Andrew.movieTitle}")
print(f" name: {Tom.name.upper()},  Movie: {Tom.movieTitle}")