# Docker Quick Reference

## Build and Run

```bash
# Build the image
docker build -t space:latest .

# Run the container
docker run --rm space:latest

# Run with flags
docker run --rm space:latest -v  # verbose
docker run --rm space:latest -d  # debug
```

## Environment Configuration

```bash
# Set environment variables
docker run --rm \
  -e SPACE_API_BASE_URL=http://api.open-notify.org \
  -e SPACE_ASTROS_ENDPOINT=/astros.json \
  space:latest

# Use .env file
docker run --rm --env-file .env space:latest
```

## Docker Compose

```bash
# Run all services
docker-compose up

# Run specific service
docker-compose up space-verbose

# Build and run
docker-compose up --build

# Run in detached mode
docker-compose up -d

# Stop services
docker-compose down
```

## Multi-platform Build

```bash
# Build for multiple architectures
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t space:latest \
  --push .
```

## Troubleshooting

```bash
# Check logs
docker logs <container_id>

# Interactive shell in container
docker run --rm -it --entrypoint /bin/bash space:latest

# Inspect image
docker inspect space:latest

# Check image size
docker images space
```

## Security Best Practices

- ✅ Multi-stage build (reduces image size)
- ✅ Runs as non-root user (spaceuser)
- ✅ Minimal base image (python:3.11-slim)
- ✅ No secrets in image (use environment variables)
- ✅ Security scanning with Trivy in CI/CD
- ✅ Health check included
