#!/usr/bin/python3

class suma():

    sum1 = None

    def parse(self, request, rest):
        try:
            rest = int(rest[1:])
            return rest
        except ValueError:
            return None

    def process(self,parsedRequest):

        if (parsedRequest == "favicon.ico"):
            return ("404 Not Found", "<html><body><h1>Not Found</h1></body></html>")

        if (parsedRequest is None):
            return ("200 OK", "<html><body>Datos introducidos erroneos." + 
                               "</body></html>")

        if (self.sum1 is None):
            
            self.sum1 = parsedRequest
            html = "<html><body>Me has dado un: " + str(parsedRequest) + ". " + "</body></html>"
        
        else:
            
            html = "<html><body>Me habias dado un: " + str(self.sum1) + ". " + "Ahora un: " + str(parsedRequest) + ". " + "Suman: " + str(self.sum1 + parsedRequest) + "." +"</body></html>"
            self.sum1 = None

        return("200 OK",html)