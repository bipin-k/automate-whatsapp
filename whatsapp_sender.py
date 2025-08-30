
import pywhatkit
import argparse
import datetime
import time

def send_instant_message(phone_no, message):
    """Sends a WhatsApp message instantly."""
    try:
        # The wait_time is the time in seconds to wait for the tab to open
        # tab_close=True will close the tab after sending the message
        pywhatkit.sendwhatmsg_instantly(phone_no, message, wait_time=15, tab_close=True)
        print("Successfully Sent the instant message!")
    except Exception as e:
        print(f"An error occurred while sending the instant message: {e}")

def schedule_message(phone_no, message, year, month, day, hour, minute):
    """Schedules a WhatsApp message for a specific date and time."""
    try:
        target_datetime = datetime.datetime(year, month, day, hour, minute)
        now = datetime.datetime.now()

        if target_datetime < now:
            print("Error: Scheduled time cannot be in the past.")
            return

        delay = (target_datetime - now).total_seconds()
        print(f"Message scheduled for {target_datetime}. Waiting for {int(delay)} seconds to send.")
        
        time.sleep(delay)

        pywhatkit.sendwhatmsg_instantly(phone_no, message, wait_time=15, tab_close=True)
        print("Successfully sent the scheduled message!")

    except Exception as e:
        print(f"An error occurred while scheduling the message: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send WhatsApp messages instantly or schedule them for a future date and time.")
    parser.add_argument("phone_no", help="The recipient's phone number (e.g., +919990799315).")
    parser.add_argument("message", help="The message you want to send.")
    parser.add_argument("--schedule", nargs=5, metavar=("YYYY", "MM", "DD", "HH", "MM"),
                        help="Schedule the message for a specific date and time (e.g., --schedule 2025 8 30 23 59).")

    args = parser.parse_args()

    if args.schedule:
        try:
            year, month, day, hour, minute = map(int, args.schedule)
            schedule_message(args.phone_no, args.message, year, month, day, hour, minute)
        except ValueError:
            print("Invalid date/time format for scheduling. Please use YYYY MM DD HH MM.")
    else:
        send_instant_message(args.phone_no, args.message)
