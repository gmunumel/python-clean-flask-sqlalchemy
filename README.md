# python-clean-flask-sqlalchemy

This project is to create a small boilerplate project using Clean Arquitecture with framework Flask and SQLAlchemy.

## Project structure

    /app
        /main
            __init__.py
            /controller
                __init__.py
                example_controller.py
            /service
                __init__.py
                example_service.py
            /repository
                __init__.py
                example_repository.py
            /model
                __init__.py
                example_model.py
        /test
            __init__.py
            test_example.py
    /instance
        __init__.py
        config.py
    requirements.txt
    run.py

## Setup virtual Environment and install dependencies

Create the virtual environment

    python3 -m venv .venv

Load the environment

In Linux/Mac

    source .venv/bin/activate

In Windows

    .\.venv\Scripts\activate

Install dependencies

    pip install -r requirements.txt