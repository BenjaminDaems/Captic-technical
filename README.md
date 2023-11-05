# Docker

To run the Docker container, use the following command: \
```
docker run -it
    -v <path/to/local/images>:/app/images
    -v <path/to/local/output>:/app/output
    containername:version
    <path/of/image/to/process>
```

*<path/to/local/output>* and *<path/to/local/images>* link to the container directories /app/output and /app/images,
respectively. \
*<path/of/image/to/process>* is the relative path of the image to process on the container starting from /app/images.

