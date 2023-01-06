from collections.abc import Sequence
from django.db.models import Model
from typing import Type


class BaseModelManager:
    model: Type[Model] = None
    
    fields: Sequence = None


    @staticmethod
    def _read_from_instance(instance: Model, fields: Sequence):
        result = {}

        for field in fields:
            field_path = field.split('__')
            result[field] = BaseModelManager._get_field_value(field_path, instance)

        return result


    @staticmethod
    def _get_field_value(field_path: list[str], field_values):
        current_path, *sub_path = field_path

        if len(field_path) > 1:
            sub_values = getattr(field_values, current_path)

            return BaseModelManager._get_field_value(sub_path, sub_values)
        
        return getattr(field_values, current_path)
