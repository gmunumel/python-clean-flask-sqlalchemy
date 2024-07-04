from .model.example_model import db, ExampleModel

class ExampleRepository:
    @staticmethod
    def get_all():
        return ExampleModel.query.all()