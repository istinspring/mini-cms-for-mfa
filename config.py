# -*- coding: utf-8 -*-
import os.path as op
import settings

'''Constants'''
FEED_TITLE = 'Latest articels'
FEED_DESCRIPTION = 'rss feed for lates articles. subscribe now!'

'''Projects settings'''
settings.TEMPLATE_CONTEXT_PROCESSORS += ("mfa_articles.context_processors.mfa_context",)

'''Config for grappelli'''
GRAPPELLI_ADMIN_TITLE = "Mini-cms for MFA sites"

'''Config for filebrowser'''

# The absolute path to the directory that holds the media-files you want to browse
FILEBROWSER_MEDIA_ROOT = settings.MEDIA_ROOT
# URL that handles the media served from MEDIA_ROOT
FILEBROWSER_MEDIA_URL = settings.MEDIA_URL
# Main FileBrowser Directory. Leave empty in order to browse all files and folders within MEDIA_ROOT
FILEBROWSER_DIRECTORY = ''
# The URL and Path to your FileBrowser media-files
FILEBROWSER_URL_FILEBROWSER_MEDIA = settings.STATIC_URL + 'filebrowser/'
FILEBROWSER_PATH_FILEBROWSER_MEDIA = op.join(settings.STATIC_ROOT, 'filebrowser/')

# API keys
