## pygame circle draw test

import pygame 
import pygame.locals as loc

import pygame.gfxdraw as d

import math


def supersampled_aacircle(surf, pos, r, i):
    temp_surf = pygame.Surface((r*2*i, r*2*i))
    temp_surf.fill((255,255,255))
    pygame.draw.circle(temp_surf, (200,0,0), (r*i, r*i), r*i)
    surf.blit(pygame.transform.smoothscale(temp_surf, (r*2, r*2)), pos)

def draw_aacircle(surf, color, pos, rad):
    pygame.gfxdraw.aacircle(surf, pos[0], pos[1], rad, color)
    pygame.gfxdraw.filled_circle(surf, pos[0], pos[1], rad, color)
    
#def draw_circle_segment(surf, color, pos, rad1, rad2, start, stop, aa=5):
#    temp_surf = pygame.Surface((rad1*aa, rad2*aa))
#    temp_surf.fill((255,255,255))
##   start = 0
##   stop = deg
#    size = temp_surf.get_size()
#    off_x, off_y = size[0]/2, size[1]/2                
#    r = min(off_x, off_y) - 10
#    points = []
#    # maybe multiply stop value by factor f and then use i/f in calculation?                  
#    for i in xrange(start+90, stop+91):  
        
#        y = off_y - math.sin(math.radians(i)) * r #* aa
#        x = off_x - math.cos(math.radians(i)) * r #* aa
#        points.append((x,y))
        
#    pygame.draw.polygon(temp_surf, color, points+[(off_x, off_y)])
#    w, h = temp_surf.get_size()
#    surf.blit(pygame.transform.smoothscale(temp_surf, (w/aa, h/aa)), pos)


def bounding_box(points):
    xs = [int(x) for x, y in points]
    ys = [int(y) for x, y in points]
    left, top = min(xs), min(ys)
    width, height = max(xs) - left, max(ys) - top
    return pygame.Rect(left, top, width+1, height+1)


#def bounding_box(points):
#    l = [(1,1)]*len(points)
    
#    print zip(points, l)
#    return pygame.Rect().unionall(zip(points, l))
    
    

def draw_line(surf, color, start, stop, width, aa=5):
    x1, y1 = start
    x2, y2 = stop
    w = width / 2.
    if x1 == x2:
        points = [(x1-w, y1), (x1+w, y1), (x1+w, y2), (x1-w, y2)]
    elif y1 == y2:
        points = [(x1, y1-w), (x1, y1+w), (x2, y1+w), (x2, y1-w)]
    else:
        orig_m = float(y2-y1) / float(x2-x1)
        m = - 1. / orig_m
        l = math.sqrt(1+m*m)
        n = width/ (2.*l)
        points = []
        for (x, y), i in (((x1, y1), 1), ((x2, y2), 1), ((x2, y2), -1), ((x1, y1), -1)):
            points.append((x+n*i, y+n*m*i))
        
   # old_rect = old_bounding_box(points)
    rect = bounding_box(points)
   # print rect, old_rect, rect==old_rect
    x_off, y_off = rect.topleft
    if aa:
        points = [((x-x_off)*aa, (y-y_off)*aa) for x, y in points]
        temp_surf = pygame.Surface((rect.width*aa, rect.height*aa)).convert_alpha()
        temp_surf.fill((0,0,0,0))
        pygame.draw.polygon(temp_surf, color, points)
        surf.blit(pygame.transform.smoothscale(temp_surf, rect.size), rect.topleft)
    else:
        pygame.draw.polygon(surf, color, points)
    return rect
   
    
        
    


def _arc_coords(r, start, stop, off_x, off_y):
    #off_x, off_y = r, r
    points = []
    for i in xrange(start, stop+1):  
        y = off_y - math.sin(math.radians(i)) * r #* aa
        x = off_x - math.cos(math.radians(i)) * r #* aa
        points.append((x,y))
    return points

def draw_circle_segment(surf, color, pos, rad1, rad2, start, stop, aa=5):
    if rad1 < rad2:
        rad1, rad2 = rad2, rad1
    if start == stop:
        raise ValueError
    temp_surf = pygame.Surface((rad1*aa*2, rad1*aa*2)).convert_alpha()
    #temp_surf.fill((255,255,255,0))
    temp_surf.fill(color[:3]+(0,))
    start += 90
    stop += 90
    size = temp_surf.get_size()
    off_x, off_y = size[0]/2., size[1]/2.
   # r = min(off_x, off_y) - 10
   # points = []
    # maybe multiply stop value by factor f and then use i/f in calculation?                  
#    print "rad", rad1, rad2
    outer = _arc_coords(rad1*aa, start, stop, rad1*aa, rad1*aa)
    if rad2 == 0:
        inner = [(off_x, off_y)]
    else:
        inner = _arc_coords(rad2*aa, start, stop, rad1*aa, rad1*aa)
        inner.reverse()
   # print off_x, off_y
    points = outer + inner
   # points = inner
   # points = outer +  inner
   # print start, stop
#    print inner
   # print points
#    print outer
    pygame.draw.polygon(temp_surf, color, points)
    #pygame.draw.lines(temp_surf, (0,200,0), 0, outer, 2)
    #pygame.draw.lines(temp_surf, (200,0,0), 0, inner, 2)
    
    w, h = temp_surf.get_size()
    x, y = pos
    pos = (x-rad1, y-rad1)
    surf.blit(pygame.transform.smoothscale(temp_surf, (w/aa, h/aa)), pos)
    
def draw_cog(surf, pos,r1, r2, color, offset):
    for y in xrange(0, 360, 60):
        draw_circle_segment(surf, color, pos, r1, r2, 
                            start=y+offset, stop=y+offset+30)
        draw_aacircle(surf, color, pos, r2+1)

