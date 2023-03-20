from Obj.Ahorcado import Ahorcado



class AhorcadoServicio:
    objeto = Ahorcado()
    def inicializar_parametros(self, objeto, palabra):
        if isinstance(objeto, Ahorcado):
            objeto.set_palabra(palabra)
            objeto.inicializar_ahorcado()

    def iniciar_juego(self, objeto, letra):
        if isinstance(objeto, Ahorcado):
                objeto.set_letra(letra)
                if letra in objeto.get_palabra():
                    objeto.llenar()
                else:
                    objeto.no_adivina()
                objeto.gano()

