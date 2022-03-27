from PIL import Image, ImageDraw
import numpy as np

 
#generateFrame(frameNumber, field, nextNumber)
#frame will be saved as frame_'frameNumber'.png 
#field is all fields of the game
#next number is the next number of the turn to be printed out
def generateFrame(frameNumber, field, nextNumber):
        img = Image.new('RGB', (500, 600), color = (187, 173, 160))
        color_empty = (204, 192, 179)
        color_2 = (238, 228, 218)
        color_4 = (237, 224, 200)
        color_8 = (242, 177, 121)
        color_16 = (245, 149, 99)
        color_32 = (246, 124, 95)
        color_64 = (246, 94, 59)
        color_128 = (237, 207, 114)
        color_256 = (237, 204, 97)
        color_512 = (237, 200, 80)
        color_1024 = (237, 197, 63)
        color_2048 = (237, 194, 46)
        font_light = (249, 246, 242)
        font_dark = (119, 110, 101)


        d = ImageDraw.Draw(img)
        d.text((200, 585), 'Next Number is: ' + str(nextNumber))
        for col in range (0,6):
                for height in range (0,7):
                        if height == 0: #header
                                fontColor = font_dark
                                row = height
                                d.rounded_rectangle((83 * (col),  83 * (row), 83 * (col+1), 83 * (row+1)), fill=font_light, outline=font_dark, width=3, radius=7)
                                #d.text((83 * (col), 83 * (row)), str(col) + ' ' + str(row), fill=(255,255,0)) #adds row / col for debugging
                                d.text((83 * (col) + 83/4, 83 * (row)+  83/4), "column:", fill=fontColor)
                                d.text((83 * (col) + 83/2, 83 * (row)+  83/2), str(col), fill=fontColor)
                        else:
                                row = height - 1
                                if field[row][col] == 0:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_empty, outline=(187, 173, 160), width=3, radius=7)
                                        #d.text((83 * (col), 83 * (height)), str(col) + ' ' + str(height), fill=(255,255,0)) #adds row / col for debugging
                                        continue
                                if field[row][col] == 2:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_2, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 4:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_4, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 8:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_8, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 16:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_16, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 32:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_32, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 64:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_64, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 128:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_128, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 256:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_256, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 512:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_512, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 1024:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_1024, outline=(187, 173, 160), width=3, radius=7)
                                if field[row][col] == 2048:
                                        d.rounded_rectangle((83 * (col),  83 * (height), 83 * (col+1), 83 * (height+1)), fill=color_2048, outline=(187, 173, 160), width=3, radius=7)

                                # d.rounded_rectangle((83 * (col),  83 * (row), 83 * (col+1), 83 * (row+1)), fill=(0, 192, 192), outline="yellow",
                                #    width=1, radius=7)
                                if field[row][col] < 8:
                                        fontColor = font_dark
                                else:
                                        fontColor = font_light
                        
                                #d.text((83 * (col), 83 * (height)), str(col) + ' ' + str(height), fill=(255,255,0)) #adds row / col for debugging
                                d.text((83 * (col) + 83/2, 83 * (height)+  83/2), str(int(field[row][col])), fill=fontColor)

        
        img.save('pngs'frame_' + str(frameNumber) + '.png')

#test code
# field = np.zeros((6,6))
# field[0][0] = 0
# field[0][1] = 2
# field[0][2] = 4
# field[0][3] = 8
# field[0][4] = 16
# field[0][5] = 32
# field[1][0] = 64
# field[1][1] = 128
# field[1][2] = 256
# field[1][3] = 512
# field[1][4] = 1024
# field[1][5] = 2048

# generateFrame(1,field,1)

