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
    return replaceEmptyItemWithHomeProperty(getItemFromHomeProperty(sourcebase + '.Title'), sourcebase + '.EpisodeTitle')

def createSongName(sourcebase):
    return getItemFromHomeProperty(sourcebase + '.Artist') + ' - ' + getItemFromHomeProperty(sourcebase + '.Title')

def createGenericSubtitle(sourcebase):
    return joinItems(
        getItemFromHomeProperty(sourcebase + '.ShowTitle'),
        getItemFromHomeProperty(sourcebase + '.TVShowTitle'),
        getItemFromHomeProperty(sourcebase + '.Studio'),
        getItemFromHomeProperty(sourcebase + '.Artist'),
        getNumericValue(getItemFromHomeProperty(sourcebase + '.Year')),
        getNumericValue(getItemFromHomeProperty(sourcebase + '.Version')))

def createEpisodeSubtitle(sourcebase):
    seasonNumber = replaceEmptyItemWithHomeProperty(getItemFromHomeProperty(sourcebase + '.Season'), sourcebase + '.EpisodeSeason')
    episodeNumber = replaceEmptyItemWithHomeProperty(getItemFromHomeProperty(sourcebase + '.Episode'), sourcebase + '.EpisodeNumber')
    
    return joinItems(
        getItemFromHomeProperty(sourcebase + '.ShowTitle'),
        getItemFromHomeProperty(sourcebase + '.TVShowTitle'),
        addPrefixToItem(getLocalizedValue(20373) + ' ', getNumericValue(seasonNumber)),
        addPrefixToItem(getLocalizedValue(20359) + ' ', getNumericValue(episodeNumber)))

def createSongSubtitle(sourcebase):
    return joinItems(
        getItemFromHomeProperty(sourcebase + '.Album'),
        getNumericValue(getItemFromHomeProperty(sourcebase + '.Year')))

def createGenericThumbnail(sourcebase):
    result = getItemFromHomeProperty(sourcebase + '.Art(poster)')
    result = replaceEmptyItemWithHomeProperty(result, sourcebase + '.Thumb')
    result = replaceEmptyItemWithHomeProperty(result, sourcebase + '.Icon')
    return result

def createGenericBackgroundImage(sourcebase):
    result = getItemFromHomeProperty(sourcebase + '.Art(Fanart)')
    result = replaceEmptyItemWithHomeProperty(result, sourcebase + '.Property(Fanart_image)')
    result = replaceEmptyItemWithHomeProperty(result, sourcebase + '.Fanart')
    return result

def createGenericAction(sourcebase):
    result = getItemFromHomeProperty(sourcebase + '.Play')
    if result == '':
        result = addPrefixAndSuffixToItem('PlayMedia("', getItemFromHomeProperty(sourcebase + '.Path'), '")')
    if result == '':
        result = getItemFromHomeProperty(sourcebase + '.LibraryPath')
        if 'videodb' in result.lower():
            result = addPrefixAndSuffixToItem("ActivateWindow(videos,", result, ",return)")
        if 'musicdb' in result.lower():
            result = addPrefixAndSuffixToItem("ActivateWindow(music,", result, ",return)")
    return result


def determineNameMethod(sourcemask):
    result = createGenericName    
    if 'song' in sourcemask.lower():
        result = createSongName
    return result

def determineSubtitleMethod(sourcemask):
    result = createGenericSubtitle
    if 'episode' in sourcemask.lower():
        result = createEpisodeSubtitle
    if 'song' in sourcemask.lower():
        result = createSongSubtitle
    return result
    
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

        setItemToProperty(targetbase + '.Name', nameMethod(sourcebase), targetwindow)
        setItemToProperty(targetbase + '.Subtitle', subtitleMethod(sourcebase), targetwindow)
        setItemToProperty(targetbase + '.Thumbnail', thumbnailMethod(sourcebase), targetwindow)
        setItemToProperty(targetbase + '.BackgroundImage', backgroundImageMethod(sourcebase), targetwindow)
        setItemToProperty(targetbase + '.Action', actionMethod(sourcebase), targetwindow)

        
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
