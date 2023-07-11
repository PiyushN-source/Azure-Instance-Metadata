import requests
import json

metadata_url = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
headers = {
    "Metadata": "true"
}

response = requests.get(metadata_url, headers=headers)
metadata = response.json()


json_output = json.dumps(metadata, indent=4)
print(json_output)

print("Select the option from below to choose which key you want to retrieve:")
print("1. compute")
print("2. network")

selected_option = input("Enter the option number: ")

if selected_option == "1":
    key_to_retrieve = "compute"
elif selected_option == "2":
    key_to_retrieve = "network"
else:
    print("Invalid option selected.")
    exit()

if key_to_retrieve in metadata:
    specific_data = metadata[key_to_retrieve]
    print("Value of '{}' key: {}".format(key_to_retrieve, specific_data))
else:
    print("Key '{}' not found in metadata.".format(key_to_retrieve))
