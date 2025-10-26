#!/bin/bash
# Docker build and run script for qfinbox

set -e

echo "🐳 qfinbox Docker Management Script"
echo "==================================="

show_help() {
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  build-dev     Build development Docker image"
    echo "  build-prod    Build production Docker image"
    echo "  run-dev       Run development container with Jupyter Lab"
    echo "  run-prod      Run production container"
    echo "  compose-up    Start services with docker-compose"
    echo "  compose-down  Stop services with docker-compose"
    echo "  clean         Remove all qfinbox Docker images and containers"
    echo "  help          Show this help message"
}

build_dev() {
    echo "📦 Building development Docker image..."
    docker build -f Dockerfile.dev -t qfinbox:dev .
    echo "✅ Development image built successfully!"
}

build_prod() {
    echo "📦 Building production Docker image..."
    docker build -f Dockerfile -t qfinbox:prod .
    echo "✅ Production image built successfully!"
}

run_dev() {
    echo "🚀 Starting development container..."
    docker run -it --rm \
        -p 8888:8888 \
        -v $(pwd):/app \
        --name qfinbox-dev \
        qfinbox:dev
}

run_prod() {
    echo "🚀 Starting production container..."
    docker run -it --rm \
        -p 5000:5000 \
        --name qfinbox-prod \
        qfinbox:prod
}

compose_up() {
    echo "🚀 Starting services with docker-compose..."
    docker-compose up -d
    echo "✅ Services started! Access Jupyter Lab at http://localhost:8888"
}

compose_down() {
    echo "🛑 Stopping services..."
    docker-compose down
    echo "✅ Services stopped!"
}

clean() {
    echo "🧹 Cleaning up Docker resources..."

    # Stop and remove containers
    docker ps -a --filter "name=qfinbox" --format "table {{.ID}}" | tail -n +2 | xargs -r docker stop
    docker ps -a --filter "name=qfinbox" --format "table {{.ID}}" | tail -n +2 | xargs -r docker rm

    # Remove images
    docker images --filter "reference=qfinbox*" --format "table {{.ID}}" | tail -n +2 | xargs -r docker rmi

    # Remove volumes
    docker volume ls --filter "name=qfinbox" --format "table {{.Name}}" | tail -n +2 | xargs -r docker volume rm

    echo "✅ Cleanup complete!"
}

case "$1" in
    build-dev)
        build_dev
        ;;
    build-prod)
        build_prod
        ;;
    run-dev)
        build_dev
        run_dev
        ;;
    run-prod)
        build_prod
        run_prod
        ;;
    compose-up)
        compose_up
        ;;
    compose-down)
        compose_down
        ;;
    clean)
        clean
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        echo "Use '$0 help' for usage information."
        exit 1
        ;;
esac
