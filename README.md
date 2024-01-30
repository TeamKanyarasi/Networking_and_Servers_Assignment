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
4. Move your website to the Apache2 directory:
    - Move your website directory to the /var/www directory, which is the default directory for Apache2 to serve web pages.
    - You can find the “Hostit” website directory in the /wamp64/www directory of the wampserver folder.
5. Access your website:
    - After moving your website to the Apache2 directory, you can access it by opening a web browser and going to http://localhost
7. Create a DNS name:
    - As per requirement, we need to create a DNS name for this website as ‘awesomeweb’.
    - DNS Name : DNS stands for Domain Name System. It is a system that translates human-readable domain names, such as example.com, into the numerical IP addresses that computers use to identify each other on the internet.
    - In order to change the DNS name of the website, we need to add ServerName ‘awesomeweb’ to the httpd-vhosts conf file in the wamp64/bin/apache/apache2.4.54.2/conf/extra folder.
8. Access the website after DNS name change:
    - After changing the DNS name in the above step, we need to restart all the servers in order to reflect our latest changes in the web server.
    - Enter http://awesomeweb in the browser page and you’ll find the application hosted on this particular DNS name.
