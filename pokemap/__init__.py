from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('css', 'static/css/', cache_max_age=3600)
    config.add_static_view('js', 'static/js/')
    config.add_static_view('img', 'static/img/')
    config.add_route('home', '/')
    config.add_route('locations', '/locations/')
    config.add_route('about', '/about/')
    config.add_route('contact', '/contact/')
    config.add_route('world', '/world/{region}/gen{gen_id}')
    config.add_route('map', '/map/{region}/gen{gen_id}/{location_name}/')
    config.scan()
    return config.make_wsgi_app()
