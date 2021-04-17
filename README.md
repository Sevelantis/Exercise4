# Credentials
Simple Flask Docker cloned from https://github.com/nikos/python3-alpine-flask-docker

Repository created for educational purposes.

# how to run
docker needs to be installed
```
git clone https://github.com/Sevelantis/Exercise4
cd Exercise4/
sudo make build
sudo make run
```
## example POST
```
curl -X POST -H "Content-Type: application/json" -d @example_json.json 0.0.0.0:5000/postjson
```
