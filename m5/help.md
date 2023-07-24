# Docker Cheat Sheet

This document contains a list of fundamental Docker commands along with brief descriptions of what they do. As always, practicing these commands will be much more valuable than simply reading about them, but this document should serve as a good starting point and reference for future use.

## Writing the Dockerfile

- `FROM <image>` - Specifies the base image for the Dockerfile.
  - e.g., `FROM ubuntu` specifies that the base image for the Dockerfile is `ubuntu`.
- `RUN <command>` - Executes the specified command in the container.
  - e.g., `RUN apt-get update` executes the `apt-get update` command in the container.
- `COPY <host-path> <container-path>` - Copies the specified host path to the specified container path.
  - e.g., `COPY . /app` copies the current directory on the host to the `/app` directory in the container.
- `WORKDIR <path>` - Sets the working directory for the Dockerfile.
  - e.g., `WORKDIR /app` sets the working directory for the Dockerfile to `/app`.
- `CMD <command>` - Specifies the command to run when the container starts.
  - e.g., `CMD ["python", "app.py"]` specifies that the command to run when the container starts is `python app.py`.
- `EXPOSE <port>` - Exposes the specified port in the container.
  - e.g., `EXPOSE 80` exposes port `80` in the container.
- `ENV <key> <value>` - Sets the specified environment variable to the specified value.
  - e.g., `ENV PORT 80` sets the `PORT` environment variable to `80`.
- `ARG <key> <value>` - Sets the specified build argument to the specified value.
  - e.g., `ARG PORT 80` sets the `PORT` build argument to `80`.
- `VOLUME <path>` - Creates a mount point with the specified path.
  - e.g., `VOLUME /app` creates a mount point with the path `/app`.
- `USER <user>` - Sets the user for the Dockerfile.
  - e.g., `USER root` sets the user for the Dockerfile to `root`.
- `LABEL <key> <value>` - Adds the specified key-value pair to the Dockerfile.
  - e.g., `LABEL version="1.0"` adds the key-value pair `version="1.0"` to the Dockerfile.
- `MAINTAINER <name>` - Sets the maintainer for the Dockerfile.
  - e.g., `MAINTAINER John Doe` sets the maintainer for the Dockerfile to `John Doe`.
- `ONBUILD <command>` - Executes the specified command when the image is used as the base for another image.
  - e.g., `ONBUILD RUN apt-get update` executes the `apt-get update` command when the image is used as the base for another image.
- `STOPSIGNAL <signal>` - Sets the signal that will be sent to the container to stop it.
  - e.g., `STOPSIGNAL SIGTERM` sets the signal that will be sent to the container to stop it to `SIGTERM`.

## Running a Container

- `docker run <image>` - Runs a container from the specified image.
  - e.g., `docker run hello-world` runs the `hello-world` container.
- `docker run -it <image> <command>` - Runs a container from the specified image and executes the specified command in the container.
  - e.g., `docker run -it ubuntu bash` runs the `ubuntu` container and executes the `bash` command in the container.
- `docker run -d <image>` - Runs a container from the specified image in the background.
  - e.g., `docker run -d nginx` runs the `nginx` container in the background.
- `docker run -p <host-port>:<container-port> <image>` - Runs a container from the specified image and maps the specified host port to the specified container port.
  - e.g., `docker run -p 8080:80 nginx` runs the `nginx` container and maps port `8080` on the host to port `80` in the container.
- `docker run -v <host-path>:<container-path> <image>` - Runs a container from the specified image and maps the specified host path to the specified container path.
  - e.g., `docker run -v /home/user:/home/user ubuntu` runs the `ubuntu` container and maps the `/home/user` directory on the host to the `/home/user` directory in the container.

## Managing Containers and Images

- `docker ps` - Lists all running containers.
  - e.g., `docker ps` lists all running containers.
- `docker ps -a` - Lists all containers.
  - e.g., `docker ps -a` lists all containers.
- `docker images` - Lists all images.
  - e.g., `docker images` lists all images.
- `docker rm <container>` - Removes the specified container.
  - e.g., `docker rm hello-world` removes the `hello-world` container.
- `docker rmi <image>` - Removes the specified image.
  - e.g., `docker rmi hello-world` removes the `hello-world` image.
- `docker stop <container>` - Stops the specified container.
  - e.g., `docker stop hello-world` stops the `hello-world` container.
- `docker start <container>` - Starts the specified container.
  - e.g., `docker start hello-world` starts the `hello-world` container.
- `docker restart <container>` - Restarts the specified container.
  - e.g., `docker restart hello-world` restarts the `hello-world` container.
- `docker pause <container>` - Pauses the specified container.
  - e.g., `docker pause hello-world` pauses the `hello-world` container.
- `docker unpause <container>` - Unpauses the specified container.
  - e.g., `docker unpause hello-world` unpauses the `hello-world` container.
- `docker kill <container>` - Kills the specified container.
  - e.g., `docker kill hello-world` kills the `hello-world` container.
- `docker exec <container> <command>` - Executes the specified command in the specified container.
  - e.g., `docker exec hello-world ls` executes the `ls` command in the `hello-world` container.
- `docker pull <image>` - Pulls the specified image.
  - e.g., `docker pull hello-world` pulls the `hello-world` image.
- `docker push <image>` - Pushes the specified image.
  - e.g., `docker push hello-world` pushes the `hello-world` image.
- `docker build -t <image> <path>` - Builds an image from the specified path and tags it with the specified image name.
  - e.g., `docker build -t hello-world .` builds an image from the current directory and tags it with the `hello-world` image name.
- `docker save <image> > <file>` - Saves the specified image to the specified file.
  - e.g., `docker save hello-world > hello-world.tar` saves the `hello-world` image to the `hello-world.tar` file.
- `docker load < <file>` - Loads the specified image from the specified file.
  - e.g., `docker load < hello-world.tar` loads the `hello-world` image from the `hello-world.tar` file.
  