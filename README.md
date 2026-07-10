# Chapter 13 SCI

This repository contains the SCI calculation tutorial mentioned in **Chapter 13** of the book:

[**Cloud Computing for Artificial Intelligence: Concepts, Methods, and Practical Tools**](https://amzn.eu/d/02lMPIKf)

# Carbon Tracking API

This project provides a FastAPI-based application integrated with CodeCarbon to measure and track carbon emissions during simulated tasks.

## Project Structure
- **Dockerfile**: Defines the container environment, installs dependencies, and runs the FastAPI application.
- **main.py**: Contains the FastAPI application with endpoints for simulating CPU-heavy tasks and retrieving emissions data.
- **requirements.txt**: Lists Python dependencies, including `fastapi` and `codecarbon`.

## Endpoints
- `/` : Health check endpoint that confirms the API is running.
- `/simulate-task` : Simulates a CPU-intensive task for a specified duration and returns estimated emissions.
- `/debug-emissions` : Provides detailed energy consumption and emissions data.

## Build and Run Instructions
To build and run the Docker container, execute the following commands:

```bash
sudo docker build . -t carbon
sudo docker run -p 8010:8010 -v $(pwd)/outputs:/app/outputs -it carbon
```

The API will be available at `http://localhost:8010`.
