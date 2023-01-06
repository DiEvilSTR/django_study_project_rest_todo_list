from utils.model.manager.model_set_manager import ModelSetManager

from task.models import Task


class TaskListManager(ModelSetManager):
    model = Task
    
    fields = (
        'id',
        'title',
        'is_done',
        'user__username',
        'updated_at',
    )