# GitHub Anomaly Detection Tool

## Overview

The GitHub Anomaly Detection Tool is a Python command-line application implemented with FastAPI. It is designed to detect and notify suspicious behavior within an integrated GitHub organization. Leveraging GitHub webhooks to monitor events, this tool employs a simple "anomaly detection" mechanism to notify users of suspicious activities. When such behavior is detected, event details are printed to the console. Python and FastAPI provide a robust foundation, ensuring efficient event processing and extensibility for custom detection mechanisms.

## Suspicious Behaviors

The application identifies the following suspicious behaviors:

1. **Pushing Code Between 14:00-16:00**: The tool checks if code is pushed to repositories within the specified time
   frame (2:00 PM to 4:00 PM).

2. **Creating a Team with the Prefix "hacker"**: It monitors the creation of teams created with the prefix "hacker"
   with "hacker."

3. **Creating and Deleting a Repository in Less Than 10 Minutes**: The tool tracks the creation and deletion of
   repositories and alerts if these actions occur within a 10-minute window.

## Getting Started

Follow these steps to set up and run the GitHub Anomaly Detection Tool:

1. Clone this repository to your local machine.

2. Install the required dependencies if necessary.

```bash
pip install -r requirements.txt
```

3. Configure the application to receive GitHub webhook events locally (at /webhook) using one of the recommended tools (smee.io or
   ngrok).

## Usage

```bash
# Example usage:
python main.py
