# Sunset Agent OS - Prototype

This directory contains the initial Python prototype of the **Sunset Agent OS - AI System Controller**. 

## Objective
The goal of this script is to simulate the **AI Agent Partition** analyzing system health and automatically controlling running apps/memory based on rules, mimicking the intelligence of the proposed OS.

## Requirements
* Python 3.x
* `psutil` library (`pip install psutil`)

## How to Run
1. Install requirements:
   ```bash
   pip install psutil
   ```
2. Run the agent:
   ```bash
   python sunset_agent.py
   ```

## Simulation Details
The script monitors CPU and RAM usage via `psutil`. If memory usage exceeds normal boundaries, it enters optimization mode, scanning for heavy non-whitelisted background apps to "suspend" (for safety, the `proc.kill()` method is mocked and just logs the action).

*This represents step 1 of the real-world application of Sunset Agent OS.*
