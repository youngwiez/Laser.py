#mengimpor library yang diperlukan
from tkinter import *
from tkinter import simpledialog, messagebox
from playsound import playsound
import datetime as dt
import time

#class sebagai 'template' yang bisa digunakan untuk membuat object baru
class AlarmApp:
    #function untuk mendesain GUI dari alarm
    #parameter self untuk merepresentasikan tiap object yang dibuat
    def __init__(self, root):
        self.root = root
        self.root.title("Antares.py")
        self.root.geometry("464x230")
        self.root.config(bg="#36486B")
        self.root.resizable(width=False, height=False)
        #mendefinisikan tipe data jam, menit, & detik alarm
        self.hour = StringVar()
        self.minute = StringVar()
        self.second = StringVar()
        #mengatur nama judul
        self.judul = Label(
            self.root,
            text="Alarm Pintar Berbasis Python",
            fg="white",
            bg="#36486B",
            font=("Arial", 15)
        ).place(
            x=100,
            y=1
        )
        #mengatur label waktu alarm
        self.add_time = Label(
            self.root,
            text="Hour     Minute   Second",
            font=60,
            fg="white",
            bg="#36486B"
        ).place(
            x=220,
            y=40
        )
        #mengatur label perintah set time for alarm
        self.set_alarm = Label(
            self.root,
            text="Set Time for Alarm: ",
            fg="white",
            bg="#36486B",
            font=("Helvetica", 13, "bold")
        ).place(
            x=5,
            y=83
        )
        #mengatur kotak input jam alarm
        self.hour_time = Entry(
            self.root,
            textvariable=self.hour,
            bg="#FEFBD8",
            width=4,
            font=(20)
        ).place(
            x=220,
            y=83
        )
        #mengatur kotak input menit alarm
        self.minute_time = Entry(
            self.root,
            textvariable=self.minute,
            bg="#FEFBD8",
            width=4,
            font=(20)
        ).place(
            x=297,
            y=83
        )
        #mengatur kotak input detik alarm
        self.second_time = Entry(
            self.root,
            textvariable=self.second,
            bg="#FEFBD8",
            width=4,
            font=(20)
        ).place(
            x=377,
            y=83
        )
        #mengatur tombol submit pengaturan alarm
        self.submit = Button(
            self.root,
            text="Set The Alarm",
            fg="white",
            bg="#05a630",
            width=15,
            command=self.get_alarm_time,
            font=(20)
        ).place(
            x=140,
            y=135
        )
        #mengatur label pesan format alarm
        self.time_format = Label(
            self.root,
            text="Remember to set time in 24-hour format!",
            fg="white",
            bg="#36486B",
            font=("Arial", 15)
        ).place(
            x=50,
            y=190
        )

    #function untuk mengatur kapan alarm berdering
    def alarm(self, set_alarm_timer):
        while True:
            time.sleep(1)
            current_time = dt.datetime.now().strftime("%H:%M:%S")
            #apabila jam saat ini = jam alarm yang diset
            if current_time == set_alarm_timer:
                #putar nada dering alarm.mp3
                playsound("alarm.mp3")
                #munculkan pilihan apakah alarm ingin di-snooze atau tidak
                snooze_response = messagebox.askyesno("Snooze", "Do you want to snooze the alarm?")
                #apabila opsi snooze dipilih, jalankan function snooze_alarm
                if snooze_response:
                    self.snooze_alarm()
                #apabila opsi no dipilih, tutup aplikasi alarm
                else:
                    self.root.destroy()
                    break

    #function untuk mengatur jam alarm terpasang
    def get_alarm_time(self):
        alarm_set_time = f"{self.hour.get()}:{self.minute.get()}:{self.second.get()}"
        self.alarm(alarm_set_time)

    #function untuk mengatur alarm apabila di-snooze
    def snooze_alarm(self):
        snooze_time = 60  # durasi snooze dalam detik (1 menit)
        snooze_alarm_time = dt.datetime.now() + dt.timedelta(seconds=snooze_time)
        snooze_alarm_time_str = snooze_alarm_time.strftime("%H:%M:%S")
        self.alarm(snooze_alarm_time_str)

# membuat instance dari tkinter
root = Tk()
app = AlarmApp(root)

# menjalankan aplikasi tkinter
root.mainloop()