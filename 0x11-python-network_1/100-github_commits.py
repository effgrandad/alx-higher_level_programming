#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

    try:
        r = get(url)
        j = r.json()
        for commit in j[:10]:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit')
                                  .get('author')
                                  .get('name')))
    except IndexError as e:
        print(e)
