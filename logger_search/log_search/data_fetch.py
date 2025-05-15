import logging

def search_log_entries(file_path, keyword, batch_size=10):

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            batch = []
            for line in f:
                if keyword in line:
                    batch.append(line.strip())
                    if len(batch) == batch_size:
                        yield batch
                        batch = []  
            if batch:  
                yield batch
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while searching the log: {e}")
        raise
