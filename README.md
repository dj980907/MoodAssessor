# Mood Assessor

This is an app where a user can enter their mood every day, and the program will diagnose any mood disorders detected over the course of the last week (7 days).

_Please note that this application is for educational and fun purposes only. It is intentionally simplistic, and does not attempt to accurately diagnose moods or psychiatric conditions!!!_

## Details

I created a function named `assess_mood()` in a file named `mood_assessor.py`, which performs the following tasks: Running this file directly will do nothing. 

This function is called from a file named `main.py` - running `main.py` is how the program should be run.


### Asking for a mood entry

Every day the program is run, it should do the following once:

1. ask the user to input their current mood
1. validate the user's response (the code must accept the following moods: `happy`, `relaxed`, `apathetic`, `sad`, and `angry`)
1. if the response was invalid, repeat starting from step 1 until valid response is gathered
1. translate the user's response to an integer (`happy` -> 2, `relaxed` -> 1, `apathetic` -> 0, `sad` -> -1, `angry` -> -2)
1. store the integer as a new line in a text file named `mood_diary.txt` within a subdirectory named `data`.

### Limit input to once-per-day

If the user has already entered a valid mood on any given day, and the user attempts to run the program again on that same day, the program must simply print, "Sorry, you have already entered your mood today." and quit.

Use the `datetime` module's `date.today()` function to determine the current date. For example:

```python
import datetime
date_today = datetime.date.today() # get the date today as a date object
date_today = str(date_today) # convert it to a string
```

### Diagnosing disorders

The first time the program is run each day, after gathering the mood from the user according to the instructions above, the program does the following:

1. check whether there are at least 7 entries in the `mood_diary.txt` file.
1. if not, do nothing further.
1. if so, retrieve the most recent 7 entries from the `mood_diary.txt` text file (i.e. the last 7 lines)
1. calculate the average mood from those entries (take the rounded numeric average of the 7 entries, and convert that to the appropriate string representing their average mood.)
1. if the user has been happy for 5 or more days out of the last 7 days, the user should be diagnosed as `manic`
1. if the user has been sad for 4 or more days out of the last 7, the user should be diagnosed as `depressive`
1. if the user has been apathetic for 6 or more days out of the last 7, the user should be diagnosed as `schizoid`
1. if none of the above apply, the user should be diagnosed with their average mood over the last 7 days
1. print out the user's diagnosis, following the format, "`Your diagnosis: schizoid!`", where `schizoid` is replaced with the correct diagnosis.
