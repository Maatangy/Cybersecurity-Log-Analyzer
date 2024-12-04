# Cybersecurity-Log-Analyzer
## Overview
The Cybersecurity-Log-Analyzer is a Python-based script designed to efficiently process server log files and extract valuable insights for cybersecurity and operational purposes. It demonstrates expertise in file handling, string manipulation, data analysis, and reporting, making it an essential utility for organizations seeking robust log analysis solutions.

This project highlights my ability to work with real-world data and develop tools to identify key metrics, patterns, and potential security risks. It showcases my commitment to building solutions that are both practical and impactful.

---

## Features
### 1. **IP Address Analysis**
   - Counts the number of requests from each IP address.
   - Provides a clear breakdown of activity for better monitoring and resource allocation.

### 2. **Endpoint Analysis**
   - Identifies the most frequently accessed URLs (endpoints).
   - Offers insights into user behavior and popular resources on the server.

### 3. **Suspicious Activity Detection**
   - Flags IPs with excessive failed login attempts (default threshold: 10).
   - Helps detect potential brute force attacks or unauthorized access attempts.

### 4. **Export Results to CSV**
   - Outputs the analysis in a structured CSV format.
   - Easy to integrate with other reporting tools or share with stakeholders.

---

## Key Highlights
- **Efficient Data Processing**: Uses Python’s built-in modules and libraries like `collections.Counter` for fast and accurate analysis.
- **Clean and Modular Code**: Designed with readability and extensibility in mind.
- **Real-World Applicability**: Addresses common log analysis use cases in cybersecurity and system monitoring.
- **CSV Reporting**: Facilitates seamless integration with data visualization and reporting platforms.

---

## File Structure
VRV_Project/ ├── log_analysis.py # The Python script for log analysis ├── sample.log # Sample log file used for testing ├── log_analysis_results.csv # CSV file containing the analysis results ├── README.md # Documentation for the project

---

## How It Works
### **Step 1: Process the Log File**
The script reads the server log file (`sample.log`) line by line and extracts:
- IP addresses.
- Endpoints (URLs).
- Status codes to detect failed login attempts.

### **Step 2: Perform Analysis**
- **Requests per IP**: Counts and sorts the number of requests from each IP.
- **Most Accessed Endpoint**: Identifies the endpoint accessed most frequently.
- **Suspicious Activity Detection**: Flags IPs exceeding a configurable threshold for failed login attempts (default: 10).

### **Step 3: Save Results**
All results are saved in a CSV file (`log_analysis_results.csv`) with a clean structure:
1. Requests per IP.
2. Most accessed endpoint.
3. Suspicious activity (if any).

---

## Usage Instructions
### **Requirements**
- Python 3.13 or later.
- A server log file (e.g., `sample.log`).

### **Steps to Run**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/VRV-Log-Analyzer.git
   cd VRV-Log-Analyzer
 ---
Sample Output 
Sample terminal output 
 IP Address           Request Count
192.168.1.1          7
203.0.113.5          8
192.168.1.100        5
10.0.0.2             6
198.51.100.23        5

Most Frequently Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Detected:
IP Address           Failed Login Attempts
203.0.113.5          12
192.168.1.100        15

Sample CSV file output 
Requests per IP
IP Address,Request Count
192.168.1.1,7
203.0.113.5,8
192.168.1.100,5
10.0.0.2,6
198.51.100.23,5

Most Accessed Endpoint
Endpoint,Access Count
/login,13

Suspicious Activity
IP Address,Failed Login Count
203.0.113.5,12
192.168.1.100,15

     

   

