import turtle
import pandas

screen = turtle.Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.setup(width=725, height=491)
states = pandas.read_csv("50_states.csv")
us_states = states.state
state_list = us_states.to_list()
states_guessed = 0
tries = 5
guessed_states = []
game_on = True
while game_on:

    answer = turtle.textinput(f"{states_guessed}/50     Tries:{tries}", "Enter a state:").title()
    state_coord = states[states.state == answer]
    if answer in guessed_states:
        pass
    elif answer in state_list:
        states_guessed += 1
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state_coord.x), int(state_coord.y))
        t.write(answer)

    if states_guessed == 50:
        game_on = False
        z = turtle.Turtle()
        z.penup()
        z.hideturtle()
        z.goto(-250, 0)
        z.write(f"Congratulations, you guessed {states_guessed} states!", font=("arial", 18, "normal"))
    if answer not in state_list:
        tries -= 1
        if tries == 0:
            game_on = False
            z = turtle.Turtle()
            z.penup()
            z.hideturtle()
            z.goto(-250, 0)
            z.write(f"Congratulations, you guessed {states_guessed} states!", font=("arial", 18, "normal"))

    if not game_on:
        remaining_states = [state for state in state_list if state not in guessed_states]
        to_learn = pandas.DataFrame(remaining_states)
        to_learn.to_csv("Remaining States")





screen.mainloop()