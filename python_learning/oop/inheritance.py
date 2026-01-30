"""
# Multilevel inheritance
class A:
    def call(self):
        print("A Called.")

class B(A):
    def callB(self):
        print("B Called.")

class C(B):
    def callC(self):
        print("C Called.")

# I can access both A and B class's functions
def main():
    c = C()
    c.call()
    c.callB()
    c.callC()
"""

"""
# Multiple inheritance
class A:
    def call(self):
        print("A Called.")

class B:
    def call(self):
        print("B Called.")

    def callB(self):
        print("B Called.")

class C(A, B):
    def callC(self):
        print("C Called.")

# I can access both A and B class's functions; Similar functions gets called accrding to MRO (Method Resolution Order)
# Like if class B(A,C) -> so priority to A; B(C, A) -> priority to C;
def main():
    c = C()
    c.call()
    c.callB()
    c.callC()
"""

"""
# Hieraechical Inheritance
class A:
    def call(self):
        print("A Called.")

class B(A):
    def callB(self):
        print("B Called.")

class C(A):
    def callC(self):
        print("C Called.")

def main():
    c = C()
    c.call()
    c.callC()
"""

"""
# Hybrid Inheritance
class A:
    def call(self):
        print("A Called.")

class B(A):
    def call(self):
        print("B Called.")

    def callB(self):
        print("B Called.")

class C(A):
    def call(self):
        print("C Called.")

    def callC(self):
        print("C Called.")

class D(B, C):
    def callD(self):
        print("D Called.")

def main():
    d = D()
    d.call()
    d.callB()
    d.callC()
    d.callD()
"""

# super() -> it is reffered to Base/Parent class
class A:
    def call(self):
        print("A Called.")

class B(A):
    def callB(self):
        # both of these super() and self will call class A's call() function 
        super().call()
        self.call()

        print("B Called.")

def main():
    b = B()
    b.callB()

if __name__ == "__main__":
    main()