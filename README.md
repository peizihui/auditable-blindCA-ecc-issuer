# Auditable-blindCA-demo

Auditable-blindCA-demo issues certificates blindly and reveals the blindness by tracing with the privacy-preserving smart contract. 

## Quick start using Docker

### Getting the image

1. First ensure you have Docker installed. [See Docker installation help](https://docs.docker.com/install/).

2. From a command line in cert-issuer dir, build your docker container:
    
    ```
    docker pull rujia/contract-kit:v14.
    ```

    This image will expose port 8080 and 8081 inside the container and receive web requests, passing different requests to issuing service and tracing service respectively.

### Running the Docker

    ```
    docker run -t -i -p 8080:8080 -p 8081:8081 rujia/contract-kit:v14.
    ```

### Starting  the services
 
 ```
   > cd auditable-blindCA-demo/src
   > python start_app.py 
    
   > cd auditable-blindCA-tracer
   > npm run dev 
   ```