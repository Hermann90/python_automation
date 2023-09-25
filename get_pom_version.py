import os, sys, os.path

"""
   Params : argv[1] directory_name ==> path to pom.xml to be archived
   command to call : python3 get_pom_version path/to/pom.xml
"""

def get_pom_version(input_file_name):
    import xml.etree.ElementTree as ET
    
    ns = "http://maven.apache.org/POM/4.0.0"
    tree = ET.parse(input_file_name)
    root = tree.getroot()
    version = tree.getroot().find("{%s}version" %ns)
    
    return version


try:
    directory_name=sys.argv[1]

    if os.path.exists(directory_name):
        os.environ['VERSIONAPP'] = get_pom_version (directory_name).txt
        VERSION = os.getenv('VERSIONAPP')
        print(VERSION)
    else:
        print("We don't have a version flag in this file")
except:
    print('Please pass the pom.xmi directory')