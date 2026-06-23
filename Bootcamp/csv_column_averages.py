import csv

def process_csv(filepath):
    file = None
    try:
        file = open(filepath, mode='r', newline='', encoding='utf-8')
        reader = csv.reader(file)
        
        headers = next(reader, None)
        if not headers:
            print("The CSV file is empty.")
            return
            
        num_columns = len(headers)
        col_sums = [0.0] * num_columns
        row_count = 0
        
        for row_idx, row in enumerate(reader, start=2):
            if len(row) != num_columns:
                raise csv.Error(f"Malformed data at row {row_idx}: expected {num_columns} columns, got {len(row)}.")
            
            for col_idx, value in enumerate(row):
                try:
                    col_sums[col_idx] += float(value)
                except ValueError:
                    raise csv.Error(f"Malformed data at row {row_idx}, column '{headers[col_idx]}': Cannot convert '{value}' to a number.")
            row_count += 1

        if row_count > 0:
            print(f"\n--- Averages for {filepath} ---")
            for col_idx, header in enumerate(headers):
                avg = col_sums[col_idx] / row_count
                print(f"Column '{header}': {avg:.2f}")
        else:
            print("No data rows found to average.")

    except FileNotFoundError:
        print(f"Error: The file at '{filepath}' could not be found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to access '{filepath}'.")
    except csv.Error as e:
        print(f"CSV Processing Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    finally:
        if file is not None:
            file.close()
            print("[System Notice]: File resources successfully closed via 'finally' block.")

if __name__ == "__main__":
    print("\n--- Testing Robust File Processor ---")
    process_csv("non_existent_file.csv")                                                  