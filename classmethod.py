class laptop():
    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price=35

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

    @classmethod
    def changechargertype(cls):
        cls.chargertype="b-type"
        print("charger type change to b-type")
    @staticmethod
    def info():
        print("laptop")

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype()
hp.info()