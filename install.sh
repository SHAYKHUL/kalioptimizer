#!/bin/bash

# Welcome message
echo "Welcome to the KaliOptimizer Installer!"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is required but not installed. Please install Git and try again."
    exit 1
fi

# Clone the repository
echo "Cloning the KaliOptimizer repository..."
git clone https://github.com/SHAYKHUL/kalioptimizer
cd KaliOptimizer

# Create a symbolic link
echo "Creating a symbolic link for the kalioptimizer script..."
chmod +x kalioptimizer.py
sudo ln -s "$(pwd)/kalioptimizer.py" /usr/local/bin/kalioptimizer

# Run the KaliOptimizer script
echo "Running the KaliOptimizer script..."
kalioptimizer

# End of installation
echo "KaliOptimizer installation completed!"
