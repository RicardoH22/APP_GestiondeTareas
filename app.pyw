import customtkinter as ctk 

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("375x667")  # Tamaño típico de móvil

        # Configuración del grid
        self.root.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 se ajuste al ancho
        self.root.grid_rowconfigure(2, weight=1)  # Hacer que la fila 2 (lista de tareas) se ajuste al alto

        # Lista para almacenar tareas
        self.tasks = []

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Entrada para agregar tareas
        self.entry_task = ctk.CTkEntry(self.root, placeholder_text="Nueva tarea")
        self.entry_task.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Botón para agregar tarea
        self.button_add = ctk.CTkButton(self.root, text="Agregar Tarea", command=self.add_task)
        self.button_add.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Lista de tareas (con scroll)
        self.task_frame = ctk.CTkFrame(self.root)
        self.task_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Entrada para buscar tareas
        self.entry_search = ctk.CTkEntry(self.root, placeholder_text="Buscar tarea")
        self.entry_search.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        # Botón para buscar tarea
        self.button_search = ctk.CTkButton(self.root, text="Buscar Tarea", command=self.search_task)
        self.button_search.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        # Etiqueta para mostrar mensajes
        self.message_label = ctk.CTkLabel(self.root, text="", fg_color="lightgray", corner_radius=6, text_color="black")
        self.message_label.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    def add_task(self):
        """Agregar una nueva tarea."""
        task = self.entry_task.get().strip()
        if task:
            self.tasks.append(task)
            self.entry_task.delete(0, "end")
            self.update_task_list()
            self.show_message("Tarea agregada exitosamente.", "green")
        else:
            self.show_message("Por favor, escribe una tarea.", "red")

    def remove_task(self, task):
        """Eliminar una tarea específica."""
        if task in self.tasks:
            self.tasks.remove(task)
            self.update_task_list()
            self.show_message("Tarea eliminada correctamente.", "green")
        else:
            self.show_message("La tarea no se pudo eliminar.", "red")

    def search_task(self):
        """Buscar y resaltar tareas que coincidan con el texto ingresado."""
        query = self.entry_search.get().strip().lower()
        if query:
            found_tasks = [task for task in self.tasks if query in task.lower()]
            if found_tasks:
                self.show_message(f"Se encontraron coincidencias: {', '.join(found_tasks)}", "green")
            else:
                self.show_message("No se encontró ninguna tarea con ese término.", "red")
        else:
            self.show_message("Por favor, escribe un término para buscar.", "red")

    def update_task_list(self):
        """Actualizar la lista de tareas en el frame."""
        # Limpiar el frame
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Crear una nueva lista de tareas con botones de eliminar
        for task in self.tasks:
            task_row = ctk.CTkFrame(self.task_frame)
            task_row.pack(fill="x", pady=5)

            task_label = ctk.CTkLabel(task_row, text=task, anchor="w")
            task_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            button_remove = ctk.CTkButton(task_row, text="Eliminar", command=lambda t=task: self.remove_task(t))
            button_remove.pack(side="right", padx=10)

    def show_message(self, message, color):
        """Mostrar un mensaje en la etiqueta."""
        self.message_label.configure(text=message, text_color=color)


# Inicializar la aplicación
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Opciones: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Tema por defecto
    root = ctk.CTk()
    app = TaskManagerApp(root)
    root.mainloop()
