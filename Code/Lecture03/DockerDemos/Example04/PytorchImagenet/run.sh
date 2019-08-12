docker build -t pytorch-imagenet . && \
docker run -d -p 5555:5555 --name pytorch-imagenet pytorch-imagenet:latest
