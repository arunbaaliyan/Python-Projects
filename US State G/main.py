from turtle import Turtle, Screen
import pandas

data = pandas.read_csv('50_states.csv')
total = 50
correct_guess = []
screen = Screen()
screen.setup(width=725, height=491)
screen.title('US states game')
img = 'blank_states_img.gif'
screen.bgpic(img)

t = Turtle()
t.hideturtle()
t.penup()
states = data.state.to_list()


while len(correct_guess) < total:
    ans = screen.textinput(f'Guess the state?({len(correct_guess)}/{total})', "What's another state name?").title()
    # ans = states[correct]
    if ans == 'Exit':
        missed_states = [s for s in states if s not in correct_guess]
        pandas.Series(missed_states).to_csv('missed_states.csv' )
        break
    else:
        new_data = data[data.state == ans]
        if new_data.size:
            x = int(new_data.x)
            y = int(new_data.y)
            t.goto(x, y)
            t.write(arg=ans, align='center')
            correct_guess.append(ans)
            
