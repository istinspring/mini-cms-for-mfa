from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

import os
import shutil
import os.path as op
import zipfile
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Default folders
THEME_FOLDERS = ['js', 'img', 'css']

TEMPLATES_FOLDER = 'themes'
TEMPLATES_PATH = op.join(settings.MEDIA_ROOT, TEMPLATES_FOLDER)

class MfaTheme(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True)
    theme_zip = models.FileField(upload_to=TEMPLATES_FOLDER)
    active = models.BooleanField(default=False)

    def template_folder_name(self):
        '''make folder name from filename'''
        f, e = op.splitext(op.basename(self.theme_zip.name))
        return slugify(f).lower()

    def unpack_template(self):
        '''Unpack template from zip file to folder'''
        zf_path = op.join(settings.PROJECT_ROOT, self.theme_zip.path)
        if zipfile.is_zipfile(zf_path):
            zf = zipfile.ZipFile(zf_path, 'r')
            folder = op.join(TEMPLATES_PATH, self.template_folder_name())
            if not op.exists(folder):
                os.mkdir(folder)
                zf.extractall(folder)
                zf.close()
                return folder
        else:
            return ""

    def copy_theme(self):
        ''' Copy theme files to django template and static_filse places'''
        source = self.unpack_template()
        try:
            dest = list(settings.TEMPLATE_DIRS).pop(0) # get first template folder
        except IndexError:
            logger.error("Cant get first item of settings.TEMPLATE_DIR")
            return False

        # clear template folder
        if op.exists(dest) and op.isdir(dest):
            shutil.rmtree(dest)
            os.mkdir(dest)
            
        # get all files from source root
        template_files = [op.join(source, f) for f in os.listdir(source)
                          if op.isfile(op.join(source, f))]
        
        # move theme files to django template folder
        for f in template_files:
            shutil.move(f, dest)

        try:
            dest = list(settings.STATICFILES_DIRS).pop(0) # get first static folder
        except IndexError:
            logger.error("Cant get first item of settings.TEMPLATE_DIR")
            return False

        # remove static folder (copytree function issues)
        if op.exists(dest) and op.isdir(dest):
            shutil.rmtree(dest)
            os.mkdir(dest)

        # get all folders from source root
        template_folders = [op.join(source, f) for f in os.listdir(source)
                            if op.isdir(op.join(source, f)) and (f in THEME_FOLDERS)]
        
        # move static files to django file dir
        for f in template_folders:
            shutil.move(f, dest)

        shutil.rmtree(source)

        logger.info("Copying theme done")
        return True
            

    def set_active(self):
        # set this theme as active
        themes = MfaTheme.objects.all().update(active=False)
        self.active = True
        return self.copy_theme()

    def save(self, *args, **kwargs):
        super(MfaTheme, self).save(*args, **kwargs)
        if self.active:
            if self.set_active():
                logger.info("Theme activated")
            else:
                logger.info("Error while trying to activate theme")
        super(MfaTheme, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
