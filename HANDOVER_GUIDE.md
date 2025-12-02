# ISKCON Ahillyanagar Website - Handover Guide

## Overview
This is the complete source code for the ISKCON Ahillyanagar website. It includes a fully functional **Python Backend** and a **SQLite Database** to store donations, contact messages, and subscribers.

## System Requirements
- **Python 3.12** or higher.
- **Internet Connection** (for loading fonts/icons).

## Installation

1.  **Install Python**: Download and install Python from [python.org](https://www.python.org/).
2.  **Open Terminal**: Open Command Prompt (cmd) or PowerShell in this folder.
3.  **Install Dependencies**:
    ```bash
    pip install flask flask-cors
    ```

## How to Run

1.  **Start the Server**:
    Run the following command in the terminal:
    ```bash
    python backend/app.py
    ```
2.  **Access the Website**:
    Open your browser and go to:
    [http://localhost:5000](http://localhost:5000)

## Admin Dashboard

- **URL**: [http://localhost:5000/admin.html](http://localhost:5000/admin.html)
- **Password**: `admin123` (Note: Change this in `admin.html` for better security).
- **Features**:
    - View all Donations.
    - Read Contact Messages.
    - Manage Newsletter Subscribers.
    - **Export Data**: All data is saved in `backend/iskcon.db`.

## Database
The website uses **SQLite**.
- **File**: `backend/iskcon.db`
- **Backup**: Simply copy this file to a safe location to backup your data.

## Support
For any technical issues, please ensure the Python server is running in the background.
