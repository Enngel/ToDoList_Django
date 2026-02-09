from django.shortcuts import render, redirect  # Importamos redirect para movernos entre páginas
from django.contrib.auth.models import User  # Importamos la "tabla" de usuarios
from django.contrib import messages  # Herramienta para enviar alertas
from django.contrib.auth import authenticate, login, logout  # Funciones de sesión
from .models import Todo  # <--- NUEVO: Importamos tu modelo de tareas para usar la BD

# Create your views here.

def home(request):
    # PARTE 1: GUARDAR UNA NUEVA TAREA (Si el método es POST)
    if request.method == 'POST':
        # Capturamos lo que escribió el usuario en el input name="task"
        task_texto = request.POST.get('task')

        # Si el texto no está vacío, guardamos en la base de datos
        if task_texto:
            # Creamos el objeto Todo relacionándolo con el usuario actual (request.user)
            new_todo = Todo(user=request.user, todo_name=task_texto, status=False)
            new_todo.save()  # Guardar en la BD
            messages.success(request, 'Tarea añadida correctamente.')

        # Redirigimos a 'home' para limpiar el formulario y evitar envíos duplicados
        return redirect('home')

    # PARTE 2: MOSTRAR LAS TAREAS (Si el método es GET)
    # Primero verificamos si el usuario está logueado para evitar errores
    if request.user.is_authenticated:
        # Buscamos en la BD solo las tareas que pertenecen a este usuario
        mis_tareas = Todo.objects.filter(user=request.user)
    else:
        # Si no está logueado, lo mandamos al login (o dejamos la lista vacía)
        return redirect('login')

    # Pasamos las tareas al HTML en el diccionario de contexto
    context = {'todos': mis_tareas}
    return render(request, 'todo_app/todo.html', context)


def register(request):
    # Paso 1: Detectar si el usuario le dio al botón "Register Now" (eso envía un POST)
    if request.method == 'POST':
        # Paso 2: Capturar lo que escribieron en el HTML
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Paso 3: Validaciones (Reglas de seguridad)

        # Validar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ese nombre de usuario ya está ocupado.')
            return redirect('register')  # Recargamos la misma página

        # Validar si el email ya existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ese correo ya está registrado.')
            return redirect('register')

        # Validar longitud de contraseña
        if len(password) < 3:
            messages.error(request, 'La contraseña es muy corta (mínimo 3 caracteres).')
            return redirect('register')

        # Paso 4: Si todo está bien, CREAR el usuario
        my_user = User.objects.create_user(username, email, password)
        my_user.save()  # Guardar en la base de datos

        # Paso 5: Mensaje de éxito y mandar al Login
        messages.success(request, '¡Cuenta creada con éxito! Por favor inicia sesión.')
        return redirect('login')

    # Si entran a la página normal (GET), solo mostramos el formulario
    return render(request, 'todo_app/register.html', {})


def loginPage(request):
    # Paso 1: Si le dan al botón Login (POST)
    if request.method == 'POST':
        # Capturamos datos
        username_recibido = request.POST['username']
        password_recibido = request.POST['password']

        # Paso 2: Verificar credenciales
        user = authenticate(request, username=username_recibido, password=password_recibido)

        if user is not None:
            # Paso 3: Si existe, iniciamos la sesión en el navegador
            login(request, user)
            return redirect('home')  # Los mandamos a su lista de tareas
        else:
            # Paso 4: Si falló
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('login')

    # Si es GET, mostramos el formulario de login
    return render(request, 'todo_app/login.html', {})






# Función para BORRAR una tarea
def deleteTask(request, name):
    # Buscamos la tarea específica que coincida con el usuario logueado Y el nombre que pasamos en la URL
    task = Todo.objects.get(user=request.user, todo_name=name)

    # La borramos de la base de datos
    task.delete()

    # Volvemos a la lista de tareas
    return redirect('home')


# Función para COMPLETAR una tarea (Update)
def updateTask(request, name):
    # Buscamos la tarea igual que antes
    task = Todo.objects.get(user=request.user, todo_name=name)

    # Cambiamos su estado a True (Completado)
    task.status = True

    # Guardamos el cambio en la base de datos
    task.save()

    # Volvemos a la lista
    return redirect('home')