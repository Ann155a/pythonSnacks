# Convert seconds to hours
def secs2time(sec):
    # Calculate the number of days
    days = sec // (24 * 60 * 60)
    sec %= (24 * 60 * 60)  # Update sec to the remaining seconds after days

    # Calculate the number of hours
    hrs = sec // (60 * 60)
    sec %= (60 * 60)  # Update sec to the remaining seconds after hours

    # Calculate the number of minutes
    minutes = sec // 60
    sec %= 60  # Update sec to the remaining seconds after minutes

    # Remaining seconds
    seconds = sec
    return f"days {days}, hrs {hrs}, minutes {minutes}, seconds {seconds}"
