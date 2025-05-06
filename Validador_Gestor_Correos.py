class Correo:
    # Método constructor
    def __init__(self):
        self.correosEstudiantes = [] 
        self.correosProfesores = []
        self.todosLosCorreos = {
            "Estudiante": self.correosEstudiantes,
            "Profesor": self.correosProfesores
        }

    #Guardar correo electronico
    def AgregarCorreo(self, Correo1):
            # Verificar si ya existe en cualquiera de las listas
            if Correo1 in self.correosEstudiantes or Correo1 in self.correosProfesores: # Verifica si ya existe en cualquiera de las listas
                print("\n Este correo ya ha sido registrado. Intente con uno diferente.")
                return #Salir del metodo si este correo ya ha sido registrado 
            # Validamos el dominio y agregar 
            if Correo1.endswith("@estudiante.utv.edu.co"):
                self.correosEstudiantes.append(Correo1)
                self.todosLosCorreos[Correo1] = "Estudiante"
                print(f"\n Correo de estudiante agregado correctamente: '{Correo1}'")

            elif Correo1.endswith("@utv.edu.co"):
                self.correosProfesores.append(Correo1)
                self.todosLosCorreos[Correo1] = "Profesor"
                print(f"\n Correo de profesor agregado correctamente: '{Correo1}'")
        
            else:
                print("\n Dominio no válido. Solo se aceptan correos institucionales.\n"
                    "Intente nuevamente.")

    #Ver todos los correos guardados
    def VerCorreos(self):
        if self.correosEstudiantes:
            print("Lista de correos de Estudiantes: ")
            for c in self.correosEstudiantes: #recorre la lista de estudiante
                print("-", c) #imprime cada valor recopilado en la variable c
        else:
            print("No existe correos de estudiantes")
        if self.correosProfesores:
            print("Lista de correos de Profesores:")
            for c in self.correosProfesores: #recorre la lista de profesores
                print("-", c) #imprime cada valor recopilado en la variable c
        else:
            print("No existe correos de profesores")

    #Buscar coincidencias
    def BuscarCorreo(self, buscado):
        print("Buscando...")
        correoencontrado = [] #instanciamos la lista
        for lista in [self.correosEstudiantes, self.correosProfesores]:
            for c in lista:            
                if buscado.lower() in c.lower(): #busca el valor ingresado en la variable c que contiene los correos sin importar mayusculas
                    correoencontrado.append(c) #agrega el correo a la lista correoencontrado

        if correoencontrado: #si la lista correoencontrado tiene elementos 
            print(f"Coincendias encontradas con:  '{buscado}'") 
            for a in correoencontrado: #recorre cada elemento en la lista correoencontrado y lo asigna a la variable a 
                print("-", a) #imprime los correo que coincides
        
        else: 
                print(f"No existe coincidencias con:  '{buscado}'") # si la liesta esta vacia se imprime este mensaje 
#Metodo para visualizar el menu        
def MostrarMenu(): 
    print("\n --- Menu: ---")
    print("1. Registrar un nuevo correo electrónico")
    print("2. Ver correos registrados")
    print("3. Buscar un correo específico")
    print("4. Salir de la aplicación")

def main():
    #Crear la instancia del objeto
    nuevocorreo = Correo()
    #Crear bucle para el menu principal
    while True:
        MostrarMenu()
        opcion = input("Seleccione Opción: ") #Ingresa la a opción
        if opcion == "1":
            print("\n ¡Recuerde!, los correos ingresados deben terminar en @utv.edu.co para los profesores \n y en @estudiante.utv.edu.co para los estudiantes.")
            Correo1 = input("\n Escriba una dirección de correo: ").strip() #Llama el metodo AgregarCorreo y le envia el correo que el usuario ingreso
            nuevocorreo.AgregarCorreo(Correo1)
        elif opcion == "2":
            nuevocorreo.VerCorreos() #Llama el metodo VerCorreo
        elif opcion == "3":
            buscado = input("Ingrese: ") #Ingresa 
            nuevocorreo.BuscarCorreo(buscado) #Llama el metodo BuscarCorreo y le envia lo que el usuario ingreso
        elif opcion == "4":
            print("Saliendo... ")
            break # detiene el bucle de while y sale del programa 
        else:
            print("Opción no valida.Intente de nuevo") #Si no ingresa las opción 1,2,3,4 sale el mensaje

if __name__ == "__main__":
    main()