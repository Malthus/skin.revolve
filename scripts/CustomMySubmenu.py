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

from Library_Property import *

SCRIPT_NAME = 'Revolve MyHub Python Script'
TARGET_WINDOW = '1101'
TOTAL_ITEMS = 20

def logMessage(annotation):
    message = '%s: %s' % (SCRIPT_NAME, annotation.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

def clear_target_property(destination):
    xbmc.executebuiltin('ClearProperty(' + destination + ',' + TARGET_WINDOW + ')')

def copy_skin_setting(origin, destination):
    value = xbmc.getInfoLabel('Skin.String(' + origin + ')')
    if value != '':
        xbmc.executebuiltin('SetProperty(' + destination + ',' + value + ',' + TARGET_WINDOW + ')')


def save_window_parameters(menuname, hubidentifier):
    xbmc.executebuiltin('Skin.SetString(Dialog.MyHubMenuTitle,' + menuname + ')')
    xbmc.executebuiltin('Skin.SetString(Dialog.MyHubIdentifier,' + originmask + ')')
    
def copy_settings(hubidentifier):
    for index in range (1, TOTAL_ITEMS):
        origin = 'MyHub' + hubidentifier + ('%02d' % (index)) + 'Option'
        destination = 'MyHub%02dOption' % (index)

        clear_target_property(destination + '.Name')
        clear_target_property(destination + '.Subtitle')
        clear_target_property(destination + '.BackgroundImage')
        clear_target_property(destination + '.Action')
        
        copy_skin_setting(origin + '.Name', destination + '.Name')
        copy_skin_setting(origin + '.Subtitle', destination + '.Subtitle')
        copy_skin_setting(origin + '.BackgroundImage', destination + '.BackgroundImage')
        copy_skin_setting(origin + '.Action', destination + '.Action')

def set_menuname(menuname):
    xbmc.executebuiltin('SetProperty(MyHubMenuTitle,' + menuname + ',' + TARGET_WINDOW + ')')

def open_window(executeopenwindow):    
    if executeopenwindow:
        xbmc.executebuiltin('ActivateWindow(' + TARGET_WINDOW + ')')


if len(sys.argv) >= 3:
    logMessage('Call to ' + SCRIPT_NAME + ' script with arguments: ' + str(sys.argv) + '.')	
    menuname = sys.argv[1]
    hubidentifier = sys.argv[2]
    executeopenwindow = (len(sys.argv) <= 3) or ((len(sys.argv) > 3) and (sys.argv[3] == 'true'))

    logMessage(SCRIPT_NAME + ' saves window parameters: ' + menuname + ', ' + hubidentifier)	
    save_window_parameters(menuname, hubidentifier)
    
    logMessage(SCRIPT_NAME + ' copies settings: ' + hubidentifier + ' to MyHub-properties')	
    copy_settings(hubidentifier)
    
    logMessage(SCRIPT_NAME + ' initializes menu-name setting: ' + menuname)	
    set_menuname(menuname)

    logMessage(SCRIPT_NAME + ' opens MyHub menu for: ' + menuname)	
    open_window(executeopenwindow)
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
