import requests, json

import os
token = os.environ.get("GITHUB_TOKEN", "")
gist_id = "fffb6dc678e5298c6b76aaa2057de4bf"

with open("helper-pancake.user.js", "r") as f:
    content = f.read()

r = requests.patch(
    f"https://api.github.com/gists/{gist_id}",
    headers={"Authorization": f"token {token}"},
    json={"files": {"helper-pancake.user.js": {"content": content}}}
)
print(r.status_code, r.json().get("message","OK"))
