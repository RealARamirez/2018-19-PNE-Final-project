from Client import Client
# Program for creating an object that allow us to threat the request as an object
def mapper(dictionary, arg):
    value = [False, 0]
    for key in dictionary:
        if key.startswith("parameter"):
            if dictionary[key]["type"] == arg: value = [True, key]
    return value

class Request:
    def __init__(self, request):
        # the request given by the GET
        self.request = request
        # Auxiliary value of type boolean that indicates that the request there are different parameters
        self.value = False
        # data is a dictionary that will give us the following information
        # The endpoint assigned to the key endpoint
        # A dictionary for each parameter, which keys starts with the word parameter and give us its type and its value
        # If it is a json request with the key json and the possible values Yes/No
        self.data = {"endpoint": "/", "parameter1": {"type": "none", "value": "none"}, "parameter2": {"type": "none", "value": "none"}, "parameter3": {"type": "none", "value": "none"}, "json": "no"}
        # Fix the endpoint
        self.data["endpoint"] = self.request.split("?")[0]
        # Fis if it is json
        if self.request.split("?")[-1] == "json=1": self.data["json"] = "yes"
        # Assign value True if the function could contain parameters
        if len(self.request.split("?")) > 1: self.value = True
        # Fix the different values and types in the dictionary of each parameter
        if self.value and self.request.split("?")[1] != "json=1":
            b = 1
            for elem in self.request.split("?")[1].split("&"):
                if elem == "json=1": self.data["json"] = "yes"
                if "=" in elem:
                    self.data["parameter" + str(b)] = {}
                    self.data["parameter" + str(b)]["type"] = elem.split("=")[0]
                    self.data["parameter" + str(b)]["value"] = elem.split("=")[1]
                    b += 1
        # Will reassign the parameter gene to its ID
        for key in self.data:
            if key.startswith("parameter"):
                if self.data[key]["type"] == "gene":
                    try:
                        self.data[key]["value"] = Client("/xrefs/symbol/homo_sapiens/{}?content-type=application/json".format(self.data[key]["value"]))[0]["id"]
                    except (KeyError, IndexError):
                        continue
        return

    # This method will assign the str value of the request to the object
    def __str__(self):
        return self.request

    # This method will tell us if the user is asking for a Json object or not
    def isjson(self):
        if self.data["json"] == "yes":
            return True
        else:
            return False

    # The method will give the client the endpoint it must use according to the request
    # It will give a dictionary
    # The key type will tell the server if it should return an error page or it should execute a client with a determined path
    # The key value will give that error message or that path respectively
    def answer(self):
        # A set that achieve the valid possible endpoints
        endpoints = {"/listSpecies", "/karyotype", "/chromosomeLength", "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"}
        if self.data["endpoint"] in endpoints:
            if self.data["endpoint"] == "/listSpecies":
                return {"type": "client", "value": "/info/species?content-type=application/json"}
            elif self.data["endpoint"] == "/karyotype":
                if mapper(self.data, "specie")[0]:
                    return {"type": "client", "value": "/info/assembly/{}?content-type=application/json".format(self.data[mapper(self.data, "specie")[1]]["value"])}
                else:
                    return {"type": "error", "value": "The function kayotype requires an specie parameter."}
            elif self.data["endpoint"] == "/chromosomeLength":
                if mapper(self.data, "specie")[0] and mapper(self.data, "chromo")[0]:
                    return {"type": "client", "value": "/info/assembly/{}?content-type=application/json".format(self.data[mapper(self.data, "specie")[1]]["value"])}
                else:
                    return {"type": "error", "value": "The function chromosome Length requires an specie and chromo parameter."}
            elif self.data["endpoint"] == "/geneSeq" or self.data["endpoint"] == "/geneCalc":
                if mapper(self.data, "gene")[0]:
                    return {"type": "client", "value": "/sequence/id/{}?content-type=text/plain".format(self.data[mapper(self.data, "gene")[1]]["value"])}
                else:
                    return {"type": "client", "value": "This function requires a gene parameter."}
            elif self.data["endpoint"] == "/geneInfo":
                if mapper(self.data, "gene")[0]:
                    return {"type": "client", "value": "/sequence/id/{}?content-type=text/plain".format(self.data[mapper(self.data, "gene")[1]]["value"])}
                else:
                    return {"type": "error", "value": "The function gene Info requires a gene parameter."}
            elif self.data["endpoint"] == "/geneList":
                if mapper(self.data, "chromo")[0] and mapper(self.data, "stat") and mapper(self.data, "end"):
                    return {"type": "client", "value": "/overlap/region/human/{}:{}-{}?feature=gene".format(self.data[mapper(self.data, "chromo")[1]]["value"], self.data[mapper(self.data, "stat")[1]]["value"], self.data[mapper(self.data, "end")[1]]["value"])}
                else:
                    return {"type": "error", "value": "The function gene List requires a gene parameter."}
        else:
            return {"type": "error", "value": "Sorry, we do not perform {} operation, please check that you have typed it correctly.".format(self.data["endpoint"][1:])}

    # This function will give the server the endpoint when it is needed for managing the HTML/json that is needed as an output
    def endpoint(self):
        return self.data["endpoint"]

    # This method will return a list of different parameters that could be needed for different HTML and Json
    def parameters(self):
        # The list will have at least an standard dictionary
        List = [{"type": "none", "value": "none"}]
        # Append the dictionaries to the list
        for key in self.data:
            if key.startswith("parameter"):
                if self.data[key]["type"] != "none" and self.data[key]["value"] != "none":
                    List.append(self.data[key])
        return List


R = Request("/geneCalc?gene=FRAT1")
print(R.data)
print(R.isjson())
print(R.answer())
print(R.endpoint())
print(R.parameters())
