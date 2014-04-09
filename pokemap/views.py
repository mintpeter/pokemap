from collections import defaultdict

from pyramid.response import Response
from pyramid.view import view_config, notfound_view_config

from sqlalchemy import and_
from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Patch
    )

from pokedex.db import connect
import pokedex.db.tables as t

PDSession = connect('sqlite:////home/zack/playground/pokemap/pokedex/pokedex/data/pokedex.sqlite')


@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    return {'project': 'pokemap'}

@view_config(route_name='map', renderer='map.mako')
def view_map(request):
    location_identifier = request.matchdict['route_identifier']

    location_area = PDSession.query(t.LocationArea).join(t.Location)\
                    .filter(t.Location.identifier == location_identifier).first()
#    encounters = PDSession.query(t.Encounter).join(t.Version)\
#                    .filter(t.Version.version_group_id == 7)

    encounters = PDSession.query(t.Encounter).join(t.Encounter.version)\
                    .filter(t.Version.version_group_id == 7)\
                    .join(t.Encounter.location_area)\
                    .join(t.LocationArea.location)\
                    .filter(t.Location.identifier == location_identifier)\
#                    .join(t.Encounter.pokemon)\
#                    .join(t.Encounter.slot)\
#                    .join(t.EncounterSlot.method)

    # Collapse redundant encounters


    # Structure the pokemon that are going to be listed.
    # First, the method of encounter.
    # Second, the game version
    # Third, the pokemon.
    # Finally, the frequency of the pokemon's occurrence.
    # Based on the original:
    # https://github.com/veekun/spline-pokedex/blob/master/splinext/pokedex/controllers/pokedex.py
    sorted_encounters = defaultdict(
                            lambda: defaultdict(
                                lambda: defaultdict(lambda: 0)
                            )
                        )

    versions = []

    for encounter in encounters:
        sorted_encounters\
            [encounter.slot.method]\
            [encounter.pokemon]\
            [encounter.version]\
            += encounter.slot.rarity
        if encounter.version not in versions:
            versions.append(encounter.version)

    patches = DBSession.query(Patch).filter(Patch.routeid == 1).all()

    return {'patches': patches,
            'versions': versions,
            'sorted_encounters': sorted_encounters}

@notfound_view_config(renderer='404.mako', append_slash=True)
def not_found(request):
    return {}
