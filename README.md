# apikey

## Installation via pip
The `apikey` [git repo](http://github.com/ulf1/apikey) is a private package

```
pip install git+ssh://git@github.com/ulf1/apikey.git
```

with GemFury

```
FURY_AUTH="<deploy token>" pip install apikey --extra-index-url https://${FURY_AUTH}:@pypi.fury.io/kmedian/
```

## Install via requirements.txt
when using `apikey==0.1.1` in `requirements.txt`, 
add on top of `requirements.txt`:

```
# Access private packages on gemfury
--index-url https://${FURY_AUTH}:@pypi.fury.io/kmedian/
...
```

Set `FURY_AUTH` with the deploy token before pip commands:

```
FURY_AUTH="<deploy token>"
pip install -r requirements.txt
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
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `pytest`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Publish on GemFury pypi server: `python setup.py sdist && twine upload -r fury dist/*`
