# deutsche-telekom-hackathon

this is a hackathon project with basic prototype of application, which ables users to visualise and 'speak' to their data

## Usage (for Debian-based systems only)

### install backend packages (from root folder)

```
sudo apt install pipx
pipx install poetry
pipx ensurepath
poetry shell
poetry install --no-root
```

### set backend environment

create .env file in ```backend``` folder and write into it:
```
OPENAI_API_KEY = "your-api-key"
```

### run backend server

```
cd backend
fastapi dev main.py
```

### install frontend packages (from root folder)

```
cd frontend
npm i && npm i victory
```

### run Vite frontend server (from ```frontend``` folder)

```
npm run dev
```
