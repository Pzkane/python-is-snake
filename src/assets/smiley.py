import arcade

def drawSmiley():
    x = 300
    y = 300
    radius = 200
    arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

    x = 370
    y = 350
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

    x = 230
    y = 350
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

    x = 300
    y = 280
    width= 300
    height = 100
    start_angle = 190
    end_angle = 350
    arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle, 10)