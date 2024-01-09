# TELEGRAM MESSAGE SENDER
This script allows you to send messages to members of a Telegram group using the Telethon library asynchronously.

## Prerequisites
- Python 3.7 or higher
- telethon
- aiofiles
- python-dotenv
- cryptg

## Setup
1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/telegram-message-sender.git
    ```
2. Create virtual environment:
   ```
    python -m venv venv
   ```
   and activate it 
   <br>
   <br>
    - on windows:
    ```
    venv\Scripts\activate
    ```   
    - on Mac:
    ```
    source venv/bin/activate
   ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file in the root directory of the project and add the following:
    ```
    API_ID=your_api_id
    API_HASH=your_api_hash
    ```
    Replace your_api_id, your_api_hash, and your_phone_number with your actual Telegram API credentials and phone number.

5. Write group name to the `groups.txt` file and text to send to the `text.txt`

## Usage
Run the script by executing the following command:

```bash
python send_messages.py
```
The script will prompt you to enter the message delay in seconds. After providing the delay, it will start sending messages to the members of specified group.

Notes
Make sure your Telegram API credentials are kept secret and not shared publicly.
Use this script responsibly and avoid spamming messages.
