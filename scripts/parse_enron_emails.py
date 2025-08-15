
import re
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import click
import numpy as np
import pandas as pd
from tqdm import tqdm


def parse_enron_email(file: Path) -> pd.DataFrame:
    """Loads a single enron email file and extracts interesting values"""
    try:
        with file.open("r", encoding="utf-8") as email_file:
            text = email_file.readlines()
    except:
        print(f"Unreadable file at {file}")
        return pd.DataFrame()


    # date and sender are easy, fields are essentially fixed length
    date_regex = r"^Date: ([a-zA-Z0-9, :-]+)"
    date_match = get_field(date_regex, text)
    if date_match is None:
        return pd.DataFrame()
    
    date = datetime.strptime(date_match, "%a, %d %b %Y %H:%M:%S %z")

    sender_regex = r"^From: ([a-z.0-9]+@[a-z.0-9]+)"
    sender_match = get_field(sender_regex, text)
    if sender_match is None:
        return pd.DataFrame()
    sender = sender_match

    # receiver and subject require looping to ensure full coverage
    receiver_regex = r"^To: (.+)$"
    receivers_match = get_field(receiver_regex, text, r"Subject:")
    if receivers_match is None:
        return pd.DataFrame()
    
    receivers = receivers_match.split(" ")

    subject_regex = r"^Subject: (.+)$"
    subject = get_field(subject_regex, text, r"^Mime")
    if subject is None:
        return pd.DataFrame()

    # body we can just pull everything following the header
    body_line = find_line(r"^X-FileName", text) + 1
    body = "\n".join(text[body_line:])

    date_col = [date] * len(receivers)
    sender_col = [sender] * len(receivers)
    subject_col = [subject] * len(receivers)
    body_col = [body] * len(receivers)

    return pd.DataFrame({"sender": sender_col,
                         "receiver": receivers,
                         "datetime": date_col,
                         "subject": subject_col,
                         "body": body_col})


def find_line(match_string: str, text_lines: List[str]) -> int:
    """Finds a line containing a specified regular expression"""

    for i, line in enumerate(text_lines):
        if re.match(match_string, line):
            return i


def check_additional_lines(text: List[str],
                           start_line: int,
                           stop_string: str,
                           init_vals: str) -> Optional[str]:
    """Loop over lines from a starting line to extract field that overflows a
    single line"""

    forward_i = 1
    vals = init_vals
    while True:
        if start_line + forward_i >= len(text):
            return None
        if re.match(stop_string, text[start_line + forward_i]):
            return vals
        else:
            vals += text[start_line + forward_i].strip()
            forward_i += 1
        
        if forward_i > 10:
            return vals


def get_field(field_regex: str, text_lines: List[str], stop_regex: Optional[str] = None) -> Optional[str]:
    """Gets the text from a field in an email header. Provide stop regex if the field is potentially multiple lines"""
    
    field_line = find_line(field_regex, text_lines)
    
    if field_line is None:
        return None
    
    field_match = re.findall(field_regex, text_lines[field_line])
    field_str = field_match[0].strip()
    
    if stop_regex is not None:
        field_str = check_additional_lines(text_lines, field_line, stop_regex, field_str)

    return field_str


@click.command()
@click.argument("list_of_paths", type=Path)
@click.option("--output", "-o", type=Path, help="Path to save parsed emails to in csv format")
def parse_enron(list_of_paths, output):
    """Parses the emails stored in each file listed in LIST_OF_PATHS and saves a csv in OUTPUT"""

    with list_of_paths.open("r", encoding="utf-8") as email_list_file:
        email_list = email_list_file.readlines()
     
    df_list = []
    for email_file in tqdm(email_list):
        df = parse_enron_email(Path(email_file.strip()))
        df_list.append(df)
    
    all_parsed = pd.concat(df_list)
    all_parsed.to_csv(output, index=False)


if __name__ == "__main__":
    parse_enron()