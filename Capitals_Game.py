
import random
states = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta','Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

print('Welcome to the game that helps you learn the capitals for each state.\n')
#num = input('How many capitals would you like to guess?\n')
study_states = str(input('Would you like to study the capitals first?\n Type YES to study the capitals and NO to proceed directly to the game.\n'))
if study_states == 'YES' or study_states == 'Yes' or study_states == 'yes':
    print('Here is a list of the states and their capitals to study.\n')
    print('The format is:\n\n State               Capital\n')
    for key, value in states.items():
        print('{:20} {}\n'. format(key, value))
else:
    print('Ok, lets start the game!\n')
states_tupe = ('Alabama',
'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
'Utah', 'Vermont', 'Virginia','Washington', 'West Virginia', 'Wisconsin',
'Wyoming')

num = input('How many capitals would you like to guess?\n')
num = int(num)

right = 0
wrong = 0
right_set = set()
wrong_set = set()
for number in range (0,num):
    n = random.randint(0,49)
    random_state = (states_tupe[n])
    user_capital = str(input('\nWhat is the captiol of {}?\n'. format(random_state)))
    correct_answer = states[states_tupe[n]]
    if user_capital == correct_answer:
        print('Yes! The capital of {} is {}!\n'. format(random_state,correct_answer))
        right = right + 1
        right_set.add(random_state)

    else:
        print('No, the capital of {} is {}.\n'. format(random_state, correct_answer ))
        wrong = wrong + 1

        wrong_set.add(random_state)

print('Thanks for playing!\n')
summary = 'You got {} right and {} wrong.\n'. format(right,wrong)
print(summary)

wrong_list = list(wrong_set)

states2 = {x:states[x] for x in wrong_list}
if wrong > 0:
    print('You should study the following combinations of states and capitals:\n')
    for key, value in states2.items():
        print('{:20} {}\n'. format(key, value))
else:
    print('Congratulations on a perfect score!')
