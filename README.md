# Directory Search Tool (FUZZER)

![FUZZER Logo](https://static.thenounproject.com/png/2221438-200.png)

## Introduction

FUZZER is a simple pytha-fuzz tool developed by Shivang-Maurya It helps you discover directories on a target website by probing different paths. This tool is designed for security testing, web application analysis, and penetration testing.

## Features

- Fast and efficient directory scanning
- Customizable User-Agent header
- Option to follow HTTP redirects
- Verbose mode for detailed output
- Save results to an output file
- Colorful and user-friendly command-line interface

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/shivangmauryaa/pytha-fuzz.git
   cd Dir-Miner
   ```
2. Install the required packages:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

Use the following command-line arguments to run Dir-Miner:
```shell
-u or --url: The target URL to search (required).
-w or --wordlist: Wordlist file containing directories to check.
-t or --timeout: Timeout for HTTP requests (default: 5.0 seconds).
-ua or --user-agent: Custom User-Agent header for HTTP requests (default: DirectorySearchBot).
-f or --follow-redirects: Follow HTTP redirects (optional).
-v or --verbose: Enable verbose mode (optional).
-o or --output: Output file to save results (optional).
```

Example usage:
```shell
python3 dirminer.py -u http://example.com -w wordlist.txt -o output.txt    // Custom
python3 dirminer.py -u http://example.com // Auto
```



## Author
[ShivangMaurya](https://github.com/shivangmauryaa)
<br>
[linkedin](https://www.linkedin.com/in/shivangmauryaa/)
<br>

## License

This tool is licensed under the MIT License. See the LICENSE file for details.

## Support
For bug reports, feature requests, or general inquiries, please create an issue. for more good result use your self made wordlist 
