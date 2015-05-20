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

SCRIPT_NAME = 'Revolve/PopulateStaticItemsFromHomeProperties'
DEFAULT_TARGETWINDOW = '0'
DEFAULT_TARGETMASK = 'MyItems%02dOption'
TOTAL_ITEMS = 20

def logMessage(annotation):
    message = '%s: %s' % (SCRIPT_NAME, annotation.encode('ascii', 'ignore'))
    print message
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

def createGenericNameProperty(sourcebase, targetproperty, targetwindow):
    value = getValueFromHomeProperty(sourcebase + '.Title')
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.EpisodeTitle', value)
    setValueToProperty(targetproperty, value, targetwindow)
    
def createGenericSubtitleProperty(sourcebase, targetproperty, targetwindow):
    value = joinLabels(
        getValueFromHomeProperty(sourcebase + '.ShowTitle'),
        getValueFromHomeProperty(sourcebase + '.TVShowTitle'),
        getValueFromHomeProperty(sourcebase + '.Studio'),
        getValueFromHomeProperty(sourcebase + '.Artist'),
        getValueFromHomeProperty(sourcebase + '.Author'),
        getValueFromHomeProperty(sourcebase + '.Album'),
        ignoreNumericZeroValue(getValueFromHomeProperty(sourcebase + '.Year')),
        ignoreNumericZeroValue(getValueFromHomeProperty(sourcebase + '.Version')))
    setValueToProperty(targetproperty, value, targetwindow)
    
def createGenericIconProperty(sourcebase, targetproperty, targetwindow):
    value = getValueFromHomeProperty(sourcebase + '.Art(poster)')
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Thumb', value)
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Icon', value)
    setValueToProperty(targetproperty, value, targetwindow)
    
def createGenericBackgroundImageProperty(sourcebase, targetproperty, targetwindow):
    value = getValueFromHomeProperty(sourcebase + '.Art(Fanart)')
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Property(Fanart_image)', value)
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Fanart', value)
    setValueToProperty(targetproperty, value, targetwindow)
    
def createGenericActionProperty(sourcebase, targetproperty, targetwindow):
    value = getValueFromHomeProperty(sourcebase + '.Play')
    if value == '':
        value = addPrefixAndSuffixToLabel(getValueFromHomeProperty(sourcebase + '.Path'), 'PlayMedia("', '")')
    if value == '':
        value = getValueFromHomeProperty(sourcebase + '.LibraryPath')
        if "videodb" in value:
            value = addPrefixAndSuffixToLabel(value, "ActivateWindow(videos,", ",return)")
        if "musicdb" in value:
            value = addPrefixAndSuffixToLabel(value, "ActivateWindow(music,", ",return)")
    setValueToProperty(targetproperty, value, targetwindow)
    

def copyProperties(sourcemask, targetmask, targetwindow):
    for index in range (1, TOTAL_ITEMS):
        sourcebase = sourcemask % (index)
        targetbase = targetmask % (index)

        createGenericNameProperty(sourcebase, targetbase + '.Label', targetwindow)
        createGenericSubtitleProperty(sourcebase, targetbase + '.Label2', targetwindow)
        createGenericIconProperty(sourcebase, targetbase + '.Thumb', targetwindow)
        createGenericBackgroundImageProperty(sourcebase, targetbase + '.Fanart', targetwindow)
        createGenericActionProperty(sourcebase, targetbase + '.Action', targetwindow)


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
    
    logMessage(SCRIPT_NAME + ' copies properties: ' + sourcemask + ' to ' + targetmask + ' on window ' + targetwindow)	
    copyProperties(sourcemask, targetmask, targetwindow)
else:
    logMessage(SCRIPT_NAME + ' terminates: Missing argument(s) in call to script.')	
