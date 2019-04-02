# Python file for achieving the client that is needed in the final project

# http.client and Json are needed to import
import http.client
import json

# API Information
# The HOSTNAME will always be rest.ensembl.org
HOSTNAME = "rest.ensembl.org"
# The methods used will always be GET
Method = "GET"

# Use the standard headers
headers = {'User-Agent': 'http-client'}

# We will define a client that connect the Ensembl server and return the information from the server
def Client(ENDPOINT):
    # Connect to the server
    conn = http.client.HTTPSConnection(HOSTNAME)
    # Send the request
    conn.request(Method, ENDPOINT, None, headers)
    # Wait for ir response
    r = conn.getresponse()
    # Read the response
    txt_json = r.read().decode("utf-8")
    # Close the connection
    conn.close()
    # Return the text in json format
    return json.loads(txt_json)
