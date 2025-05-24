class cuenta_xbox:
    # Atributos estáticos con valores iniciales
    __gamertag = "SPLIT GEARS"
    __juegos = "Cuphead"
    __imagen = "Mugman"

    def get_gamertag(self):
        print(cuenta_xbox.__gamertag)

    def set_gamertag(self, gamertag):
        cuenta_xbox.__gamertag = gamertag

    def get_juegos(self):
        print(cuenta_xbox.__juegos)

    def set_juegos(self, juegos):
        cuenta_xbox.__juegos = juegos

    def get_imagen(self):
        print(cuenta_xbox.__imagen)

    def set_imagen(self, imagen):
        cuenta_xbox.__imagen = imagen    


# Crear una instancia para usar los métodos
cuenta = cuenta_xbox()

# Usar los métodos
cuenta.get_gamertag()

cuenta.set_gamertag("Leonex657")
cuenta.get_gamertag()

cuenta.get_juegos()

cuenta.set_juegos("Gears of War")
cuenta.get_juegos()

cuenta.get_imagen()

cuenta.set_imagen("Master chief")
cuenta.get_imagen()


#El código define una clase cuenta_xbox con atributos estáticos (gamertag, juegos, imagen) que tienen valores iniciales. Usa métodos para mostrar y cambiar esos valores. Aunque los datos son de clase, se necesita una instancia para llamar a los métodos. Así se simula el manejo básico de una cuenta de Xbox.

#Torres Pérez Roberto Angel