import re

class Correo:
    # Método constructor
    def __init__(self):
        self.correosEstudiantes = [] 
        self.correosProfesores = []
        self.todosLosCorreos = {
            "Estudiante": self.correosEstudiantes,
            "Profesor": self.correosProfesores
        }

    # Guardar correo electrónico
    def AgregarCorreo(self, Correo1):
        # Validar estructura del correo
        correo_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(correo_regex, Correo1):
            print("\n El formato del correo no es válido. Intente nuevamente.")
            return    
        
        # Verificar si ya existe en cualquiera de las listas
        if Correo1 in self.correosEstudiantes or Correo1 in self.correosProfesores:
            print("\n Este correo ya ha sido registrado. Intente con uno diferente.")
            return 
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
            print("\n Dominio no válido. Solo se aceptan correos institucionales.\nIntente nuevamente.")

    # Ver todos los correos guardados
    def VerCorreos(self):
        if self.correosEstudiantes:
            print("Lista de correos de Estudiantes:")
            for c in self.correosEstudiantes:
                print("-", c)
        else:
            print("No existe correos de estudiantes.")

        if self.correosProfesores:
            print("Lista de correos de Profesores:")
            for c in self.correosProfesores:
                print("-", c)
        else:
            print("No existe correos de profesores.")

    # Buscar coincidencias
    def BuscarCorreo(self, buscado):
        print("Buscando...")
        correoencontrado = []  # Lista para almacenar tuplas (correo, tipo)

        for c in self.correosEstudiantes:
            if buscado.lower() in c.lower():
                correoencontrado.append((c, "Estudiante"))

        for c in self.correosProfesores:
            if buscado.lower() in c.lower():
                correoencontrado.append((c, "Profesor"))

        if correoencontrado:
            print(f"Coincidencias encontradas con: '{buscado}'")
            for correo, tipo in correoencontrado:
                print(f"- {correo} ({tipo})")
        else:
            print(f"No existen coincidencias con: '{buscado}'")

# Método para visualizar el menú        
def MostrarMenu(): 
    print("\n --- Menú: ---")
    print("1. Registrar un nuevo correo electrónico")
    print("2. Ver correos registrados")
    print("3. Buscar un correo específico")
    print("4. Salir de la aplicación")
    print("Seleccione un opción valida del 1 al 4")

def main():
    # Crear la instancia del objeto
    nuevocorreo = Correo()
    # Bucle para el menú principal
    while True:
        MostrarMenu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n ¡Recuerde! Los correos deben terminar en @utv.edu.co para profesores \n y en @estudiante.utv.edu.co para estudiantes.")
            Correo1 = input("\n Escriba una dirección de correo: ").strip()
            nuevocorreo.AgregarCorreo(Correo1)

        elif opcion == "2":
            nuevocorreo.VerCorreos()

        elif opcion == "3":
            buscado = input("Ingrese parte o la totalidad del correo a buscar: ").strip()
            nuevocorreo.BuscarCorreo(buscado)

        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()