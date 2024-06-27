from github import Auth, Github
import os

token = os.environ["GITHUB_TOKEN"]
repo = os.environ["GITHUB_REPOSITORY"]
pull_request = int(os.environ["GITHUB_REF_NAME"].split("/")[0])

auth = Auth.Token(token)
g = Github(auth=auth)

repo = g.get_repo(repo)
pr = repo.get_pull(pull_request)
for f in pr.get_files():
    print(f.filename)
