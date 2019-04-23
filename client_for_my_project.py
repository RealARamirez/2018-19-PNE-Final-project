# Python file for achieving the client that is needed in the final project

# http.client, socket and Json are needed to import
import http.client
import json
import socket

# API Information
# The HOSTNAME will always be the IP where it has been executed
HOSTNAME = "localhost"
# The methods used will always be GET
Method = "GET"

# Use the standard headers
headers = {'User-Agent': 'http-client'}

# We will define a client that connect the Ensembl server and return the information from the server
def Client(ENDPOINT):
    # Connect to the server
    conn = http.client.HTTPConnection(HOSTNAME, 8000)
    # Send the request
    conn.request(Method, ENDPOINT, None, headers)
    # Wait for ir response
    r = conn.getresponse()
    # Read the response
    txt_json = r.read().decode("utf-8")
    # Close the connection
    conn.close()
    # Return the text in json format
    try:
        txt_json = json.loads(txt_json)
    except json.decoder.JSONDecodeError:
        txt_json = txt_json
    return txt_json

# Main program
while True:
    try:
        endpoint = input("Please type the endpoint: ")
        print(Client(endpoint))
    except KeyboardInterrupt:
        print("Client stopped.")
