import sys, os, logging
from artifactory import ArtifactoryPath
from zipfile import ZipFile

def get_scripts_from_artifactory(url, token, path, folder_name):
    path = ArtifactoryPath(url, verify=False, apikey=token)
    
    with path.archive(archive_type="zip", check_sum=False).open() as archive:
        with open(os.getewd()+"/tmp_file.zip", "wb") as out:
            out.write(archive.read())
            
    with ZipFile("tmp_file.zip",'r') as folder:
        folder.extractal1 (folder_name)
        
    if os.path.isfile("tmp_file.zip"):
        os.remove("tmp_file.zip")
        
try :
    urlArtifact=sys.argv[1]
    token=sys.argv[2]
    path=sys.argv[3]
    folderName=sys.argv[4]
    
    print('The URL that we are going to Download is ---› : '+ urlArtifact) 
    print('The Path to save folder is ---> : '+ path)
    print('The folder name is ---> :' + folderName)
    print( 'The all args is--->：'+ str(sys.argv))

    if len(sys.argv) > 4:
        get_scripts_from_artifactory (urlArtifact, token, path, folderName)
        print("Alle script for this project is in the folder: "+folderName)
    else:
        logging.critical("The number of params for this operation is incorrect")
except Exception as e:
    logging.exception("Please Enter the corrects params for this operation: "+ str(e))