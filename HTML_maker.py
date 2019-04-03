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
        <title>{}</title>""".format(title)


# Part of the HTML that ends the head and begin the body
medium = """
</head>
<body background="background_image.jpg" style=" no-repeat center center fixed; 
-webkit-background-size: cover; 
-moz-background-size: cover; 
-o-background-size: cover; 
background-size: cover">"""

# Define how all html files will end
closing = """
</body>
</html>"""

class HTMLFile:
    def __init__(self):
        return

    def error(self):
        file = opening
        file += title("Error")
        file += medium
        file += """
            <h1>Error page</h1>
            <p>This page is not recognize, if you want to go back to the initial page:</p>
            <a href="/">Click here.</a>
        """
        file += closing
        return file
