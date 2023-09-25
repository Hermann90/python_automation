import paramiko, sys

def send_file_to_remote_server(host, username, password, localpath, remotepath):
    paramiko.util.log_to_file("paramiko.log")

    # Open a transport then Authentication 
    transport = paramiko.Transport((host,22))  
    transport.connect(None,username,password)

    # Go!    
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath,remotepath)
    #sftp.get(filepath,localpath)

    # Close
    if sftp: sftp.close()
    if transport: transport.close()

try:
    host_server = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    app_remote_path=sys.argv[4]
    file_local_path=sys.argv[5]
    file_name=sys.argv[6]
    
    print("----------------> host_server : "+host_server)
    print("----------------> username : "+username)
    print("----------------> password : "+password)
    print("----------------> app_remote_path : "+app_remote_path)
    print("----------------> file_local_path : "+file_local_path)
        
    if len(sys.argv) > 6:
        remotepath = app_remote_path + file_name
        print("----------------> remotepath1 : "+remotepath)

        send_file_to_remote_server(host_server, username, password, file_local_path, remotepath)
        print(" ==================> SUCCESS TO UPLOAD FILE ")
    else:
        print(" ==================> ARGUMENT NUMBER INCORECT ")
except Exception as e:
    print("Please enter the correct params for this operation "+str(e))
