class Canli:
    degisken = "degisken"
    def __init__(self):
        self._name = "Canli"
        print("Constructor Canli")

    def writemyname(self):
        print(self._name)
        print(self.degisken)

    def changemyname(self, newname):
        self._name = newname


a = Canli()
a.writemyname()
a.changemyname("Serkan")
a.writemyname()
print("a._name", a._name)
print("a.degisken", a.degisken)
