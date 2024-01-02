from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    holiday = ["Saturday", "Sunday"]
    birthday_dict = {day: [] for day in weekdays}
    birthday_holiday = {day: [] for day in holiday}
    
    for user in users:
        user_birthday = user['birthday'].replace(year=today.year)

        if user_birthday < today:
            user_birthday = user_birthday.replace(year=today.year + 1)
        
        days_until_birthday = (user_birthday - today).days
        if days_until_birthday <= 6:
            if days_until_birthday < 0:
                days_until_birthday += 365
            
            day_of_week = (today + timedelta(days_until_birthday)).strftime('%A')
            
            if day_of_week in birthday_holiday:    
                birthday_holiday[day_of_week].append(user['name'].split()[0])
                if birthday_holiday:
                    if 'Sunday' in birthday_holiday:
                        birthday_dict['Monday'].extend(birthday_holiday['Sunday'])
                    if 'Saturday' in birthday_holiday:
                        birthday_dict['Monday'].extend(birthday_holiday['Saturday'])
           
            if day_of_week in birthday_dict:
                birthday_dict[day_of_week].append(user['name'].split()[0])
                
    if not any(birthday_dict.values()):
        return {}
    else:
        non_empty_days = {day: users for day, users in birthday_dict.items() if users}
        return non_empty_days