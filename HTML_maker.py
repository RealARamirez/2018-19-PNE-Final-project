# Python program for designing the html files that would be used in this project
# Define how all html files will start
opening = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">"""


# HTML part that defines the title
def title(title):
    return """
    <title>{}</title>
        """.format(title).rstrip("\n")


# Part of the HTML that ends the head and begin the body
medium = """
</head>
<body style="background-image: url('background_image.jpg');
no-repeat center center fixed;
-webkit-background-size: cover;
-moz-background-size: cover;
-o-background-size: cover;
background-size: cover">
""".rstrip("\n")

# Define how all html files will end
closing = """
</body>
</html>
""".rstrip("\n")

class HTMLFile:
    def error(self, message):
        file = opening
        file += title("Error")
        file += medium
        file += """
    <h1>Error page</h1>
    <p>{}, if you want to go back to the initial page:</p>
    <a href="/">Click here.</a>
        """.format(message).rstrip("\n")
        file += closing
        return file

    def listSpecies(self, data, parameters):
        file = opening
        file += title("list Species")
        file += medium
        file += """
    <h1>List Species page</h1>
        """.rstrip("\n")
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
        file += closing
        return file
