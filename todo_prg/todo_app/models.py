from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo de usuario de Django

# Create your models here.

class Todo(models.Model):
    # 1. Relación con el Usuario (ForeignKey)
    # Esto conecta cada tarea con un usuario específico.
    # on_delete=models.CASCADE significa que si borras al usuario, se borran todas sus tareas automáticamente.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 2. Nombre de la tarea
    # CharField es para texto. En el video le pone un tamaño máximo de 1000 caracteres.
    # IMPORTANTE: En el video usa el nombre 'todo_name' para este campo.
    todo_name = models.CharField(max_length=1000)

    # 3. Estado de la tarea (Completada o no)
    # BooleanField guarda Verdadero (True) o Falso (False).
    # default=False significa que cuando creas una tarea, por defecto aparece como "no terminada".
    status = models.BooleanField(default=False)

    # 4. Método string
    # Esto define cómo se verá la tarea en el panel de administración.
    # En lugar de decir "Todo object (1)", dirá el nombre de la tarea (ej: "Comprar pan").
    def __str__(self):
        return self.todo_name