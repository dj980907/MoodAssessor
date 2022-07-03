
def ask_mood():
    """
    This function asks the user for their mood\n
    : return: user's response.
    """
    is_valid_input = False
    valid_input = ['happy', 'relaxed', 'apathetic', 'sad', 'angry']
    while not is_valid_input:
        response = input("What is your current mood? ")
        if response in valid_input:
            is_valid_input = True
            return response
  

def convert_mood_to_int(response): 
    """
    This function converts mood into an integer\n
    : return: integer version of the response.
    """  
    if response.lower() == 'happy':
        response = 2
        return response
    elif response.lower() == 'relaxed':
        response = 1
        return response
    elif response.lower() == 'apathetic':
        response = 0
        return response
    elif response.lower() == 'sad':
        response = -1
        return response
    elif response.lower() == 'angry':
        response = -2
        return response


def write_text(response_int_version, date):
    """
    This function writes integer converted version of mood to the mood_diary.txt.
    """
    f = open('data/mood_diary.txt', 'a')
    f.write(response_int_version)
    f.write(',')
    f.write(date)
    f.write('\n')
    f.close()

def calculate_average(lines):
    """
    This function calculates the average of moods within 7 days\n
    : return: average in integer
    """
    sum = 0
    for i in lines:
        num = int(i.split(',')[0])
        sum = sum + num
    average = round(sum / len(lines))
    return average


def convert_average_to_string(average):
    """
    This function converts average calculated in calculate_average() into string that matches the appropriate mood\n
    : return: if the average is 2, happy, if the average is 1, relaxed, if the average is 0, apathetic, 
    if the average is -1, sad, and if the average is -2, angry
    """
    if average == 2:
        return 'happy'
    elif average == 1:
        return 'relaxed'
    elif average == 0:
        return 'apathetic'
    elif average == -1:
        return 'sad'
    elif average == -2:
        return 'angry'


def diagnosis(lines):
    """
    This function gives diagnosis of the user using 7 responses\n
    : return: diagnosis
    """
    mood_list = []
    for i in lines:
        mood_list.append(i.split(',')[0])
    if mood_list.count('2') >= 5:
        return 'manic'
    elif mood_list.count('-1') >= 4:
        return 'depressive'
    elif mood_list.count('0') >= 6:
        return 'schizoid'
    else:
        average = calculate_average(lines)
        return convert_average_to_string(average)


def print_diagnosis(diag):
    """
    This function just prints out the text saying the diagnosis of the user.
    """
    print("Your diagnosis: {}!".format(diag))


def date():
    """
    This function returns today's date\n
    : return: today's date.
    """
    import datetime
    date_today = datetime.date.today() 
    date_today = str(date_today)
    return date_today


def assess_mood():
    """
    This function is the final step of actually assesing the mood. 
    all the necessary functions are run here.
    """
    f = open('data/mood_diary.txt', 'r')
    lines = f.readlines()
    dates_list = []
    for i in lines:
        dates_list.append(i.split(',')[1])
    print(dates_list)
    if (date()+'\n') in dates_list:
         print("Sorry, you have already entered your mood today.")
    else:         
        response = ask_mood()
        response_int_version = convert_mood_to_int(response)
        date_today = date()
        write_text(str(response_int_version), date_today)
        f = open('data/mood_diary.txt', 'r')
        lines = f.readlines()
        if len(lines) >= 7:
            lines = lines[-7:]
            diag = diagnosis(lines)
            print_diagnosis(diag)


# def assess_mood():
#     """
#     This function is the final step of actually assesing the mood. 
#     all the necessary functions are run here.
#     """   
#     response = ask_mood()
#     response_int_version = convert_mood_to_int(response)
#     write_text(str(response_int_version))
#     date_today = date()
#     write_date(date_today)
#     f = open('data/mood_diary.txt', 'r')
#     lines = f.readlines()
#     if len(lines) >= 7:
#         lines = lines[-7:]
#         diag = diagnosis(lines)
#         print_diagnosis(diag)




    
        