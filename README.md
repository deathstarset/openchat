# Openchat Ai Chatbot

This is my first attempt of trying to integrate a large language model into a web app

## How to run this project locally

### Prerequisites

In order for you to be able to run this project you need to have [Ollama](https://ollama.com/) installed for the llm and [Docker](https://www.docker.com/products/docker-desktop/) to run the postgres instance

### Root File

in te root file you need to .env file for the database credentials that you will see in the docker-compose.yaml file and start the postgres database instance using this command

```bash
docker compose up -d
```

### Server

in the server directory you need first to create and start a python virtual environment using this command

```bash
python3 -m venv .venv
source .venv/bin/activate
```

after starting the evironment you need to install the project dependencies using this command

```bash
pip install -r requirements.txt
```

after this, you need to add a .env file with environment variables to be able to connect to the database and with all this finished we can run the database migrations using alembic

```bash
alembic upgrade head
```

finally we can start the dev server using this command

```bash
fastapi dev app/index.py
```

### Frontend

to start the frontend we need to be in the frontend directory and run those commands

```bash
npm install
npm run dev
```
