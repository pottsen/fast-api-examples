# fast-api-template

Can run the main.py stand-alone or in a docker container.

## Running Locally un-dockerized
Uses [Uvicorn](https://www.uvicorn.org/) to run the API. It can be run from the command line:
- ```uvicorn  main:app --reload```

Or it can be run programmatically. See the bottom of the main.py file for programmatic implementation:
```python main.py```

## Running dockerized
See the Dockerfile for the contianer specifications.
- Build the docker image
    - ```docker build -t yourusername/yourimagename .```
- Run the docker image and connect your localhost port to the port you exposed on the docker container
    - ```docker run -p 8888:5000 yourusername/yourimagename```
    - localhost:8888 will be connected to the docker container port 5000
