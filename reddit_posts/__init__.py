__version__ = '0.1.0'

import connexion

connexion = connexion.FlaskApp(__name__, specification_dir='api/')
