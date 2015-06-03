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

SCRIPT_NAME = 'Revolve/PopulateStaticItemsFromHomeProperties'
DEFAULT_TARGETWINDOW = '0'
DEFAULT_TARGETMASK = 'MyItems%02dOption'
TOTAL_ITEMS = 20

def logMessage(annotation):
    if isinstance(annotation, str):
        annotation = annotation.decode("utf-8")
    message = u'%s: %s' % (SCRIPT_NAME, annotation)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

def createGenericName(sourcebase):
    value = getValueFromHomeProperty(sourcebase + '.Title')
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.EpisodeTitle', value)
    return value
    
def createGenericSubtitle(sourcebase):
    value = joinLabels(
        getValueFromHomeProperty(sourcebase + '.ShowTitle'),
        getValueFromHomeProperty(sourcebase + '.TVShowTitle'),
        getValueFromHomeProperty(sourcebase + '.Studio'),
        getValueFromHomeProperty(sourcebase + '.Artist'),
        getValueFromHomeProperty(sourcebase + '.Author'),
        getNumericValue(getValueFromHomeProperty(sourcebase + '.Year')),
        getNumericValue(getValueFromHomeProperty(sourcebase + '.Version')))
    return value

def createSongSubtitle(sourcebase):
    value = joinLabels(
        getNumericValue(getValueFromHomeProperty(sourcebase + '.Artist')),
        getNumericValue(getValueFromHomeProperty(sourcebase + '.Album')),
        getNumericValue(getValueFromHomeProperty(sourcebase + '.Year')))
    return value
    
def createGenericThumbnail(sourcebase):
    value = getValueFromHomeProperty(sourcebase + '.Art(poster)')
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Thumb', value)
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Icon', value)
    return value

def createGenericBackgroundImage(sourcebase):
    value = getValueFromHomeProperty(sourcebase + '.Art(Fanart)')
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Property(Fanart_image)', value)
    value = replaceEmptyValueFromHomeProperty(sourcebase + '.Fanart', value)
    return value

def createGenericAction(sourcebase):
    value = getValueFromHomeProperty(sourcebase + '.Play')
    if value == '':
        value = addPrefixAndSuffixToLabel(getValueFromHomeProperty(sourcebase + '.Path'), 'PlayMedia("', '")')
    if value == '':
        value = getValueFromHomeProperty(sourcebase + '.LibraryPath')
        if 'videodb' in value.lower():
            value = addPrefixAndSuffixToLabel(value, "ActivateWindow(videos,", ",return)")
        if 'musicdb' in value.lower():
            value = addPrefixAndSuffixToLabel(value, "ActivateWindow(music,", ",return)")
    return value


def determineNameMethod(sourcemask):
    return createGenericName    
    
def determineSubtitleMethod(sourcemask):
    value = createGenericSubtitle
    if 'song' in sourcemask.lower():
        value = createSongSubtitle
    return value
    
def determineThumbnailMethod(sourcemask):
    return createGenericThumbnail
    
def determineBackgroundImageMethod(sourcemask):
    return createGenericBackgroundImage
    
def determineActionMethod(sourcemask):
    return createGenericAction

    
def copyProperties(sourcemask, targetmask, targetwindow):
    nameMethod = determineNameMethod(sourcemask)
    subtitleMethod = determineSubtitleMethod(sourcemask)
    thumbnailMethod = determineThumbnailMethod(sourcemask)
    backgroundImageMethod = determineBackgroundImageMethod(sourcemask)
    actionMethod = determineActionMethod(sourcemask)

    for index in range (1, TOTAL_ITEMS + 1):
        sourcebase = sourcemask % (index)
        targetbase = targetmask % (index)

        setValueToProperty(targetbase + '.Name', nameMethod(sourcebase), targetwindow)
        setValueToProperty(targetbase + '.Subtitle', subtitleMethod(sourcebase), targetwindow)
        setValueToProperty(targetbase + '.Thumbnail', thumbnailMethod(sourcebase), targetwindow)
        setValueToProperty(targetbase + '.BackgroundImage', backgroundImageMethod(sourcebase), targetwindow)
        setValueToProperty(targetbase + '.Action', actionMethod(sourcebase), targetwindow)

        
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
