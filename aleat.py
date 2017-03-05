#!/usr/bin/python3

import random

class aleat():
	def parse(self, request, rest):
		return None

	def process(self, parsedRequest):
		numRand = str(random.randrange(999999999))
		newUrl = "http://localhost:1235/aleat/" + numRand
		return ("200 OK", "<html><body><h1><a href=" + newUrl +  ">Dame otra.</a></body></h1></html>")

