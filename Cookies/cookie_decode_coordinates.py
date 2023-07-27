import urllib.parse

data = "paste-here-your-coordinates"

# Decodifica i dati utilizzando urllib.parse.unquote()
decoded_data = urllib.parse.unquote(data)

print(decoded_data)