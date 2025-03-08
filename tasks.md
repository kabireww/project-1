# Tasks for Olympic Data Project

## Group Members:
- Kabir Donda (140630229)
- Himanshu (171285224)
- Vritant (101025237)

## Task List:

### 1. Data Loading and Writing (Assigned to: Kabir Donda)
- Implement functions to read data from CSV files (`load_csv`) and write data to new CSV files (`save_csv`).
- Ensure that all data from the input files is correctly read and written to the new output files.

### 2. Data Cleaning (Assigned to: Himanshu)
- Standardize the "born" column in `olympic_athlete_bio.csv` to the format `dd-Mon-yyyy` (e.g., 25-Feb-2025).
- Handle any missing or incomplete data, leaving fields empty when necessary or making reasonable estimates.

### 3. Paris Data Integration (Assigned to: Vritant)
- Merge the Paris 2024 Olympic data with the existing datasets.
- Assign unique IDs to Paris data, ensuring no duplicates are added from athletes who already participated in previous Olympics.

### 4. Medal Tally Calculation (Assigned to: Himanshu)
- Implement the function `generate_medal_tally()` to calculate the number of gold, silver, and bronze medals by country and Olympic edition.
- Write the tally to a new CSV file (`new_medal_tally.csv`).

### 5. Final Testing and Debugging (Assigned to: All members)
- Test the entire program to ensure it works as expected (loading, cleaning, merging, and writing the data).
- Debug any issues or errors that arise during testing.
