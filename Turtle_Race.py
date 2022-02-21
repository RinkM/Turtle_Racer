from random import randint
from turtle import Turtle, Screen, done, resetscreen, clearscreen

from turtletest import flower

#things to improve for racers - a countdown 1,2,3 go!  sort of thing!  more audience members?  making bets on the winner. 

#TO DO Next 
#Show off winner!!
#what happens when a person has 0 money?
#upload to Github
#how to get rid of triangle turtle

# importing from turtletest is dirty.  loads 2 screens. exits out too early when 2 is selected.   

# def main():


#########   Program Starts Here   ###############

#Screen Settings : 
screen = Screen()
screen.colormode(255)


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
        print("1. Turtle Races")
        answer = screen.numinput("What do you want to see?", "1. Turtle Racer\n 2. Spirals (Not Working Yet) \n Select an option", 1, minval=1, maxval=5)
        
        # answer = input("What do you want to see? ")
        if int(answer) == 1:
            race_setup()
            screen.onscreenclick(resetscreen())
            
        elif int(answer) ==2:
            flower()
            screen.resetscreen()

def race_setup():
    racer_num = screen.numinput("Turtle Racer", "1 - 14: How many turtles will race?", 7, minval=1, maxval=14)
    total = int(racer_num)

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


    def update():    
        for k, v in profile.items():
            profile[k][0].turtle.clear()
            profile[k][0].turtle.write(f"    {k}: {profile[k][1]} Shells", False, align="left")

    def race_start():
        distance = 10
        while distance < 320:
            for k,car in racers.racers_dict.items():
                distance = car.ycor()
                if car.ycor() > 320:
                    print("We have a winner!")
                    race_start.winner = k
                    print(f"I was {k}")                 #here is teh winner.   K stores it!!!!!!!
                    car.write("I did it! I won!\n Bye Suckers!", True, align="center")
                    break

                elif car != racers.big_purple :
                    car.forward(2*roll())
                else: 
                    racers.big_purple.forward(2.3*roll())

    def payday():
        for k,v in profile.items():
            print(profile[k][2])
            if race_start.winner == profile[k][2]:
                profile[k][1] = profile[k][1] + (profile[k][3]*total)
            elif race_start.winner != profile[k][2]:
                profile[k][1] = profile[k][1] - (profile[k][3])
        update()

    def bets():
        for k,v in profile.items():
            selection = int(screen.numinput(f"{k}: "," Which Turt will win?", 1,  minval=1, maxval= total))
            select_turt = f"Racer{selection}"
            wager = int(screen.numinput(f"{k}:"," How much do you want to bet?", 10,  minval=1, maxval=profile[k][1]))

            profile[k][2]=select_turt
            profile[k][3]=wager

#######################
#####
####Race_setup - Load list :  

    create_course() #draws the course
    racers() 
    gamblers() #places gamblers. places bets
    race_start() #race starts. 
    payday()

    while True:
        for racer in racers.racers:                 #racers clear the track. 
            racer.clear()
            racer.hideturtle()
        racers()                #racers are remade
        bets()                  #bets are placed
        race_start()            #race starts
        payday()                #payday


    # screen.exitonclick()

main_menu()     #Starts at main menu
done()



if __name__ == '__main__':
    main_menu()