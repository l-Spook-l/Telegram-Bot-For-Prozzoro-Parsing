# Telegram Bot for Prozorro Parsing

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQLite3](https://img.shields.io/badge/SQLite3-Database-orange?logo=sqlite)
![aiogram](https://img.shields.io/badge/aiogram-Async_Library-blueviolet)
![aiofiles](https://img.shields.io/badge/aiofiles-Async_File_Operations-yellowgreen)
![aiosmtplib](https://img.shields.io/badge/aiosmtplib-Async_Email-yellow)
![aiohttp](https://img.shields.io/badge/aiohttp-Async_HTTP-blue)

This project represents a Telegram bot that allows users to fetch tender information from the Prozorro system based on specified parameters and receive daily updates via email.

## Description

The bot is designed for convenient and swift retrieval of tender information directly within Telegram from the Prozorro system. Users can specify parameters to search for tenders, and the bot will send daily updates on the found tenders to the user's email.

## Functionality

- Search for tenders based on specified parameters (e.g., keywords, region, tender type, etc.).
- Subscription to daily updates of found tenders via email.

## Usage

1. **Bot Startup:**
   - Install all dependencies, launch the bot on your server or locally.
   - Provide the Telegram API token and mail sending parameters.

2. **Interacting with the Bot::**
   - Users can use bot commands to search for tenders and subscribe to daily updates.
   - Example usage: /search keyword region tender_type.

## Installation Requirements

- Python 3.x
- Installed packages from requirements.txt
- 
## Planned Changes

### Updating Queries Using ORM

During development, there's an ongoing transition from using raw SQL queries to using Object-Relational Mapping (ORM). 
This will simplify working with the database, enhance code readability and maintainability, and reduce the chances of errors when querying the database.

#### Expected Changes:
- Replacement of raw SQL queries with ORM methods for data insertion, updating, deletion, and retrieval.
- Creation of corresponding models for database tables.
- Use of ORM methods to access data instead of direct SQL queries.

### Additional Functionality

In addition to this, there are plans to add new functionality for modifying database queries. 
These new features will make it easier to modify and update user queries.

Expect updates in the bot's functionality for easier data handling and the transition to ORM.

## Developers

- https://github.com/l-Spook-l

## Contact

If you have any questions or suggestions for improving the project, please contact uaspookua@gmail.com.
