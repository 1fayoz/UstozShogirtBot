from aiogram import Bot, Dispatcher, types, Router
import asyncio
from aiogram.filters import Command
from aiogram.types import Message
import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
import re
import sqlite3
# from db import creat_user
# from db import users


bot = Bot(token="7075122607:AAGTY_N_9ZSteiw1A5HZwJfKisqvweeucaw")
dp = Dispatcher()
form_router = Router()
logging.basicConfig(level=logging.INFO)

def reyly_button():
    buttons = [
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def reyly2_button():
    buttons = [
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def ask_button():
    buttons = [
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)



def start_buttons():
    buttons = [
       [ KeyboardButton(text="sherik kerak"), KeyboardButton(text="ish joyi kerak")],
       [KeyboardButton(text="hodim kerak"), KeyboardButton(text="ustoz kerak")],
       [KeyboardButton(text="Shogirt kerak")],
       [KeyboardButton(text="   USERS   ")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

  
class RegisterForm(StatesGroup): #ish joy kerak
    ism = State()
    yosh = State()
    texnalogy = State()
    nomer = State()
    hudud = State()
    narx = State()
    kasbi = State()
    vaqt = State()
    maqsad = State()


check_phone = r"\+998[0-9]{9}"


  
class RegisterForm2(StatesGroup): # ustoz kerak
    ism = State()
    yosh = State()
    texnalogy = State()
    nomer = State()
    hudud = State()
    narx = State()
    kasbi = State()
    vaqt = State()
    maqsad = State()


check_phone2 = r"\+998[0-9]{9}"

  
class RegisterForm3(StatesGroup):  # shogirt kerak
    ism = State()
    yosh = State()
    texnalogy = State()
    nomer = State()
    hudud = State()
    narx = State()
    kasbi = State()
    vaqt = State()
    maqsad = State()


check_phone3 = r"\+998[0-9]{9}"

class RegisterForm4(StatesGroup):  # sherik kerak
    ism = State()
    texnalogy = State()
    nomer = State()
    hudud = State()
    narx = State()
    kasbi = State()
    vaqt = State()
    maqsad = State()



class RegisterForm5(StatesGroup):  # xodim kerak
    idora = State()
    texnalogy = State()
    nomer = State()
    hudud = State()
    masul = State()
    vaqt = State()
    ish_vaqti = State()
    moash = State()
    qoshimcha = State()



@form_router.message(Command("start"))
async def start_button(message: Message):
    # print(message.chat.id)  5593831038
    await message.answer(text=f"Assalomu alaykum: {message.from_user.full_name}", reply_markup=start_buttons())











@form_router.message(F.text == "ish joyi kerak")
async def ish_joy_kerak(message: Message, state:FSMContext ):
    text = """
    Ish joyi topish uchun ariza berish

    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
    Ustoz-Shogird Kanaliga ariza olish Boti
    Ism, familiyangizni kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm.ism)
@form_router.message(RegisterForm.ism)
async def set_ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 
    Yoshingizni kiriting?
    Masalan, 19"""
    await message.answer(text=text)
    await state.set_state(RegisterForm.yosh)

@form_router.message(RegisterForm.yosh)
async def set_yosh(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer(text="xato")
    await state.update_data(yosh=message.text)
    text = """📚 Texnologiya:
    Talab qilinadigan texnologiyalarni kiriting?
    Texnologiya nomlarini vergul bilan ajrating. Masalan, 
    Java, C++, C#"""
    await message.answer(text=text)
    await state.set_state(RegisterForm.texnalogy)

@form_router.message(RegisterForm.texnalogy)
async def set_texnology(message: Message, state: FSMContext):
    await state.update_data(texnalogy=message.text)
    text = """📞 Aloqa: 
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await message.answer(text=text)
    await state.set_state(RegisterForm.nomer)

@form_router.message(RegisterForm.nomer)
async def set_nomer(message: Message, state: FSMContext):
    if not re.match(check_phone, message.text):
        return await message.answer(text="notigri nomer")
    await state.update_data(nomer=message.text)
    text = """🌐 Hudud: 
    Qaysi hududdansiz?
    Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await message.answer(text=text)
    await state.set_state(RegisterForm.hudud)

@form_router.message(RegisterForm.hudud)
async def set_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text = """💰 Narxi:
    Tolov qilasizmi yoki Tekinmi?
    Kerak bo`lsa, Summani kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm.narx)

@form_router.message(RegisterForm.narx)
async def set_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text = """👨🏻‍💻 Kasbi: 
    Ishlaysizmi yoki o`qiysizmi?
    Masalan, Talaba"""
    await message.answer(text=text)
    await state.set_state(RegisterForm.kasbi)

@form_router.message(RegisterForm.kasbi)
async def set_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    text = """🕰 Murojaat qilish vaqti: 
    Qaysi vaqtda murojaat qilish mumkin?
    Masalan, 9:00 - 18:00"""
    await message.answer(text=text)
    await state.set_state(RegisterForm.vaqt)

@form_router.message(RegisterForm.vaqt)
async def set_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text = """🔎 Maqsad: 
    Maqsadingizni qisqacha yozib bering."""
    await message.answer(text=text)
    await state.set_state(RegisterForm.maqsad)

@form_router.message(RegisterForm.maqsad, F.text == "Ha")
async def yes_button(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"""Ish joyi kerak:
    👨‍💼 Xodim: {message.from_user.full_name}
    🕑 Yosh: {data['yosh']}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await bot.send_message(chat_id=5593831038, text=text)
    # creat_user(data['ism'], data['yosh'])

    await state.clear()

@form_router.message(RegisterForm.maqsad, F.text == "Yo'q")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("malumot yuborilmadi")
    await state.clear()  

@form_router.message(RegisterForm.maqsad)
async def set_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    # print(data)
    text = f"""Ish joyi kerak:
    👨‍💼 Xodim: {message.from_user.full_name}
    🕑 Yosh: {data['yosh']}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await message.answer(text=text, reply_markup=reyly_button())
    await message.answer(text="Hamma malulotlar to'grimi")

# @form_router.message(F.text == USERS)
# async def user(message: Message, state: FSMContext)
    # data 


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



@form_router.message(F.text == "ustoz kerak")
async def ustoz_kerak(message: Message, state:FSMContext ):
    text = """
    Ustoz-Shogird Kanaliga ariza olish Boti


    Ustoz topish uchun ariza berish
    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.

    Ism, familiyangizni kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.ism)
@form_router.message(RegisterForm2.ism)
async def set_ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 
    Yoshingizni kiriting?
    Masalan, 19"""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.yosh)

@form_router.message(RegisterForm2.yosh)
async def set_yosh(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer(text="xato")
    await state.update_data(yosh=message.text)
    text = """📚 Texnologiya:
    Talab qilinadigan texnologiyalarni kiriting?
    Texnologiya nomlarini vergul bilan ajrating. Masalan, 
    Java, C++, C#"""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.texnalogy)

@form_router.message(RegisterForm2.texnalogy)
async def set_texnology(message: Message, state: FSMContext):
    await state.update_data(texnalogy=message.text)
    text = """📞 Aloqa: 
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.nomer)

@form_router.message(RegisterForm2.nomer)
async def set_nomer(message: Message, state: FSMContext):
    if not re.match(check_phone2, message.text):
        return await message.answer(text="notigri nomer")
    await state.update_data(nomer=message.text)
    text = """🌐 Hudud: 
    Qaysi hududdansiz?
    Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.hudud)

@form_router.message(RegisterForm2.hudud)
async def set_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text = """💰 Narxi:
    Tolov qilasizmi yoki Tekinmi?
    Kerak bo`lsa, Summani kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.narx)

@form_router.message(RegisterForm2.narx)
async def set_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text = """👨🏻‍💻 Kasbi: 
    Ishlaysizmi yoki o`qiysizmi?
    Masalan, Talaba"""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.kasbi)

@form_router.message(RegisterForm2.kasbi)
async def set_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    text = """🕰 Murojaat qilish vaqti: 
    Qaysi vaqtda murojaat qilish mumkin?
    Masalan, 9:00 - 18:00"""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.vaqt)

@form_router.message(RegisterForm2.vaqt)
async def set_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text = """🔎 Maqsad: 
    Maqsadingizni qisqacha yozib bering."""
    await message.answer(text=text)
    await state.set_state(RegisterForm2.maqsad)

@form_router.message(RegisterForm2.maqsad, F.text == "Ha")
async def yes_button(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"""Ish joyi kerak:
    👨‍💼 Xodim: {message.from_user.full_name}
    🕑 Yosh: {data['yosh']}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await bot.send_message(chat_id=5593831038, text=text)
    await state.clear()

@form_router.message(RegisterForm2.maqsad, F.text == "Yo'q")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("malumot yuborilmadi")
    await state.clear()  

@form_router.message(RegisterForm2.maqsad)
async def set_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    # print(data)
    text = f"""ustoz kerak:

    👨‍💼 shogirt: {message.from_user.full_name}
    🕑 Yosh: {data['yosh']}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await message.answer(text=text, reply_markup=ask_button())
    await message.answer(text="Hamma malulotlar to'grimi")



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




@form_router.message(F.text == "Shogirt kerak")
async def ish_joy_kerak(message: Message, state:FSMContext ):
    text = """
    Ustoz-Shogird Kanaliga ariza olish Boti


    Shogird topish uchun ariza berish
    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.

    Ism, familiyangizni kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.ism)
@form_router.message(RegisterForm3.ism)
async def set_ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """🕑 Yosh: 
    Yoshingizni kiriting?
    Masalan, 19"""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.yosh)

@form_router.message(RegisterForm3.yosh)
async def set_yosh(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer(text="xato")
    await state.update_data(yosh=message.text)
    text = """📚 Texnologiya:
    Talab qilinadigan texnologiyalarni kiriting?
    Texnologiya nomlarini vergul bilan ajrating. Masalan, 
    Java, C++, C#"""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.texnalogy)

@form_router.message(RegisterForm3.texnalogy)
async def set_texnology(message: Message, state: FSMContext):
    await state.update_data(texnalogy=message.text)
    text = """📞 Aloqa: 
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.nomer)

@form_router.message(RegisterForm3.nomer)
async def set_nomer(message: Message, state: FSMContext):
    if not re.match(check_phone3, message.text):
        return await message.answer(text="notigri nomer")
    await state.update_data(nomer=message.text)
    text = """🌐 Hudud: 
    Qaysi hududdansiz?
    Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.hudud)

@form_router.message(RegisterForm3.hudud)
async def set_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text = """💰 Narxi:
    Tolov qilasizmi yoki Tekinmi?
    Kerak bo`lsa, Summani kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.narx)

@form_router.message(RegisterForm3.narx)
async def set_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text = """👨🏻‍💻 Kasbi: 
    Ishlaysizmi yoki o`qiysizmi?
    Masalan, Talaba"""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.kasbi)

@form_router.message(RegisterForm3.kasbi)
async def set_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    text = """🕰 Murojaat qilish vaqti: 
    Qaysi vaqtda murojaat qilish mumkin?
    Masalan, 9:00 - 18:00"""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.vaqt)

@form_router.message(RegisterForm3.vaqt)
async def set_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text = """🔎 Maqsad: 
    Maqsadingizni qisqacha yozib bering."""
    await message.answer(text=text)
    await state.set_state(RegisterForm3.maqsad)

@form_router.message(RegisterForm3.maqsad, F.text == "Ha")
async def yes_button(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"""Ish joyi kerak:
    👨‍💼 Xodim: {message.from_user.full_name}
    🕑 Yosh: {data['yosh']}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await bot.send_message(chat_id=5593831038, text=text)
    await state.clear()

@form_router.message(RegisterForm3.maqsad, F.text == "Yo'q")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("malumot yuborilmadi")
    await state.clear()  

@form_router.message(RegisterForm3.maqsad)
async def set_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    # print(data)
    text = f"""shogirt kerak:
    
    👨‍💼 Xodim: {message.from_user.full_name}
    🕑 Yosh: {data['yosh']}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await message.answer(text=text, reply_markup=reyly2_button())
    await message.answer(text="Hamma malulotlar to'grimi")






#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@







@form_router.message(F.text == "sherik kerak")
async def sherik_kerak(message: Message, state:FSMContext ):
    text = """
    Ustoz-Shogird Kanaliga ariza olish Boti

    Sherik topish uchun ariza berish
    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
    Ustoz-Shogird Kanaliga ariza olish Boti

    Ism, familiyangizni kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.ism)
@form_router.message(RegisterForm4.ism)
async def set_ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    text = """📚 Texnologiya:
    Talab qilinadigan texnologiyalarni kiriting?
    Texnologiya nomlarini vergul bilan ajrating. Masalan, 
    Java, C++, C#"""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.texnalogy)


@form_router.message(RegisterForm4.texnalogy)
async def set_texnology(message: Message, state: FSMContext):
    await state.update_data(texnalogy=message.text)
    text = """📞 Aloqa: 
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.nomer)

@form_router.message(RegisterForm4.nomer)
async def set_nomer(message: Message, state: FSMContext):
    if not re.match(check_phone2, message.text):
        return await message.answer(text="notigri nomer")
    await state.update_data(nomer=message.text)
    text = """🌐 Hudud: 
    Qaysi hududdansiz?
    Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.hudud)

@form_router.message(RegisterForm4.hudud)
async def set_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text = """💰 Narxi:
    Tolov qilasizmi yoki Tekinmi?
    Kerak bo`lsa, Summani kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.narx)

@form_router.message(RegisterForm4.narx)
async def set_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    text = """👨🏻‍💻 Kasbi: 
    Ishlaysizmi yoki o`qiysizmi?
    Masalan, Talaba"""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.kasbi)

