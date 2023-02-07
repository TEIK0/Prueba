

A = []

i = int(input("Ingrese numero de valores que tendra el arreglo: "))

for x in range(i):

    valor = int(input("Ingrese valor "+str(x)+" del arreglo:"))

    A.append(valor)

Negativos = 0

Positivos = 0

Zero = 0

for x in range(i):

    if A[x] < 0:
        Negativos = Negativos + 1
    elif A[x] > 0:
        Positivos = Positivos + 1
    else:
        Zero = Zero + 1

RN = Negativos / i
RS = Positivos / i
RZ = Zero / i

A = str(RS)+"/1"
B = str(RN)+"/1"
C = str(RZ)+"/1"

Result = {

    'Positive': A,
    'Negative': B,
    'Zero': C

}

print(Result)
