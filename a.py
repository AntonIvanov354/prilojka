from tkinter import *
import tkinter as tk  # Стандартный модуль tkinter
import customtkinter as CTk  # Библиотека customtkinter
from tkinter import filedialog # чет не на сложном хахахахах
import shutil
import os
import speech_recognition as sr
from pydub import AudioSegment
from datetime import datetime
from functools import partial
import random

okno = CTk.CTk()

okno_fremevork4_nomer_xz5 = None
okno_fremevork4_nomer_xz6 = None
a = 0

def q9():
    okno_fremevork1_center = CTk.CTkFrame(okno,  width=1920, height=100, fg_color="Black")
    okno_fremevork1_center.grid(column=0, row=0)
    okno_fremevork1_center.grid_propagate(False)

    okno_fremevork_center_name = CTk.CTkLabel(okno_fremevork1_center, text="KnowMAP", text_color="white", bg_color="Black",
                                            font=('Arial', 40))

    okno_fremevork_center_name.grid(column=0,row=0, padx= 700, pady=30)

    okno_fremevork_left_knopa_menu = CTk.CTkButton(okno_fremevork1_center, text="Меню", fg_color="Black", text_color="white",
                                                    font=('Arial', 40), command=q)
    okno_fremevork_left_knopa_menu.grid(column = 0, row = 0,padx = 20, pady = 20, sticky = "w")

    emae_fremvork_3647468 = CTk.CTkFrame(okno, width=1920, height=1080, fg_color="#808080")
    emae_fremvork_3647468.grid(column = 0, row = 1)
    emae_fremvork_3647468.grid_propagate(False)


    okno_fremevork1_center1 = CTk.CTkLabel(emae_fremvork_3647468, text="Файл сюда ⬇️", fg_color= "#808080", text_color="Black",
                                           font= ("Arial", 30,"bold"))
    okno_fremevork1_center1.grid(column = 0, row = 0, stick = "w", padx = 700, pady = 50)

    okno_fremevork1_center_knopka = CTk.CTkButton(emae_fremvork_3647468, text="Открыть файл", fg_color="Black", #этооооооо другая чать код, не залезай сюды
                                                  text_color="#808080", font=("Arial", 25,"bold"), command=open_file) #этооооооо другая чать код, не залезай сюды
    okno_fremevork1_center_knopka.grid(column = 0, row = 2, stick="w", padx = 700)#этооооооо другая чать код, не залезай сюды

    okno.configure(fg_color="#808080")
    okno.geometry("1920x1080")  
    okno.mainloop()

