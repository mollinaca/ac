FROM python:3.4.3
USER root

RUN apt-get update
ENV TZ JST-9
ENV TERM xterm
ENV HOSTNAME ac_python

RUN apt-get update -y
RUN apt-get install python3-numpy -y
RUN apt-get install python3-scipy -y
RUN apt-get install python-scikits-learn -y
#RUN pip install --upgrade pip
#RUN pip install --upgrade setuptools
RUN pip install numpy==1.8.2
#RUN pip install scipy==0.13.3 

RUN echo "# add" >>/root/.bashrc
RUN echo "alias ll='ls -l'" >>/root/.bashrc
RUN echo "export PS1='\n@\[\e[32m\]ac_python\[\e[0m\] \W # '" >>/root/.bashrc
RUN echo "cd ~/code" >>/root/.bashrc
