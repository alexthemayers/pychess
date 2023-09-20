# Makefile for building and installing a Python library in a venv

# Set the name of your Python package and the version
PACKAGE_NAME = chesslibrary
PACKAGE_VERSION = 0.0.1

# Virtual environment directory
VENV_DIR = venv

# Define Python interpreter (modify if needed)
PYTHON = python3

# Directory where distribution files will be created
DIST_DIR = dist


# Default target
all: clean build

# Create a virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)

# Create distribution files
build: venv
	@echo "Building distribution files..."
	@source $(VENV_DIR)/bin/activate && \
	$(PYTHON) -m pip install --upgrade pip && \
	$(PYTHON) -m pip install build &&
	$(PYTHON) -m build sdist

# Create distribution files
requirements: venv
	@echo "Building distribution files..."
	@source $(VENV_DIR)/bin/activate && \
	$(PYTHON) -m pip install --upgrade pip && \
	$(PYTHON) -m pip install -r requirements.txt

test_lib: requirements
	@source $(VENV_DIR)/bin/activate && \
	PYTHONPATH=./chess/lib $(PYTHON) -m pytest

test_main: requirements
	@source $(VENV_DIR)/bin/activate && \
	PYTHONPATH=./chess $(PYTHON) -m pytest

run_server: requirements
	$(PYTHON) chess/main.py server --host 0.0.0.0 --port 8000

run_client: requirements
	$(PYTHON) chess/main.py client --host $(API_BASE)

run_standalone: requirements
	$(PYTHON) chess/main.py
# Clean up distribution files and virtual environment
clean:
	@echo "Cleaning up..."
	rm -rf $(DIST_DIR)
	rm -rf $(VENV_DIR)

.PHONY: all build venv-build clean
