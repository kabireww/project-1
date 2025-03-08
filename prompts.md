AI Prompt Tracking
Kabir Donda
Prompt 1:
Prompt: "Generate a function to clean athlete birthdates in the olympic_athlete_bio.csv file and format them to dd-Mon-yyyy."

Result: GitHub Copilot provided a function that tried to parse and format dates. However, it did not fully handle invalid or incomplete dates (e.g., missing month or year).
Tweak: I modified the function to return an empty string "" for invalid or incomplete dates, and to account for the cases where only the year was provided.
Prompt 2:
Prompt: "Write a Python function to merge the Paris 2024 data into the existing Olympic data without duplicates. Use csv.reader and assign new unique IDs to the Paris athletes."

Result: Copilot provided a basic structure for reading CSV files and merging data, but it did not specify how to handle duplicate entries or assign unique IDs.
Tweak: I added logic to check for duplicate athletes based on their ID or name, and used a max() function to determine the highest existing ID in the main dataset to assign new IDs to the Paris data.


Himanshu
Prompt 1:
Prompt: "How do I calculate the age of an athlete during a specific Olympic event using the born column and the event date?"

Result: ChatGPT suggested using Python's datetime module to calculate the difference between the birthdate and the event date.
Tweak: I implemented this approach by adding an "age" column in the olympic_athlete_event_results.csv file. I also made sure to handle cases where birthdates were missing or incomplete.
Prompt 2:
Prompt: "Provide a function that generates a medal tally summary for each country based on the event results file."

Result: ChatGPT provided a basic version of a medal_tally() function that summed the number of medals by country.
Tweak: I expanded the function to include gold, silver, and bronze counts and ensured it wrote the summary data to a new CSV file (new_medal_tally.csv).


Vritant
Prompt 1:
Prompt: "How do I merge two datasets in Python while ensuring there are no duplicates?"

Result: ChatGPT suggested using the pandas.merge() function, but since pandas was not allowed, it also mentioned using csv.reader and manual merging.
Tweak: I used csv.reader and added logic to ensure no duplicate entries for athletes already existing in the main dataset.


Conclusion:

Kabir Donda worked on the date formatting and Paris data merging.
Himanshu handled calculating athlete ages and medal tally generation.
Vritant worked on merging datasets and ensuring no duplicates.