def open_file():
    file = filedialog.askopenfilename(title = "Выбор файла")
    if file:
        emae_frem_file = CTk.CTkFrame(okno, width=1920, height=1080, fg_color="#808080")
        emae_frem_file.grid(column = 0, row = 1)
        emae_frem_file.grid_propagate(False)

        emae_frem_file_1435465465 = CTk.CTkFrame(emae_frem_file, width= 500, height= 150, fg_color="black")
        emae_frem_file_1435465465.grid(column = 0, row = 1, stick="w", padx  = 600, pady = 15)
        emae_frem_file_1435465465.grid_propagate(False)

        text0 =[
                "Путь к вашему фуйлу:",
                file,
        ]
        for i, text0 in enumerate(text0): 
            emae_frem_file_txt = CTk.CTkLabel(emae_frem_file_1435465465, text = text0,
                                            fg_color = "black", text_color = "#808080", font=("Arial", 15,"bold"))
            emae_frem_file_txt.grid(column = 0, row = i, stick = "w", padx = 10, pady=  15)
                    # Указываем директорию для сохранения файла
        save_directory = "D:\\"

        # Получаем имя файла
        file_name = os.path.basename(file)
            # Полный путь к новому файлу
        destination = os.path.join(save_directory, file_name)
            
            # Копируем файл в указанную директорию
        shutil.copy(file, destination)
        print(f"Файл скопирован в: {destination}")
        save_directory2 =  destination

            # Укажите путь к вашей папке с файлами
        path = "C:\\"
        file_base_name = destination

            # Конвертируем файлы с 1 до N (укажите нужное количество файлов для конвертации)
        input_file = os.path.join(path, f"{file_base_name}")
        output_file = os.path.join(path, f"{file_base_name}.wav")  # Сохраним как .wav
        output_file1 = file_base_name.replace(".mp3", "")
        output_file2 = (f"{output_file1}.wav")
                # Проверяем, существует ли файл
        if os.path.exists(input_file):
                    # Загрузка звукового файла в формате MP3
            audio_mp3 = AudioSegment.from_file(input_file, format="mp3", ffmpeg="D:\\Anton\\ffmpeg")
                    
                    # Конвертация в формат WAV
            audio_mp3.export(output_file2, format="wav")
            print(f"Конвертация {input_file} в {output_file2} завершена.")
        else:
            print(f"Файл {input_file} не найден.")

        def convert_large_audio_to_text(file_name):
            recognizer = sr.Recognizer()
            full_text = ""

                # Загружаем аудиофайл с помощью pydub
            audio = AudioSegment.from_file(file_name, format="wav")

                # Деля на части чуть меньше чем 1 минута (например, по 50 секунд)
            segment_length_ms = 50 * 1000  # 50 секунд
            segments = [audio[i:i + segment_length_ms] for i in range(0, len(audio), segment_length_ms)]

                # Распознаём текст из каждого сегмента
            for i, segment in enumerate(segments):
                    # Сохраняем сегмент во временный файл
                segment.export("temp.wav", format="wav")

                with sr.AudioFile("temp.wav") as source:
                    audio_data = recognizer.record(source)
                    try:
                            # Распознаем текст в сегменте
                        text = recognizer.recognize_google(audio_data, language='ru-RU')
                        full_text += text + " "  # Добавляем текст сегмента к полному тексту
                        print(f"Сегмент {i+1}/{len(segments)} распознан.")
                    except sr.UnknownValueError:
                        print(f"Сегмент {i+1} не удалось распознать.")
                    except sr.RequestError as e:
                        print(f"Ошибка запроса к сервису: {e}")
            return full_text
            
        a = file_name.replace(".mp3", "")
        b = a+".wav"
        destination1 = destination.replace(".mp3", "")
        audio_file_path = os.path.join(f"{destination1}.wav")  # Укажите путь к вашему аудиофайлу
        print(f"Обработка файла: {audio_file_path}")

                # Преобразуем аудиофайл в текст
        text00 = convert_large_audio_to_text(audio_file_path)

                # Выводим результат
        print("Распознанный текст:")
        print(text00)
            

                    # Сохраняем текст в файл
        bara = b.replace(".wav", "")
        with open(bara, "w", encoding='utf-8') as itog:
            itog.write(text00)

        def w1():
            okno_framvaemae_itog = CTk.CTkFrame(okno, width=1920, height=1080, fg_color="#808080")
            okno_framvaemae_itog.grid(column=0, row=1, sticky="nsew")  # Используйте "nsew" для растягивания фрейма
            okno_framvaemae_itog.grid_propagate(False)

            # Создание текстового поля
            # Создание текстового поля
            okno_fram_Textbox = CTk.CTkTextbox(okno_framvaemae_itog, width=400, height=300, fg_color="#808080", wrap='word',
                                                font=("Arial", 25, "bold"))
            okno_fram_Textbox.grid(column=0, row=1, sticky="w", padx=400, pady=20)  # Используйте "nw" для верхнего левого выравнивания

            # Вставка текста 
            okno_fram_Textbox.insert(CTk.END, text00)

            okno_fram_pyti = CTk.CTkLabel(okno_framvaemae_itog, text = f"Путь к вашему файлу:{audio_file_path}", fg_color = "#808080",
                                            text_color = "Black", font = ("Arial", 25, "bold"))
            okno_fram_pyti.grid(column = 0, row = 2, stick = "w", padx = 400, pady = 20)

            okono_fram10_exit_aaaaaa = CTk.CTkButton(okno_framvaemae_itog, text = "Выход", fg_color = "Black", text_color="#808080",
                                                        font=  ("Arial", 25, "bold"), command= q9)
            okono_fram10_exit_aaaaaa.grid(column = 0, row = 3, stick = "w", padx = 1000, pady = 20)

        emae_frem_file_exit = CTk.CTkButton(emae_frem_file, text = "Верно", fg_color="Black", text_color ="#808080",
                                            font = ("Arial",24, "bold"),command = w1)
        emae_frem_file_exit.grid(column = 0, row = 2, stick = "w", padx = 965)

        emae_frem_file_exit_1 = CTk.CTkButton(emae_frem_file, text="Назад", fg_color = "Black", text_color="#808080",
                                                font=("Arial", 24,"bold"), command= q9)
        emae_frem_file_exit_1.grid(column = 0, row = 3, stick = "w", padx = 965, pady = 20)
    else:
        emae_frem_file = CTk.CTkFrame(okno, width=1920, height=1080, fg_color="#808080")
        emae_frem_file.grid(column = 0, row = 1)
        emae_frem_file.grid_propagate(False)

        emae_frem_file_error = CTk.CTkFrame(emae_frem_file, width=300, height=45, fg_color = "black")
        emae_frem_file_error.grid(column = 0, row= 0, padx = 650, pady =50, stick =  "w")
        emae_frem_file_error.grid_propagate(False)

        emae_frem_file_txt = CTk.CTkLabel(emae_frem_file_error, text = "Файл не был открыт!",
                                        fg_color = "Black", text_color = "#808080", font=("Arial", 24,"bold"))
        emae_frem_file_txt.grid(column = 0, row = 0, stick = "w", padx = 20, pady=  10)
        emae_frem_file_exit = CTk.CTkButton(emae_frem_file, text= "Назад", fg_color="Black", text_color ="#808080",
                                            font = ("Aria",24, "bold"), command= q9)
        emae_frem_file_exit.grid(column = 0, row = 1, stick = "w", padx = 810)

