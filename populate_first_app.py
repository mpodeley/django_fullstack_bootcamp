import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## FAKE POP JavaScript
import random
from first_app.models import AccessRecord, Webpage, Topic
from second_app.models import User


from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name =fakegen.company()
        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url, name=fake_name)[0]

        #crate a fake access record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)

def populate_users(N=5):
    for entry in range(N):
        first_n = fakegen.first_name()
        last_n = fakegen.last_name()
        mail =fakegen.email()
        #create the new webpage entry
        usr = User.objects.get_or_create(first_name=first_n,last_name=last_n, email=mail)[0]




if __name__ == '__main__':
    print("populating script!")
    #populate(20)
    populate_users(20)
    print("populating complete")
