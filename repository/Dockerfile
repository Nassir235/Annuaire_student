#utilisez une image mariadb de base
FROM mariadb:latest

#set the root password
ENV MYSQL_ROOT_PASSWORD=266139

#Expose le port au lieu de 3306 on utilise 3315
EXPOSE 3306

#initialisatio de la base de donnees
COPY init.sql /docker-entrypoint-initdb.d/

#Volume pour les donnees
VOLUME /var/lib/mysql

#
#docker build -t hda_mariadb:annuaire_student .
#docker rmi hda_mariadb:annuaire_student .