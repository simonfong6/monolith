# Template Flask React App

# Dependencies
- Docker
- Docker Compose

# Development
Run all commands at the root of the repo.

### Note
These are all `docker-compose` commands.

## Development Server

### Start the server
```bash
./scripts/development.sh up
```

### Start the server in the background
```bash
./scripts/development.sh up -d
```

## Tests
### Run tests
```bash
./scripts/test.sh
```


## Production Build
### Start the server
```bash
./scripts/development.sh up
```

### Start the server in the background
```bash
./scripts/development.sh up -d
```

# Deployment
- Nginx Reverse Proxy
- Symlink the nginx confs
- Start the production and optionally dev containers.

# TODO
- Intergrate with CI/CD, Buildkite?
- ECS/EKS

# Buildkite
Getting weird error.
