# Some Commands

- Connecting to VM: Copy command from AWS EC2 console.


- Get environment up to date:
  - ```sudo apt update```
  - ```sudo apt upgrade```


- Python:
  - Python should be on the installation.
  - ```alias python=python3```
  - ```python --version```


- MySQL:
  - Followed [some online](https://linuxbeast.com/tutorials/aws/how-to-install-mysql-on-amazon-ec2-ubuntu-18-04/) instructions, with some modifications.
  - See ```.secret_stuff``` for commands I used. Once again, putting this stuff in the project is a __really bad idea.__
  - ```sudo service mysql status```: mysqld should automatically start on boot/reboot.
  - You can use the Ubuntu ```service``` command to manage. <br> https://www.journaldev.com/39332/ubuntu-start-stop-restart-services
  - Enable remote access:
    - ```mysqld.cnf``` file.
      - ```/etc/mysql/mysql.conf.d/mysqld.cnf```
      - Change bind addresses to ```0.0.0.0```, which is a really bad idea.
      - Restart mysql: ```sudo service restart mysql```


- Install Git: ```sudo apt install git``` (It may already be there).


- Configure remote access to MySQL by configuring security group rules.
  - Allow access for 3306 from 0.0.0.0. 
  - Once again, a really bad idea.
  - We will cover VPC and security groups in a future lecture.
  - Test access: 
    - Terminal: mysql -h ec2-54-196-132-219.compute-1.amazonaws.com -u dbuser -p
    - Set up connection in DataGrip or some other DB IDE.
  - Note: The DNS name and IP address may change over time. We will resolve later.


- Set up application configuration:
  - Database:
    - Create database and table.
    - Add test row.
  - Git clone microservice. We will automate deployment via Git and pipelines later.
  - Make sure ```pip``` is installed.
  - ```pip install requirements.txt```
  - Write a script to set environment variables. Once again, a bad idea. We can configure more securely later. ```app_env.sh```


- Modify security group to allow ```5001```, cross your fingers and try it.
  - Make sure you use the public IP address or DNS name.
  - ```curl ec2-54-196-132-219.compute-1.amazonaws.com:5001/api/students/uni123```

