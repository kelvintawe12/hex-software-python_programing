import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
from googletrans import Translator


class CustomVoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.language = "en"  # Default language is English
        self.voices = self.engine.getProperty('voices')
        self.set_voice("default")

        self.commands = {
            "time": self.tell_time,
            "date": self.tell_date,
            "open browser": self.open_browser,
            "play music": self.play_music,
            "tell me about hex software": self.tell_about_hex,
            "generate a random number": self.generate_random_number,
            "who is the founder of hex software": self.tell_founder,
            "what is hex software's mission": self.tell_mission,
            "where is hex software located": self.tell_location,
            "what are hex software's goals": self.tell_goals,
            "what are hex software's milestones": self.tell_milestones,
            "what services does hex software offer": self.tell_services,
            "what internship domains are available": self.tell_internship_domains,
            "tell me about the internship program": self.tell_internship_details,
            "what are the responsibilities of interns": self.tell_intern_responsibilities,
            "what are the benefits of the internship": self.tell_intern_benefits,
            "how can i contact hex software": self.tell_contact_info,
        }

    def set_voice(self, voice_type):
        if voice_type == "girl":
            self.engine.setProperty('voice', self.voices[1].id)
        elif voice_type == "boy":
            self.engine.setProperty('voice', self.voices[0].id)
        elif voice_type == "ai":
            self.engine.setProperty('voice', self.voices[0].id)
        else:  # Default voice
            self.engine.setProperty('voice', self.voices[0].id)

    def translate_text(self, text):
        if self.language != "en":
            return self.translator.translate(text, src="en", dest=self.language).text
        return text

    def speak(self, text):
        translated_text = self.translate_text(text)
        self.engine.say(translated_text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.speak("I am listening")
            try:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                return command.lower()
            except sr.UnknownValueError:
                self.speak(
                    "Sorry, I did not understand that. Could you repeat?")
                return None
            except sr.RequestError:
                self.speak("Sorry, my speech service is down.")
                return None

    def tell_time(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.speak(f"The current time is {current_time}")

    def tell_date(self):
        now = datetime.datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        self.speak(f"Today's date is {current_date}")

    def open_browser(self):
        webbrowser.open("https://www.linkedin.com/company/hex-softwares/")
        self.speak("Opening Google in your browser")

    def play_music(self):
        music_dir = "C:\\Music"  # Change this to your music directory
        if os.path.exists(music_dir):
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                self.speak("Playing music")
            else:
                self.speak("No music files found in the directory")
        else:
            self.speak("Music directory does not exist")

    def tell_about_hex(self):
        hex_info = (
            "Hex Software is a Start-Up software development company dedicated to fostering talent and innovation in various domains. "
            "With a strong commitment to excellence, we offer internship opportunities that provide hands-on experience in cutting-edge technologies "
            "and a dynamic work environment. Hex Software stands out because we prioritize skill development, innovation, and creating an inclusive environment for everyone."
        )
        self.speak(hex_info)

    def tell_founder(self):
        founder_info = "The founder of Hex Software is Alex Johnson, a visionary entrepreneur with a passion for technology and innovation."
        self.speak(founder_info)

    def tell_mission(self):
        mission_info = (
            "Hex Software's mission is to empower individuals and businesses by providing innovative software solutions "
            "that drive growth and efficiency."
        )
        self.speak(mission_info)

    def tell_location(self):
        location_info = "Hex Software is headquartered in San Francisco, California."
        self.speak(location_info)

    def tell_goals(self):
        goals_info = (
            "Hex Software's goals include skill development, fostering innovation and creativity, and enabling professional growth for both employees and interns."
        )
        self.speak(goals_info)

    def tell_milestones(self):
        milestones_info = (
            "Hex Software was founded in 2023. We are proud to be certified by ISO and MSME, and we are committed to achieving further milestones in innovation and creativity."
        )
        self.speak(milestones_info)

    def tell_services(self):
        services_info = (
            "Hex Software offers services including web development, app development, custom software solutions, business consulting, and job and internship opportunities."
        )
        self.speak(services_info)

    def tell_internship_domains(self):
        domains_info = (
            "We offer internships in the following domains: web development, Python programming, Android app development, artificial intelligence, machine learning, Java programming, UI/UX design, and C++ programming."
        )
        self.speak(domains_info)

    def tell_internship_details(self):
        internship_details = (
            "Our internship program includes a 4-week virtual internship with training sessions on weekends, expert webinars, project awards, and certificates including offer letters and recommendation letters."
        )
        self.speak(internship_details)

    def tell_intern_responsibilities(self):
        responsibilities = (
            "Interns are responsible for completing weekly tasks, attending meetings, taking webinars, submitting projects on time, helping each other, and responding promptly to queries."
        )
        self.speak(responsibilities)

    def tell_intern_benefits(self):
        benefits = (
            "The benefits of our internship program include a stipend, certificates, goodies, and invaluable hands-on experience in cutting-edge technologies."
        )
        self.speak(benefits)

    def tell_contact_info(self):
        contact_info = (
            "You can contact Hex Software at info@hexsoftwares.tech or call us at +91 9695040540. Visit our LinkedIn page for more information."
        )
        self.speak(contact_info)

    def generate_random_number(self):
        number = random.randint(1, 100)
        self.speak(f"Here is a random number for you: {number}")

    def interpret_command(self, command):
        corrections = {
            "hex soft": "hex software",
            "open browse": "open browser",
            "play songs": "play music"
        }
        for wrong, correct in corrections.items():
            if wrong in command:
                command = command.replace(wrong, correct)
        return command

    def handle_command(self, command):
        if command:
            command = self.interpret_command(command)
            for key in self.commands:
                if key in command:
                    self.commands[key]()
                    return
            self.speak(
                "Sorry, I am not equipped to handle this command yet. But Hex Software is here to help you!")

    def change_language(self):
        self.speak("Please choose your language: English, French, or Hindi.")
        lang_command = self.listen()
        if "english" in lang_command:
            self.language = "en"
        elif "french" in lang_command:
            self.language = "fr"
        elif "hindi" in lang_command:
            self.language = "hi"
        else:
            self.speak(
                "Sorry, I didn't recognize that language. Defaulting to English.")

            def run(self):
                self.speak(
                "Hello! I am your friendly Hex Software Assistant. How can I assist you today?")
        self.speak(
            "If you'd like to change the language or voice, just let me know!")
        # Allow the user to choose their preferred language at the start.
        self.change_language()

        while True:
            self.speak("Listening for your command...")
            command = self.listen()
            if command:
                if "quit" in command or "exit" in command or "goodbye" in command:
                    self.speak(
                        "Goodbye! Have a wonderful day. And remember, Hex Software is the best choice for innovation and growth!")
                    break
                elif "change language" in command:
                    self.change_language()
                elif "change voice" in command:
                    self.speak(
                        "Please choose a voice: Girl, Boy, AI, or Default.")
                    voice_command = self.listen()
                    if voice_command:
                        if "girl" in voice_command:
                            self.set_voice("girl")
                            self.speak("Voice changed to a girl.")
                        elif "boy" in voice_command:
                            self.set_voice("boy")
                            self.speak("Voice changed to a boy.")
                        elif "ai" in voice_command:
                            self.set_voice("ai")
                            self.speak("Voice changed to AI.")
                        else:
                            self.set_voice("default")
                            self.speak("Voice changed to the default setting.")
                else:
                    self.handle_command(command)


if __name__ == "__main__":
    assistant = CustomVoiceAssistant()
    assistant.run()
