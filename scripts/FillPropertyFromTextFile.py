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

SCRIPT_NAME = 'Revolve/FillPropertyFromTextFile'
DEFAULT_TARGETPROPERTY = 'TextFileContent'
DEFAULT_TARGETWINDOW = '0'

def logMessage(annotation):
    if isinstance(annotation, str):
        annotation = annotation.decode("utf-8")
    message = u'%s: %s' % (SCRIPT_NAME, annotation)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

def loadPropertyFromTextFile(filename, targetproperty, targetwindow):
    try:
        sourcefilename = xbmc.translatePath(filename)
        with open(sourcefilename) as file:
            value = file.read()
        setItemToProperty(targetproperty, value, targetwindow)
    except IOError:
        logMessage(SCRIPT_NAME + ' terminates: Error while reading file ' + filename)


if len(sys.argv) > 1:
    logMessage('Call to ' + SCRIPT_NAME + ' script with arguments: ' + str(sys.argv) + '.')	
    filename = sys.argv[1]

    if len(sys.argv) > 2:
        targetproperty = sys.argv[2]
    else:
        targetproperty = DEFAULT_TARGETPROPERTY
    
    if len(sys.argv) > 3:
        targetwindow = sys.argv[3]
    else:
        targetwindow = DEFAULT_TARGETWINDOW
    
    logMessage(SCRIPT_NAME + ' copies contenst from file: ' + filename + ' to ' + targetproperty + ' on window ' + targetwindow)	
    loadPropertyFromTextFile(filename, targetproperty, targetwindow)
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
