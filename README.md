# Disaster Alert System

This project uses the **Tweepy API** to fetch Twitter hashtags and check for keywords related to disasters like **earthquake**, **flood**, and more. If any of these disaster-related keywords are found in the tweet, an alert message is sent out to the registered users via email.

## Features:
- **Tweepy API** integration to fetch hashtags from Twitter.
- Detection of disaster-related keywords such as **earthquake** and **flood** in tweets.
- Sending alert messages to users via email.
- A **registration page** to allow users to sign up and receive alerts.

## Requirements:
- Python 3.x
- `smtplib` for sending emails.
- `tweepy` library for accessing Twitter API.
  
## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
