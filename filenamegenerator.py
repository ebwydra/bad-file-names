import random
import datetime
import calendar

### Function that generates a string representing random file extension ###
def get_format():
    file_formats = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx','.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.bmp', '.gif', '.zip', '.mp3', '.jpg', '.rtf']

    extension_str = random.choice(file_formats)

    return extension_str

### Function that generates a string representing random date in a random format ###
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_day = random.randrange(delta.days)
    return start_date + datetime.timedelta(days=random_day) # this is a datetime object

def get_date(result_date):
    r = random.randint(0,1) # might or might not be a date
    if r == 1:
        # Month could be represented as the month number, name, or abbreviation #
        month_index = result_date.month
        month_formats = [str(month_index), calendar.month_name[month_index], calendar.month_abbr[month_index]]
        month = random.choice(month_formats)

        # Randomize whether the month or day comes first #
        monthday_as_list = [month, result_date.day]
        random.shuffle(monthday_as_list)

        # Also randomize the separator elements between parts of the date #
        date_separators = ['/', '.', '-', ' ']
        separator = random.choice(date_separators)

        # Randomly decide whether or not the year is included
        year_optional = (separator + str(result_date.year))*random.randint(0,1)

        # Put these elements together to generate a string representing the date
        date_str = str(monthday_as_list[0]) + separator + str(monthday_as_list[1]) + year_optional

        return date_str

    else:
        return ''

### Function that generates a string representing random version or draft number ###
def get_version():
    r = random.randint(0,1) # might or might not be a version number
    if r == 1:
        v = ['v', 'draft', 'DRAFT', 'version']
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        v_separators = ['', ' ', '-']
        v_str = random.choice(v) + random.choice(v_separators) + random.choice(nums)
        return v_str
    else:
        return ''

### Function that generates a string for something extra ###
def get_extra():
    r = random.randint(0,1) # might or might not be something extra
    if r == 1:
        extra_list = ['final', 'FINAL', 'clean', 'new', 'old', 'updated', 'current', 'approved', 'revised', 'DRAFT']
        separators = [' ', '_', '-']
        result = random.choice(separators) + random.choice(extra_list)
        r2 = random.randint(1,6)
        if r2 == 1:
            result += random.choice(separators) + random.choice(extra_list)
        else:
            pass
        return result

    else:
        return ''

### Function that generates a string for the 'body' of the file name ###
def get_filename():
    filename_list = ['Untitled', 'New Project', 'data', 'presentation', 'memo', 'schedule', 'agenda', 'notes', 'tracking', 'meeting agenda', 'meeting notes', 'tracking spreadsheet', 'project', 'results', 'final results', 'attendance', 'presentation slides', 'project']
    return random.choice(filename_list)

### Putting it all together! ###
def badfilename():
    result_date = generate_random_date(earliest_date,latest_date) # choose a date
    date_str = get_date(result_date) # string representing the date (can be empty)
    filename_str = get_filename() # string representing the 'body' of the filename
    datename_list = [date_str, filename_str] # put these two in a list
    random.shuffle(datename_list) # randomize so either date or 'body' can come first

    version_str = get_version() # string representing the version number (can be empty)
    extra_str = get_extra() # string representing 'extra' fun part (can be empty)
    format_str = get_format() # string representing file format extension

    elem_separators = [' ', '_', '-', ' ', '.']

    result = ''
    if len(datename_list[0]) > 0:
        result += datename_list[0]
    if len(datename_list[1]) > 0:
        if len(result) > 0:
            result +=  random.choice(elem_separators)
        result += datename_list[1]
    if len(version_str) > 0:
        result += random.choice(elem_separators) + version_str
    if len(extra_str) > 0:
        result += extra_str
    r = random.randint(1,8)
    if r == 1:
        result = str.upper(result)
    result += format_str

    return result

### Set the date range to something plausible ###
earliest_date = datetime.datetime.strptime('1/1/2010', '%m/%d/%Y')
latest_date = datetime.datetime.strptime('2/29/2020', '%m/%d/%Y')

### Show me some results ###
# i=0
# while i < 10:
#     print(badfilename())
#     i += 1
