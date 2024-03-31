import argparse
import httpx
import asyncio
import sys
import os
import pyfiglet
from termcolor import colored
from colorama import init

init(autoreset=True)

def load_wordlist(wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(colored(f"Wordlist file '{wordlist_file}' not found.", 'red'))
        return []
    except Exception as e:
        print(colored(f"An error occurred while loading the wordlist: {e}", 'red'))
        return []

def print_status_code(status_code):
    if status_code == 200:
        return colored(f"[{status_code}]", 'green', attrs=['bold'])
    elif status_code == 404:
        return colored(f"[{status_code}]", 'red', attrs=['bold'])
    elif status_code == 302:
        return colored(f"[{status_code}]", 'yellow', attrs=['bold'])
    elif status_code == 500:
        return colored(f"[{status_code}]", 'magenta', attrs=['bold'])
    elif status_code == 403:
        return colored(f"[{status_code}]", 'blue', attrs=['bold'])
    elif status_code == 301:
        return colored(f"[{status_code}]", 'gold', attrs=['bold'])
    else:
        return colored(f"[{status_code}]", 'white', attrs=['bold'])


def print_welcome_message():
    welcome_text = r"""
██████╗ ██╗   ██╗████████╗██╗  ██╗ █████╗ 
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔══██╗
██████╔╝ ╚████╔╝    ██║   ███████║███████║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██╔══██║
██║        ██║      ██║   ██║  ██║██║  ██║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                          
"""
    separator = '-' * 50
    print(colored(welcome_text, 'blue'))
    print(colored(separator, 'cyan'))
    print(colored("A PYTHA-FUZZ tool developed by Shivang.join our telegram @pythagorex", 'green'))
    print(colored("Getting Issue? Check Github https://github.com/shivangmauryaa", 'green'))
    print(colored(separator, 'cyan'))

def print_farewell_message(author_name):
    separator = '-' * 50
    print(colored(separator, 'cyan'))
    print(colored("I Hope You Like The tool for more check Github : https://github.com/shivangmauryaa", 'yellow'))
    print(colored(f"Author: {author_name}", 'blue'))
    print(colored(separator, 'cyan'))

def save_to_file(output_file, text):
    try:
        with open(output_file, 'a') as file:
            file.write(text + '\n')
    except Exception as e:
        print(colored(f"An error occurred while saving to the output file: {e}", 'red'))

async def dirsearch(target_url, wordlist, max_retries, timeout, user_agent, follow_redirects, output_file=None):
    try:
        async with httpx.AsyncClient() as client:
            client.headers['User-Agent'] = user_agent

            for directory in wordlist:
                url = f"{target_url}/{directory}"
                retries = 0

                while retries <= max_retries:
                    try:
                        response = await client.get(url, timeout=timeout, follow_redirects=follow_redirects)

                        status_code = response.status_code
                        result = f"{print_status_code(status_code)} {url}"
                        print(result)

                        if output_file:
                            save_to_file(output_file, result)

                        break

                    except httpx.NetworkError as e:
                        if retries < max_retries:
                            retries += 1
                            print(colored(f"Network error (retrying {retries}/{max_retries}): {e}", 'yellow'))
                            await asyncio.sleep(2 ** retries)
                        else:
                            print(colored(f"Network error (max retries reached): {e}", 'red'))
                            break

                    except KeyboardInterrupt:
                        print(colored("Fuzzing interrupted by user.", 'yellow'))
                        return

                    except Exception as e:
                        print(colored(f"An error occurred: {e}", 'red'))
                        break

    except asyncio.CancelledError:
        print(colored("Fuzzing task was canceled.", 'yellow'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Dir-Miner tool.")
    parser.add_argument("-u", "--url", required=True, help="Target URL to search.")
    parser.add_argument("-w", "--wordlist", help="Wordlist file containing directories to check.")
    parser.add_argument("-t", "--timeout", type=float, default=5.0, help="Timeout for HTTP requests (default: 5.0 seconds)")
    parser.add_argument("-ua", "--user-agent", default="DirectorySearchBot", help="Custom User-Agent header for HTTP requests")
    parser.add_argument("-f", "--follow-redirects", action="store_true", help="Follow HTTP redirects")
    parser.add_argument("-o", "--output", help="Output file to save results.")
    parser.add_argument("-r", "--retries", type=int, default=3, help="Maximum number of retries for failed requests")

    args = parser.parse_args()

    print_welcome_message()

    if args.wordlist is None:
        wordlist = load_wordlist("wordlist.txt")
    else:
        wordlist = load_wordlist(args.wordlist)

    asyncio.run(dirsearch(args.url, wordlist, args.retries, args.timeout, args.user_agent, args.follow_redirects, args.output))

    print_farewell_message("Shivang")

    if args.output:
        sys.exit(0)