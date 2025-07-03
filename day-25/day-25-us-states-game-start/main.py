import turtle 
import pandas as pd 

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while(len(guessed_states) < 50):

    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's a state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(f'{answer_state}', align='center', font=("Arial", 8, 'normal'))
    
difference = [s for s in all_states if s not in guessed_states]

state_dict = {
    "Missed States": sorted(difference)
}
    
df = pd.DataFrame(state_dict)

df.to_csv("states_to_learn.csv")


turtle.mainloop()
