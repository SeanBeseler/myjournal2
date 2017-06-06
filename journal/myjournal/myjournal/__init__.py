from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    #config.include('.views')
    #config.include('.models')
    config.include('.routes')
    config.add_static_view(name = "static", path = "myjournal:static")
    config.scan()
    return config.make_wsgi_app()
