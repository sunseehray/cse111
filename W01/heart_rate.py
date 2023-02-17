# CSE 111 - Checkpoint 01
# Sunseehray Tirazona

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

def calculate_heart_rate(x):
    heart_rate = 220 - x
    return heart_rate

def calculate_lower_limit(y):
    lower_limit = .65 * y
    return lower_limit

def calculate_upper_limit(z):
    upper_limit = .85 * z
    return upper_limit


age = int(input('Please enter your age: '))

print('When you exercise to strengthen your heart, you should')
print(f'keep your heart rate between {(calculate_lower_limit(calculate_heart_rate(age))):.0f} and {(calculate_upper_limit(calculate_heart_rate(age))):.0f}')
print('beats per minute.')

input('Press ENTER to quit. ')