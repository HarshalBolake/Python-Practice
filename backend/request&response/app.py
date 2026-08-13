import requests
 
resp = requests.get("https://api.github.com/users/octocat")
print(resp.status_code)
print(resp.headers["content-type"])
print(resp.json())

payload = {"title": "Hello", "body":"world"}
resp1 = requests.post(
    "https://api.example.com/posts",
    json=payload,
    headers={"Authorization"}
    )