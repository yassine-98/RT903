# ourbase image
FROM alpine:latest
## ENV
ENV Port 80
ENV message "Hello Wolrd !"

# Install python and pip
RUN apk add --update py3-pip

# upgrade pip
RUN pip install --upgrade pip

# install Python modules neededby the Python app
RUN pip install --no-cache-dir Flask

# copy files required for the appto run
COPY rt903.py /usr/src/app/

#COPY templates/index.html /usr/src/app/templates/
# tell the port numberthe container should
EXPOSE 80

# run the application
CMD ["python3", "/usr/src/app/rt903.py"]
