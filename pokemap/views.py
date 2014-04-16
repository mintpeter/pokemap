from collections import defaultdict

from pyramid import config as c
from pyramid.response import Response
from pyramid.view import view_config, notfound_view_config
from pyramid.events import subscriber, BeforeRender
from pyramid.httpexceptions import exception_response

from sqlalchemy import and_
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import NoResultFound

from .models import (
    DBSession,
    Patch,
    PatchType,
    Route
    )

from pokedex.db import connect
import pokedex.db.tables as t

PDSession = connect()

@subscriber(BeforeRender)
def add_globals(event):
    event['c'] = c

@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    return {'project': 'pokemap'}

@view_config(route_name='world', renderer='world.mako')
def view_world(request):
    c.region_identifier = request.matchdict['region']
    c.gen_id = request.matchdict['gen_id']

    try:
        region = PDSession.query(t.Region)\
                    .filter(t.Region.identifier == c.region_identifier)\
                    .one()
    except NoResultFound:
        raise exception_response(404)
    
    c.routes = DBSession.query(Route)\
                .filter(Route.region_id == region.id)\
                .all()

    q = PDSession.query(t.Location)

    for route in c.routes:
        route.location = q.filter(t.Location.id == route.location_id).one()
    
    return {}


@view_config(route_name='map', renderer='map.mako')
def view_map(request):
    region_identifier = request.matchdict['region']
    gen_id = request.matchdict['gen_id']
    location_name = request.matchdict['route_name'].title()

    c.gen_id = gen_id

    c.location = PDSession.query(t.Location)\
                    .filter(t.Location.name == location_name)\
                    .join(t.Location.region)\
                    .filter(t.Region.identifier == region_identifier)

    try:
        c.location = c.location.one()
    except NoResultFound:
        raise exception_response(404)

    # TO DO: Adapt for safari zone areas, etc.
    
    encounters = PDSession.query(t.Encounter)\
                    .join(t.Encounter.location_area)\
                    .join(t.LocationArea.location)\
                    .filter(t.Location.name == location_name)\
                    .join(t.Location.region)\
                    .filter(t.Region.identifier == region_identifier)\
                    .join(t.Encounter.slot)\
                    .join(t.EncounterSlot.version_group)\
                    .join(t.VersionGroup.generation)\
                    .filter(t.Generation.id == gen_id)\
                    .order_by(t.Encounter.version_id)


    # Structure the pokemon that are going to be listed.
    # First, the method of encounter.
    # Second, the pokemon.
    # Third, the game version.
    # Finally, the frequency of the pokemon's occurrence.
    # Based on the original:
    # https://github.com/veekun/spline-pokedex/blob/master/splinext/pokedex/controllers/pokedex.py
    c.encounters = defaultdict(
                            lambda: defaultdict(
                                lambda: defaultdict(lambda: 0)
                            )
                        )

    c.versions = []

    for encounter in encounters:
        c.encounters\
            [encounter.slot.method]\
            [encounter.pokemon]\
            [encounter.version]\
            += encounter.slot.rarity
        if encounter.version not in c.versions:
            c.versions.append(encounter.version)

    patches = DBSession.query(Patch)\
                .filter(Patch.generation_id == gen_id)\
                .filter(Patch.location_id == c.location.id).all()
    c.patch_types = DBSession.query(PatchType).all()

    # Structuring the patches sort of like the pokemon.
    # First, the encounter method id.
    # Second, the patch type.
    # Finally, the patch.
    c.patches = defaultdict(list)
    for patch in patches:
        c.patches\
            [patch.patch_type].append(patch)

    return {}

@view_config(route_name='patches', renderer='patches.mako')
def view_patches(request):
    patches = DBSession.query(Patch).all()

    return {'patches': patches}

@notfound_view_config(renderer='404.mako', append_slash=True)
def not_found(request):
    return {}
