# django_DRF
- In this POC , we have a database model called Article which is used throughout project for building APIs.
- This POCs is totally based on Python Django Rest Framework (DRF).
- I have make use of Both Functional and class based API View for building APIs but all of them do same CRUD Operation.
### API views used :
- Normal API using Just Django CRUD with @csrf_exempt decorator
- api_view decorator
- APIView class
- GenericAPIView class
- ViewSet class
- GenericViewSet
- ModelViewSet

### Permission Used
- IsAuthenticated

### Authentication Used
- Basic Authentication
- Session Authentication
- Token Authentication

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+
* Virtual Environment

### To install virtual environment on your system use:

**bash**
```
pip install virtualenv
```
**or**
```
pip3 install virtualenv #if using linux(for python 3 and above)
```

## Installation and Running :

**bash**
```
git clone https://github.com/himanshugupta0158/DRF_poc.git
```
- This will clone whole project

```
virtualenv venv 
```   
**or**
```
virtualenv venv -p python3 #if using linux(for python 3 and above)
```
*NOTE : 'venv' is the name of your isolated virtual environment for python.*
```
venv\Scripts\activate # for windows
```
**or**
```
source venv/bin/activate # for linux
```
# install required packages for the project to run
```
pip install django djangorestframework
```
