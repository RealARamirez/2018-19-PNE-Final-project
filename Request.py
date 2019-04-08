# Program for creating an object that allow us to threat the request as an object
class Request:
    def __init__(self, request):
        self.request = request
        self.value = False
        self.data = {"endpoint": "/", "parameter1": {"type": "none", "value": "none"}, "parameter2": {"type": "none", "value": "none"}, "parameter3": {"type": "none", "value": "none"}, "json": "no"}
        self.data["endpoint"] = self.request.split("?")[0]
        if self.request.split("?")[-1] == "json=1": self.data["json"] = "yes"
        if self.request.split("?") > 1: self.value = True
        if self.value and self.request.split("?")[1] != "json=1":
            b = 1
            for elem in self.request.split("?")[1].split("&"):
                if "=" in elem:
                    self.data["parameter"+str(b)] = {}
                    self.data["parameter" + str(b)]["type"] = elem.split("=")[0]
                    self.data["parameter" + str(b)]["value"] = elem.split("=")[1]
                    b += 1
        return

    def __str__(self):
        return self.request

    # This method will tell us if the user is asking for a Json object or not
    def isjson(self):
        if self.data["json"] == "yes": return True
        else: return False

    # The method will give the client the endpoint it must use according to the request
    def answer(self):
        dictionary = {}
        if self.endpoint() == "listSpecies": return "/info/species?content-type=application/json"
        elif self.endpoint() == "karyotype" or self.endpoint() == "chromosomeLength": return "/info/assembly/{}?content-type=application/json".format(self.parameters().get("specie"))
        elif self.endpoint() == "geneSeq" or self.endpoint() == "geneCal": return "/sequence/id/{}?content-type=text/plain".format(self.parameters().get("gene"))
        elif self.endpoint() == "geneInfo":



