def mostrar_menu():
    print("\n=== GESTOR DE TAREAS CLI ===") 
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "0":
            print("Saliendo...")
            break
        print(f"Opcion '{opcion}' aun no implementada.")


if __name__ == "__main__":
    main()
