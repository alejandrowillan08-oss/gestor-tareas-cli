tareas = []


def agregar_tarea():
    titulo = input("Escribe el titulo de la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "[X]" if tarea["completada"] else "[ ]"
        print(f"{i}. {estado} {tarea['titulo']}")


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
        elif opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        else:
            print(f"Opcion '{opcion}' aun no implementada.")


if __name__ == "__main__":
    main()
