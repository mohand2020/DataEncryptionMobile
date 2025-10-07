from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
import json, hashlib, os
from cryptography.fernet import Fernet

def load_users():
    with open("users.json", "r", encoding="utf-8") as f:
        raw = json.load(f)["users"]
        for user in raw:
            user["encryption_key"] = user["encryption_key"].encode()
        return raw

def verify_password(input_password, stored_hash):
    return hashlib.sha256(input_password.encode()).hexdigest() == stored_hash

def find_user(username, users):
    for user in users:
        if user["username"] == username:
            return user
    return None

def encrypt_file(file_path, key):
    try:
        print(f"🔐 Encrypting with key: {key}")
        with open(file_path, "rb") as f:
            data = f.read()
        cipher = Fernet(key)
        encrypted = cipher.encrypt(data)
        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted)
        return f"✅ File encrypted:\n{file_path}.enc"
    except Exception as e:
        return f"❌ Encryption failed:\n{str(e)}"

def decrypt_file(file_path, key):
    print(f"🔑 Using encryption key: {key}")
    try:
        with open(file_path, "rb") as f:
            encrypted = f.read()
        cipher = Fernet(key)
        decrypted = cipher.decrypt(encrypted)
        output_path = file_path.replace(".enc", ".dec")
        with open(output_path, "wb") as f:
            f.write(decrypted)
        return f"✅ File decrypted:\n{output_path}"
    except Exception as e:
        return f"❌ Decryption failed:\n{str(e)}"

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.users = load_users()

        self.add_widget(Label(text="Username"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        login_btn = Button(text="Login")
        login_btn.bind(on_press=self.attempt_login)
        self.add_widget(login_btn)

    def attempt_login(self, instance):
        username = self.username.text
        password = self.password.text
        print(f"Entered username: {username}")
        print(f"Entered password: {password}")
        user = find_user(username, self.users)
        print(f"Matched user: {user}")
        if not user or not verify_password(password, user["password_hash"]):
            print("Password verification failed.")
            Popup(title="Error", content=Label(text="Invalid login credentials."), size_hint=(0.6, 0.4)).open()
        else:
            print("Login successful.")
            self.clear_widgets()
            self.add_widget(Label(text=f"Welcome {user['username']}"))
            self.add_widget(
                Button(text="🔐 Encrypt File", on_press=lambda x: self.choose_file(user["encryption_key"], "encrypt")))
            self.add_widget(
                Button(text="🔓 Decrypt File", on_press=lambda x: self.choose_file(user["encryption_key"], "decrypt")))

    def choose_file(self, key, mode):
        layout = BoxLayout(orientation='vertical')
        start_path = os.path.join(os.path.expanduser("~"), "Desktop")
        chooser = FileChooserIconView(path=start_path)
        layout.add_widget(chooser)
        btn = Button(text="Select")
        layout.add_widget(btn)
        popup = Popup(title="Select File", content=layout, size_hint=(0.9, 0.9))

        def on_select(instance):
            if chooser.selection:
                file_path = chooser.selection[0]
                popup.dismiss()
                if mode == "encrypt":
                    result = encrypt_file(file_path, key)
                else:
                    result = decrypt_file(file_path, key)
                Popup(title="Result", content=Label(text=result), size_hint=(0.7, 0.4)).open()

        btn.bind(on_press=on_select)
        popup.open()

class EncryptionApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    EncryptionApp().run()
