import datetime

def get_days_from_today(date):
# string turn in object "datetime" and handle the error    
    try:
        required_day = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return 'Wrong format. It have to be "YYYY-MM-DD"'      

    current_day = datetime.datetime.today() # get current date
    interval = current_day - required_day # get the interval between input and current days
    return interval.days # return required interval in days


