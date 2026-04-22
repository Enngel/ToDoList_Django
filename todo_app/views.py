from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskList, Task
from .serializers import TaskListSerializer, TaskSerializer

@api_view(['GET', 'POST'])
def task_list_collection(request):
    """
    GET: List all TaskLists.
    POST: Create a new TaskList.
    """
    if request.method == 'GET':
        lists = TaskList.objects.all().order_by('-created_at')
        serializer = TaskListSerializer(lists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def task_list_detail(request, list_id):
    """
    DELETE: Delete a TaskList.
    """
    try:
        task_list = TaskList.objects.get(pk=list_id)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def task_collection(request, list_id):
    """
    GET: List tasks of a specific TaskList.
    POST: Add a task to a TaskList.
    """
    try:
        task_list = TaskList.objects.get(pk=list_id)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tasks = task_list.tasks.all().order_by('-created_at')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Add task_list id to the data
        data = request.data.copy()
        data['task_list'] = list_id
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE'])
def task_detail(request, list_id, task_id):
    """
    PATCH: Mark a task as completed or pending.
    DELETE: Delete a task.
    """
    try:
        task = Task.objects.get(pk=task_id, task_list_id=list_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
