Trying to follow instructions from https://docs.docker.com/installation/ubuntulinux/
I first installed the ubuntu package and removed it, since it seemed to be a 
better idea to use a more upto-date package.

>>> sudo sh -c "echo deb https://get.docker.com/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list

did  not do what I expected. So I manually created the file 

>>> sudo vi /etc/apt/sources.list.d/docker.list 

and inserted the following line
>>> deb https://get.docker.com/ubuntu docker main

I then ran 

>>> sudo docker run -i -t ubuntu /bin/bash

which seemed to load a new ubuntu image and give me a root terminal. However I did not understand where this image was located on the hard drive.


Having installed this, I will try to move back to https://www.codeschool.com/blog/2014/10/21/containing-world-docker/


>>> docker run hello-world 
did not work

However, 
>>> sudo docker run hello-world 
worked 
with the following output:
>>> Unable to find image 'hello-world:latest' locally
hello-world:latest: The image you are pulling has been verified
7fa0dcdc88de: Pull complete 
ef872312fe1b: Pull complete 
511136ea3c5a: Already exists 
Status: Downloaded newer image for hello-world:latest
Hello from Docker.
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (Assuming it was not already locally available.)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

For more examples and ideas, visit:
 http://docs.docker.com/userguide/
rbiswas@accelerator:~/tmp/scratch/docker$ vi README.rst

