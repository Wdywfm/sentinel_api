# FastAPI application
REST API to work with polygons

## Dependencies
```text
fastapi==0.110.0
SQLAlchemy==2.0.28
GeoAlchemy2==0.14.6
pystac-client==0.7.6
shapely==2.0.3
```

## Database
```text
PostgreSQL 16.2
PostGIS 3.4
```

## Usage
```text
export db_username=<username>
export db_password=<password>
export db_name=<name>
cd src
uvicorn api_app.main:app --reload
```
Navigate to ```127.0.0.1:8000/docs``` to try out API requests.

```examples/polygon_1.json``` and ```examples/polygon_2.json``` can be used as polygon input examples