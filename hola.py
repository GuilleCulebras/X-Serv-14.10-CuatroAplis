#!/usr/bin/python3

import webapp

class hola(webapp.app):
    def process(self,parsedRequest):
        return ("200 OK", "<html><body><h1>" +
                          "HOLA" +
                          "</h1></body></html>")

class adios(webapp.app):
    def process(self,parsedRequest):
        return ("200 OK", "<html><body><h1>" +
                          "ADIOS" +
                          "</h1></body></html>")