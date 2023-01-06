from utils.model.manager.model_manager import ModelManager

from task.models import Task


class TaskManager(ModelManager):
    model = Task
    
    fields = (
        'id',
        'title',
        'description',
        'is_done',
        'user__username',
        'created_at',
        'updated_at',
    )