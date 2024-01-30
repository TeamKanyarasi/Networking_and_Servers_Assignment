# Herovired_devops_assignment

## Question 1
Deploy a website on localhost using either apache2 or nginx. Create a DNS name for this website as ‘awesomeweb’.

1. Install Apache2 :
   - First, we need to install Apache2 on our system. Downloaded [wampserver3.3.0_x64](https://sourceforge.net/projects/wampserver/) application.
2. Start Apache2 :
   - After installing Apache2, you need to start the Apache2 service. 
3. Create your website:
   - Create your website files (HTML, CSS, JavaScript, images, etc.) and organize them in a directory. 
   - Here we have utilised Hostit directory with all the required website files inside it.
![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/cc222a1c-c622-4ee7-a30d-4c73b03402cd)

4. Move your website to the Apache2 directory:
    - Move your website directory to the /var/www directory, which is the default directory for Apache2 to serve web pages.
    - You can find the “Hostit” website directory in the /wamp64/www directory of the wampserver folder.
![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/886db07b-16bd-4ad1-9aa6-3630e2dcc168)

5. Access your website:
    - After moving your website to the Apache2 directory, you can access it by opening a web browser and going to http://localhost
![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/72a0fc39-9a4f-4c7b-ba68-a79614155396)

6. Create a DNS name:
    - As per requirement, we need to create a DNS name for this website as ‘awesomeweb’.
    - DNS Name : DNS stands for Domain Name System. It is a system that translates human-readable domain names, such as example.com, into the numerical IP addresses that computers use to identify each other on the internet.
![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/8665cf40-c7fe-4b03-8159-a469917b00e7)

    - In order to change the DNS name of the website, we need to add ServerName ‘awesomeweb’ to the httpd-vhosts conf file in the wamp64/bin/apache/apache2.4.54.2/conf/extra folder.
7. Access the website after DNS name change:
    - After changing the DNS name in the above step, we need to restart all the servers in order to reflect our latest changes in the web server.
    - Enter http://awesomeweb in the browser page and you’ll find the application hosted on this particular DNS name.
![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/83faa206-6140-4f0f-901f-435b47bb9348)


## Question 2
A website can have many subdomains and different services are running on them. A Python script to check the status of the subdomains which are up or down. The script should automatically check the status every min and should update it in tabular format on the screen


1.	A subdomain is a prefix added to a domain name to separate a section of your website. Site owners primarily use subdomains to manage extensive sections that require their own content hierarchy, such as online stores, blogs, job boards or support platforms.
2.	In this task we need to create a python script which automatically check the status of list of subdomains which are up or down.
3.	The python script uses the requests library to send HTTP requests to the subdomains and check their status. Use the following command in the terminal to install the requests library : pip install requests

![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/bdc0cb4f-703c-491f-bdd0-85e744ec754d)

4.	The prettytable library is used to display the status of the subdomains in a tabular format on the screen. : pip install prettytable
5.	you can run the script by navigating to its directory in a terminal and running the command : python subDomains.py

![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/8d5c5f46-f339-4784-b134-557ac82b386f)

6.	Output :

![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/eb62b5da-409b-45bb-8e54-31454ec75632)

## Question 3:  Hosting and Scanning a website on Virtual Machine

### How to Install VirtualBox
Here's a step-by-step guide to installing Oracle VirtualBox on your Windows, macOS, or Linux computer:
#### Step 1: Download VirtualBox
1.	Go to the official VirtualBox website: https://www.virtualbox.org/
2.	Click on the "Downloads" link in the top navigation menu.
#### Step 2: Choose the Correct Package
1.	On the Downloads page, you'll see various packages for different host operating systems. Select the appropriate package for your OS (e.g., Windows, macOS, or Linux).
#### Step 3: Install VirtualBox
-	Download the installer for Windows and double-click on the downloaded file to start the installation.
-	Follow the on-screen instructions and accept the license agreement.
-	Choose the components you want to install and the installation path.
-	Complete the installation process.
#### Step 4: Launch VirtualBox
1.	Once the installation is complete, you can launch VirtualBox from your application menu.
2.	Install Nginx inside the Ubuntu machine and host a website.
 
VM running on Oracle VirtualBox :

![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/d617ee85-a3aa-4e3b-b5b5-6603b3ea11b7)

Status of Nginx :

 ![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/4ec0d699-a8da-40f8-8cfb-81004e0d4c18)

Website successfully hosted on localhost :

![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/4e1ea7ff-0504-4fa9-af53-23e5b34b0cb5)

Output of the Nmap Scan :

![image](https://github.com/TeamKanyarasi/Herovired_devops_assignment/assets/139607786/10dc2720-e1a2-40a6-9c95-4edffd87906d)
