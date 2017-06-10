import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import Model_Entry
import datetime


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    Entry = [
        {'id':0,'title': 'Sean Beseler', 'date': '6/3/17', 'text': 'Pyramid is getting much clearer!'},
        {'id':1,'title': 'Sean Beseler', 'date': '6/1/17', 'text': 'To day we started learning how to add a SQL data to our website.'},
        {'id':2,'title': 'Sean Beseler', 'date': '5/30/17', 'text': 'We stared graphs today as well as going over pyramid. I feel that I am way behind in pyramid'},
        {'id':3,'title': 'Sean Beseler', 'date': '5/29/17', 'text': 'To day we had a long code review which did help with the sever project. Thanks for do it.'},
    ]
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')

    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        for en in Entry:
            entry = Model_Entry(
                title=en['title'],
                text=en['text'],
                date=en['date'],
            )

            dbsession.add(entry)
