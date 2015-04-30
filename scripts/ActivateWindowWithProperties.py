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

SCRIPT_NAME = 'Revolve/ActivateWindowWithProperties'

def logMessage(annotation):
    message = '%s: %s' % (SCRIPT_NAME, annotation.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

def setWindowProperty(propertyname, value, windowid):
    setValueToProperty(propertyname, value, windowid)

def openWindow(windowid):
    xbmc.executebuiltin('ActivateWindow('+ windowid + ')')

if len(sys.argv) > 1:
    logMessage('Call to ' + SCRIPT_NAME + ' script with arguments: ' + str(sys.argv) + '.')	
    windowid = sys.argv[1]

    index = 3
    while (len(sys.argv) > index):
        logMessage(SCRIPT_NAME + ' sets window parameter ' + sys.argv[index - 1] + ' with value ' + sys.argv[index])
        setWindowProperty(sys.argv[index - 1], sys.argv[index], windowid)
        index = index + 2
    
    logMessage(SCRIPT_NAME + ' opens window with id: ' + windowid)	
    openWindow(windowid)
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
