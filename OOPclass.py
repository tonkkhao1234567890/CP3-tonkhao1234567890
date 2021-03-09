class Customer:
    name = ""
    lastname = ""
    age = 23

    Fathername = ""
    Fatherlastname = ""
    Father_ages = 47

    Friendname = ""
    Friendlastname = ""
    Friend_ages = 30

    def addCart(self):
        print("Added Product to",self.name,self.lastname,"'s cart. Ages: ",self.age)
        print("Added Product to",self.Fathername,self.Fatherlastname,"'s cart. Ages: ",self.Father_ages)
        print("Added Product to",self.Friendname,self.Friendlastname,"'s cart. Ages: ",self.Friend_ages)

customer1 = Customer()
customer1.name = "Kittikorn"
customer1.lastname = "P"
customer1.age = 30
customer1.Fathername = "Jeehoy"
customer1.Fatherlastname = "Peesadert"
customer1.age = 46
customer1.Friendname = "John"
customer1.Friendlastname = "ชาวไร่"
customer1.Friend_ages = 27
customer1.addCart()
