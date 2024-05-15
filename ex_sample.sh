curl -X POST 'http://127.0.0.1:8004/caption' \
    -H 'accept:application/json' \
    -H 'Content-Type:multipart/form-data' \
    -F 'images=@cat.jpg;type=image/jpeg' \
    -F 'images=@dog.jpg;type=image/jpeg'