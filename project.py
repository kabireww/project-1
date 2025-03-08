import csv
from datetime import datetime

# Function to read a CSV file
def read_csv_file(file_name):
    data_set = []
    with open(file_name, mode='r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_set.append(row)
    return data_set

# Function to write into CSV file
def write_csv_file(file_name, data_set):
    with open(file_name, mode='w', newline='', encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        for row in data_set:
            csv_writer.writerow(row)

def write_csv_file(file_name, data_set):
    if not data_set:  # handle error
        print(f"Skipping {file_name} because data is empty.") 
        return
    try:
       with open(file_name, mode='w', newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data_set) 
    except Exception as e: # handle error
        print(f"Error writing {file_name}: {e}")

# function to clean and format dates 
def format_date(date_str):
    date_formats = ["%d-%b-%y", "%Y-%m-%d", "%Y"]
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            return date_obj.strftime("%d-%b-%Y")  #format dates
        except ValueError:
            continue
    return ""  # return empty string if date is missing

# function to clean athlete bio 
def clean_athlete_bio(data):
    for row in data[1:]:  
        row[3] = format_date(row[3])   #access the born column to format date
    return data

# Function to generate unique IDs by accessing max id 
def create_new_id(main_data, paris_data):
    last_id = max(int(row[0]) for row in main_data[1:]) #find the maximum id
    for i, row in enumerate(paris_data[1:], start=last_id + 1):
        row[0] = str(i) 
    return paris_data

# Function to count the medals and tally them
def create_medal_tally(event_data):
    medal_tally = {}  # create dictionary to track medal counts
    for row in event_data[1:]: #iterate through event_data
        edition = row[0]
        noc = row[2]
        medal = row[9]
        if medal: 
            key = (edition, noc)
            if key not in medal_tally: 
                medal_tally[key] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            medal_tally[key][medal] += 1

    tally_rows = [['Edition', 'NOC', 'Gold', 'Silver', 'Bronze']]
    for (edition, noc), counts in medal_tally.items():
        tally_rows.append([edition, noc, counts['Gold'], counts['Silver'], counts['Bronze']])
    return tally_rows

if __name__ == "__main__":

    # read all the provided csv files 
    athlete_bio_file = read_csv_file("olympic_athlete_bio.csv")
    athlete_event_file = read_csv_file("olympic_athlete_event_results.csv")
    country_file = read_csv_file("olympics_country.csv")
    games_file = read_csv_file("olympics_games.csv")

    # Clean the athlete bio data
    cleaned_athlete_bio = clean_athlete_bio(athlete_bio_file)
    write_csv_file("new_olympic_athlete_bio.csv", cleaned_athlete_bio)

    # read all the csv files and merge the paris files into the existing csv files
    paris_athletes_file = read_csv_file("paris/athletes.csv")
    paris_athletes_file[0] = ['athlete_id', 'name', 'sex', 'born', 'height', 'weight', 'country', 'country_noc']
    paris_athletes_file = create_new_id(athlete_bio_file, paris_athletes_file)
    merged_athlete_bio = athlete_bio_file + paris_athletes_file[1:]  # Skip Paris header
    write_csv_file("new_olympic_athlete_bio.csv", merged_athlete_bio)

    medal_tally = create_medal_tally(athlete_event_file)
    write_csv_file("new_medal_tally.csv", medal_tally)

    # write into new csv files with the cleaned and integrated data
    write_csv_file("new_olympic_athlete_event_results.csv", athlete_event_file)
    write_csv_file("new_olympics_country.csv", country_file)
    write_csv_file("new_olympics_games.csv", games_file)