def q5():#FAQ ёу
    okno_fremevork5_FAQ = CTk.CTkFrame(okno, width=1920, height=1080, fg_color="#808080")
    okno_fremevork5_FAQ.grid(column = 0, row=1, stick ="w", pady=1)
    okno_fremevork5_FAQ.grid_propagate(False)

    def q6(): #Часто задаваемые вопросы okno_fremevork5_FAQ_name_dop1
        okno_fremevork5_FAQ_name_dop2.destroy()
        okno_fremevork5_FAQ_name_dop3.destroy()
        okno_fremevork5_FAQ_name_dop1_okno1.destroy()
        okno_fremevork5_FAQ_name_dop1_okno3.destroy()

        okno_fremevork5_FAQ_name_dop1_okno = CTk.CTkFrame(okno_fremevork5_FAQ, width=600, height=200, fg_color="Black")
        okno_fremevork5_FAQ_name_dop1_okno.grid(column = 0, row=4, stick = "w", padx = 270, pady = 30)
        okno_fremevork5_FAQ_name_dop1_okno.grid_propagate(False)

        texts = [
            "Приложение значительно упрощает процесс конспектирования аудио",
            "позволяя пользователям экономить время и усилия.",
            "С помощью современных технологий оно автоматически",
            "преобразует аудиозаписи в текст, выделяет ключевые",
            "моменты и создает структурированные заметки.",
            "Это делает обучение и работу с информацией более эффективными,",
            "позволяя сосредоточиться на главном и избегать рутинных задач."
        ]

        for i, text in enumerate(texts):
            label = CTk.CTkLabel(okno_fremevork5_FAQ_name_dop1_okno, text=text, fg_color="Black", text_color="#808080", 
                                    font=('Arial', 15, "bold"))
            label.grid(column=0, row=i, stick="w", padx=5, pady=5)

        okno_fremevork5_FAQ_name_dop1_okno_vixod = CTk.CTkButton(okno_fremevork5_FAQ , text= "Назад", fg_color="Black",  
                                                                    text_color="#808080",
                                                                    width=25, height=25, font=("Arial", 30), command=q5)
        okno_fremevork5_FAQ_name_dop1_okno_vixod.grid(column = 0, row = 5, stick= "w", padx = 770,)
    def q7(): #Часто задаваемые вопросы okno_fremevork5_FAQ_name_dop2
        okno_fremevork5_FAQ_name_dop1.destroy()
        okno_fremevork5_FAQ_name_dop3.destroy()
        okno_fremevork5_FAQ_name_dop1_okno.destroy()
        okno_fremevork5_FAQ_name_dop1_okno3.destroy()

        okno_fremevork5_FAQ_name_dop1_okno2 = CTk.CTkFrame(okno_fremevork5_FAQ, width=600, height=280, fg_color="Black")
        okno_fremevork5_FAQ_name_dop1_okno2.grid(column = 0, row=5, stick = "w", padx = 270, pady =30)
        okno_fremevork5_FAQ_name_dop1_okno2.grid_propagate(False)

        textss = [
            "В настоящее время приложение поддерживает только формат аудио.",
            "В будущем планируется расширить функциональность, ",
            "чтобы оно могло работать и с другими расширениями файлов, ",
            "такими как видео и текстовые документы. Это позволит пользователям ",
            "обрабатывать разнообразные типы данных, улучшая их опыт",
            "и эффективность работы с информацией. Мы стремимся сделать ",
            "приложение более универсальным и удобным для всех пользователей."
        ]


        for i, text in enumerate(textss):
            label = CTk.CTkLabel(okno_fremevork5_FAQ_name_dop1_okno2, text=text, fg_color="Black", text_color="#808080", 
                                    font=('Arial', 15, "bold"))
            label.grid(column=0, row=i, stick="w", padx=5, pady=5)
        
        okno_fremevork5_FAQ_name_dop1_okno_vixod2 = CTk.CTkButton(okno_fremevork5_FAQ , text= "Назад", fg_color="Black",  
                                                                    text_color="#808080",
                                                                    width=25, height=25, font=("Arial", 30), command=q5)
        okno_fremevork5_FAQ_name_dop1_okno_vixod2.grid(column = 0, row = 6, stick= "w", padx = 770,)

    def q8(): #Часто задаваемые вопросы okno_fremevork5_FAQ_name_dop3
        okno_fremevork5_FAQ_name_dop1.destroy()
        okno_fremevork5_FAQ_name_dop2.destroy()
        okno_fremevork5_FAQ_name_dop1_okno.destroy()
        okno_fremevork5_FAQ_name_dop1_okno1.destroy()
        okno_fremevork5_FAQ_name_dop1_okno_text3.destroy()
        okno_fremevork5_FAQ_name_dop1_okno3.destroy()


        okno_fremevork5_FAQ_name_dop1_okno4 = CTk.CTkFrame(okno_fremevork5_FAQ, width=600, height=280, fg_color="Black")
        okno_fremevork5_FAQ_name_dop1_okno4.grid(column = 0, row=6, stick = "w", padx = 270, pady =30)
        okno_fremevork5_FAQ_name_dop1_okno4.grid_propagate(False)

        textss = [
            "Нет, специальное программное обеспечение не нужно скачивать,",
            " так как оно уже встроено в программу.",
            "Это позволяет пользователям сразу же начать работу без лишних шагов.  ",
            "Все необходимые функции доступны изначально, ",
            "что значительно упрощает процесс использования и",
            "повышает эффективность работы с программой",
            "Вам не нужно беспокоиться о дополнительных загрузках.",
        ]

        for i, text in enumerate(textss):
            label = CTk.CTkLabel(okno_fremevork5_FAQ_name_dop1_okno4, text=text, fg_color="Black", text_color="#808080", 
                                    font=('Arial', 15, "bold"))
            label.grid(column=0, row=i, stick="w", padx=5, pady=5)
        
        okno_fremevork5_FAQ_name_dop1_okno_vixod2 = CTk.CTkButton(okno_fremevork5_FAQ , text= "Назад", fg_color="Black",  
                                                                    text_color="#808080",
                                                                    width=25, height=25, font=("Arial", 30), command=q5)
        okno_fremevork5_FAQ_name_dop1_okno_vixod2.grid(column = 0, row = 7, stick= "w", padx = 770,)
    okno_fremevork5_FAQ_name = CTk.CTkLabel(okno_fremevork5_FAQ, text="FAQ", fg_color="#808080", text_color="Black",
                                              font=('Arial', 30, "bold"))
    okno_fremevork5_FAQ_name.grid(column = 0, row = 0, stick ="w", padx =200, pady = 20)

    text = [
        "KnowMAP  - Приложение позволяет пользователям загружать аудиофайлы и автоматически преобразовывать их в текст.",
        "После загрузки аудио, приложение использует технологии распознавания речи для транскрипции.",
        "Полученный текст можно сохранить в виде текстового файла для дальнейшего использования."
    ]
    for i, text in enumerate(text):
        label1 =CTk.CTkLabel(okno_fremevork5_FAQ_name, text = text, fg_color="#808080", text_color="Black", 
                                              font=('Arial', 20, "bold"))
        label1.grid(column = 1, row =i+1, stick ="w", padx =1, pady = 5)
    okno_fremevork5_FAQ_name_dop1 = CTk.CTkButton(okno_fremevork5_FAQ, text="+", fg_color="Black",  text_color="white",
                                                        width=40, height=40, font=("Arial", 30), command= q6)
    okno_fremevork5_FAQ_name_dop1.grid(column = 0, row = 4, stick = "w", padx = 200, pady = 30)
    

    okno_fremevork5_FAQ_name_dop2 = CTk.CTkButton(okno_fremevork5_FAQ, text="+", fg_color="Black",  text_color="white",
                                                        width=40, height=40, font=("Arial", 30), command= q7)
    okno_fremevork5_FAQ_name_dop2.grid(column = 0, row = 5, stick = "w", padx = 200, pady = 30)

    okno_fremevork5_FAQ_name_dop3 = CTk.CTkButton(okno_fremevork5_FAQ, text="+", fg_color="Black",  text_color="white",
                                                        width=40, height=40, font=("Arial", 30), command= q8)
    okno_fremevork5_FAQ_name_dop3.grid(column = 0, row = 6, stick = "w", padx = 200, pady = 30)

    okno_fremevork5_FAQ_name_dop1_okno = CTk.CTkFrame(okno_fremevork5_FAQ, width=600, height=40, fg_color="Black")
    okno_fremevork5_FAQ_name_dop1_okno.grid(column = 0, row=4, stick = "w", padx = 270, pady = 30)
    okno_fremevork5_FAQ_name_dop1_okno.grid_propagate(False)

    okno_fremevork5_FAQ_name_dop1_okno_text = CTk.CTkLabel(okno_fremevork5_FAQ_name_dop1_okno, text="Чем может помочь ваше приложение?",
                                                            fg_color="Black", text_color = "#808080", font=("Arial", 20, "bold"))
    okno_fremevork5_FAQ_name_dop1_okno_text.grid(column = 0, row = 0, stick = "w", padx = 10, pady=5)

    okno_fremevork5_FAQ_name_dop1_okno1 = CTk.CTkFrame(okno_fremevork5_FAQ, width=600, height=40, fg_color="Black")
    okno_fremevork5_FAQ_name_dop1_okno1.grid(column = 0, row=5, stick = "w", padx = 270, pady = 60)
    okno_fremevork5_FAQ_name_dop1_okno1.grid_propagate(False)

    okno_fremevork5_FAQ_name_dop1_okno_text1 = CTk.CTkLabel(okno_fremevork5_FAQ_name_dop1_okno1, text="Какие форматы файлов принимает приложение?",
                                                            fg_color="Black", text_color = "#808080", font=("Arial", 20, "bold"))
    okno_fremevork5_FAQ_name_dop1_okno_text1.grid(column = 0, row = 0, stick = "w", padx = 10, pady=5)

    okno_fremevork5_FAQ_name_dop1_okno3 = CTk.CTkFrame(okno_fremevork5_FAQ, width=830, height=40, fg_color="Black")
    okno_fremevork5_FAQ_name_dop1_okno3.grid(column = 0, row=6, stick = "w", padx = 270, pady = 30)
    okno_fremevork5_FAQ_name_dop1_okno3.grid_propagate(False)

    okno_fremevork5_FAQ_name_dop1_okno_text3 = CTk.CTkLabel(okno_fremevork5_FAQ_name_dop1_okno3, text="Требуется ли специальное программное обеспечение для работы приложения?",
                                                            fg_color="Black", text_color = "#808080", font=("Arial", 20, "bold"))
    okno_fremevork5_FAQ_name_dop1_okno_text3.grid(column = 0, row = 0, stick = "w", padx = 10, pady=5)

