# Import the unquote function to decode URL-encoded strings
from urllib.parse import unquote

def parse_raw_body(raw_body):
    # Split the raw_body into key-value pairs using '&' as a separator
    elements = raw_body.split('&')

    # Define a dictionary to temporarily hold the parsed data
    parsed_data = {}

    # Iterate through each element and parse the key-value pair
    for element in elements:
        # Split each element into a key and a value using '=' as a separator
        key, value = element.split('=')
        # Decode the URL-encoded value and replace "+" with a space
        parsed_data[key] = unquote(value.replace('+', ' '))

    # Construct the dictionary with the specific format that maps to the named variables
    output = {
        'Name': parsed_data['name'],                # Extract the 'name' value
        'Title': parsed_data['title'],              # Extract the 'title' value
        'Description': parsed_data['description'],  # Extract the 'description' value
        'Severity': parsed_data['severity'],        # Extract the 'severity' value
        'DeviceType': parsed_data['device'],        # Extract the 'device' value
        'AttachmentURL': parsed_data['fileURL']     # Extract the 'fileURL' value
    }

    # Return the output dictionary containing the named variables
    return output

# Example usage
raw_body = "name=Jill+Huckels&title=Takes+me+3+tries+to+save+content&description=When+tapping+on+the+bookmark+icon+on+the+content%2C+it+takes+me+3+times+to+get+it+to+activate&severity=Minor&device=iOS&fileURL=https%3A%2F%2Fcdn.filestackcontent.com%2FbZsqe0DHSYS2iAZHH7Dt"
output = parse_raw_body(raw_body)
# Print the output dictionary to the console
print(output)
