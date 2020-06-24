import importlib


class GenericHelper:
    @staticmethod
    def create_object_by_dict(class_name: str, parameters: dict) -> object:
        try:
            split_class_name = class_name.rsplit('.', 1)
            module = importlib.import_module(split_class_name[0])
            class_ = getattr(module, split_class_name[1])
            return class_(**parameters)
        except ModuleNotFoundError as me:
            raise RuntimeError(me)

