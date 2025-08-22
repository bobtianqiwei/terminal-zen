#!/bin/bash
# Clean script for Terminal Zen project
# Removes all auto-generated files and directories

echo "🧹 Cleaning Terminal Zen project..."

# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.pyo" -delete 2>/dev/null || true

# Remove egg-info directories
find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

# Remove build directories
rm -rf build/ dist/ *.egg-info/ 2>/dev/null || true

# Remove virtual environment if exists
rm -rf .venv/ venv/ env/ 2>/dev/null || true

echo "✅ Cleanup completed!"
echo "📁 Current project structure:"
ls -la
