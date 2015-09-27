import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_bbc.settings')

import django
django.setup()

from links.models import Link

def add_link(name, url):
    Link.objects.get_or_create(name=name, url=url)

def populate_links():
    add_link("Belgian Society for Neuroscience",
             "https://sites.google.com/site/belgiansocietyforneuroscience/")
    add_link("Belgian Association for Sleep Research and Sleep Medicine (BASS)",
             "http://www.belsleep.org/bass.aspx")
    add_link("Belgian Pain Society",
             "http://www.belgianpainsociety.org")
    add_link("International Brain Tumor Association",
             "http://www.theibta.org")
    add_link("Fondation Roi Baudoin",
             "http://www.kbs-frb.be/index.aspx?LangType=2060")
    add_link("The Belgian Society of Neurosurgery",
             "http://www.bsn.be")
    add_link("Belgische Zelfhulpgroep voor Dystoniepatienten vzw - Association Belge des Patients Dystoniques asbl",
             "http://www.dystonie.be")
    add_link("Fonds voor wetenschapelijk onderzoek op ruggenmergletsels",
             "http://www.fwor.be")
    add_link("Werkgroep Hersentumoren vzw - Study Group Brain Tumours Belgium",
             "http://www.wg-hersentumoren.be")
    add_link("Société Royale de Médecine Mentale de Belgique",
             "http://www.srmmb.be")
    add_link("Department of Neurology, UZ Leuven",
             "http://www.neurology-kuleuven.be")
    add_link("Ligue Nationale Belge de la Sclérose en Plaques - Nationale Belgische Multiple Sclerose Liga",
             "http://www.ms-sep.be")
    add_link("European Brain Council",
             "http://www.europeanbraincouncil.org/")
    add_link("Belgian Society of Pediatric Neurology",
             "http://www.neuro.be/bspn/")
    add_link("Belgian Neurological Society",
             "http://www.neuro.be/bvn-sbn")
    add_link("Latran Foundation",
             "http://www.fondation-thierry-latran.org")
    add_link("Diplomatic World",
             "http://www.diplomatic-world.com/")
    add_link("The Brain Prize",
             "http://www.thebrainprize.org/")
    add_link("ALS Liga",
             "http://www.alsliga.be/")
    add_link("Acta Neurologica Belgica",
             "http://www.actaneurologica.be/page.asp?lang=en&mod=home&page=index")

if __name__ == '__main__':
    print("Populating links")
    populate_links()
    print("Done!")
