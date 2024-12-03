## Django Project with REST API, User Authentication and Admin Panel

This project is a Django based application that provides REST API endpoints for points management and task completion.


## Setup

### Prerequisites

* Python 3.6 or later
* pipenv (or any other virtual environment manager)

### Installation

1. Clone the repository:

```bash
git clone [your-git-url]
```

2. Create a virtual environment and activate it:

```bash
pipenv install
```

3. Install dependencies:

```bash
pipenv install -r requirements.txt
```

4. Apply database migrations:

- Make Migrations

```bash
pipenv run python manage.py makemigrations
```

- Migrate Changes

```bash
pipenv run python manage.py migrate
```

5. Create a superuser account:

```bash
pipenv run python manage.py createsuperuser
```


## Usage

Start the development server:

```bash
pipenv run python manage.py runserver
```

This will start the server on `http://127.0.0.1:8000/` by default.



## Admin Panel

The admin panel can be accessed at `http://127.0.0.1:8000/admin/`. Login using the superuser credentials created during setup.
