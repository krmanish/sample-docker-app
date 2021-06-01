# sample-docker-app
Dockerize a sample Flask app that can be accessed from outside container.

## Prereqsites
<ol>
  <li>Works best on Linux Distro. tested with Fedora 29</li>
  <li>Should have docker installed</li>
  <li>Should have <strong>python3</strong> and all its required packages such as <strong>pip, flask</strong> etc. installed</li>
</ol>

## Setup & Run
* ```git clone https://github.com/krmanish/sample-docker-app```
* ```cd sample-docker-app```
* ```python3 apps.py```  # Verify if server running fine at http://0.0.0.0:5000. Kill this if all is well
* Next Build container: ```
    sudo docker build --tag sample-flask-app . ```
 
* Finally run the container: ```sh sudo docker run --name sample-flask-app -p 5000 --expose 5000 sample-flask-app```

That's it, if all goes well, you should be able to see a server running at http://172.17.0.2:5000 or something similar ip.


## Test container app using CURL
* ```curl -X GET http://<container ip address>:5000/hello```
* ```curl -X GET http://<container ip address>:5000/ack/hello-world```
* ```curl -X POST http://<container ip address>:5000/postme -d '{"foo": "wah", "bar": 12}' -H 'content-type: application/json'```

### Other Useful Docker commands
* Remove Container: ``` sudo docker rm sample-flask-app [or use container id]```
* Kill running container: ```sudo docker kill sample-flask-app ```
 


