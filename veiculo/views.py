from .models import Blog
import pymongo
# Create your views here.
from django.http import HttpResponse

from time import sleep
from .models import Blog
import pymongo
# Create your views here.
from django.http import HttpResponse

def callback(session):
    orders = session.client.db.orders
    orders.insert_one({"sku": "abc123", "qty": 100})
    session.commit_transaction()

def index(request):
    client = pymongo.MongoClient('localhost', 27017,)
    orders = client.db.orders
    inventory = client.db.inventory
    with client.start_session() as session:
        with session.start_transaction():
            orders.insert_one({"sku": "abc123", "qty": 100}, session=session)
            #session.commit_transaction()
            session.abort_transaction()
    return HttpResponse()


def callback2(session):
    orders = session.client.db.orders
    orders.insert_one({"sku": "abc123", "qty": 100})
    session.commit_transaction()

def index2(request):
    client = pymongo.MongoClient('localhost', 27017,)

    with client.start_session() as session:
        session.with_transaction(callback2)
            

    return HttpResponse()
