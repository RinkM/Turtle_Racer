from random import randint, choice
from turtle import Turtle, Screen 
from time import sleep


#TO DO Next 
#upload to Github
#clean up the while lists and function lists at the bottom.
# Can I divide out functions?  
#What about global variables?  It works... but they're messy 


#########   Program Starts Here   ###############

#Screen Settings : 
screen = Screen()
screen.colormode(255)

#Globals 
global big_font
big_font=('Arial', 14, 'normal')



def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rand_color = (r,g,b)
    return rand_color

def roll():
    return randint(1,8)

class PlayerTurtle():
    def __init__ (self, count):
        self.self= self
        self.count = count
        self.turtle = Turtle()
        self.turtle.color(random_color())
        self.turtle.penup()
        self.turtle.shape("turtle")
        self.turtle.setposition((360,280-(count*25)))
        self.turtle.setheading(180)
        count += 1


class RacingTurtle(Turtle):
    def __init__(self, speed, position, words):
        super().__init__(shape='turtle', visible=False)
        self.color(random_color())
        self.penup()
        self.setposition(position)
        self.speed(speed)
        self.showturtle()
        self.setheading(90)
        self.write("\n\n" + words, False, 'left',  ('Arial', 8, 'bold'))


#### Game Code ####

def main_menu():
    for x in screen.turtles():
        x.hideturtle()
    while 1 == True:
        answer = screen.numinput("What do you want to see?", "1. Turtle Racer\n Select an option", 1, minval=1, maxval=5)
        if int(answer) == 1:
            race_setup()

