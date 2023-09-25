import paramiko, sys, os

def exec_remote_commands(host, user, pwd, app_path, starter_dir_name, start_script, app_name, extension_file):
    connection_context = paramiko.SSHClient()
    connection_context.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection_context.connect(hostname = host, username = user, password = pwd)
    
    # Command to make to the server that start application
    working_dir="cd "+app_path
    make_script_exec= working_dir+ " && chmod +x *.sh && mkdir -p "+starter_dir_name
    move_script_to_dir= working_dir +" && mv *.sh *."+extension_file +" " +starter_dir_name
    start_app= working_dir+starter_dir_name + " && ./"+start_script +" --name "+app_name

    commands =[make_script_exec, move_script_to_dir,start_app]
    print("MAKE SCRIPTS EXECUTABLE ==========================> " + make_script_exec)
    print("MOVE SCRIPTS AN ARTIFACT TO FINAL EXEC DIR ==========================> " + move_script_to_dir)
    print("LUNCH THE APPLICATION ==========================> " + start_app)

    try:
        for cmd in commands:
            stdin, stdout, stderr = connection_context.exec_command(cmd)
            for output in stdout.readlines () :
                print(output)
                print(stdin)
                print(stderr)
                
    except Exception as e :
        print("exec command exception ---> "+ str(e))
    connection_context.close()
    
try:
    host_server=sys.argv[1]
    user=sys.argv[2] 
    password=sys.argv[3]
    app_path=sys.argv[4] 
    directory_name=sys.argv[5] 
    file_started=sys.argv[6] 
    application_name = sys.argv[7] 
    extension_copy_file = sys.argv[8]
    
    print('Hostname is --> : '+ host_server)
    print('The Application Home Path is a '+ app_path)

    if len(sys.argv) > 7:
        exec_remote_commands(host_server, user, password, app_path, directory_name, file_started, application_name, extension_file) 
    else:
        print("The number of params for this operation is incorrect")
except Exception as e:
    print("Please Enter the corrects params for this operation: "+ str(e))