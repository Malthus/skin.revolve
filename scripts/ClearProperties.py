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

from library_xbmc import *

SCRIPT_NAME = 'Revolve/ClearProperties'
DEFAULT_TARGETWINDOW = '0'
DEFAULT_TARGETMASK = 'List%02dOption'
TOTAL_ITEMS = 20

def logMessage(annotation):
    if isinstance(annotation, str):
        annotation = annotation.decode("utf-8")
    message = u'%s: %s' % (SCRIPT_NAME, annotation)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

def clearProperties(targetmask, targetwindow):
    for index in range (1, TOTAL_ITEMS + 1):
        targetbase = targetmask % (index)

        clearProperty(targetbase + '.Name', targetwindow)
        clearProperty(targetbase + '.Subtitle', targetwindow)
        clearProperty(targetbase + '.Thumbnail', targetwindow)
        clearProperty(targetbase + '.BackgroundImage', targetwindow)
        clearProperty(targetbase + '.Action', targetwindow)

        
if len(sys.argv) > 1:
    logMessage('Call to ' + SCRIPT_NAME + ' script with arguments: ' + str(sys.argv) + '.')	

    if len(sys.argv) > 1:
        targetmask = sys.argv[1]
    else:
        targetmask = DEFAULT_TARGETMASK
    
    if len(sys.argv) > 2:
        targetwindow = sys.argv[2]
    else:
        targetwindow = DEFAULT_TARGETWINDOW
    
    logMessage(SCRIPT_NAME + ' clears properties: ' + targetmask + ' on window ' + targetwindow)	
    clearProperties(targetmask, targetwindow)
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
