import requests
from send_email import send_email
topic = "tesla"

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news\n\n "
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
print(body)
send_email(message=body)