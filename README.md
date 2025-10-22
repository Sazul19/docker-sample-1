


build docker image
``` 
docker build -t student-grade-predictor .

```
run the container
```
docker run -d -p 8000:8000 student-grade-predictor


```

test API
```
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{"hours": 6}'

```