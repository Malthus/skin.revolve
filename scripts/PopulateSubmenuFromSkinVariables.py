# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.

import sys
import xbmc

from xbmc_property import *

SCRIPT_NAME = 'Revolve/PopulateListFromSkinVariables'
DEFAULT_TARGETMASK = 'MySubmenu%02dOption'
DEFAULT_TARGETWINDOW = '0'
TOTAL_ITEMS = 20

def logMessage(annotation):
    message = '%s: %s' % (SCRIPT_NAME, annotation.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)


def copyProperties(sourcemask, targetmask, targetwindow):
    for index in range (1, TOTAL_ITEMS):
        sourcebase = sourcemask % (index)
        targetbase = targetmask % (index)

        copySkinSettingToProperty(sourcebase + '.Name', targetbase + '.Name', targetwindow)
        copySkinSettingToProperty(sourcebase + '.Subtitle', targetbase + '.Subtitle', targetwindow)
        copySkinSettingToProperty(sourcebase + '.BackgroundImage', targetbase + '.BackgroundImage', targetwindow)
        copySkinSettingToProperty(sourcebase + '.MenuTitle', targetbase + '.MenuTitle', targetwindow)
        copySkinSettingToProperty(sourcebase + '.SourceInfo', targetbase + '.SourceInfo', targetwindow)
        copySkinSettingToProperty(sourcebase + '.Window', targetbase + '.Window', targetwindow)
        copySkinSettingToProperty(sourcebase + '.Action', targetbase + '.Action', targetwindow)


if len(sys.argv) > 1:
    logMessage('Call to ' + SCRIPT_NAME + ' script with arguments: ' + str(sys.argv) + '.')	
    sourcemask = sys.argv[1]

    if len(sys.argv) > 2:
        targetmask = sys.argv[2]
    else:
        targetmask = DEFAULT_TARGETMASK
    
    if len(sys.argv) > 3:
        targetwindow = sys.argv[3]
    else:
        targetwindow = DEFAULT_TARGETWINDOW
    
    logMessage(SCRIPT_NAME + ' copies variables: ' + sourcemask + ' to ' + targetmask + ' on window ' + targetwindow)	
    copyProperties(sourcemask, targetmask, targetwindow)
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
