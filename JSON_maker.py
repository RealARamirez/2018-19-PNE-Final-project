# Function similar to HTML_maker which purpose is to design the Json outputs

# Import JSON
import json

# Import Seq object
from Seq import Seq

# It will crate listSpecies dictionary
def listSpecies(data, parameters):
    dictionary = {}
    top = len(data["species"])
    for elem in parameters:
        if elem["type"] == "limit":
            if elem["value"].isdigit():
                if int(elem["value"]) <= len(data["species"]):
                    top = int(elem["value"])
                else:
                    top = len(data["species"])
                    dictionary["detected_error"] = "Your limit is higher than the number of species, so all the species will be listed"
            else:
                top = len(data["species"])
                dictionary["detected_error"] = "Your limit is not a number, all species will be listed."
    for b in range(top):
        dictionary["Specie_"+str(b+1)] = "Specie {} most common known as {}.\n".format(data[b]["name"],data[b]["common_name"])
    return dictionary

# It will create karyotype dictionary
def karyotype(data):
    dictionary = {}
    b = 1
    for elem in data["karyotype"]:
        if elem == "MT": continue
        else: dictionary["karyotype_"+str(b)], b = elem, b+1
    return dictionary

# For creating chromosomeLength dictionary
def chromosomeLength(data, parameters):
    dictionary = {}
    value = [False]
    name = "none"
    for elem in parameters:
        if elem["type"] == "chromo":
            name = elem["value"]
    for elem in data["top_level_region"]:
        if elem["name"] == name:
            value = [True, elem["length"]]
    if value[0]:
        dictionary["length"] = value[1]
    else:
        dictionary["error"]= "Your chromosome has not been found in our data base."
    return dictionary

# Return an standard error Json
def error(message):
    dictionary = {}
    dictionary["error"] = str(message)
    return dictionary

# Dictionary for the sequence
def geneSeq(data):
    dictionary = {}
    dictionary["sequence"] = str(data)
    return dictionary

# Dictionary for geneInfo
def geneInfo(data):
    dictionary = {}
    dictionary["gene_ID"] = data["id"]
    dictionary["start"] = data["start"]
    dictionary["end"] = data["end"]
    dictionary["length"] = str(int(data["end"])-(int(data["start"])-1))
    dictionary["chromosome"] = data["seq_region_name"]
    return dictionary

# Generate a dictionary for geneCalc
def geneCalc(data):
    # Threat the data as a sequence
    S = Seq(data)
    dictionary = {}
    dictionary["length"] = str(S.len())
    dictionary["perc_BaseA"] = str(S.perc("A")) + "%"
    dictionary["perc_BaseC"] = str(S.perc("C")) + "%"
    dictionary["perc_BaseT"] = str(S.perc("T")) + "%"
    dictionary["perc_BaseG"] = str(S.perc("C")) + "%"
    return dictionary

# Dictionary for geneList
def geneList(data):
    dictionary = {}
    if len(data) > 0:
        b = 1
        for elem in data:
            dictionary["gene_n"+str(b)] = {"gene_id":str(elem["gene_id"]), "gene_assembly_name": str(elem["assembly_name"])}
            b += 1
    else:
        dictionary["error"] = "There are not genes in this part of the chromosome.</p>"
    return dictionary

# Function that will return the correct appendix for the JSON file
def chooser(endpoint, message, data, parameters):
    if endpoint == "listSpecies": return listSpecies(data, parameters)
    elif endpoint == "karyotype": return karyotype(data)
    elif endpoint == "chromosomeLength": return chromosomeLength(data, parameters)
    elif endpoint == "error": return error(message)
    elif endpoint == "geneSeq": return geneSeq(data)
    elif endpoint == "geneInfo": return geneInfo(data)
    elif endpoint == "geneCalc": return geneCalc(data)
    elif endpoint == "geneList": return geneList(data)
    else: return error("Sorry, we do not perform that operation, please check that you have typed it correctly.")

# Function that will create the json file
def JSONFile(endpoint, message, data, parameters):
    return json.dumps(chooser(endpoint, message, data, parameters))
