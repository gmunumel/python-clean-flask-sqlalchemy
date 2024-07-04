from .repository.example_repository import ExampleRepository

class ExampleService:
    @staticmethod
    def get_all_examples():
        return ExampleRepository.get_all()