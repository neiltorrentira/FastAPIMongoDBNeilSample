# Sample FastAPI using MongoDB - REST API

Install package (install beforehand Python and MongoDB)
```
pip install fastapi pymongo uvicorn
```
Setup virtual env
```
virtualenv venv
OR
python -m virtualenv venv
```
Activate for Linux/Mac
```
source venv/bin/activate
```
Activate for Windows
```
source venv/Scripts/activate
```
Start localhost server - http://127.0.0.1:8000
```
uvicorn index:app --reload
```
Access FastAPI Docs
```
http://127.0.0.1:8000/docs
```