def main():
    pygame.init()
    print pygame.transform.get_smoothscale_backend()
    big_font = pygame.font.SysFont("Arial", 17, bold=True, italic=True)
    font = pygame.font.SysFont("Arial", 15)
    
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("PyGamery")
    screen.fill((255,255,255))
    
    s = big_font.render("PyGamery",
                        1, (0,200,0), (255,255,255))
    sr = s.get_rect(midtop=(300,10))
    screen.blit(s,sr)
    

    
    
    static = screen.copy()
    # surf, color, pos, rad1, rad2, start, stop, aa=5):
#    i = +70
#    draw_circle_segment(screen, (200,0,0), (450, 300), 40, 25, start=0+i, stop=100+i)
#    draw_circle_segment(screen, (200,0,0), (450, 300), 40, 25, start=120+i, stop=220+i)
#    draw_circle_segment(screen, (200,0,0), (450, 300), 40, 25, start=240+i, stop=340+i)
    i = 0
    counter = 0
    line_counter = 0
    line_offset = 0
    clock = pygame.time.Clock()
    offset = 0
    paper_speed = 3
    points = []
    lines = pygame.Surface((160, 360))
    lines.fill((255,255,255))
    for i in xrange(0, 360, 20):
        pygame.draw.aaline(lines, (0,0,0), (0, i), (160, i))
#    draw_line(screen, (200,0,0), p1, p2, 20)
    while True:
        screen.fill((255,255,255), (0, 50, 600, 500))
        milli = clock.tick(60)
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == loc.QUIT:
                return
            elif event.type == loc.KEYDOWN:
                if event.key == loc.K_ESCAPE:
                    return
            elif event.type == loc.MOUSEBUTTONDOWN:
                if event.button == 1:
                    p2 = event.pos
#                elif event.button == 3:
#                    p2 = event.pos
                elif event.button == 4:
                    offset += 50
                    if offset > 0:
                        paper_speed += 1
                    else:
                        paper_speed -= 1
                elif event.button == 5:
                    offset -= 50
                    if offset < 0:
                        paper_speed += 1
                    else:
                        paper_speed -= 1
                fps = clock.get_fps()
                print offset*int(fps) / 360 *60, "rmp with %s fps" % fps
        
        i += offset*milli/1000. 
        i %= 360
        line_counter += milli/1000. * offset*188/360.
        line_counter %= 31
#        if any(pygame.mouse.get_pressed()):
#            p1 = pygame.mouse.get_pos()
        #screen.fill((255,255,255, 255), (400,280, 200,100))
#        screen.blit(static, (0,0))
      #  screen.fill((20,0,0, 255), (400,280, 200,100))
        p = (500,100) # (350, 340)
        draw_circle_segment(screen, (200,0,0), p, 40, 25, start=0+i, stop=100+i)
        draw_circle_segment(screen, (246, 238, 98), p, 40, 25, start=120+i, stop=220+i)
        draw_circle_segment(screen, (0,0,200), p, 40, 25, start=240+i, stop=340+i)
    
        
        draw_circle_segment(screen, (200,200,200), (370, 300), 40, 0, start=0+i, stop=150+i)
        draw_circle_segment(screen, (100,100,100), (370, 300), 40, 0, start=180+i, stop=360+i)
        draw_circle_segment(screen, (100,100,100), (370, 300), 50, 40, start=180+i, stop=360+i)
        draw_cog(screen, (500, 340), 40, 30, (200,40,105), i)
        draw_cog(screen, (500, 267), 40, 30, (40,200,105), -i)
        # "assembly line"
        color = (0,200,200)
        x, y = -60, 205
        l = 660
        draw_line(screen, color, (x+60-i%60, y), (x+l, y), 20)
#        for j in xrange(60, l+60, 60):
#            draw_line(screen, color, (x-i%60+j, y+20), (x+j-i%60+18, y+20), 20)
        for j in xrange(31, l+31, 31):
            draw_line(screen, color, (x-line_counter+j, y+20), (x+j-line_counter+14, y+20), 20)
        # "paper"
        line_offset -= milli/100. * paper_speed
        line_offset %= 20
        screen.blit(lines, (120, line_offset+40))
        
        
        y1 = 340 - math.sin(math.radians(i)) * 25 #* aa
        x1 = 500 - math.cos(math.radians(i)) * 25 #* aa
        y2 = 340
        c = 200    
        a = y1 - y2
        b = math.sqrt(c*c -  a*a)
        x2 = x1 - b

        counter += milli*paper_speed
        if counter > 100:
            for n in xrange(counter / 100):                    
                points.insert(0, x2-100)
            counter %= 100
        if len(points) >= 280:
            points = points[:280]
        if len(points) > 2:
            points_ = zip(points, range(340, 340-len(points), -1))
            pygame.draw.lines(screen, (255,255,255), 0, points_, 20)
            pygame.draw.aalines(screen, (0,0,0), 0, points_)
        pygame.draw.line(screen, (0,0,0), (110, 60), (290, 60), 7)
#            for x,y in points_[int(i%10)::10]:
#                print "x,y", x, y
#                pygame.draw.aaline(screen, (0,0,0), (120,y), (x-10, y))
#                pygame.draw.aaline(screen, (0,0,0), (x+10, y), (280, y))
        
        p1, p2, p3 = (x1, y1), (x2, y2), (x2-100, y2,)
        draw_line(screen, (200,0,0), p1, p2, 10)
        draw_line(screen, (200,0,0), p2, p3, 10)
    
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
