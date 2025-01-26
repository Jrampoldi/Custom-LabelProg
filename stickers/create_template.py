from PIL import Image, ImageDraw, ImageFont

def make_template(name, color, symbol, ord_num):
    truck_in_name = name.lower().find("truck")
    inc_in_name = name.lower().find(" inc ")
    inc_in_name2 = name.lower().find("inc.")
    construction_in_name = name.lower().find("construction")
    transport_in_name = name.lower().find("transport")
    animals_in_name = name.lower().find("animals")
    express_in_name = name.lower().find("express")

    show_label = False

    if (truck_in_name == -1 and inc_in_name == -1 and express_in_name == -1 and animals_in_name == -1 and inc_in_name2 == -1 and construction_in_name == -1 and transport_in_name == -1 and symbol != "Racecar" and symbol != "NewTruck"):
        show_label=True

    CANVAS_START = (15, 19)
    CANVAS_END = (940, 184)
    if not show_label:
        CANVAS_END = (940, 230)
    template = Image.open(f'blanks/{symbol}-{color}.png')

    WIDTH, HEIGHT = template.size


    CANVAS_WIDTH, CANVAS_HEIGHT = (CANVAS_END[0]-CANVAS_START[0], CANVAS_END[1]-CANVAS_START[1])
    TRUCKLABEL_POS = (305, 185)
    TRUCKLABEL_SIZE = 50

    canvas = ImageDraw.Draw(template)
    font_path = "fonts/daddy-day.ttf"
    text_size = 10
    DADDYDAY = ImageFont.truetype(font_path, text_size)

    while True:
        t_width, t_height = canvas.textsize(name, font=DADDYDAY)
        if t_width >= CANVAS_WIDTH or t_height >= CANVAS_HEIGHT:
            break
        text_size += 1
        DADDYDAY = ImageFont.truetype(font_path, text_size)
    
    text_size -= 1
    DADDYDAY = ImageFont.truetype(font_path, text_size)

    t_width, t_height = canvas.textsize(name, font=DADDYDAY)
    text_x = CANVAS_START[0] + ((CANVAS_WIDTH - t_width) // 2)
    text_y = CANVAS_START[1] + ((CANVAS_HEIGHT - t_height) // 2)

    canvas.text((text_x, text_y), name, font=DADDYDAY, fill=color)

    DADDYDAY = ImageFont.truetype(font_path, TRUCKLABEL_SIZE)

    if show_label:
        canvas.text((TRUCKLABEL_POS[0], TRUCKLABEL_POS[1]), "Trucking Company", font=DADDYDAY, fill=color)
    template.save(f"labels/{ord_num:02}-{name}.png")

def make_flame_template(name, order):
    CANVAS_START_1 = (300, 20)
    CANVAS_END_1 = (1240,228)
    CANVAS_START_2 = (15, 20)
    CANVAS_END_2 = (950, 230)

    CANVAS_WIDTH_1, CANVAS_HEIGHT_1 = (CANVAS_END_1[0]-CANVAS_START_1[0], CANVAS_END_1[1] - CANVAS_START_1[1])
    CANVAS_WIDTH_2, CANVAS_HEIGHT_2 = (CANVAS_END_2[0]-CANVAS_START_2[0], CANVAS_END_2[1]-CANVAS_START_2[1])

    template_1 = Image.open("blanks/flame_driver_side.png")
    template_2 = Image.open("blanks/flame_passenger_side.png")

    canvas_1 = ImageDraw.Draw(template_1)
    canvas_2 = ImageDraw.Draw(template_2)

    font_path = "fonts/daddy-day.ttf"
    text_size = 10
    DADDYDAY = ImageFont.truetype(font_path, text_size)

    while True:
        t_width, t_height = canvas_1.textsize(name, font=DADDYDAY)
        if t_width >= CANVAS_WIDTH_1 or t_height >= CANVAS_HEIGHT_1:
            break
        text_size += 1
        DADDYDAY = ImageFont.truetype(font_path, text_size)

    text_size -= 1
    DADDYDAY = ImageFont.truetype(font_path, text_size)
    t_width, t_height = canvas_1.textsize(name, font=DADDYDAY)
    text_x = CANVAS_START_1[0] + ((CANVAS_WIDTH_1 - t_width) // 2)
    text_y = CANVAS_START_1[1] + ((CANVAS_HEIGHT_1 - t_height) // 2)

    canvas_1.text((text_x, text_y), name, font=DADDYDAY, fill="Red")

    text_size = 10
    DADDYDAY = ImageFont.truetype(font_path, text_size)

    while True:
        t_width, t_height = canvas_2.textsize(name, font=DADDYDAY)
        if t_width >= CANVAS_WIDTH_2 or t_height >= CANVAS_HEIGHT_2:
            break
        text_size += 1
        DADDYDAY = ImageFont.truetype(font_path, text_size)

    text_size -= 1
    DADDYDAY = ImageFont.truetype(font_path, text_size)

    t_width, t_height = canvas_2.textsize(name, font=DADDYDAY)
    text_x = CANVAS_START_2[0] + ((CANVAS_WIDTH_2 - t_width) // 2)
    text_y = CANVAS_START_2[1] + ((CANVAS_HEIGHT_2 - t_height) // 2)

    canvas_2.text((text_x, text_y), name, font=DADDYDAY, fill="Red")

    template_1.save(f"labels/{order:02}-f-{name}-1.png")
    template_2.save(f"labels/{order:02}-f-{name}-2.png")


#create_template("Caleb Trucking Inc.", "Red", "Trucker")