@form_router.message(RegisterForm4.kasbi)
async def set_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    text = """🕰 Murojaat qilish vaqti: 
    Qaysi vaqtda murojaat qilish mumkin?
    Masalan, 9:00 - 18:00"""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.vaqt)

@form_router.message(RegisterForm4.vaqt)
async def set_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text = """🔎 Maqsad: 
    Maqsadingizni qisqacha yozib bering."""
    await message.answer(text=text)
    await state.set_state(RegisterForm4.maqsad)

@form_router.message(RegisterForm4.maqsad, F.text == "Ha")
async def yes_button(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"""Ish joyi kerak:
    👨‍💼 Xodim: {message.from_user.full_name}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await bot.send_message(chat_id=5593831038, text=text)
    await state.clear()

@form_router.message(RegisterForm4.maqsad, F.text == "Yo'q")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("malumot yuborilmadi")
    await state.clear()  

@form_router.message(RegisterForm4.maqsad)
async def set_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    # print(data)
    text = f"""ustoz kerak:

    👨‍💼 sherik: {message.from_user.full_name}
    📚 Texnologiya: {data['texnalogy']} 
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    💰 Narxi: {data['narx']}
    👨🏻‍💻 Kasbi: {data['kasbi']}
    🕰 Murojaat qilish vaqti: {data['vaqt']}
    🔎 Maqsad: {data['maqsad']}
"""
    await message.answer(text=text, reply_markup=ask_button())
    await message.answer(text="Hamma malulotlar to'grimi")





#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@form_router.message(F.text == "hodim kerak")
async def xodim_kerak(message: Message, state:FSMContext ):
    text = """
    Ustoz-Shogird Kanaliga ariza olish Boti

    Xodim topish uchun ariza berish
    Hozir sizga birnecha savollar beriladi. 
    Har biriga javob bering. 
    Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
    Ustoz-Shogird Kanaliga ariza olish Boti

    🎓 Idora nomi?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm5.idora)
