class myComplex(complex):
    def __mod__(self, other):
        return myComplex(self.real % other.real, self.imag % other.imag)

    def __floordiv__(self, other):
        return myComplex(self.real // other.real, self.imag // other.imag)


print(myComplex(10, 10) % (7 + 6j))
print(myComplex(10, 10) // (7 + 6j))
