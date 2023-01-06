from collections.abc import Sequence
from django.db.models import Model, QuerySet
from typing import Type

from utils.math.clamp import clamp

from .base_model_manager import BaseModelManager


default_count = 25
default_page = 1
max_count = 100


class ModelSetManager(BaseModelManager):
    model: Type[Model] = None

    fields: Sequence = None

    _model_instance_set: QuerySet = None
    _model_instance_count: int = 0

    def __init__(self, instance):
        self._model_instance_set = instance
        self._model_instance_count = instance.count()


    @classmethod
    def filter(cls, **kwargs):
        model_instance_set = cls.model.objects.filter(**kwargs)

        instance = cls(model_instance_set)

        return instance


    def aggregate(self, *args, **kwargs):
        pass

    def read(self, *, count:int=default_count, page:int=default_page):
        normalized_count = clamp(count, 0, max_count)
        count_from = (page - 1) * normalized_count
        count_to = page * normalized_count 

        get_from = clamp(count_from, 0, self._model_instance_count)
        get_to = clamp(count_to, 0, self._model_instance_count)

        model_instance_subset = self._model_instance_set[get_from:get_to]

        result = {
            'item_list': [self._read_from_instance(instance, self.fields) for instance in model_instance_subset],
            'total_count': self._model_instance_count,
        }

        return result
