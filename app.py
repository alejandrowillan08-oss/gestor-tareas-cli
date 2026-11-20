tareas = []


def completar_tarea():
    if not tareas:
        print("No hay tareas para completar.")
        return
    indice = int(input("Numero de tarea a completar: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Numero de tarea invalido.")


def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    indice = int(input("Numero de tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        eliminada = tareas.pop(indice)
        print(f"Tarea '{eliminada['titulo']}' eliminada.")
    else:
        print("Numero de tarea invalido.")


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
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        else:
            print(f"Opcion '{opcion}' aun no implementada.")


if __name__ == "__main__":
    main()
