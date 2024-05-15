docker rm -f blip2-api
# cd app
# uvicorn main:app --reload
docker build -t blip2-api .
docker run --name blip2-api -p 8004:8004 blip2-api