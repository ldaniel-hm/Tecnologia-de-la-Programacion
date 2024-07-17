class A:
    def imprime(self):
        print("A")

class B1(A):
    # def imprime(self):
    #     print("B1")
    #     super().imprime()
    pass

class B2(A):
    def imprime(self):
        print("B2")
        super().imprime()
    pass

class C(B1, B2):
    def imprime(self):
        print(C.mro())
        print("C")
        super().imprime()

C().imprime()
