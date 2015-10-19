from github import Github
from yattag import Doc
from yattag import indentation
from os import getenv
from sys import exit
from time import strftime

__author__ = 'John Berlin<jberlin@cs.odu.edu>'


def runderscore_capitalize(repo_name):
    """
        :param repo_name: string
        :rtype: string
    """
    if '_' in repo_name:
        return repo_name.replace('_', ' ').title()
    else:
        return repo_name.title()


def scrape_github():
    print("Starting WS-DL GitHub repository html generation")
    dt = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/' \
         'DTD/xhtml1-transitional.dtd">'

    commented_style = '<!-- ' \
            'ul, ol, pre, dl, p { margin-top:0px; margin-bottom:0px; }' \
            'code.escaped { white-space: nowrap; } .vspace { margin-top:1.33em; } '\
            '.indent { margin-left:40px; } .outdent { margin-left:40px; text-indent:-40px; } '\
            'a.createlinktext { text-decoration:none; border-bottom:1px dotted gray; }'\
            'a.createlink { text-decoration:none; position:relative; top:-0.5em;'\
            'font-weight:bold; font-size:smaller; border-bottom:none; } img { border:0px; }'\
            '.editconflict { color:green; font-style:italic; margin-top:1.33em; margin-bottom:1.33em; }'\
            'table.markup { border:2px dotted #ccf; width:90%; }'\
            'td.markup1, td.markup2 { padding-left:10px; padding-right:10px; }'\
            'table.vert td.markup1 { border-bottom:1px solid #ccf; }'\
            'table.horiz td.markup1 { width:23em; border-right:1px solid #ccf; }'\
            'table.markup caption { text-align:left; }'\
            'div.faq p, div.faq pre { margin-left:2em; }'\
            'div.faq p.question { margin:1em 0 0.75em 0; font-weight:bold; }'\
            'div.faqtoc div.faq * { display:none; }'\
            'div.faqtoc div.faq p.question'\
            '{ display:block; font-weight:normal; margin:0.5em 0 0.5em 20px; line-height:normal; }'\
            'div.faqtoc div.faq p.question * { display:inline; }'\
            '.frame { border:1px solid #cccccc; padding:4px; background-color:#f9f9f9; }'\
            '.lfloat { float:left; margin-right:0.5em; } .rfloat { float:right; margin-left:0.5em; }'\
            'a.varlink { text-decoration:none; }'\
            '-->'

    span_style = 'text-align: center; margin-top: 0px; margin-right: 10px; margin-bottom: 10px; margin-left: 10px;'

    desc = 'Web Science and Digital Libraries Research Group in' \
           'the Department ofComputer Science at Old Dominion University'

    foot_text = 'This page was last modified on '+strftime('%B %d, %Y at %I:%M %p EST') +'<br>' \
                'Copyright &#169; 2013, Old Dominion University. All rights reserved.'


    # this list contains the items to be placed inside the link bar as href -> text
    linkbar_items = [('https://ws-dl.cs.odu.edu/', 'Home'), ('http://ws-dl.blogspot.com/', 'Blog'),
                     ('https://ws-dl.cs.odu.edu/Main/People', 'People'),
                     ('https://ws-dl.cs.odu.edu/Main/Pubs', 'Publications'),
                     ('https://ws-dl.cs.odu.edu/Main/Software', 'Software'),
                     ('https://ws-dl.cs.odu.edu/Main/Press', 'Press'),
                     ('https://ws-dl.cs.odu.edu/Main/GitHub', 'GitHub')]

    # use OAuth token set as a environment variable for a user to log in to GitHub
    g = Github(getenv('GitOath'))
    user = g.get_user()
    wsdl_org = None

    # loop through the logged in user and find the WS-DL org
    for org in user.get_orgs():
        if org.name == 'ODU Web Science / Digital Libraries Research Group':
            wsdl_org = org
            break

    if wsdl_org is None:
        print(user.name+" you are not a member of the WS-DL at ODU-CS exiting")
        exit()

    # see www.yattag.org or github.com/leforestier/yattag
    doc, tag, text = Doc().tagtext()
    # use asis to ensure that < > characters of <!DOCTYPE html> do not get substituted with &lt; and &gt;
    doc.asis(dt)

    with tag('html', xmlns='http://www.w3.org/1999/xhtml'):
        with tag('head'):
            with tag('title'):
                text('GitHub')
            # stag is self closing tag
            doc.stag('meta', ('http-equiv', 'Content-Style-Type'), content='text/css')
            doc.stag('meta', name='google-site-verification', content='IaM4qV58mAMQVvEkegBKwOgICTYZsEdO2l4HVs1jREg')
            doc.stag('link', rel='stylesheet', href='https://ws-dl.cs.odu.edu/pub/skins/public/public.css',
                     type='text/css')
            with tag('style', type='text/css'):
                doc.asis(commented_style)
            doc.stag('meta', ('http-equiv', 'Content-Type'), content='text/html; charset=utf-8')
            doc.stag('meta', name='robots', content='index,follow')
        with tag('body'):
            with tag('table', id='wikimid', cellspacing='0', cellpadding='0', width='95%'):
                with tag('tbody'):
                    with tag('tr'):
                        with tag('td', id='wikileft', valign='top'):
                            pass
                        with tag('td', id='wikibody', valign='top'):
                            with tag('div', id='title'):
                                text('WS-DL at ODU-CS')
                            with tag('div', id='description'):
                                text(desc)
                            with tag('div', id='linkbar'):
                                with tag('ul'):
                                    for item in linkbar_items:
                                        with tag('li'):
                                            with tag('a', href=item[0]):
                                                text(item[1])
                            # klass is used a substitute for class
                            with tag('h1', klass='pagetitle'):
                                text('GitHub Repositories')
                            with tag('div', id='wikitext'):
                                for repo in wsdl_org.get_repos():
                                    # noticed that the WS-DL GitHub has non-code repos so skip them
                                    if ".io" in repo.name or 'ORS' == repo.name:
                                        continue
                                    with tag('div'):
                                        with tag('span', klass='lfloat', style=span_style):
                                            doc.stag('img', src=wsdl_org.avatar_url, width='75px')
                                    with tag('p'):
                                        with tag('strong'):
                                            with tag('a', klass='urllink',href=repo.html_url, rel='nofollow'):
                                                text(runderscore_capitalize(repo.name))
                                        doc.stag('br')
                                        text(repo.description)
                                        doc.stag('br', clear='all')
                                with tag('div', klass='vspace'):
                                    pass
                    with tag('tr'):
                        with tag('td'):
                            pass
                        with tag('td', id='wikibody', valign='top'):
                            pass
            with tag('div', id='footer'):
                doc.stag('hr')
                with tag('table'):
                    with tag('tbody'):
                        with tag('tr'):
                            with tag('td', valign='top'):
                                doc.stag('img', src='Software_files/odu2l.png', width='130px')
                            with tag('td'):
                                with tag('div', id='wikifoot'):
                                    doc.asis(foot_text)
                                with tag('div', id='actionfoot'):
                                    with tag('p'):
                                        with tag('a', klass='wikilink', href='https://ws-dl.cs.odu.edu/Main/Software?action=print'):
                                            text('Print')
                                        text(' - ')
                                        with tag('a', klass='wikilink', href='https://ws-dl.cs.odu.edu/Main/Software?action=login'):
                                            text('Admin')

    git_html = open('GitHub.html', 'w+')
    git_html.write(indentation.indent(doc.getvalue()))
    git_html.close()
    print("Finished WS-DL GitHub repository html generation")
    print("File generated is called GitHub.html")


if __name__ == "__main__":
    scrape_github()
