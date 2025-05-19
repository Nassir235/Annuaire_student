FROM python:3.9-slim-buster

WORKDIR /annuaire_student

RUN apt-get update && apt-get install -y gcc wget
RUN wget https://dlm.mariadb.com/2678574/Connectors/c/connector-c-3.3.3/mariadb-connector-c-3.3.3-debian-bullseye-amd64.tar.gz -O - | tar -xz
RUN apt-get update && apt-get install -y libmariadb3 libmariadb-dev
RUN pip install --upgrade pip
RUN pip install mariadb==1.0.11 
#RUN wget mariadb-11.6.2-linux-systemd-x86_64.tar.gz -O - | tar -xz
#RUN wget https://dlm.mariadb.com/3964816/MariaDB/mariadb-11.6.2/repo/ubuntu/mariadb-11.6.2-ubuntu-jammy-arm64-debs.tar -O - | tar -xz
RUN apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential -y

#RUN apt-get update && apt-get install -y libmariadb3 libmariadb-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

EXPOSE 5000

ENV FLASK_APP=run.py
#CMD ["python", "run.py", "--host=0.0.0.0"]
CMD ["flask", "run", "--host", "0.0.0.0", "--no-debugger"]

#docker build -t hda_python:annuaire_student .
#docker rmi hda_python:annuaire_student .
#docker run -it -p 5000:5000 --rm --name as1 hda_python:annuaire_student
#docker run -it -p 5000:5000 -v "data:/annuaire_student/instance" --rm --name as1 hda_python:annuaire_student