def race_setup():
    racer_num = screen.numinput("Turtle Racer",
     "1 - 14: How many turtles will race?", 7, minval=1, maxval=14
     )
    total = int(racer_num)
    loser_retort = ["I'm out of shells. I'm going home.",
     "This game sucks.", 
     "That was fun while it lasted.", 
     "Anyone want to loan me some money?", 
     "Stupid turtle racing", 
     "I should have bet on Big Purple."
     ]

    def purp_roll():
        return randint(1,total)

    def create_course():
        curtle = RacingTurtle('normal', (-420,-380), " ")
        curtle.color("black")
        curtle.pendown()
        curtle.width(3)
        curtle.fd(700)
        curtle.rt(90)
        curtle.fd(760)
        curtle.rt(90)
        curtle.fd(700)
        curtle.penup()
        curtle.setposition(360,310)
        curtle.setheading(180)

    def racers():
        x,y = -400, -360            #starts racers line up on bottom
        racers.racers_dict = {}            # creates dict racer : turtleobject
        for i in range(1, 1+total):
            text = f"\nTurt {i}"
            racers.racers_dict[f"Racer{i}"] = RacingTurtle('normal', (x+(i*50),y), text)
        purp_roll()                 #rolls for which one will be purp
        racers.big_purple = racers.racers_dict[f"Racer{purp_roll()}"]
        racers.big_purple.color("indigo")   #applies purple paint
        racers.racers = racers.racers_dict.values()         #list of just the racers. 
        for turt in racers.racers:
            turt.forward(20)                #scoots racers ahead of their name. 


    def gamblers():
        count = 0
        global profile
        profile = {}
        total_players = int(screen.numinput("Players", "1 - 4 : How many people are betting?", 4,  minval=1, maxval=10))
        for num in range(1, 1+total_players):           #Creates gamblers and places them. 
            profile[f"Player{num}"] =  [PlayerTurtle(count),100,2,3]
            count+=1

        for k, v in profile.items():
            profile[k][0].turtle.clear()
            profile[k][0].turtle.write(f"    {k}: {profile[k][1]} Shells", False, align="left")

        for k,v in profile.items():
            selection = int(screen.numinput(f"{k}: "," Which Turt will win?", 1,  minval=1, maxval= total))
            select_turt = f"Racer{selection}"
            wager = int(screen.numinput(f"{k}:"," How much do you want to bet?", 10,  minval=1, maxval=profile[k][1]))

            profile[k][2]=select_turt
            profile[k][3]=wager
        


    def update():    #updates the purses for gamblers. 
        for k, v in profile.items():
            profile[k][0].turtle.clear()
            profile[k][0].turtle.write(f"    {k}: {profile[k][1]} Shells", False, align="left")

    def create_announcer():
        global flag
        flag = RacingTurtle('normal', (-450,30), " ")
        flag.color("red")
        flag.penup()
        
        #flag global co-ordinates.
        global home 
        home = (-450,30)
        global write_space 
        write_space = (-220,200)


    def count_down():       #announcer counts down the start of the race. turns red, orange, green.
        sleep(1)
        flag.goto(write_space)
        flag.color("red")
        flag.write(f"ON YOUR MARKS!", True, align="left", font = big_font)
        flag.color("orange")
        flag.backward(50)
        sleep(1)
        flag.write(f"GET SET!", True, align="left", font = big_font)
        flag.backward(50)
        flag.color("green")
        sleep(1)
        flag.write(f"GOOOOOOO!", True, align="left", font = big_font)
        sleep(.5)
        flag_return_home()

    def winner_announce():   #announces who won race and betting
        sleep(.5)
        flag.goto(write_space)
        flag.seth(90)
        flag.backward(75)
        flag.write(f"THE WINNING TURT IS {race_start.winner}!!!!", True, align="left", font = big_font)# fix {k}
        sleep(2)
        flag.color("orange")
        flag.goto(write_space)
        flag.backward(100)
        if winners == False:
            flag.write("Nobody won. Lame.", True, align="left", font = big_font)
        elif len(winners) >=2:
            flag.write(f" and ".join(winners) + " won shells!", True, align="left", font = big_font)# fix {k} 
        elif len(winners) == 1:
            flag.write(f"".join(winners) + " won shells!", True, align="left", font = big_font)# fix {k} 

        sleep(2)
        flag.color("red")
        flag.goto(write_space)
        flag.backward(150)
        flag.write("Is anyone out of money?", True, align="left", font = big_font)
        sleep(2)
        
        flag_return_home()



    def flag_return_home():  

        flag.clear()
        flag.setposition(-450,30)
        flag.setheading(0)


    def race_start():       #Racers start the race. 
        
        distance = 10
        while distance < 320:
            for k,car in racers.racers_dict.items():
                distance = car.ycor()
                if car.ycor() > 320:
                    race_start.winner = k
                    # print(f"The winner was {k}")                 #here is teh winner.   K stores it!!!!!!!
                    car.write("I did it! I won!\n Bye Suckers!", True, align="center")
                    break

                elif car != racers.big_purple :
                    car.forward(2*roll())
                else: 
                    racers.big_purple.forward((2.2*roll()))

    def payday():
        global winners

        winners = []
        print(winners)
        for k,v in profile.items():
            if race_start.winner == profile[k][2]:
                profile[k][1] = profile[k][1] + (profile[k][3]*total)
                winners.append(k)
            elif race_start.winner != profile[k][2]:
                profile[k][1] = profile[k][1] - (profile[k][3])
        print(f"The winners are {winners}")
        update()




    def remove_losers():
        global losers
        losers = []
        for k,v in profile.items():
            if profile[k][1] == 0:
                losers.append(k)
                profile[k][0].turtle.setposition(0,0)
                profile[k][0].turtle.clear()
                profile[k][0].turtle.write(choice(loser_retort), True, align="left", font = big_font)
                sleep(.5)
                profile[k][0].turtle.clear()
                profile[k][0].turtle.forward(450)
                profile[k][0].turtle.hideturtle()

            elif profile[k][1] > 0:
                continue
        for loser in losers:
            del profile[loser]

    def bets():

            
        for k,v in profile.items():
            selection = int(screen.numinput(f"{k}: "," Which Turt will win?", 1,  minval=1, maxval= total))
            select_turt = f"Racer{selection}"
            wager = int(screen.numinput(f"{k}:"," How much do you want to bet?", 10,  minval=1, maxval=profile[k][1]))

            profile[k][2]=select_turt
            profile[k][3]=wager

    def clear_track():
            for racer in racers.racers:                 #racers clear the track. 
                racer.clear()
                racer.hideturtle()
                flag.goto(home)



#######################
#####
####Race_setup - Load list :  
    
    # flag_wave()
    create_course() #draws the course
    racers() 
    create_announcer()
    gamblers() #places gamblers. places bets
    count_down()
    race_start() #race starts. 
    payday()
    winner_announce()

    remove_losers()

    

    while True:
    
        clear_track()
        racers()                #racers are remade
        bets()                  #bets are placed
        count_down()
        race_start()            #race starts
        payday()
        winner_announce()

        remove_losers()
        

    # screen.exitonclick()

main_menu()     #Starts at main menu
screen.done()



if __name__ == '__main__':
    main_menu()
