from collections.abc import Sequence
from django.db.models import Model
from typing import Type

from .base_model_manager import BaseModelManager


class ModelManager(BaseModelManager):
    model: Type[Model] = None
    
    fields: Sequence = None
    
    _model_instance: Model = None
    
    def __init__(self, instance):
        self._model_instance = instance


    @classmethod
    def create(cls, **kwargs):
        model_instance = cls.model.objects.create(**kwargs)
        model_instance.save()
        
        instance = cls(model_instance)
        
        return instance


    @classmethod
    def get(cls, **kwargs):
        try:
            model_instance = cls.model.objects.get(**kwargs)
        except cls.model.DoesNotExist:
            return None
        
        instance = cls(model_instance)
        
        return instance


    def delete(self):
        self._model_instance.delete()


    def read(self):
        return self._read_from_instance(self._model_instance, self.fields)


    def update(self, data):
        for field in data.keys():
            value = data[field]

            setattr(self._model_instance, field, value)

        self._model_instance.save()
