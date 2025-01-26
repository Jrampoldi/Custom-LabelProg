from PIL import Image, ImageDraw


def create_label(file1_path, file2_path, file3_path, file4_path, file_number):
    LETTER_SIZE = (2550, 3300)
    WHITE = (255, 255, 255, 255)
    LABEL_HEIGHT = int((1.13/11)*LETTER_SIZE[1])
    LABEL_WIDTH = int((6/8.5)*LETTER_SIZE[0])
    TOP_MARGIN = int((0.78/11)*LETTER_SIZE[1])
    SIDE_MARGIN = int((1.25/8.5)*LETTER_SIZE[0])    
    SPACER = int(((LETTER_SIZE[1]-(TOP_MARGIN*2)) - (8*LABEL_HEIGHT))/7)
    printable_image = Image.new("RGBA", LETTER_SIZE, WHITE)

#   Check placement of labels
#    draw = ImageDraw.Draw(printable_image)
#    GRAY = (169,169,169)
#    for i in range(1, 9):
#        draw.rectangle([SIDE_MARGIN, TOP_MARGIN + ((i - 1) * LABEL_HEIGHT), SIDE_MARGIN + LABEL_WIDTH, TOP_MARGIN + (i * LABEL_HEIGHT)],fill=GRAY)
#        TOP_MARGIN += 17
    print(file1_path)
    print(file2_path)
    print(file3_path)
    print(file4_path)

    file1 = Image.open("labels/" + file1_path)
    file2 = Image.open("labels/" + file2_path)
    file3 = Image.open("labels/" + file3_path)
    file4 = Image.open("labels/" + file4_path)

    resized_img = [0, 0, 0, 0]
    resized_img[0] = file1.resize((LABEL_WIDTH, LABEL_HEIGHT))
    resized_img[1] = file2.resize((LABEL_WIDTH, LABEL_HEIGHT))
    resized_img[2] = file3.resize((LABEL_WIDTH, LABEL_HEIGHT))
    resized_img[3] = file4.resize((LABEL_WIDTH, LABEL_HEIGHT))

    for i in range(8):
        printable_image.paste(resized_img[int(i/2)], (SIDE_MARGIN, TOP_MARGIN + (i * LABEL_HEIGHT)), resized_img[int(i/2)])
        TOP_MARGIN += SPACER



    label_order_val = file_number
    file_name = f"{label_order_val}-{file1_path[2:len(file1_path)-4]}_{file2_path[2:len(file2_path)-4]}_{file3_path[2:len(file3_path)-4]}_{file4_path[2:len(file4_path)-4]}"

    printable_image.save("go_for_pdf/" + file_name + ".pdf")

def make_label(file1_path, file2_path, file3_path, file4_path, file5_path, file6_path, file7_path, file8_path, order_number):
    LETTER_SIZE = (2550, 3300)
    WHITE = (255, 255, 255, 255)
    LABEL_HEIGHT = int((1.13/11)*LETTER_SIZE[1])
    LABEL_WIDTH = int((6/8.5)*LETTER_SIZE[0])
    TOP_MARGIN = int((0.78/11)*LETTER_SIZE[1])
    SIDE_MARGIN = int((1.25/8.5)*LETTER_SIZE[0])    
    SPACER = int(((LETTER_SIZE[1]-(TOP_MARGIN*2)) - (8*LABEL_HEIGHT))/7)
    printable_image = Image.new("RGBA", LETTER_SIZE, WHITE)

    file_1 = Image.open("labels/" + file1_path)
    file_2 = Image.open("labels/" + file2_path)
    file_3 = Image.open("labels/" + file3_path)
    file_4 = Image.open("labels/" + file4_path)
    file_5 = Image.open("labels/" + file5_path)
    file_6 = Image.open("labels/" + file6_path)
    file_7 = Image.open("labels/" + file7_path)
    file_8 = Image.open("labels/" + file8_path)

    resized_img = []
    resized_img.append(file_1.resize((LABEL_WIDTH, LABEL_HEIGHT)))
    resized_img.append(file_2.resize((LABEL_WIDTH, LABEL_HEIGHT)))
    resized_img.append(file_3.resize((LABEL_WIDTH, LABEL_HEIGHT)))
    resized_img.append(file_4.resize((LABEL_WIDTH, LABEL_HEIGHT)))
    resized_img.append(file_5.resize((LABEL_WIDTH, LABEL_HEIGHT)))
    resized_img.append(file_6.resize((LABEL_WIDTH, LABEL_HEIGHT)))
    resized_img.append(file_7.resize((LABEL_WIDTH, LABEL_HEIGHT)))
    resized_img.append(file_8.resize((LABEL_WIDTH, LABEL_HEIGHT)))

    for i in range(8):
        printable_image.paste(resized_img[i], (SIDE_MARGIN, TOP_MARGIN + (i * LABEL_HEIGHT)), resized_img[i])
        TOP_MARGIN += SPACER

    file_name = f"go_for_pdf/{order_number}_{file1_path[2:len(file1_path)-4]}_{file3_path[2:len(file3_path)-4]}_{file5_path[2:len(file5_path)-4]}_{file7_path[2:len(file7_path)-4]}"
    printable_image.convert("RGB").save(file_name + ".pdf", resolution=300)
