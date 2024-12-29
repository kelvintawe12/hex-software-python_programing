import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

class CustomVoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
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

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.speak("I am listening")
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I did not understand that. Could you repeat?")
            return None
        except sr.RequestError:
            self.speak("Sorry, my speech service is down.")
            return None
        except AttributeError:
            self.speak("PyAudio is not installed. Please install it to use the voice recognition feature.")
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
        webbrowser.open("https://www.linkedin.com/company/hex-softwares/")         # Opening hex softwares in the default browser
        self.speak("Opening hexo softwares in your default browser")

    def play_music(self):
        self.speak("Opening Spotify to play music")
        webbrowser.open("https://open.spotify.com/")
        def play_playlist(self, playlist_name):
            playlists = {
                "chill": "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6",
                "workout": "https://open.spotify.com/playlist/37i9dQZF1DX70RN3TfWWJh",
                "party": "https://open.spotify.com/playlist/37i9dQZF1DXaXB8fQg7xif"
            }
            if playlist_name in playlists:
                self.speak(f"Playing {playlist_name} playlist on Spotify")
                webbrowser.open(playlists[playlist_name])
            else:
                self.speak(f"Sorry, I couldn't find a playlist named {playlist_name}")

        def handle_command(self, command):
            if command:
                for key in self.commands:
                    if key in command:
                        self.commands[key]()
                        return
                if "play playlist" in command:
                    playlist_name = command.replace("play playlist", "").strip()
                    self.play_playlist(playlist_name)
                else:
                    self.speak("Sorry, I am not equipped to handle this command yet.")
    def tell_about_hex(self):
        hex_info = (
            "Hex Software is a Start-Up software development company dedicated to fostering talent and innovation in various domains. "
            "With a strong commitment to excellence, we offer internship opportunities that provide hands-on experience in cutting-edge technologies "
            "and a dynamic work environment."
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

    def handle_command(self, command):
        if command:
            for key in self.commands:
                if key in command:
                    self.commands[key]()
                    return
            self.speak("Sorry, I am not equipped to handle this command yet.")

    def run(self):
        self.speak("Hello! I am your custom voice assistant. How can I help you today?")
        while True:
            command = self.listen()
            if command == "quit":
                self.speak("Goodbye! Have a great day.")
                break
            self.handle_command(command)

if __name__ == "__main__":
    assistant = CustomVoiceAssistant()
    assistant.run()