# Python program for designing the html files that would be used in this project

# Import Seq to threat the sequences in Gene Cal
from Seq import Seq

# ListSpecies program
# This method will create the HTML page for list Species
def listSpecies(data, parameters):
    file = ""
    top = len(data["species"])
    for elem in parameters:
        if elem["type"] == "limit":
            if elem["value"].isdigit():
                if int(elem["value"]) <= len(data["species"]):
                    top = int(elem["value"])
                else:
                    top = len(data["species"])
                    file += """
<p>Your limit is higher than the number of species, so all the species will be listed</p>
                    """.rstrip("\n")
            else:
                top = len(data["species"])
                file += """
<p>Your limit is not a number, all species will be listed.</p>
                """.rstrip("\n")
    for b in range(top):
        file += """
<p>Specie number {} is {} most common known as {}.</p>
        """.format((b + 1), data["species"][b]["name"], data["species"][b]["common_name"])
    return file

# This method will create an HTML answer for the karyotype
def karyotype(data):
    Message = "The karyotype is compassed by the following elements: "
    for elem in data["karyotype"]:
        if elem == "MT": continue
        else: Message += elem + ", "
    Message = Message.rstrip(", ")
    file = """
<p>{}.</p>
    """.format(Message)
    return file

# This method will create the HTML page for the answer to the chromosome length
def chromosomeLength(data, parameters):
    file = ""
    value = [False]
    name = "none"
    for elem in parameters:
        if elem["type"] == "chromo":
            name = elem["value"]
    for elem in data["top_level_region"]:
        if elem["name"] == name:
            value = [True, elem["length"]]
    if value[0]:
        file += """
<p>Your chromosome has a length of {}.</p>
        """.format(value[1]).rstrip("\n")
    else:
        file += """
<p>Your chromosome has not been found in our data base.</p>
        """.rstrip("\n")
    return file

# Gives the error message
def error(message):
    file = """
    <p>{}</p>
    """.format(message).rstrip("\n")
    return file

# The method that create the HTML file for the gene Seq
def geneSeq(data):
    file = """
<p>The sequence of your human gene is : {}</p>
    """.format(data).rstrip("\n")
    return file

# The method create an HTML file part for geneInfo
def geneInfo(data):
    file = """
<p>Your gene ID is: {}</p><br>
<p>Its start is {}, its end is {} and its length is {}.</p><br>
<p>It belongs to {} chromosome.</p>
    """.format(data["id"], data["start"], data["end"], int(data["end"])-(int(data["start"])-1), data["seq_region_name"]).rstrip("\n")
    return file

# It will create the HTML part for gene Calc
def geneCalc(data):
    # Threat the data as a sequence
    S = Seq(data)
    file = """
<p>It has a length of {}. The percentages of the bases are the following:</p>
<p style='padding-left: 3em'>Base A: {}%</p><br>
<p style='padding-left: 3em'>Base C: {}%</p><br>
<p style='padding-left: 3em'>Base T: {}%</p><br>
<p style='padding-left: 3em'>Base G: {}%</p>
    """.format(S.len(), S.perc("A"), S.perc("C"), S.perc("T"), S.perc("G")).rstrip("\n")
    return file

# It will create the appendix for the HTML file of Gene List
def geneList(data):
    file = ""
    if len(data) > 0:
        for elem in data:
            file += """
<p>Gene {} which assembly name is : {}.</p>
            """.format(elem["gene_id"], elem["assembly_name"]).rstrip("\n")
    else:
        file += """
<p>There are not genes in this part of the chromosome.</p>
        """.rstrip("\n")
    return file

# Function that will return the correct appendix for the HTML file
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

# Method that will be used to create each HTML file
def HTMLFile(endpoint, message, data, parameters):
    # Define how all html files will start
    opening = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">"""
    File = opening
    # HTML part that defines the title

    File +="""
    <title>{}</title>
        """.format(endpoint).rstrip("\n")
    # Part of the HTML that ends the head and begin the body
    medium = """
</head>
<body style="background-image: url('background_image.jpg');
no-repeat center center fixed;
background-attachment: fixed;
-webkit-background-size: cover;
-moz-background-size: cover;
-o-background-size: cover;
background-size: cover">
    """.rstrip("\n")
    File += medium
    # Define how all html files will end
    closing = """
</body>
</html>
    """.rstrip("\n")
    File += """
    <h1 style="color:brown">{} page</h1>
    """.format(endpoint).rstrip("\n")
    # Now the appendix that variates on the endpoint is given by chooser that will select the function needed
    File += chooser(endpoint, message, data, parameters)
    # Add an option to go back to the initial page
    File += '<p>If you want to go back to the initial page: </p>'
    File += '<a href="/">Click here.</a>'
    # Add the end to the file
    File += closing
    # Return the file for the server
    return File



