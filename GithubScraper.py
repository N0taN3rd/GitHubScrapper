from github import Github

from yattag import Doc
from yattag import indentation
from os import getenv

__author__ = 'John Berlin<jberlin@cs.odu.edu>'

def runderscore_capitalize(string):
    if '_' in string:
        return string.replace('_',' ').title()
    else:
        return string.title()

def scrape_github():

    sing = "'"
    dt = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
    inline_style = '#fi #fic {margin-right:100px !important}  #fi #rh {margin-left:-115px !important;width:95px !important}'\
                   +'  #fi .rh {display:none !important}  body:not(.xE) div[role='+sing\
                   +'main'+sing+'] .Bu:not(:first-child) {display: none !important}'
    desc = 'Web Science and Digital Libraries Research Group in the Department ofComputer Science at Old Dominion University'
    linkbar_items = [('https://ws-dl.cs.odu.edu/','Home'),('http://ws-dl.blogspot.com/','Blog'),
                     ('https://ws-dl.cs.odu.edu/Main/People','People'),('https://ws-dl.cs.odu.edu/Main/Pubs','Publications'),
                     ('https://ws-dl.cs.odu.edu/Main/Software','Software'),('https://ws-dl.cs.odu.edu/Main/Press','Press'),
                     ('https://ws-dl.cs.odu.edu/Main/GitHub','GitHub')]
    doc, tag, text = Doc().tagtext()
    doc.asis(dt)

    with tag('html',xmlns='http://www.w3.org/1999/xhtml'):
        with tag('head'):
            with tag('title'):
                text('GitHub')
            doc.stag('meta',('http-equiv','Content-Style-Type'), content='text/css')
            doc.stag('meta',name='google-site-verification',content='IaM4qV58mAMQVvEkegBKwOgICTYZsEdO2l4HVs1jREg')
            doc.stag('link',rel='stylesheet',href='https://ws-dl.cs.odu.edu/pub/skins/public/public.css',type='text/css')
            doc.stag('meta',('http-equiv','Content-Type'), content='text/html; charset=utf-8')
            doc.stag('meta',name='robots', content='index,follow')
            with tag('style',type='text/css'):
                text(inline_style)
        with tag('body'):
            with tag('table',id='wikimid', width='95%', cellspacing='0', cellpadding='0'):
                with tag('tbody'):
                    with tag('tr'):
                        with tag('td',id='wikileft',valign='top'):
                            pass
                        with tag('td',id='wikibody', valign='top'):
                            with tag('div',id='title'):
                                text('WS-DL at ODU-CS')
                            with tag('div',id='description'):
                                text(desc)
                            with tag('div',id='linkbar'):
                                with tag('ul'):
                                    for item in linkbar_items:
                                        with tag('li'):
                                            with tag('a',href=item[0]):
                                                text(item[1])
                            with tag('h1', klass='pagetitle'):
                                text('GitHub')
                            with tag('div',id='wikitext'):
                                with tag('div'):
                                    pass




    print(indentation.indent(doc.getvalue()))




    '''
    g = Github(getenv("GitOath"))
    user = g.get_user()
    wsdl_org = None
    for org in user.get_orgs():
        if org.name == 'ODU Web Science / Digital Libraries Research Group':
            wsdl_org = org
            break
    print(org.avatar_url)
    for repo in wsdl_org.get_repos():
        if ".io" in repo.name or 'ORS' == repo.name:
            continue
        rname = runderscore_capitalize(repo.name)
        print(rname)
        print(repo.description)
        print(repo.html_url)
        print(repo.forks)
        print(repo.stargazers_count)
        print()





    repo_langs = repo.get_languages()
        if not len(repo_langs) == 0:
            top_lang = max(repo_langs.keys(), key=lambda k: repo_langs[k])
            print('The top language is %s' % top_lang)
        for item in repo.get_languages().items():
            print(item)
        print()
    memberLogin = {}
    for member in org.get_members():
        if member.name == None:
            print("No Name but the users login is "+member.login)
        else:
            print(member.name)



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


if __name__ == "__main__":
    scrape_github()
