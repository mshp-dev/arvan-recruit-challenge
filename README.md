
# Python Django REST-API for IP Geo-Location information

In this branch, i started a django project and and installed djangorestframework and geocoder to build an REST API for selective part of the task.


## Installation

Install ip_info with python

```bash
  python -m pip install -r requirements.txt
  cd ip_info
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
```
    
## API Reference

#### Get info of IPv4

```http
  POST /api/ip-info
```

| Parameter | Type     | Description                     |
| :-------- | :------- | :-----------------------------  |
| `ip`      | `string` | **Required**. The IPv4 Address  |

##### Use with Basic Authentication


## Documentation

[Documentation](https://djangoproject.com)

