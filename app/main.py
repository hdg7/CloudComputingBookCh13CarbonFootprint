from fastapi import FastAPI
from codecarbon import EmissionsTracker
import time
import random

app = FastAPI()
tracker = EmissionsTracker(measure_power_secs=1,
                           log_level="info",
                           output_dir="/app/outputs",
                           output_file="my_emissions_log.csv"
                           )

requests=0

@app.get("/")
def root():
    return {"status": "Carbon tracking API is running!"}


@app.get("/simulate-task")
def simulate_task(duration: float = 1.0):
    """
    Simulate a CPU-heavy task and track emissions.
    """
    global requests
    global tracker

    requests += 1
    tracker.start()

    # Simulated heavy computation
    start = time.time()
    x = 0
    while time.time() - start < duration:
        x += random.random() ** 2

    emissions = tracker.stop()

    return {
        "message": f"Simulated work for {duration} seconds.",
        "total_estimated_emissions_kg": emissions,
        "total_requests": requests
    }

@app.get("/debug-emissions")
def debug():
    details = tracker.final_emissions_data
    return {
        "Total energy_kwh": details.energy_consumed,
        "Total emission": details.emissions,
        "cpu_power": details.cpu_power,
        "gpu_power": details.gpu_power,
        "total requests": requests
    }
