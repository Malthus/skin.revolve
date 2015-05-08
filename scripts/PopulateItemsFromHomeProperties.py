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

SCRIPT_NAME = 'Revolve/PopulateListFromHomeProperties'
DEFAULT_WINDOW = '1102'
DEFAULT_TARGETMASK = 'MyItems%02dOption'
TOTAL_ITEMS = 20

def logMessage(annotation):
    message = '%s: %s' % (SCRIPT_NAME, annotation.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

def createNameProperty(originbase, destination, targetwindow):
    value = getValueFromHomeProperty(originbase + '.Title')
    value = replaceEmptyValueFromHomeProperty(originbase + '.EpisodeTitle', value)
    setValueToProperty(destination, value, targetwindow)
    
def createSubtitleProperty(originbase, destination, targetwindow):
    value = joinLabels(
        getValueFromHomeProperty(originbase + '.ShowTitle'),
        getValueFromHomeProperty(originbase + '.TVShowTitle'),
        getValueFromHomeProperty(originbase + '.Studio'),
        getValueFromHomeProperty(originbase + '.Artist'),
        getValueFromHomeProperty(originbase + '.Author'),
        getValueFromHomeProperty(originbase + '.Album'),
        ignoreNumericZeroValue(getValueFromHomeProperty(originbase + '.Year')),
        ignoreNumericZeroValue(getValueFromHomeProperty(originbase + '.Version')))
    setValueToProperty(destination, value, targetwindow)
    
def createIconProperty(originbase, destination, targetwindow):
    value = getValueFromHomeProperty(originbase + '.Art(poster)')
    value = replaceEmptyValueFromHomeProperty(originbase + '.Thumb', value)
    setValueToProperty(destination, value, targetwindow)
    
def createBackgroundImageProperty(originbase, destination, targetwindow):
    value = getValueFromHomeProperty(originbase + '.Art(fanart)')
    value = replaceEmptyValueFromHomeProperty(originbase + '.Art(fanart_image)', value)
    value = replaceEmptyValueFromHomeProperty(originbase + '.Fanart', value)
    setValueToProperty(destination, value, targetwindow)
    
def createActionProperty(originbase, destination, targetwindow):
    value = getValueFromHomeProperty(originbase + '.Play')
    if value == '':
        value = addPrefixAndSuffixToLabel(getValueFromHomeProperty(originbase + '.Path'), 'PlayMedia("', '")')
    if value == '':
        value = getValueFromHomeProperty(originbase + '.LibraryPath')
    setValueToProperty(destination, value, targetwindow)
    

def copyProperties(originmask, destinationmask, targetwindow):
    for index in range (1, TOTAL_ITEMS):
        originbase = originmask % (index)
        destinationbase = destinationmask % (index)

        createNameProperty(originbase, destinationbase + '.Name', targetwindow)
        createSubtitleProperty(originbase, destinationbase + '.Subtitle', targetwindow)
        createIconProperty(originbase, destinationbase + '.Icon', targetwindow)
        createBackgroundImageProperty(originbase, destinationbase + '.BackgroundImage', targetwindow)
        createActionProperty(originbase, destinationbase + '.Action', targetwindow)


if len(sys.argv) > 1:
    logMessage('Call to ' + SCRIPT_NAME + ' script with arguments: ' + str(sys.argv) + '.')	
    originmask = sys.argv[1]

    if len(sys.argv) > 2:
        destinationmask = sys.argv[2]
    else:
        destinationmask = DEFAULT_TARGETMASK
    
    if len(sys.argv) > 3:
        targetwindow = sys.argv[3]
    else:
        targetwindow = DEFAULT_WINDOW
    
    logMessage(SCRIPT_NAME + ' copies properties: ' + originmask + ' to ' + destinationmask + ' on window ' + targetwindow)	
    copyProperties(originmask, destinationmask, targetwindow)
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
