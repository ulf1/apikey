# apikey

## Installation 
The `apikey` [git repo](http://github.com/ulf1/apikey) is available as [PyPi package](https://pypi.org/project/apikey)

```
pip install "apikey>=0.2.*"
pip install git+ssh://git@github.com/ulf1/apikey.git
```

## Usage
Store in default location `$HOME/.apikey-store` 

```
from apikey import save_apikey, read_apikey

save_apikey("service1", "supersecret")
save_apikey("service2", "donttellanyone")
save_apikey("service3", "aboutthiskey")

key1 = read_apikey("service1")
key2 = read_apikey("service2")
key3 = read_apikey("service3")
```

Store in a specific file

```
save_apikey("service42", "topsecretkey", filename="/srv/.secretkeys")
key = read_apikey("service42", filename="/srv/.secretkeys")
```


## Commands
Install a virtual environment

```
python3.6 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


Python commands

* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `pytest`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`
