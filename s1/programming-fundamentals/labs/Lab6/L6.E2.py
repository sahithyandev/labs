from datetime import datetime


def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Your code should be included here.
# You may use the days_to_birthday(date) function in your solution.

lines = [
    "Saman 1990-05-03 M",
    "Aruni 1990-04-06 F",
    "Kumaran 1988-03-05 M",
    "Nazar 1997-09-24 M",
]


def pad_start(base_str: str, expected_length: int, fill_character: str):
    length_difference = expected_length - len(base_str)
    if length_difference <= 0:
        return base_str

    return fill_character * length_difference + base_str


# to store the count of people born on the same year
year_count = {
    2003: 10
}

for line in lines:
    [name, date_of_birth, gender] = line.split()

    year = date_of_birth.split("-")[0]
    # if the year is not included in the year_count dictionary
    # I set it to 0
    # otherwise I increment the count by 1
    if year in year_count:
        year_count[year] += 1
    else:
        year_count[year] = 1

    days_since_jan_first = days_to_birthday(date_of_birth)
    if gender == "F":
        days_since_jan_first += 500

    nic = year + pad_start(str(days_since_jan_first), 3, "0") + \
        pad_start(str(year_count[year]), 3, "0")

    print(nic)
