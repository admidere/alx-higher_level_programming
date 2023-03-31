#!/usr/bin/python3
"""Python script that lists list 10 commits (from the most recent
to oldest) of the repository “rails” by the user “rails”."""


if __name__ == "__main__":
    """ LIST 10 COMMITS """
    import requests
    from sys import argv
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
          .format(argv[2], argv[1])

    request = requests.get(url)
    commits = request.json()
    for commit in commits:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
