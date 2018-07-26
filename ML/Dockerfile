FROM centos
RUN yum -y install which
### setup python ####
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN yum -y install epel-release
RUN yum -y install libgomp
RUN pip install gunicorn flask mxnet pandas opencv-python sklearn scipy tweepy
### setup R ####
RUN yum -y install R
COPY load.R /
RUN yum -y install libcurl-devel
RUN Rscript /load.R
### setup repositories ####
RUN yum -y install git
RUN mkdir -p /projects
RUN cd /projects && git clone https://github.com/joebluems/IrisEnsembleAPI.git
RUN cd /projects && git clone https://github.com/joebluems/MxNetImageAPI.git
