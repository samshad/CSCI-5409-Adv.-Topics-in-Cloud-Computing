FROM amazonlinux:2022

# Update the system and install required packages
RUN yum -y update && \
    yum -y install python39 python3-pip python3-devel zip && \
    yum clean all

# Upgrade pip and install virtualenv
RUN python3.9 -m pip install virtualenv
