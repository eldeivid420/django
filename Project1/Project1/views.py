from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

class Person(object):
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

#first view
def greet(req):
    p1 = Person("Test", "Blue")
    #name = "David"
    #color = "red"
    actual_pets = ["Dog","Cat","Fish"] 
    now = actual_date =  datetime.datetime.now()
    #ext_doc  = open("C:/Users/david/OneDrive/Documentos/GitHub/django/Project1/Templates/template1.html")
    #template = Template(ext_doc.read())
    #ext_doc.close()
    ext_doc = loader.get_template('template1.html')
    #context = Context({"username": p1.name, "color": p1.color, "actual_time": now, "pets": actual_pets})
    doc = ext_doc.render({"username": p1.name, "color": p1.color, "actual_time": now, "pets": actual_pets})
    return HttpResponse(doc)

def show_time(req):
    actual_date =  datetime.datetime.now()
    doc = """<html>
    <body>
    <h1>The time is: %s</h1>
    </body>
    </html>""" % actual_date

    return HttpResponse(doc)

def get_age(req, age, year):
    lapse = year-2022
    futureAge = age+lapse
    doc = "<html><body><h2>Your age at year %s is %s</h2></body></html>" %(year, futureAge)
    return HttpResponse(doc)