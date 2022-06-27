# Development journey

This is a Log\Journal\Dev Diary

The purpose of which is to help enforce a TDD paradigm

## Setup

 First Goal is minimum testable environment

### Frontend

#### create-react-app

Yay create-react-app is already setup with jest.
and has a working test.

#### Flask

Not so easy, but not hard either

I'm using vscode. For This reason I decided to jump a cpl red green cycles and installed
flask-SQLAlchemy as this will enable vscode extensions for pylint and just saves some headaches

setup python venv

pip install Flask  flask-SQLAlchemy python-dotenv

pip install pytest pytest-cov

pip install pylint pylint-flask pylint-flask-sqlalchemy

pip install python-dotenv

pip freeze > requirements.txt

create .flaskenv set

    DEBUG=True
    FLASK_ENV="development"
    FLASK_APP="ocrnightmare"

create a config.py and set add to .gitignore

    FLASK_APP=os.environ.get('FLASK_APP')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

create a .env add to .gitignore

    PYTHONPATH=< your_path_to_ocrn >/OCRNightmare/backend
    DATABASE_URL=mysql://<username>@<your_db_host>/<db_name>
    TEST_DATABASE_URL=mysql://<username>@<your_db_host>/<db_name>

Start this file

1. one
   * nested

## Testing

Ready for first Test

1. Red
   * ok my app will expect to find some things in the environment
   * test_config_class_exists_and_has_expected_attributes()

1. Make it Green
   * Create Config and env files
      a fail
   * Made a Diag test that always fail to reveal issue
   * Fix Dev environment issue
   * Green

1. Refactor
   * setup a file structure for tests
   * disable diag test as it is extraneous to most systems and will be flaky

1. Red
   * its a web app needs a root/home page
   * test_home_page_get()

1. Make it Green
   * create app module
   * create default route /
   * Green

1. Refactor
   * flesh out directory structure
   * do a compile and browser verify
   * commit back end structure with issue tag in commit message
