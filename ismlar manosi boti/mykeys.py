#button yaratish 2-usul
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

names = [
    "Ozodbek",
    "Asliddin",
    "Qobil",
    "Asilbek",
    "Sardor",
    "Boburjon",
    "Otabek",
    "Shuhrat",
    "Gulhayo",
    "Sunnat",
    "Maqsud",
    "Nurbek",
    "Behruz",
    "Abror",
    "FAYOZBEK",
    "JO'RABEK",
    "SOLIJON",
    "MAHLIYO",
    "OMON"
]

# eng_uz_colors = {
#     "red": "qizil",
#     "blue": "ko'k",
#     "green": "yashil",
#     "yellow": "sariq",
#     "orange": "orol",
#     "purple": "binafsha",
#     "pink": "pushti",
#     "brown": "jigarrang",
#     "gray": "kulrang",
#     "black": "qora",
#     "white": "oq"
    # Add more colors as needed
# }

def auto_keyboard():
    builder2 = ReplyKeyboardBuilder()

    for value  in names:

        builder2.add(KeyboardButton(text=value))

    builder2.adjust(2)

    return builder2
