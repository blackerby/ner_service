# spaCy NER Service for Open Refine

Shamelessly adapted (stolen?) from [this gist](https://gist.github.com/b2m/6e2697ce182548a98320e4b7b7b885b6). Many thanks to [b2m](https://github.com/b2m) for doing all the hard work.

## Usage

### Spinning up the server with Docker

```bash
docker pull blackerby/ner_service
docker run -p 8000:8000 blackerby/ner_service
```

### Jython expression to use in OpenRefine

```python
import json, urllib, urllib2
url = 'http://localhost:8000/ner'
request_data = json.dumps({'text': value.encode('utf-8')})
request = urllib2.Request(url, request_data, {'Content-Type': 'application/json'})
response = urllib2.urlopen(request) data = json.load(response)
if data:
    return data[0]["label"]
else:
    return "No entity recognized"
```
