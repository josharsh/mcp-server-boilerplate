#!/bin/bash

# Helper script for running the MCP server in Docker

function print_help {
    echo "MCP Server Docker Helper"
    echo ""
    echo "Usage: ./docker-run.sh [command]"
    echo ""
    echo "Commands:"
    echo "  build       Build the Docker image"
    echo "  start       Start the container"
    echo "  stop        Stop the container"
    echo "  restart     Restart the container"
    echo "  logs        View container logs"
    echo "  shell       Get a shell inside the container"
    echo "  clean       Remove all containers and images"
    echo "  help        Show this help message"
    echo ""
}

case "$1" in
    build)
        echo "Building Docker image..."
        docker-compose build
        ;;
    start)
        echo "Starting container..."
        docker-compose up -d
        echo "Container started. Access at http://localhost:8000"
        ;;
    stop)
        echo "Stopping container..."
        docker-compose down
        ;;
    restart)
        echo "Restarting container..."
        docker-compose restart
        ;;
    logs)
        echo "Showing logs..."
        docker-compose logs -f
        ;;
    shell)
        echo "Opening shell in container..."
        docker-compose exec mcp-server /bin/bash
        ;;
    clean)
        echo "Cleaning up containers and images..."
        docker-compose down
        docker rmi $(docker images -q mcp-server_mcp-server)
        ;;
    help|*)
        print_help
        ;;
esac 