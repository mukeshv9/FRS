# Food Recommendation System

Food Recommendation System built using [Starlette](https://www.starlette.io/) and [Mongodb](https://www.mongodb.com/) and containerized using [Docker](https://www.docker.com/).
## Dependencies

- python 3.7
- mongodb 4.4
- docker 20.10.5
- docker-compose 1.28.6
  
## Dataset

This Project was built using the [Food.com Recipes and Interactions](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions/code) dataset from Kaggle.

## Directory Structure

- FRS
  - app  *Starlette app directory*
    - app.py    *Application file*
    - middleware.py *Middleware used to connect to the database*
    - routes.py *Route handling*
    - Dockerfile *Dockerfile to build the starlette app*
    - static *static content to serve at the front-end*
    - templates *HTML files to serve at the front-end*
  - mongo  *Mongodb database directory*
  - docker-compose.yml  *docker-compose file to spin-up the multi-container application*

## Steps to launch the application

- [Install Docker Engine](https://docs.docker.com/engine/install/)

- [Install Docker Compose](https://docs.docker.com/compose/install/)

- [Install Git LFS](https://git-lfs.github.com/)
  
- Clone the repo
  
        git clone https://github.com/mukeshv9/FRS
        
     *Note*: If the clone is taking too long use skip-smudge, remove the previous clone and use the following two commands:

          git lfs install --skip-smudge
        
          git clone https://github.com/mukeshv9/FRS

- Move to working directory

        cd FRS
        
- Download Large Files using Git LFS

        git lfs pull

- Spin up the containers using docker-compose

        sudo docker-compose up

- Open the application in the browser at the following url:

        localhost:5000

*Note*: Images for the suggested recipes are fetched using the Google Search API. The currently used free version serves only 100 requests per day.
