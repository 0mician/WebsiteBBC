import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_bbc.settings')

import django
django.setup()

from datetime import date

from news.models import News

def add_news(name, date, description, details):
    News.objects.get_or_create(
        name=name, date=date, 
        description=description,
        details=details
    )

def populate_news():
    add_news(
        "THASGASTE GENT 2015",
        date(2015,12,11),
        "BBC participates to the Non Invasive Brain stimulation techniques (NIBS) for psychiatric disorders: First European Meeting: THASGASTE GENT",
        """ 
        <h2>This is a test event</h2> 
        <p>
        BBC participates to the Non Invasive Brain stimulation techniques (NIBS) for psychiatric disorders: First European Meeting: THASGASTE GENT
        <p>
        This is a list of related information, but it could really be anything</p> 
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

    add_news(
        "BBC General Assembly 2015",
        date(2015,6,15),
        "Details: 17:00 University Foundation",
        """ 
        <h2>This is a test event</h2> 
        <p>
        BBC General assembly: 17:00 University Foundatio
        <p>
        This is a list of related information, but it could really be anything</p> 
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

    add_news(
        "BSN Meeting Mons",
        date(2015,5,22),
        "BBC participates to the 11th Meeting of the Belgian Society for Neuroscience, Mons",
        """ 
        <h2>This is a test event</h2> 
        <p>
        BBC participates to the 11th Meeting of the Belgian Society for Neuroscience, Mons
        <p>
        This is a list of related information, but it could really be anything</p> 
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

    add_news(
        "Chaire Francqui",
        date(2015,2,1),
        "Chaire Francqui pour Jean Schoenen: Leçon inaugurale le 26 Février à 17h - plus d'info ici",
        """ 
        <h2>This is a test event</h2> 
        <p>
        Chaire Francqui pour Jean Schoenen: Leçon inaugurale le 26 Février à 17h - plus d'info ici
        <p>
        This is a list of related information, but it could really be anything</p> 
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
    print("Populating news")
    populate_news()
    print("Done!")
