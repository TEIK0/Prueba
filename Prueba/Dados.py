class Dados:
    def __init__(self, D1 , D2, D3):
        self.D1= D1
        self.D2= D2
        self.D3= D3
        self.contador = 0
        

    def proceso(self):
        if self.D1 == self.D2 and self.D1 == self.D3:
            return self.D1 * 3
        elif self.D1 != self.D2 and self.D1 == self.D3:

            return self.D1 * 2
        
        elif self.D1 != self.D3 and self.D1 == self.D2:

            return self.D1 * 2
            
        elif self.D2 != self.D1 and self.D2 == self.D3:

            return self.D2*2
            
        else:
            if self.D1 > self.D2 and self.D1 > self.D3:
                return self.D1
            elif self.D2 > self.D3 and self.D2 > self.D1:
                return self.D2
            else:
                return self.D3

L = []

for i in range(3):

    num = i+1

    x = 0

    while x < 1 or x > 6:
        x = int(input("Ingrese valor de dado numero "+str(num)+":"))

        if x < 1 or x > 6:
            print("Debe ingresar un valor entre 1 y 6")

    L.append(x)

D = Dados(L[0],L[1],L[2])

Resultado = D.proceso()

print("El resultado es: "+str(Resultado))

