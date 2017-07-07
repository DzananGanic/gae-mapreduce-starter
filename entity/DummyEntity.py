from google.appengine.ext import ndb

class DummyEntity(ndb.Model):
    dummy_property = ndb.StringProperty("DummyProperty")