container_name=lambda_docker
docker_image=aws_lambda_builder_image
docker run -td --name=$container_name $docker_image
docker cp ./requirements.txt $container_name:/

docker exec -i $container_name /bin/bask < ./docker_install.sh
docker cp $container_name:/bcrypt_layer.zip bcrypt_layer.zip
docker rm $container_name
