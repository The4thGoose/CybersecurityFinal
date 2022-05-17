import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('HOSTNAME', username="USERNAME", password="PASSWORD")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("INSERT COMMAND HERE")
time.sleep(1)
