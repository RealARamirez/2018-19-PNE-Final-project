# Python program for designing the html files that would be used in this project

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
        file += "Specie number {} is {} most common known as {}.\n".format((b + 1), data[b]["name"],data[b]["common_name"])
    return file

# This method will create an HTML answer for the karyotype
def karyotype(data):
    Message = "The karyotype is compassed by the following elements: "
    for elem in data["karyotype"]:
        if elem == "MT": continue
        else: Message += elem
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
    <p>{}, if you want to go back to the initial page:</p>
    <a href="/">Click here.</a>
    """.format(message).rstrip("\n")
    return file

# The method that create the HTML file for the gene Seq
def geneSeq(data):
    file = """
<p>The sequence of your human gene is : {}</p>
    """.format(data).rstrip("\n")
    return file

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
no-repeat center center f
ixed;
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



