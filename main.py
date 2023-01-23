import requests

api_key = "118f2870eda34982990cf765e9ceeaf4"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-12-23&sortBy=publishedAt&" \
      "apiKey=118f2870eda34982990cf765e9ceeaf4"

# Make a request, and put the results into a json (dictionary) format
request = requests.get(url)
content = request.json()


print(content)

# Step through all articles
for item in content["articles"]:
    print(item["title"])
    print(item["description"])
    print("\n")