@form_router.message(RegisterForm5.idora)
async def set_ism(message: Message, state: FSMContext):
    await state.update_data(idora=message.text)
    text = """📚 Texnologiya:
    Talab qilinadigan texnologiyalarni kiriting?
    Texnologiya nomlarini vergul bilan ajrating. Masalan, 
    Java, C++, C#"""
    await message.answer(text=text)
    await state.set_state(RegisterForm5.texnalogy)


@form_router.message(RegisterForm5.texnalogy)
async def set_texnology(message: Message, state: FSMContext):
    await state.update_data(texnalogy=message.text)
    text = """📞 Aloqa: 
Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await message.answer(text=text)
    await state.set_state(RegisterForm5.nomer)

@form_router.message(RegisterForm5.nomer)
async def set_nomer(message: Message, state: FSMContext):
    if not re.match(check_phone2, message.text):
        return await message.answer(text="notigri nomer")
    await state.update_data(nomer=message.text)
    text = """🌐 Hudud: 
    Qaysi hududdansiz?
    Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await message.answer(text=text)
    await state.set_state(RegisterForm5.hudud)

@form_router.message(RegisterForm5.hudud)
async def set_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    text = """
    ✍️Mas'ul ism sharifi?
    """
    await message.answer(text=text)
    await state.set_state(RegisterForm5.masul)

