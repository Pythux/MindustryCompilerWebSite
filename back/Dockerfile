#Grab the latest alpine image
FROM alpine:latest

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./ /opt/webapp/
WORKDIR /opt/webapp

# Expose is NOT supported by Heroku
# EXPOSE 5000

# Run the image as a non-root user
RUN adduser -D pythux
USER pythux

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT serv

# to create the docker image, in this directory:
# docker image build --tag mindustry-compiler .
# to set PORT locally:
# docker container run --name mindCompiler -e PORT='5000' --rm -p 5000:5000 mindustry-compiler
