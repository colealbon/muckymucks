# convert an xml document into django models
import sys
import elementtree.ElementTree as etree

models = []
foreign_keys = []
attributes = []

class Model():
    model_name = ''
    
class ForeignKey():
    model_name = ''
    references = ''

class Attribute():
    model_name = ''
    attribute_name = ''
    
def add_attribute(ModelName, Name, Value):
    dontadd = False
    if attributes.count != 0:
        for attribute in attributes:
            if attribute.attribute_name == Name and attribute.model_name == ModelName:
                dontadd = True
    if dontadd == False:
        attribute = Attribute()
        attribute.model_name = ModelName
        attribute.attribute_name = Name
        attributes.append(attribute)
        
    # guessAttributeType using Value param

def walk_tree(node, level, parent):
    node_name = node.tag.title().replace('-','')
    reference_name = parent.title().replace('-','')
    add_model(node_name)
    add_foreign_key(node_name, reference_name)
    add_foreign_key(reference_name, node_name)
    for (name, value) in node.attrib.items():
        add_attribute(node_name, name.title().replace('-',''), value)
    children = node.getchildren()
    for child in children:
        walk_tree(child, level + 1, node.tag)
        
def add_model(Name):
    dontadd = False
    if models.count != 0:
        for model in models:
            if model.name == Name:
                dontadd = True
    if dontadd == False:
        model = Model()
        model.name = Name
        models.append(model)
        
def add_view(Name):
    dontadd = False
    if indexViews.count != 0:
        for indexView in indexViews:
            if indexView.name == Name:
                dontadd = True
    if dontadd == False:
        indexView = IndexView()
        indexView.name = Name
        indexViews.append(indexView)

def add_foreign_key( References, Name):
    dontadd = False
    if foreign_keys.count != 0:
        for foreign_key in foreign_keys:
            if foreign_key.model_name == Name and foreign_key.references == References:
                dontadd = True
    if dontadd == False:
        foreign_key = ForeignKey()
        foreign_key.model_name = Name
        foreign_key.references = References
        foreign_keys.append(foreign_key)
        # should prevent trying to add references to tables that dont exist

def parseXML(inFileName):
    doc = etree.parse(inFileName)
    root = doc.getroot()
    walk_tree(root, 0, '')
    
def createModels():
    models_py = open('models_generated.py',"w")
    models_py.writelines('from django.db import models\n')
    allowedfkeys = [] # we dont want to add an fkey if there's no table yet
    for model in models:
        print ("creating model" + model.name)
        models_py.writelines('class ' + model.name + ' (models.Model):\n')
        allowedfkeys.append(model.name)
        for foreign_key in foreign_keys:
            if foreign_key.model_name == model.name and foreign_key.references != '' and foreign_key.references in allowedfkeys:
                models_py.writelines('    ' + foreign_key.references + ' = models.ManyToManyField(' + foreign_key.references + ')\n')
        for attribute in attributes:
            if attribute.model_name == model.name and attribute.attribute_name != '':
                models_py.writelines('    ' + attribute.attribute_name + ' = models.CharField(max_length=200)\n')
        models_py.writelines('    pass\n\n')
    models_py.close()
    
def createURLs(AppName):
    # create the write string then save it to the file
    urls_py = open('../urls.py',"w")
    urls_py.writelines('from django.conf.urls.defaults import *\n')
    urls_py.writelines('from django.views.generic import list_detail\n\n')
    for model in models:
        urls_py.writelines('from django_muckymucks.muckymucks.models import ' + model.name + '\n')
        urls_py.writelines(model.name.lower() + '_list_info = {\n')
        urls_py.writelines('    \'queryset\' : ' + model.name + '.objects.all(),\n')
        urls_py.writelines('    \'template_object_name\' : \'' + model.name.lower() + '_list\',\n')
        urls_py.writelines('}\n')
    urls_py.writelines('urlpatterns = []\n')
    urls_py.writelines('urlpatterns = patterns(\'\',\n')
    for model in models:
        # need index, detail, results
        urls_py.writelines('    (r\'' + model.name.lower() + 's/$\', list_detail.object_list, ' + model.name.lower() + '_list_info),\n')
    urls_py.writelines(')\n\n')
    urls_py.close()

def main():
        #parseXML( '../extract/all.xml' )
        parseXML( '../work/extracted.xml' )
        createModels()
        #createURLs(args[1])
        #createTemplates(args[2])

if __name__ == '__main__':
    main()
