# run the commandline compilation
import bottle
import subprocess
import os
import urllib2

app = bottle.default_app()


@bottle.get("/")
@bottle.get("/ariel")
def get_index():
    bottle.response.content_type = 'text/plain'
    return urllib2.urlopen("http://147.175.3.213:8081/ariel").read()


@bottle.get("/mab")
def get_index():
    bottle.response.content_type = 'text/plain'
    return urllib2.urlopen("http://147.175.3.213:8081/mab").read()


if __name__ == '__main__':
    bottle.run(host="", port=8080, debug=True, reloader=True)