def q3():#ну тип регистрация ёу
    global a
    if a == 0:
        okno_fremevork4_akk = CTk.CTkFrame(okno, width=1920, height=1080, fg_color="#808080")
        okno_fremevork4_akk.grid(column = 0, row=1, stick ="w", pady=1)
        okno_fremevork4_akk.grid_propagate(False)

        okno_fremevork4_akk_fremvork5 = CTk.CTkFrame(okno_fremevork4_akk, width=400, height=350, fg_color="Black")
        okno_fremevork4_akk_fremvork5.grid(column = 0, row = 0, stick ="n", pady= 1, padx = 640)
        okno_fremevork4_akk_fremvork5.grid_propagate(False)

        okno_fremevork4_akk_vxod = CTk.CTkLabel(okno_fremevork4_akk_fremvork5, text="Вход", fg_color="Black", text_color="white",
                                                font=('Arial', 30))
        okno_fremevork4_akk_vxod.grid(column = 0, row = 1, padx = 90, pady = 20, stick = "w")

        okno_fremevork4_akk_nomer = CTk.CTkLabel(okno_fremevork4_akk_fremvork5, text = "Ник/имя:", fg_color="Black", text_color="white",
                                                font=('Arial', 20))
        okno_fremevork4_akk_nomer.grid(column=0, row=2, padx = 90, pady = 10, stick = "w")

        okno_fremevork4_nomer_xz = CTk.CTkEntry(okno_fremevork4_akk_fremvork5,  placeholder_text='Введите ник/имя', font=('Arial', 15))
        okno_fremevork4_nomer_xz.grid(column = 0, row = 3, padx = 90, stick = "w")


        okno_fremevork4_akk_parol = CTk.CTkLabel(okno_fremevork4_akk_fremvork5, text = "Пароль:", fg_color="Black",  text_color="white",
                                                font=('Arial', 20))
        okno_fremevork4_akk_parol.grid(column=0, row=5, padx = 90, pady = 10, stick = "w")

        okno_fremevork4_nomer_xz2 = CTk.CTkEntry(okno_fremevork4_akk_fremvork5,  placeholder_text='Введите пароль', font=('Arial', 15))
        okno_fremevork4_nomer_xz2.grid(column = 0, row = 6, padx = 90, stick = "w")

        def text1(): #ну тип надо создать базу данных для пароля и почты-телефона
            global okno_fremevork4_nomer_xz5
            okno_fremevork4_nomer_xz5 =okno_fremevork4_nomer_xz.get()
            print(okno_fremevork4_nomer_xz5)#вывод почты, тела

            global okno_fremevork4_nomer_xz6
            okno_fremevork4_nomer_xz6 = okno_fremevork4_nomer_xz2.get()
            print(okno_fremevork4_nomer_xz6)#вывод пароля
            if okno_fremevork4_nomer_xz5 == "":
                nyyyyy_tip_xz2 = CTk.CTkLabel(okno_fremevork4_akk_fremvork5, text="Введите ник/имя", fg_color = "Black", text_color="Red",
                                            font = ("Arial", 15, "bold"))
                nyyyyy_tip_xz2.grid(column = 0, row = 4, stick = "w", padx = 90)
            else:
                q9()
            if okno_fremevork4_nomer_xz6 == "":
                nyyyyy_tip_xz = CTk.CTkLabel(okno_fremevork4_akk_fremvork5, text="Введите пароль", fg_color = "Black", text_color="Red",
                                            font = ("Arial", 15, "bold"))
                nyyyyy_tip_xz.grid(column = 0, row = 7, stick = "w", padx = 90)
                
            else:
                q9()

        okno_fremevork4_vxod = CTk.CTkButton(okno_fremevork4_akk_fremvork5, text="Вход", fg_color="Black",  text_color="white",
                                                            font=("Arial", 20), command=text1)
        okno_fremevork4_vxod.grid(column = 0, row = 8, padx = 150, pady = 20 ,stick = "w")
        a += 1
    else:

        okno_yje_voshel = CTk.CTkFrame(okno, width= 1920, height= 1080, fg_color= "#808080")
        okno_yje_voshel.grid(column =0, row = 1)
        okno_yje_voshel.grid_propagate(False)

        okno_yje_voshel_name_privet= CTk.CTkLabel(okno_yje_voshel, text = f"Здравствуте, {okno_fremevork4_nomer_xz5}",  fg_color="#808080",
                                                   text_color="Black", font = ("Arial",30, "bold"))
        okno_yje_voshel_name_privet.grid(column = 0, row = 0, padx = 600, pady  = 10)

        okno_yje_voshel_name = CTk.CTkButton(okno_yje_voshel, text="Ваш ник/имя:",  fg_color="Black", text_color="#808080",
                                             font =("Arial", 25,"bold"),state="disabled")
        okno_yje_voshel_name.grid(column = 0, row = 1, stick = "w", pady = 30, padx = 700)

        okno_yje_voshel_name1 = CTk.CTkButton(okno_yje_voshel, text=okno_fremevork4_nomer_xz5, fg_color="Black", text_color="#808080",
                                             font =("Arial", 25,"bold"),state="disabled")
        okno_yje_voshel_name1.grid(column = 0, row = 2, stick = "w", pady = 10, padx = 750)

        okno_yje_voshel_parol = CTk.CTkButton(okno_yje_voshel, text="Ваш пароль:", fg_color="Black", text_color="#808080",
                                             font =("Arial", 25,"bold"), state="disabled")
        okno_yje_voshel_parol.grid(column = 0, row = 3, stick = "w", pady = 30, padx = 700)

        okno_yje_voshel_parol1 = CTk.CTkButton(okno_yje_voshel, text=okno_fremevork4_nomer_xz6, fg_color="Black", text_color="#808080",
                                             font =("Arial", 25,"bold"), state="disabled")
        okno_yje_voshel_parol1.grid(column = 0, row = 4, stick = "w", pady = 10, padx = 740)
        
        
