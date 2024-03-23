### Development

Install dependencies:

```
python -m pip install flask requests bs4
```

Run the app:

```
python __init__.py
```

### Docker

Build the image:

```
docker build -t app .
```

Run the container:

```
docker run -it --name flask-app -p 5000:5000 app
```
