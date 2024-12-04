# Open the log file and read its content
with open("sample.log", "r") as file:  # Opens the sample.log file in read mode
    logs = file.readlines()  # Reads all lines into a list called 'logs'

# Print the logs to verify they are being read
for line in logs:  # Loop through each line in the logs
    print(line.strip())  # Print the line without extra spaces or newlines
# Open the log file and read its content
with open("sample.log", "r") as file:  # Opens the sample.log file in read mode
    logs = file.readlines()  # Reads all lines into a list called 'logs'

# Print the logs to verify they are being read
for line in logs:  # Loop through each line in the logs
    print(line.strip())  # Print the line without extra spaces or newlines

# Import Counter to count occurrences
from collections import Counter  # Import Counter for easy counting

# Extract IP addresses from the logs
ip_addresses = []  # Create an empty list to store IPs
for line in logs:
    parts = line.split()  # Split the line into parts
    ip_addresses.append(parts[0])  # The first part is the IP address

# Count the number of requests per IP
ip_counts = Counter(ip_addresses)  # Count occurrences of each IP address

# Display the IP addresses and their request counts
print("\nIP Address           Request Count")
for ip, count in ip_counts.most_common():  # Sort and print counts
    print(f"{ip:<20} {count}")
# Extract endpoints from the logs
endpoints = []  # Create an empty list to store endpoints
for line in logs:
    parts = line.split('"')  # Split the line by double quotes
    if len(parts) > 1:
        request = parts[1]  # The HTTP request is the second part
        endpoint = request.split()[1]  # The endpoint is the second word in the request
        endpoints.append(endpoint)

# Count the number of accesses for each endpoint
endpoint_counts = Counter(endpoints)  # Count occurrences of each endpoint

# Find the most accessed endpoint
most_accessed = endpoint_counts.most_common(1)[0]  # Get the most common endpoint

# Display the most accessed endpoint
print(f"\nMost Frequently Accessed Endpoint:\n{most_accessed[0]} (Accessed {most_accessed[1]} times)")
# Extract endpoints from the logs
endpoints = []  # Create an empty list to store endpoints
for line in logs:
    parts = line.split('"')  # Split the line by double quotes
    if len(parts) > 1:
        request = parts[1]  # The HTTP request is the second part
        endpoint = request.split()[1]  # The endpoint is the second word in the request
        endpoints.append(endpoint)

# Count the number of accesses for each endpoint
endpoint_counts = Counter(endpoints)  # Count occurrences of each endpoint

# Find the most accessed endpoint
most_accessed = endpoint_counts.most_common(1)[0]  # Get the most common endpoint

# Display the most accessed endpoint
print(f"\nMost Frequently Accessed Endpoint:\n{most_accessed[0]} (Accessed {most_accessed[1]} times)")
# Detect suspicious activity (failed login attempts)
failed_attempts = {}  # Dictionary to store failed login counts by IP

for line in logs:
    parts = line.split('"')  # Split the line by double quotes
    if len(parts) > 2:  # Ensure the line contains an HTTP response
        status_code = parts[2].strip().split()[0]  # Extract the status code
        if status_code == "401":  # Check for failed login status
            ip = line.split()[0]  # Extract the IP address
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1  # Increment count

# Flag IPs with more than 10 failed login attempts
print("\nSuspicious Activity Detected:")
print("IP Address           Failed Login Attempts")
for ip, count in failed_attempts.items():
    if count >10:  # Configurable threshold
        print(f"{ip:<20} {count}")
import csv  # Import the CSV module

# Open the CSV file in write mode
with open("log_analysis_results.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write Requests Per IP
    csvwriter.writerow(["Requests per IP"])  # Add a header for this section
    csvwriter.writerow(["IP Address", "Request Count"])  # Column headers
    for ip, count in ip_counts.most_common():
        csvwriter.writerow([ip, count])  # Write each IP and its request count

    # Leave a blank line
    csvwriter.writerow([])

    # Write Most Accessed Endpoint
    csvwriter.writerow(["Most Accessed Endpoint"])  # Add a header for this section
    csvwriter.writerow(["Endpoint", "Access Count"])  # Column headers
    csvwriter.writerow([most_accessed[0], most_accessed[1]])  # Write the most accessed endpoint

    # Leave a blank line
    csvwriter.writerow([])

    # Write Suspicious Activity
    csvwriter.writerow(["Suspicious Activity"])  # Add a header for this section
    csvwriter.writerow(["IP Address", "Failed Login Count"])  # Column headers
    for ip, count in failed_attempts.items():
        if count > 10:  # Only include IPs with more than 10 failed login attempts
            csvwriter.writerow([ip, count])  # Write each suspicious IP and its failed login count

print("\nResults have been saved to log_analysis_results.csv")
