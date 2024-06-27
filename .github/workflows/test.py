from github import Auth, Github


token = "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" # get from GITHUB_TOKEN env var

auth = Auth.Token(token)
g = Github(auth=auth)

repo = g.get_repo("EOEPCA/open-science-catalog-metadata-testing") # get from GITHUB_REPOSITORY
pr = repo.get_pull(11) # get from GITHUB_REF_NAME as <pr_number>/merge
for f in pr.get_files():
    print(f.filename) # validate each file against appropriate schema
