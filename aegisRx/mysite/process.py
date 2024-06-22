import requests
import json

def getData(ncode):
  # Define the base URL for the openFDA API
  base_url = "https://connect.medlineplus.gov/service?"
  # Define the search parameters
  search_params = {
    "mainSearchCriteria.v.cs": "2.16.840.1.113883.6.69",
     "knowledgeResponseType": "application/json",  # Limit the number of results to 1
    "mainSearchCriteria.v.c":str(ncode)#"00456140530"
  }
  # Send the GET request to the openFDA API
  response = requests.get(base_url, params=search_params)
  
  # Check if the request was successful
  if response.status_code == 200:
    # Extract the data from the response
    data = response.json()
    if(data['feed']['entry']): 
    # Print out the first result's summary:
      return data['feed']['entry'][0]['summary']['_value']
      
      # Save the data to a local JSON file
      # with open("data.json", "w") as file:
        # Inputs the data of the first entry including the name and the summary
        # json.dump(data['feed']['entry'][0], file)
    else:
      return "Nothing found"
  
  else:
    print("Error: Failed to retrieve data from the MedLine Connect Plus API")

def getInteractions(ncode):
  base_url = "https://api.fda.gov/drug/label.json?"
  search = {
  "search":"openfda.product_ndc.exact:"+"\""+ncode+"\""
  }
  response = requests.get(base_url, params=search)
  # Extract the data from the response
  data = response.json()
  if('results' in data):
      if('drug_interactions_table' in data['results'][0]):
        return data['results'][0]['drug_interactions_table']
      elif('drug_interactions' in data['results'][0]):
        return data['results'][0]['drug_interactions']
      elif('warnings' in data['results']):
        return data['results'][0]['warnings']
      elif('warnings_and_cautions' in data['results'][0]):
        return data['results'][0]['warnings_and_cautions']
      else:
        return "Nothing Found"
  else:
    return "No medication found for that NDC code"
  
# Use code in the botom to test it
# ncodeValue = input("Enter the ndc Code you want to see data for: ")
# getData(ncodeValue)
# ncodeVal = input("Enter the ndc Code you want to see interactions for: ")

  # Resets to standard html page before writing to file
# with open('test.html','w') as file:
#   file.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Document</title>\n</head>\n<body></body>\n</html>")

  
# htmlVal = getInteractions(ncodeVal)
# with open('test.html','r') as file:
#   html = file.read()

# index1 = html.find('<body>')
# index2 = html.find('</body>')
# html2 = html[:index1]+htmlVal[0]+ html[index2:]
  
# with open('test.html','w') as file:
#   file.write(html2)
