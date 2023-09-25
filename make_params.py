import json, os, sys

def get_pom_version (pom_file):
    import xml.etree.ElementTree as ET
    ns = "http://maven.apache.org/POM/4.0.0"
    tree = ET.parse(pom_file)
    version = tree.getroot().find ("{%s}version" % ns)
    return version.text

try :
    directory_to_pom_file=sys.argv[1]
    current_git_branche=sys.argv[2]
    if os.path.exists(directory_to_pom_file) and (len(current_git_branche)>0):
        
        print("The path to pom.xml file is : "+ directory_to_pom_file)
        print("The Git Branch That we are working on is : " + current_git_branche)
        
        app_version = get_pom_version(directory_to_pom_file)
        
        print("The version of the App ies : "+app_version)
        paramsDict = dict()
        
        match current_git_branche: 
            case "main":
                paramsDict = {"NEXUS_REPO_NAME" : os.getenv('NEXUS_REPO_NAME_PROD'), "DEPLOY_HOST_NAME" : os.getenv('HOST_NAME_PROD'),"DATABASE_URL" : os.getenv('DATABASE_URL_PROD'),
                              "DATABASE_NAME" : os.getenv('DATABASE_NAME_PROD')}
            
            case "recette":  
                paramsDict = {"NEXUS_REPO_NAME" : os.getenv('NEXUS_REPO_NAME_QA'),"DEPLOY_HOST_NAME" : os.getenv('HOST_NAME_QA'), "DATABASE_URL" : os.getenv('DATABASE_URL_QA'),
                              "DATABASE_NAME" : os.getenv('DATABASE_NAME_QA')}
            
            case _:
                paramsDict = {"NEXUS_REPO_NAME" : os.getenv('NEXUS_REPO_NAME_DEV'), "DEPLOY_HOST_NAME" : os.getenv('HOST_NAME_DEV'), "DATABASE_URL" : os.getenv('DATABASE_URL_DEV'),
                              "DATABASE_NAME" : os.getenv('DATABASE_NAME_DEV')}

        paramsDict.update({"DATABASE_PORT" : os.getenv('DATABASE_PORT'), "OPTION_CREATE_DB_IF_NOT_EXIST" : os.getenv('OPTION_CREATE_DB_IF_NOT_EXIST'), "DB_PASSWORD" : os.getenv('DB_PASSWORD'),
                           "DB_PORT" : os.getenv('DB_PORT'), "DB_USER" : os.getenv('DB_USER'), "NEXUS_USER" : os.getenv('NEXUS_USER'), "NEXUS_PASSWORD" : os.getenv('NEXUS_PASSWORD'), "APP_VERSION": app_version,
                           "DEVOPS_SCRIPTS_REPO" : os.getenv('DEVOPS_SCRIPTS_REPO'), "APP_USER":os.getenv('APP_QA_USER'), "APP_PASSWORD":os.getenv('APP_QA_PASSWORD'), "APP_PATH":os.getenv('APP_DIRECTORY')})

        jsonString = json.dumps(paramsDict)
        jsonFlle = open("data.json","w")
        jsonFlle.write(jsonString)
        jsonFlle.close()
    
        print("The config ENV and params is : "+ str(paramsDict))
    else:
        print("We don't have a version flag in the pom.xml file, or git branch isn't correct")
except Exception as e: 
    print("Please pass the pom.xml directory: "+ str(e))