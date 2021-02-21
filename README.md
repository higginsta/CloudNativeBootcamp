# CloudNativeBootcamp

Projects from cloudskills.io [Cloud Native DevOps Bootcamp](https://portal.cloudskills.io/products/cloud-native-devops-bootcamp/) course. 
## 2/21/2021
### Setting up github repo and notes.



**Configuring Gitkraken**
- Straightforward setup

**Configuring VSCode with Github**
- Local commits work right off the bat, but I cannot push to Github (which I inited with GitKraken)
```
 git pull --tags origin master ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory Host key verification failed. fatal: Could not read from remote repository.
 ```
- Installed ssh-askpass
  - The x11 app prompted be to authorize the new host, but apparently it doesn't have permission to write to the known_hosts file5. I was able to manually approve it from the commandline, going to see if this update is properly pushed. 



## 2/19/2021

## 2/17/2021
### Week 2 Lecture, Scripting like a developer

- Check out how to setup up billing alerts for AWS and Azure.

- Since I am using a Chromebook I need to setup up the Linux VM
  - Run updates
    -VM
    - VS Code
    - GitKraken
  - Install the cli tools for AWS and Azure

- There is a lot in this lecture - rewatch!

### Week 2 Project Notes
**Setting up dev environment on my Chromebook**
- Update the VM
  - Uninstall Python 2.7
  - Install Python 3
    - Install pip, pylint
  - install Powershell 7.1.2
  - Install AWS cli
  - Install Azure cli
  - Update VS Code
  - Update GitKraken

**Reusuable and clean Python code**
[s3bucket.py](s3bucket.py)

- I have to use pip3 instead of pip
- Install boto3 client
- Configured the AWS cli (I set the default region to be something other an us-east-1)



## 2/11/2021
### Review Week 1 Projects

- Set up Github account
  - Using existing account
  
- Set up Azure account
  - Using existing account, cleaning up some resources 
  - Trying to change to the Dev/test pay as you go, but I don't have an active visual student account...
  - Figured out how to clean up some empty resource groups and resources.

- Setup up AWS account
  - Tried to use existing account
  - Set up new account 
  -
- Clean up inbox for email acconut 
  - Enabled 2 step
  - 
- Create Github Project
  - Create Github Action


## 2/10/2021
### Week 1 call
- Don't Panic
- Check out cloudnative-bootcamp Slack Channel 
- Projects to complete every week between class
- [x] Check out the projects
