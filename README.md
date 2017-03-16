# Neo4jPythonVega

> **Objective** : display stats and graphs from social networks stored into Neo4j

## Setup

* Flask : python server
* Jinja2 : data injection from server into html (comes with Flask)
* Bootstrap template : [gentelella](https://github.com/puikinsh/gentelella), [demo](https://colorlib.com/polygon/gentelella/morisjs.html)
* [Vega](https://vega.github.io/vega/examples/) : plot and graph library 

Flask and Jinja2 : conda install
Bootstrap : clone github
Vega :  *TODO*

### Neo4j

Launch server and python script to import social data (see <https://github.com/Tofull/social_graph>)
``` sh
$ /home/nil/Utils/neo4j-community-3.1.1/bin/neo4j start
``` 

* Check that server is up at <http://localhost:7474/browser/>
* On the web interface, check that the social data has been imported


### Nodejs (unecessary)

* Instruction for Debian/Ubuntu: <https://nodejs.org/en/download/package-manager/>

Installation of v7

``` sh
$ curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
$ sudo apt-get install -y nodejs build-essential
$ sudo npm install -g grunt-cli     # for Bootstrap (not used)
```

> *Note*: build-essential is not required

### Icons

List available [here](https://www.w3schools.com/icons/fontawesome_icons_webapp.asp)

### Template

Bootstrap gentelella

> TODO : remove all unused css and js files

## Server - Client

* Launch server

``` sh
$ python server.py 
```

Check that it is working at : <http://127.0.0.1:5000/>