from github import Github
from base64 import b64decode
from bs4 import BeautifulSoup
from urllib import request
from dominate import document
from dominate.tags import *



__author__ = 'Johns'



if __name__ == "__main__":
    '''
    soup = BeautifulSoup(request.urlopen("https://github.com/users/N0taN3rd/contributions").read(),'html.parser')
    print(soup)
    '''
    g = Github("eda1ba1358e30a1936bf6cc422e9dcb3774e7ed9")
    user = g.get_user()
    orgs = user.get_orgs()
    org = orgs[0]
    for repo in org.get_repos():
        print(repo.name)
        print(repo.description)
        print(repo.html_url)
        print(repo.has_wiki)
        for lang,num in repo.get_languages().items():
            print(lang)

        '''
        readme = repo.get_readme()
        print(b64decode(readme.content))
        '''
        print()
    '''
    memberLogin = {}
    for member in org.get_members():
        if member.name == None:
            print("No Name but the users login is "+member.login)
        else:
            print(member.name)
            '''



    '''
    print(user.name)
    print(user.email)
    print(user.bio)
    repos = user.get_repos()
    excludeList = ["Makefile","Shell","ANTLR"]

    for repo in repos:
        print(repo.name)
        print(repo.description)
        print(repo.html_url)
        for l in filter(lambda x: x not in excludeList, repo.get_languages().keys()):
            print(l)
        for contributor in repo.get_contributors():
            print(contributor.name)
        print("\n")
        '''