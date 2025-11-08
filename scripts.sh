#!/bin/bash

# Sports Agent Development Scripts
# Similar to npm/yarn scripts

case "$1" in
    "start-mock-api")
        echo "🏏 Running mock API..."
        uv run python -m src.mocks.mock_api
        ;;
    *)
        echo "Available commands:"
        echo "  ./scripts.sh start-mock-api    - Run mock API"
        ;;
esac