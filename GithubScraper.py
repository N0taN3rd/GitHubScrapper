from github import Github
from base64 import b64decode
from bs4 import BeautifulSoup
from urllib import request
from dominate import document
from dominate.tags import *
from os import getenv




__author__ = 'Johns'



if __name__ == "__main__":
    '''
    soup = BeautifulSoup(request.urlopen("https://github.com/users/N0taN3rd/contributions").read(),'html.parser')
    print(soup)
    '''

    wsdl = "ODU Web Science / Digital Libraries Research Group"
    g = Github(getenv("GitOath"))
    user = g.get_user()
    wsdlOrg = None
    for org in user.get_orgs():
        if org.name == 'ODU Web Science / Digital Libraries Research Group':
            wsdlOrg = org
            break

    for repo in wsdlOrg.get_repos():
        print(repo.name)
        print(repo.description)
        print(repo.html_url)
        print(repo.has_wiki)

        repoLangs = repo.get_languages()
        if not len(repoLangs) == 0:
            topLang = max(repoLangs.keys(),key=lambda k : repoLangs[k])
            print(topLang)

        for item in repo.get_languages().items():
            print(item)
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