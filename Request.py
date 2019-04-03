# Program for creating an object that allow us to threat the request as an object
class Request:
    def __init__(self, request):
        self.request = request
        return

    def __str__(self):
        return self.request

    # This option will give us the endpoint of the request
    def endpoint(self):
        return self.request.split("?")[0][1:]

    # This method will tell us if the user is asking for a Json object or not
    def isjson(self):
        if self.request.split("?")[-1] == "json=1": return True
        else: return False

    # This method will return a list (if it exists) with the parameters of the request
    def parameters(self):
        if self.request.split("?") > 1:
            if self.request.split("?")[1] != "json=1":
                list = self.request.split("?")[1].split("&")
                dict = {}
                for elem in list: dict[elem.split("=")[0]] = elem.split("=")
                return dict
            else: return False
        else: return False

    # The method will give the client the endpoint it must use according to the request
    def path(self):
        if self.endpoint() == "listSpecies": return "/info/species?content-type=application/json"
        elif self.endpoint() == "karyotype" or self.endpoint() == "chromosomeLength": return "/info/assembly/{}?content-type=application/json".format(self.parameters().get("specie"))
        elif self.endpoint() == "geneSeq" or self.endpoint() == "geneCal": return "/sequence/id/{}?content-type=text/plain".format(self.parameters().get("gene"))
        elif self.endpoint() == "geneInfo":



