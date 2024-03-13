class Degree:
    def get_degree(self):
        print("I got a degree")

class Undergraduate(Degree):
    def get_degree(self):
        print("I am an Undergraduate")

class Postgraduate(Degree):
    def get_degree(self):
        print("I am a Postgraduate")

# Create objects of each class and call the method
degree_holder = Degree()
degree_holder.get_degree()

undergrad = Undergraduate()
undergrad.get_degree()

postgrad = Postgraduate()
postgrad.get_degree()
