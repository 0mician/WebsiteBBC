import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_bbc.settings')

import django
django.setup()

from datetime import date

from events.models import Event

def add_event(
        name, category, url, start, end, details):

    Event.objects.get_or_create(
        name=name, category=category, url=url, start=start, end=end,
        details=details
    )

def populate_event():
    add_event(
        "BBAD 2015",
        "OTH",
        "http://www.belgianbraincouncil.be",
        date(2015,4,14),
        date(2015,4,15),
        """
        <h2>This is a test event</h2>
        <p>This is a list of related information</p>
        <ul>
            <li>item 1</li>
            <li>item 2</li>
            <li>item 3</li>
        </ul>
        """
    )
        
    add_event(
        "BBAD 2014",
        "OTH",
        "http://www.belgianbraincouncil.be",
        date(2014,4,14),
        date(2014,4,15),
        """
        <h2>This is a test event</h2>
        <p>This is a list of related information</p>
        <ul>
            <li>item 1</li>
            <li>item 2</li>
            <li>item 3</li>
        </ul>
        """
    )

    add_event(
        "BBAD 2013",
        "OTH",
        "http://www.belgianbraincouncil.be",
        date(2013,4,14),
        date(2013,4,15),
        """
        <h2>This is a test event</h2>
        <p>This is a list of related information</p>
        <ul>
            <li>item 1</li>
            <li>item 2</li>
            <li>item 3</li>
        </ul>
        """
    )
if __name__ == '__main__':
    print("Populating events")
    populate_event()
    print("Done!")
