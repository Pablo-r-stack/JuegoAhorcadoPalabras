import re
class Ahorcado:
    def __init__(self):
        self.__palabra = ""
        self.__intentos = 10
        self.__ahorcado = []
        self.__letra = ""
        self.__check = False


    def get_palabra(self):
        return self.__palabra

    def get_intentos(self):
        return self.__intentos

    def get_ahorcado(self):
        return self.__ahorcado

    def get_letra(self):
        return self.__letra

    def get_check(self):
        return self.__check


    def set_palabra(self, palabra):
        self.__palabra = palabra

    def set_letra(self, letra):
        self.__letra = letra


    def inicializar_ahorcado(self):
        for i in range(len(self.__palabra)):
            self.__ahorcado.append("-")

    def mostrar_ahorcado(self):
        for i in self.__ahorcado:
            print(f"{i} ", end="")

    def llenar(self):
        for i in range(len(self.__palabra)):
            if self.__palabra[i] == self.__letra:
                self.__ahorcado[i] = self.__letra

    def gano(self):
        if re.match(''.join(self.__ahorcado), self.__palabra):
            self.__check = True
            return self.__check

    def no_adivina(self):
        self.__intentos -= 1


