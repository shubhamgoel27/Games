# Implementation of classic arcade game Pong
# Link: http://www.codeskulptor.org/#user38_Wz5d7tDuW3_0.py
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20

PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
paddle1_vel = 0.0
paddle2_vel = 0.0

ball_pos = [WIDTH/2 , HEIGHT/2]
ball_vel = [0,0]
LEFT = False
RIGHT = True

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is right, else left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = 200/60.0
    else:
        ball_vel[0] = -200/60.0
    ball_vel[1]= 150.0 / 60.0

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  

    if ( ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos[1] -30) and (ball_pos[1] <= (paddle1_pos[1] + 30)):
            ball_vel[0]*=(-1.1)             
        else :                            
            spawn_ball(RIGHT)
            score2+=1
    
    if ( ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH):
        if (ball_pos[1] >= paddle2_pos[1] -30) and (ball_pos[1] <= (paddle2_pos[1] + 30)):
            ball_vel[0]*=(-1.1)
        else :                            
            spawn_ball(LEFT)
            score1+=1
    
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]    
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] 
                         
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Blue")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    # draw paddles    
    canvas.draw_line((paddle1_pos[0],paddle1_pos[1]-30), (paddle1_pos[0],paddle1_pos[1]+30), 10, 'Red')
    canvas.draw_line((paddle2_pos[0],paddle2_pos[1]-30), (paddle2_pos[0],paddle2_pos[1]+30), 10, 'Red')
    # draw scores
    canvas.draw_text(str(score1),[WIDTH/2 - 75,50],50,'red')
    canvas.draw_text(str(score2),[WIDTH/2 + 75,50],50,'red')     
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3.5
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game",new_game)


# start frame
new_game()
frame.start()
