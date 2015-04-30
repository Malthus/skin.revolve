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

def escapeValue(value):
    if '"' not in value:
        value = '"' + value + '"'
    return value

def getValueFromInfoLabel(infolabel):    
    value = xbmc.getInfoLabel(infolabel)
    return value
    
def getValueFromProperty(property, window):
    value = getValueFromInfoLabel('Window(' + window + ').Property(' + property + ')')
    return value

def getValueFromHomeProperty(property):
    value = getValueFromProperty(property, 'home')
    return value

def getNumericValueFromHomeProperty(property):
    value = getValueFromProperty(property, 'home')
    if value == '0':
        value = ''
    return value

def getValueFromSkinSetting(skinsetting):
    value = getValueFromInfoLabel('Skin.String(' + skinsetting + ')')
    return value


def ignoreNumericZeroValue(value):
    if (value == '0'):
        value = '' 
    return value
    
def replaceEmptyValueFromHomeProperty(property, value):
    if value == '':
        value = getValueFromHomeProperty(property)
    return value

    
def addPrefixAndSuffixToLabel(value, prefix, suffix):
    if value != '':
        value = prefix + value + suffix
    return value
    
def joinSingleLabel(value, label):
    if value != '':
        value = value + addPrefixAndSuffixToLabel(label, ' | ', '')
    else:
        value = label    
    return value
    
def joinLabels(*labels):
    value = ''
    for label in labels:
        value = joinSingleLabel(value, label)
    return value


def setValueToProperty(property, value, window):
    if value != '':
        xbmc.executebuiltin('SetProperty(' + property + ',' + escapeValue(value) + ',' + window + ')')        
    else:
        xbmc.executebuiltin('ClearProperty(' + property + ',' + window + ')')
    
def setValueToSkinSetting(skinsetting, value):
    if value != '':
        xbmc.executebuiltin('Skin.SetString(' + skinsetting + ',' + escapeValue(value) + ')')
    else:
        xbmc.executebuiltin('Skin.Reset(' + skinsetting + ')')
    
    
def copySkinSettingToProperty(skinsetting, property, window):
    value = getValueFromSkinSetting(skinsetting)
    setValueToProperty(property, value, window)
