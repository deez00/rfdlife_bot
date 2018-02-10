# _*_ coding: utf-8 _*_

import os

# Set your api tokens and keys through environmental variables
# (add lines to your .bashrc and restart terminal):
# export RFDLIFE_BOT_TOKEN="XXXXX:XXXXXXXXXXX"
# export RFDLIFE_BOT_AUTH_LOGIN="first.second"
# export RFDLIFE_BOT_AUTH_PSWD="password"
#
# OR
#
# Manually through defaults in this file
# Important: untrack file to prevent accidential private token pushing:
# 'git update-index --assume-unchanged tokens.py'

default_bot = ""
bot = os.getenv('RFDLIFE_BOT_TOKEN', default_bot)

default_auth_login = ""
auth_login = os.getenv('RFDLIFE_BOT_AUTH_LOGIN', default_auth_login)

default_auth_pswd = ""
auth_pswd = os.getenv('RFDLIFE_BOT_AUTH_PSWD', default_auth_pswd)