import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")




data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]


while len(guessed_states) <50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "whats another state name?").title()
    if answer_state=="Exit":
        missing_states=[]
        missing_states=[state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("sates_to_learn.csv")

        print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())

# screen.exitonclick()







# def get_loc_mouse(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_loc_mouse)
# turtle.mainloop()
#
#


