# Installation

Create .env file from .env.template

Install dependencies:
`poetry install`

Create database schema:
`alembic upgrade head`

Try the docs:
`http://localhost:8000/docs`

## How to create a migration file
- Add some models or made some change
- Run: `alembic revision --autogenerate -m "<MESSAGE>"`: remember to change the message

### If want to update the existing migration file
- Downgrade the migration if you already migrated this: `alembic downgrade -1`
- Delete the obsolete migration file in `alembic/versions`
- Run `alembic upgrade head`
- Run `alembic revision --autogenerate -m "<MESSAGE>"`: remember to change the message

## Format code
### Ruff 
Ruff package is installed after running `poetry install`
**Usage**
To run Ruff as a linter, try any of the following:
```
ruff check .
ruff check path/to/code/*.py 
```

Ruff as a formatter:
```
ruff format .
ruff format path/to/code/*.py  
```
To reorganize import statements and others
```
ruff check . --fix
```

Refer to https://github.com/astral-sh/ruff?tab=readme-ov-file#usage

VS Code extension: https://github.com/astral-sh/ruff-vscode
