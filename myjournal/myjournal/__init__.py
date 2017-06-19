from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.security')
    config.add_static_view(name="static", path="myjournal:static")
    config.scan()
    return config.make_wsgi_app()
