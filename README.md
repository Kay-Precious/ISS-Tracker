# ISS-Tracker

This project uses APIs to track the International Space Station (ISS) and send an email notification when the ISS is overhead and it's nighttime.

Requirements

- Python 3.x
- requests library
- smtplib library
- datetime library
- API keys for Open Notify and Sunrise-Sunset API

Installation

1. Clone the repository using git clone
2. Install required libraries using pip install requests smtplib datetime
3. Replace MY_EMAIL and MY_PASSWORD with your Gmail credentials
4. Replace MY_LAT and MY_LONG with your latitude and longitude

Code Structure

The code is structured into the following functions:

- is_iss_overhead(): Checks if the ISS is within a 5-degree radius of the user's location
- is_night(): Checks if it's nighttime based on the user's location
- Main loop: Sends an email notification when the ISS is overhead and it's nighttime

API Documentation

- Open Notify API: http://api.open-notify.org/iss-now.json
- Sunrise-Sunset API: https://api.sunrise-sunset.org/json

Usage

1. Run the script using python iss_tracker.py
2. The script will send an email notification when the ISS is overhead and it's nighttime

Future Development

- Implement a more accurate method for determining nighttime
- Add a feature to track the ISS's trajectory
- Use a more secure method for storing email credentials

Note: Make sure to enable less secure apps in your Google account settings to allow the script to send emails.
