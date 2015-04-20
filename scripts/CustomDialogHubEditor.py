# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.

import sys, re
import xbmc

from Library_Property import *

SCRIPT_NAME = 'Revolve DialogHubEditor Python Script'
TARGET_WINDOW = '1192'
TOTAL_OPTIONS = 20

def logMessage(annotation):
    message = '%s: %s' % (SCRIPT_NAME, annotation.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

def determineIdentifier(menuname):
    return re.sub('[^0-9A-Za-z]+', '_', menuname)

    
def copySettings(hubidentifier):
    for index in range (1, TOTAL_OPTIONS):
        skinsetting = 'Hub%s%02dOption' % (hubidentifier, index)
        property = 'CustomHub%02dOption' % (index)

        copySkinSettingToProperty(skinsetting + '.Type', property + '.Type', TARGET_WINDOW)
        copySkinSettingToProperty(skinsetting + '.Name', property + '.Name', TARGET_WINDOW)
        copySkinSettingToProperty(skinsetting + '.Subtitle', property + '.Subtitle', TARGET_WINDOW)
        copySkinSettingToProperty(skinsetting + '.BackgroundImage', property + '.BackgroundImage', TARGET_WINDOW)
        copySkinSettingToProperty(skinsetting + '.Parameter', property + '.Parameter', TARGET_WINDOW)
        copySkinSettingToProperty(skinsetting + '.Action', property + '.Action', TARGET_WINDOW)

def setMenuNameAndSubmenuIdentifier(menuname, hubidentifier):
    setValueToProperty('CustomHub.Name', menuname, TARGET_WINDOW)
    setValueToProperty('CustomHub.Identifier', hubidentifier, TARGET_WINDOW)

def openWindow():    
    xbmc.executebuiltin('ActivateWindow(' + TARGET_WINDOW + ')')


if len(sys.argv) >= 1:
    logMessage('Call to ' + SCRIPT_NAME + ' script with arguments: ' + str(sys.argv) + '.')	
    menuname = sys.argv[1]

    if len(sys.argv) >= 2:
        hubidentifier = determineIdentifier(sys.argv[2])

    if hubidentifier == '':
        logMessage(SCRIPT_NAME + ' determines identifier from menu-name: ' + menuname + ' => ' + hubidentifier)	
        hubidentifier = determineIdentifier(menuname)
    
    logMessage(SCRIPT_NAME + ' copies settings labeled by: ' + hubidentifier)	
    copySettings(hubidentifier)
    
    logMessage(SCRIPT_NAME + ' initializes menu-name setting: ' + menuname)	
    setMenuNameAndSubmenuIdentifier(menuname, hubidentifier)

    logMessage(SCRIPT_NAME + ' opens DialogCustomHub window for: ' + menuname)	
    openWindow()
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
