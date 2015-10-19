# GitHubScrapper

The WS-DL GitHub repository html generator was written using python 3 and requires yattag and PyGithub

The current implementation requires you to have generated an OAuth token 
for your account and have it set to an environment called GitOath.

From there it looks for membership to ODU Web Science / Digital Libraries Research Group github group
and if you are not a member the script ends.

Otherwise after html generation will run till completion generating in the working directory the script
was run from GitHub.html
