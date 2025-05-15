from log_search.data_fetch import search_log_entries
import logging
def main():
    logging.basicConfig(
        filename="log_search_debug.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

 

    # Path to local log file
    file_path = "./logs/file_attendance.log"
    keyword = input("Enter the keyword to search for in the log file: ").strip()

    if not keyword:
        print("Keyword cannot be empty.")
        logging.error("User provided an empty search keyword.")
        return

    logging.info(f"Starting search for keyword: {keyword}")

    entry_generator = search_log_entries(file_path, keyword)
    results = []

    try:
        for batch in entry_generator:
            print("\n--- Showing next 10 entries ---")
            for entry in batch:
                print(entry)
                results.append(entry)

            user_input = input("\nType 'next' to see more, or 'exit' to stop: ").strip().lower()
            if user_input != 'next':
                print("Exiting.")
                logging.info("User exited the search.")
                break
        else:
            print("No more matching entries found.")
            logging.info("All matching entries displayed.")
        

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred during the search process: {e}")
    
    finally:
        print("Program ended.")
        logging.info("Program terminated.")

if __name__ == "__main__":
    main()