    # EXAMEN--HERRERA GOMEZ LUIS ALBERTO-1207--
    # clase
class pantalones1207:
    # atributos
    talla = 0
    marca = ""
    distribuidor = ""
    estilo = ""
    modelo = 0
    color = ""
    tela = ""

    # mostrar datos
    def mostrar_datos1207(self):
        print(f"Talla: {self.talla}")
        print(f"Marca: {self.marca}")
        print(f"Distribuidor: {self.distribuidor}")
        print(f"Estilo: {self.estilo}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Tela: {self.tela}")

    # listar
    def Lista_pantalones1207(self):
        lista_pantalon1207 = [
            "Slim", 
            "Cropped", 
            "Recto", 
            "Wide leg", 
            "Relaxed"
        ]
        for x in lista_pantalon1207:
            print(x)
        return lista_pantalon1207

    # tupla
    def Tupla_pantalon1207(self):
        tupla_pantalones1207 = (
            "Pantalon / Niños", 
            "Pantalon / Adolecentes", 
            "Pantalon / Adultos", 
            "Pantalon / Hombre", 
            "Pantalon / Mujer"
        )
        for x in tupla_pantalones1207:
            print(x)
        return tupla_pantalones1207

    # diccionario
    def Dicionario_pantalon1207(self):
        diccionario_pantalones1207 = {
            "Old money": 15,
            "Street wear": 20,
            "Starboy": 33,
            "Halo": 12,
            "Buchon": 9
        }
        for x, y in diccionario_pantalones1207.items():
            print(x, y)
        return diccionario_pantalones1207

    # ALTA
    def altas1207(self):
        print("La operación de alta se realizó correctamente.")

    # BAJA
    def bajas1207(self):
        print("La operación de baja se realizó correctamente.")

# Creación del objeto
pantalon = pantalones1207()

# Asignación de datos a los atributos
pantalon.talla = 12
pantalon.marca = "Spark"
pantalon.distribuidor = "Chrome Heart"
pantalon.estilo = "Baggy"
pantalon.modelo = 9090
pantalon.color = "Blanco"
pantalon.tela = "Algodon"

# Utilización de los objetos
# Mostrar datos
pantalon.mostrar_datos1207()

# Llamada funciones
print("\nLista de pantalones:")
print(pantalon.Lista_pantalones1207())

print("\nTupla de pantalones:")
print(pantalon.Tupla_pantalon1207())

print("\nDiccionario de pantalones:")
print(pantalon.Dicionario_pantalon1207())

# alta y baja
pantalon.altas1207()
pantalon.bajas1207()