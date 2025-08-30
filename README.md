# WhatsApp Message Automator

This script uses `pywhatkit` to send WhatsApp messages instantly or schedule them to be sent at a future date and time.

## Prerequisites

- Python 3
- `pywhatkit` library (`pip install pywhatkit`)

## Usage

You can execute the script directly from your command line.

### Sending a Message Instantly

Use the following format to send a message immediately:

```bash
python3 whatsapp_sender.py "PHONE_NUMBER" "YOUR_MESSAGE"
```

**Example:**
```bash
python3 whatsapp_sender.py "+919990799315" "Hello from my script!"
```

### Scheduling a Message

You can schedule a message to be sent at a specific date and time using the `--schedule` flag. The script will wait until the specified time and then send the message.

The format is: `YYYY MM DD HH MM` (24-hour format).

```bash
python3 whatsapp_sender.py "PHONE_NUMBER" "YOUR_MESSAGE" --schedule YYYY MM DD HH MM
```

**Example:**
To send a message on December 25, 2025, at 9:30 AM:
```bash
python3 whatsapp_sender.py "+919990799315" "Merry Christmas!" --schedule 2025 12 25 09 30
```

---

## Scheduling with Cron on macOS

You can use a cron job to automatically run the script on a recurring schedule.

### Step 1: Get Absolute Paths

You need the full path to your python executable and your script.
- **Python Path:** `/usr/local/bin/python3`
- **Script Path:** `/Users/bipin/codebase/automate-whatsapp/whatsapp_sender.py`

### Step 2: Edit Your Cron Table

Open your cron table in the terminal:
```bash
crontab -e
```

### Step 3: Add the Job

Add a line to the file with your desired schedule and command.

**Example:** To send the message "Good Morning" every day at 9:00 AM.

```cron
# Send a WhatsApp message every morning at 9:00 AM
0 9 * * * /usr/local/bin/python3 /Users/bipin/codebase/automate-whatsapp/whatsapp_sender.py "+919990799315" "Good Morning" >> /tmp/whatsapp_cron.log 2>&1
```

**Command Breakdown:**
- `0 9 * * *`: The schedule (runs at 09:00 every day).
- `/usr/local/bin/python3 ...`: The full command to execute.
- `>> /tmp/whatsapp_cron.log 2>&1`: This logs all output and errors to a file, which is essential for debugging.

### ⭐️ Important Warning for Cron Jobs

`pywhatkit` works by opening a web browser, which requires access to your Mac's graphical user interface (GUI). A standard cron job runs in the background and may fail when it tries to control a GUI application.

If your cron job doesn't work, check the `/tmp/whatsapp_cron.log` file for errors. If you see GUI-related errors, you may need to explore more advanced solutions like using `launchd` on macOS.
