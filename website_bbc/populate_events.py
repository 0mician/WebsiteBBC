import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_bbc.settings')

import django
django.setup()

from datetime import date

from events.models import Event

def add_event(
        name, description, category, url, start, end, details):

    Event.objects.get_or_create(
        name=name, description=description, category=category, url=url, start=start, end=end,
        details=details
    )

def populate_event():
    add_event(
        "BBAD 2015",
        "This is a short description for the Belgian Brain Ambassador Day 2015 for the frontpage view.",
        "OTH",
        "http://www.belgianbraincouncil.be",
        date(2015,4,14),
        date(2015,4,15),
        """ 
        <h2>This is a test event</h2> 
        <p>This is a list of related information, but it could really be anything</p> 
        <ul> 
            <li>item 1</li> 
            <li>item 2</li> 
            <li>item 3</li>
        </ul>
 
        <h3>And some more information</h3>
        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation
        ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
        aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint
        occaecat cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum</p> 

        """
    )
        
    add_event(
        "BBAD 2014",
        "This is a short description for the Belgian Brain Ambassador Day 2014 for the frontpage view.",
        "OTH",
        "http://www.belgianbraincouncil.be",
        date(2014,4,14),
        date(2014,4,15),
        """ 
        <h2>This is a test event</h2> 
        <p>This is a list of related information, but it could really be anything</p> 
        <ul> 
            <li>item 1</li> 
            <li>item 2</li> 
            <li>item 3</li>
        </ul>
 
        <h3>And some more information</h3>
        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation
        ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
        aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint
        occaecat cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum</p> 

        """
    )

    add_event(
        "BBAD 2013",
        "This is a short description for the Belgian Brain Ambassador Day 2013 for the frontpage view.",
        "OTH",
        "http://www.belgianbraincouncil.be",
        date(2013,4,14),
        date(2013,4,15),

               """ 
        <h2>This is a test event</h2> 
        <p>This is a list of related information, but it could really be anything</p> 
        <ul> 
            <li>item 1</li> 
            <li>item 2</li> 
            <li>item 3</li>
        </ul>
 
        <h3>And some more information</h3>
        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation
        ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
        aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint
        occaecat cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum</p> 

        """ 
    )
if __name__ == '__main__':
    print("Populating events")
    populate_event()
    print("Done!")
