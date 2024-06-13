#Log in to Docker
```sh
docker login

# Build Docker Images

cd communicator_service
docker build -t communicator .

cd ..
cd file_processing_service
docker build -t file-processor .

# Tag and Push Docker Images
cd ..
docker tag communicator samshad/communicator
docker push samshad/communicator

docker tag file-processor samshad/file-processor
docker push samshad/file-processor

# Pull Communicator Image
docker pull samshad/communicator
docker pull samshad/file-processor
