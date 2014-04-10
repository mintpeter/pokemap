from collections import defaultdict

from pyramid import config as c
from pyramid.response import Response
from pyramid.view import view_config, notfound_view_config
from pyramid.events import subscriber, BeforeRender

from sqlalchemy import and_
from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Patch
    )

from pokedex.db import connect
import pokedex.db.tables as t

PDSession = connect('sqlite:////home/zack/playground/pokemap/pokedex/pokedex/data/pokedex.sqlite')

@subscriber(BeforeRender)
def add_globals(event):
    event['c'] = c

@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    return {'project': 'pokemap'}

@view_config(route_name='map', renderer='map.mako')
def view_map(request):
    region_identifier = request.matchdict['region']
    gen_id = request.matchdict['gen_id']
    location_name = request.matchdict['route_name'].title()

    c.gen_id = gen_id

    c.location = PDSession.query(t.Location)\
                    .filter(t.Location.name == location_name)\
                    .join(t.Location.region)\
                    .filter(t.Region.identifier == region_identifier)\
                    .one()


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
    sorted_encounters = defaultdict(
                            lambda: defaultdict(
                                lambda: defaultdict(lambda: 0)
                            )
                        )

    c.versions = []

    for encounter in encounters:
        sorted_encounters\
            [encounter.slot.method]\
            [encounter.pokemon]\
            [encounter.version]\
            += encounter.slot.rarity
        if encounter.version not in c.versions:
            c.versions.append(encounter.version)

    patches = DBSession.query(Patch).filter(Patch.routeid == int(location_name.split(' ')[-1])).all()

    return {'patches': patches,
            'sorted_encounters': sorted_encounters}

@view_config(route_name='patches', renderer='patches.mako')
def view_patches(request):
    patches = DBSession.query(Patch).all()

    return {'patches': patches}

@notfound_view_config(renderer='404.mako', append_slash=True)
def not_found(request):
    return {}
