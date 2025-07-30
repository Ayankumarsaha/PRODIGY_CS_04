import datetime

def log_message(file, message):
    """
    Writes a message to the log file with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    file.write(f"{timestamp} {message}\n")

def keylogger_session():
    print("\n===============================")
    print("      SIMPLE TERMINAL KEYLOGGER")
    print("===============================\n")
    print("INSTRUCTIONS:")
    print("- Type anything and it will be recorded.")
    print("- Type 'STOP' (in caps) to end logging and save the file.\n")

    log_file_name = "session_log.txt"

    with open(log_file_name, 'w') as log_file:
        log_file.write("==== SESSION STARTED ====\n")
        log_file.write(f"Start Time: {datetime.datetime.now()}\n\n")

        while True:
            user_input = input("Input: ")

            if user_input.strip() == "STOP":
                log_file.write("\n==== SESSION ENDED ====\n")
                log_file.write(f"End Time: {datetime.datetime.now()}\n")
                print("\nLogging session completed. Log saved in:", log_file_name)
                break
            else:
                log_message(log_file, user_input)

if __name__ == "__main__":
    keylogger_session()
