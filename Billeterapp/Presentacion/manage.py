import os

from . import create_app

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('BILLETERAPP_ENV') or 'dev')
manager = Manager(app)


migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