@form_router.message(RegisterForm5.masul)
async def set_narx(message: Message, state: FSMContext):
    await state.update_data(masul=message.text)
    text = """🕰 Murojaat qilish vaqti: 
    Qaysi vaqtda murojaat qilish mumkin?
    Masalan, 9:00 - 18:00"""
    await message.answer(text=text)
    await state.set_state(RegisterForm5.vaqt)

@form_router.message(RegisterForm5.vaqt)
async def set_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    text = """🕰 Ish vaqtini kiriting?"""
    await message.answer(text=text)
    await state.set_state(RegisterForm5.ish_vaqti)

@form_router.message(RegisterForm5.ish_vaqti)
async def set_ish_vaqt(message: Message, state: FSMContext):
    await state.update_data(ish_vaqti=message.text)
    await message.answer(text="""💰 Maoshni kiriting?""")
    await state.set_state(RegisterForm5.moash)

@form_router.message(RegisterForm5.moash)
async def set_moash(message: Message, state: FSMContext):
    await state.update_data(moash= message.text)
    await message.answer(text="‼️ Qo`shimcha ma`lumotlar?")
    await state.set_state(RegisterForm5.qoshimcha)



@form_router.message(RegisterForm5.qoshimcha, F.text == "Ha")
async def yes_button(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"""
    🏢 Idora: {data['idora']}
    📚 Texnologiya: {data['texnalogy']}
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    ✍️ Mas'ul: {data['masul']}
    🕰 Murojaat vaqti: {data['vaqt']} 
    🕰 Ish vaqti: {data['ish_vaqti']}
    💰 Maosh: {data['moash']}
    ‼️ Qo`shimcha: {data['qoshimcha']}
"""
    await bot.send_message(chat_id=5593831038, text=text)
    await state.clear()

@form_router.message(RegisterForm5.qoshimcha, F.text == "Yo'q")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("malumot yuborilmadi")
    await state.clear()  

@form_router.message(RegisterForm5.qoshimcha)
async def set_maqsad(message: Message, state: FSMContext):
    await state.update_data(qoshimcha=message.text)
    data = await state.get_data()
    # print(data)
    text = f"""
    🏢 Idora: {data['idora']}
    📚 Texnologiya: {data['texnalogy']}
    🇺🇿 Telegram: {message.from_user.username}
    📞 Aloqa: {data['nomer']}
    🌐 Hudud: {data['hudud']}
    ✍️ Mas'ul: {data['masul']}
    🕰 Murojaat vaqti: {data['vaqt']} 
    🕰 Ish vaqti: {data['ish_vaqti']}
    💰 Maosh: {data['moash']}
    ‼️ Qo`shimcha: {data['qoshimcha']}

#ishJoyi
"""
    await message.answer(text=text, reply_markup=ask_button())
    await message.answer(text="Hamma malulotlar to'grimi")



async def main():
    print("WORKING")
    dp.include_router(form_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())





























    