# Receipt Scanner using OpenCV and FastAPI

This project is an API which provides an endpoint to generate a list of items from an image of a receipt.

## Setup Instructions

1. Fork this repository and clone to your local environment.
2. Install a version of Python 3 if you do not already have one. I recommend Python 3.8 or newer.
3. You can create a virtual environment within Python to create a sandboxed set of package installs. If you already have a preferred method of virtualenv creation, feel free to proceed with your own method. `python -m venv env`
4. You will need to activate your virtual environment each time you want to work on your project. Run the activate script within the `env/bin` folder that was generated.

### Note for OpenCV

To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:

`pip install opencv-contrib-python`

If you need help configuring your development environment for OpenCV, I highly recommend that you read the [pip install OpenCV guide](https://pyimagesearch.com/2018/09/19/pip-install-opencv/) — it will have you up and running in a matter of minutes.

### Rest of the Requirements

I have provided a `requirements.txt` file you can use to install the necessary packages. With your virtualenv activated run: `pip install -r requirements.txt`

## Steps to run the application

1. Follow the instructions on https://docs.docker.com/install/ to install docker
2. Follow the instructions on https://docs.docker.com/compose/install/ to install docker compose
3. Run `docker compose up`. 
4. docker-compose will install all the packages needed from `requirements.txt`.
5. The app will run locally at http://127.0.0.1:8000.
6. Take an image of a receipt and send that image at the following address `http://127.0.0.1:8000/get-items`.
7. List of items will be returned in the response.