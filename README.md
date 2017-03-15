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

### Nodejs

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