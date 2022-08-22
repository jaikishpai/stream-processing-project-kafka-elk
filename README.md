# stream-processing-project-kafka-elk
A small project for processing Streaming data using kafka and ELK stack

<img width="1192" alt="streaming-data-architecture" src="https://user-images.githubusercontent.com/35526514/185790315-744e6eda-edaf-459b-93d3-019529dd570a.png">

## Prerequistes:
 - `docker` - https://www.docker.com/
 - java - https://www.oracle.com/java/technologies/downloads/
 - `logstash` - https://www.elastic.co/guide/en/logstash/current/installing-logstash.html

## Environment:
- Ubuntu 20.0.4

## Docker
`docker-compose.yml` contains all the services which are required to run this project. The file contains the following serivces - 
 - kafka
 - kafka-manager
 - zookeeper
 - elasticsearch
 - kibana
 
 The below commands are used :
 - `docker compose up` # to start the docker and create containers for each service.
 - `docker ps` # to list the containers running on the machine along with their status and ports.
 - `docker compose down` # to stop the docker containers.

## Kafka and Kafka Manager
 - Kafka will be running on port `9092` and cn be accessible through port 29092 for external services (for example the producer service).
 - Kafka-Manager is an UI interface running on port `9000` for Kafka which can be used to create clusters and topics. Kafka manager helps us in easy monitring of the service. Like the incoming messages, connected producers, topics, offset etc.
 
 ![image](https://user-images.githubusercontent.com/35526514/186014667-a7992ca5-d29b-42d7-9963-938e9e72a067.png)
 
 
## logstash configuration:
- configuration file should be placed in `/etc/logstash/conf.d` folder.
- commands for logstash:
 - `sudo systemctl start logstash` # to start the logstash services.
 - `sudo systemctl status logstash` # to check status of logstash service
 - `sudo systemctl stop logstash` # to stop logstash services.
- logstash logs are available in the location `/var/logs/elasticsearch`
 

![image](https://user-images.githubusercontent.com/35526514/185790911-d196aefb-bf0d-4d7a-908f-5ab8a9f11802.png)


## Elasticsearch and Kibana
 - Elasticsearch is running on port `9200` and Kibana is running on port `5601`.
 







