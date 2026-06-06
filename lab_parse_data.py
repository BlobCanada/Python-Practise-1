#!/usr/bin/env python3

# Mock system strings to parse
log_entry = "2026-06-05:ERROR:Authentication failed for user bob"
employee_record = "  bob_it_998123  "

def get_status_code(log_str):
    # This function should extract and return the status level (e.g., 'ERROR') from the log string.
    # code here
    list = log_str.split(':')
    return(list[1])

def clean_and_split_record(record_str):
    # This function should strip off any leading/trailing whitespace from the record,
    # and split it wherever an underscore (_) occurs.
    # Returns: A list of substrings.
    # code here
    white = record_str.strip()
    return(list(white.split('_')))

def get_masked_id(record_str):
    # This function should clean the record string (remove spaces) and return 
    # only the last 3 characters of the student ID.
    # code here
    white = record_str.strip()
    return(white[-3:])


if __name__ == '__main__':
    print('Status Level: ', get_status_code(log_entry))
    print('Cleaned Record:', clean_and_split_record(employee_record))
    print('Masked ID:     ', get_masked_id(employee_record))