import json

def getDesc(lang_code, dict):
    if i == None:
        return ''
    descs = i.get('descriptions')
    if descs == None:
        return ''
    lang=descs.get(lang_code)
    if lang == None:
        return ''
    value=lang.get('value')
    if value == None:
        return ''
    return value

def getID(dict):
    return dict.get('id')

def getLangString(lang_code, dict):
    if i == None:
        return ''
    labels = i.get('labels')
    if labels == None:
        return ''
    lang=labels.get(lang_code)
    if lang == None:
        return ''
    value=lang.get('value')
    if value == None:
        return ''
    return value

def getCountry(dict):
    return getValuesFromPropertyID(dict, "P17")

def getValueFromProperty(element):
    mainsnak = element.get('mainsnak')
    if mainsnak == None:
        return ''
    datavalue = mainsnak.get('datavalue')
    if datavalue == None:
        return ''
    value = datavalue.get('value')
    if value == None:
        return ''
    itemId = value.get('id')
    if itemId == None:
        return ''
    return itemId

LIST_DELIMITER=','
#return as a list separated by LIST_DELIMITER
def getRegions(dict):
    return getValuesFromPropertyID(dict,'P131')
def getTypes(dict):
    return getValuesFromPropertyID(dict,'P31')
def getValuesFromPropertyID(dict, propertyID):
    items = []
    if i == None:
        return ''
    claimsList = i.get('claims')
    if claimsList == None:
        return ''
    values = claimsList.get(propertyID)
    if values == None:
        return ''
    for element in values:
        items.append(getValueFromProperty(element))
    ListString = ""
    for index, item in enumerate(items):
        if index==0:
            ListString=item
        else:
            ListString = ListString+LIST_DELIMITER+item
    return ListString