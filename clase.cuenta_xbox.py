class cuenta_xbox:
    def __init__(self, __gamertag, __juegos, __imagen):
        self.__gamertag = __gamertag
        self.__juegos = __juegos
        self.__imagen = __imagen
        
    def get_gamertag(self):
        print(self.__gamertag)
    
    def set_gamertag(self, gamertag):
        self.__gamertag = gamertag
        
    def get_juegos(self):
        print(self.__juegos)
        
    def set_juegos(self, juegos):
        self.__juegos = juegos
        
    def get_imagen(self):
        print(self.__imagen)
        
    def set_imagen(self, imagen):
        self.__imagen = imagen    
        
        
cuenta_principal = cuenta_xbox("SPLIT GEARS", "Cuphead", "Mugman")

cuenta_principal.get_gamertag()

cuenta_principal.set_gamertag("Leonex657")
cuenta_principal.get_gamertag()

cuenta_principal.get_juegos()

cuenta_principal.set_juegos("Gears of War")
cuenta_principal.get_juegos()

cuenta_principal.get_imagen()

cuenta_principal.set_imagen("Master chief")
cuenta_principal.get_imagen()