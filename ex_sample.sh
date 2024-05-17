curl -X POST 'http://127.0.0.1:8004/caption' \
    -H 'accept:application/json' \
    -H 'Content-Type:multipart/form-data' \
    -F 'images=@cat.jpg' \
    -F 'images=@dog.jpg' \
    -F 'max_new_tokens=64' \
    -F 'prompts=What is the cat laying on?' \
    -F 'prompts=What is the dog laying on?' \

