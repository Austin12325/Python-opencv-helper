import pyMeow as pm
import pyperclip
from time import sleep


### Hold tab and selet pixel with left mouse to print the pixel x,y and sum of color 
### Hold tab and start box select with both left and right mouse held down , draw box to get its boundry in a format for CV 
pm.overlay_init()
# start[1],end[1],start[0],end[0] this is how we need to copy it for CV
start_pos = []
end_pos = []
tab = 0x09         
while pm.overlay_loop():    
    
    pm.begin_drawing()
    mousex = pm.pixel_at_mouse()['x']
    mousey = pm.pixel_at_mouse()['y']
    color = pm.pixel_at_mouse()['color']
    sumcolor = color['r']+color['g']+color['b']
    
            

    if pm.key_pressed(tab):
            mousex = pm.pixel_at_mouse()['x']
            mousey = pm.pixel_at_mouse()['y']
            try:
                pm.draw_rectangle_lines(int(start_pos[0]),int(start_pos[1]),int(mousex)-int(start_pos[0]),int(mousey)-int(start_pos[1]),color=(pm.get_color('red')),lineThick=2)
            except:
                pm.draw_circle_lines(centerX=int(mousex),centerY=int(mousey)+2,radius=5,color=(pm.get_color('red')))

            if len(start_pos) == 0:
                
                if pm.mouse_pressed('left') and pm.mouse_pressed("right"):
                    start_pos.append(mousex)
                    start_pos.append(mousey)   

            if len(start_pos) >= 1 and len(end_pos) == 0:
                pm.end_drawing()
                    
                if pm.mouse_pressed('left'):
                    pass
                else:
                    end_pos.append(mousex)                                                                  
                    end_pos.append(mousey)
                    
                    print(f'Boundry: frame[{round(start_pos[1]*0.666666)}:{round(end_pos[1]*0.666666)},{round(start_pos[0]*0.666666)}:{round(end_pos[0]*0.666666)}]')
                    pyperclip.copy(f'frame[{round(start_pos[1]*0.666666)}:{round(end_pos[1]*0.666666)},{round(start_pos[0]*0.666666)}:{round(end_pos[0]*0.666666)}]')
                    start_pos.clear()
                    end_pos.clear()

                    # break

            if pm.mouse_pressed("left") and not pm.mouse_pressed("right"):                                                                                                      
                # print(color['r']+color['g']+color['b'])
                loc = f'[{round(mousey*0.666666)},{round(mousex*0.666666)}] {sumcolor}'
                print(f'Pixel Color: {loc}')
                pyperclip.copy(loc)
                sleep(0.2)

    pm.end_drawing()                                        

