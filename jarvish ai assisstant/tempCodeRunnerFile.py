try:
response = requests.get(url)
if response.status_code == 200:
data = response.json()
articles = data.get("articles", [])  # Extract the articles list

if articles:
print("🔹 Top 5 News Headlines:")
for i, article in enumerate(articles[:5]):  # Get only top 5 headlines
print(f"{i+1}. {article['title']} - {article['source']['name']}")
print(f"   {article['url']}\n")  # Print the URL for reference
else:
print("No news articles found.")

else:
print(f"Failed to fetch news. Status Code: {response.status_code}")

except Exception as e:
print(f"Error: {e}")
