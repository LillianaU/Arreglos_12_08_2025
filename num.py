import numpy as np # np es un alias para recortar el nombre de numpy
vector = np.array([1, 2, 3, 4, 5]) # Creamos un vector de numpy
print(vector) # Imprimimos el vector
# quiero imprimir el tercer elemento del vector
print(vector[2]) # Imprimimos el tercer elemento del vector (índice 2)
""" los vectores no son como las listas, no tienen un método append() para agregar elementos 
y no tienen un método pop() para eliminar elementos, pero sí tienen un método reshape() para cambiar su forma , adicionalmente despues de creado no se puede cambiar el tamaño del vector """
vector1 =np.zeros(5) # Creamos un vector de ceros de tamaño 5
print(vector1) # Imprimimos el vector de ceros  
vector2 = np.ones(5) # Creamos un vector de unos de tamaño 5
print(vector2) # Imprimimos el vector de unos
vector3 = np.arange(1,10) # Creamos un vector derango de 1 al 10
print("rango",vector3) # Imprimimos el vector de números rango
vector4 = np.linspace(1, 10, 5) # Creamos un vector de 5 números entre 1 y 10
print("linspace",vector4) # Imprimimos el vector de números linspace    
vector5 = np.random.rand(10) # Creamos un vector de 5 números aleatorios entre 0 y 10
print("random",vector5) # Imprimimos el vector de números aleatorios
vector6= np.random.randint(1,10,10) # Creamos un vector de 5 números aleatorios entre 0 y 10
print("randint",vector6) # Imprimimos el vector de números aleatorios
# Creamos un vector de 5 números aleatorios entre 0 y 10