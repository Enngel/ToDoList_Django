# ToDoList Django

Gestor de listas de tareas desarrollado con Django y Django REST Framework.

## Características
- Gestión de múltiples listas de tareas.
- Operaciones CRUD completas para listas y tareas.
- API RESTful con endpoints claros.
- Interfaz moderna y responsive (Premium UI).
- Eliminación en cascada (al eliminar una lista se eliminan sus tareas).

## Requisitos
- Python 3.x
- Django 5.x
- Django REST Framework

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Enngel/ToDoList_Django.git
   cd ToDoList_Django
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Realizar migraciones:
   ```bash
   python manage.py makemigrations todo_app
   python manage.py migrate
   ```

4. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

5. Acceder a la aplicación:
   - UI Dashboard: `http://127.0.0.1:8000/app/`
   - API Root: `http://127.0.0.1:8000/lists/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Endpoints API

### Listas
- `GET /lists/`: Obtener todas las listas.
- `POST /lists/`: Crear una nueva lista.
- `DELETE /lists/<list_id>/`: Eliminar una lista.

### Tareas
- `GET /lists/<list_id>/tasks/`: Obtener tareas de una lista.
- `POST /lists/<list_id>/tasks/`: Añadir tarea a una lista.
- `PATCH /lists/<list_id>/tasks/<task_id>/`: Actualizar estado de una tarea.
- `DELETE /lists/<list_id>/tasks/<task_id>/`: Eliminar una tarea.
