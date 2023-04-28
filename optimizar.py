class ClaseOptimizar:
    array=[]
    def ArrNumeros(self):
        return self.array
    def inpu(self):
        return input("Introduzca un numero: ")
    def add(self, n):
        self.array.append(n)
    def media(self):
        suma = 0
        for n in self.array:
            suma += n
            media = suma/len(self.array)
        return media
