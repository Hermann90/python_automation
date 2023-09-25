import paramiko, sys, os.path, logging

def send_jar_file(directory, file, host, user, appPath, keyStore):

    privateKey = paramiko.RSAKey.from_private_key_file(keyStore)
    
    # Create a paramiko connexion context
    connectionContext=paramiko.SSHClient()
    connectionContext. set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print("connection user :", user)
    print("connection directory: ", directory) 
    print("connection file path", appPath+file)
    
    connectionContext.connect(hostname=host,port=22, username=user, pkey=privateKey)
    
    print("connection directory : ", directory)
    print("connection file path : ", appPath+file)
    
    sftp = connectionContext.open_sftp()
    try:
        print("connection directory : ", directory)
        print("connection file path : ", appPath+file)
        sftp.put(directory, appPath+file) 
    except Exception as e :
        logging.exception("A problem occurred when sending the files "+ str(e))
    connectionContext.close()
    print('File Uploaded---> : '+ file)
    

    #uploading all scripts for the installation and managing the application to the remote server
def sftp_upload_all_script(host, username, local, remote, keyStore):
    connectionContext = paramiko.SSHClient()
    connectionContext.set_missing_host_key_policy(paramiko .AutoAddPolicy())
    connectionContext. connect(hostname = host, username = username, pkey = keyStore)
        
    create_work_dir="cd "+appPath+" && mkdir -p "+local
    commands =[create_work_dir]
    try:
        for cmd in commands:
            stdin, stdout, stderr = connectionContext.exec_command(cmd)
            for output in stdout. readlines() :
                print(output)
    except Exception as e:
        logging. exception("exec command exception ---> "+ str(e))
        
    sftp = connectionContext.open_sftp()
    try :
        if os.path.isdir(local):
            for f in os.listdir(local):
                if not os.path.isdir((os.path.join(local+f))):
                    print("uploading:", os.path.join(local+f),os.path.join(remote+f))
                    sftp.put(os.path.join(local+f),os.path. join(remote+f))
                    continue
                    print('mkdir: ',os.path.join(remote+f), "returning: ", sftp.mkdir(os.path. join(remote+f)))
                        
                    for d in os.listdir(os.path.join(local+f)) :
                        if(os.path.isdir(os.path.join(local+f+"/"+d))):
                            sftp_upload_al1_script(host, username, local+f+"/" , remote+f+'/')
                            continue
                        print("uploading: ",os.path.join(local+f+"/"+d),os.path.join(remote+f+'/'+d))
                        sftp.put(os.path.join(local+f+"/"+d),os .path.join(remote+f+'/'+d))
        else:
            sftp.put(local, remote) 
    except Exception as e:
        print('exception:',e)
    connectionContext.close()
    
try:
    directoryName=sys.argv[1]
    fileName=sys.argv[2]
    hostServer=sys.argv[3]
    user=sys.argv[4]
    appPath=sys.argv[5]
    keystore=sys.argv[6]
    PROG_STARTER_DIR=os.getenv('PROG_STARTER_DIR')+"/"
    print('The Path of file is ---> ', directoryName)

    print('The file to Upload is : ', fileName)
    print ('Hostname is :', hostServer)
    print( 'User Name is :', user)
    print ('The Application Home Path is'+ appPath)
    print('The Application keystore is ---> ', keyStore)
    print("Folder for all scripts"+PROG_STARTER_DIR)

    if len(sys.argv) > 6:
        send_jar_file(directoryName, fileName, hostServer, user, appath, keyStore)
        privateKey = paramiko. RSAKey.from_private_key_file (keyStore)
        sftp_upload_all_script(hostServer, user, PROG_STARTER_DIR, appath+PROG_STARTER_DIR, privateKey)
    else:
        logging.critical("The number of params for this operation is incorrect")
    except Exception as e:
        logging.exception("Please Enter the corrects params for this operation: "+ str(e))