import pickle
class archivoBinario:

    def guardarArchivo(self, archivo, lista):
        file = open(archivo, "wb")
        pickle.dump(lista, file)
        file.close()
        del (file)

    def abrirArchivo(self, archivo):
        file = open(archivo, "rb")
        lista = pickle.load(file)
        file.close()
        del (file)
        return lista

def main():
    nombres = ["Eduardo", "Jesus", "Pedro", "Pablo"]
    archivo_binario = archivoBinario()
    archivo_binario.guardarArchivo("Codigo_binario", nombres)
    mostrar = archivo_binario.abrirArchivo("Codigo_binario")
    print (mostrar)

if __name__ == "__main__":
    main()