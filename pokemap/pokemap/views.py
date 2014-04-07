from pyramid.response import Response
from pyramid.view import view_config, notfound_view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Patch
    )


@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    return {'project': 'pokemap'}

@view_config(route_name='map', renderer='map.mako')
def view_map(request):
    route_id = request.matchdict['rid']

    patches = DBSession.query(Patch).filter(Patch.routeid == route_id).all()

    return {'route_id': route_id, 'patches': patches}

@notfound_view_config(renderer='404.mako', append_slash=True)
def not_found(request):
    return {}