def q(): #менюшка ёу
    okno_fremevork2_menu = CTk.CTkFrame(okno, width=200, height=1080, fg_color="Black")
    okno_fremevork2_menu.grid(column = 0, row=1, stick ="w")
    okno_fremevork2_menu.grid_propagate(False)

    okno_fremevork2_menu_knopka_akkaynt = CTk.CTkButton(okno_fremevork2_menu, text="Аккаунт", fg_color = "Black", text_color="white",
                                                        font=("Arial", 30), command=q3)
    okno_fremevork2_menu_knopka_akkaynt.grid(column = 0, row = 1, padx = 25, pady = 15, stick = "w")

    okno_fremevork2_menu_knopka_nastrouki = CTk.CTkButton(okno_fremevork2_menu, text="Инструкция",  fg_color = "Black",
                                                          text_color="white", font=("Arial", 27), command=q9)
    okno_fremevork2_menu_knopka_nastrouki.grid(column = 0, row = 2, padx = 25, pady = 10, stick = "w")

    okno_fremevork2_menu_knopka_glavnai = CTk.CTkButton(okno_fremevork2_menu, text="Главная",  fg_color = "Black",
                                                          text_color="white", font=("Arial", 30), command=q9)
    okno_fremevork2_menu_knopka_glavnai.grid(column = 0, row = 3, padx = 25, pady = 15, stick = "w")

    okno_fremevork2_menu_knopka_FAQ = CTk.CTkButton(okno_fremevork2_menu, text="FAQ",  fg_color = "Black",
                                                          text_color="white", font=("Arial", 30), command=q5)
    okno_fremevork2_menu_knopka_FAQ.grid(column = 0, row = 4, padx = 25, pady = 15, stick = "w")

def time():#хз чет шамали
        now = datetime.now()  
        current_time1 = now.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time1)
        return current_time1

def time2():#хз чет шамали, дошаманился
        now1 = datetime.now()  
        current_time2 = now1.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time2)
        return current_time2

q9()
