from cryptography.fernet import Fernet
import json
import os
import time
import secrets
import string
from typing import Optional, Dict
from dataclasses import dataclass
from password_strength import PasswordStrengthChecker

@dataclass
class PasswordEntry:
    username: str
    password: str
    url: str = ""
    category: str = "General"
    created_date: float = time.time()
    last_modified: float = time.time()

class PasswordManager:
    def __init__(self):
        self.key_file = "key.key"
        self.password_file = "passwords.json"
        self.fernet = None
        self.password_dict: Dict[str, PasswordEntry] = {}
        self.last_activity = time.time()
        self.strength_checker = PasswordStrengthChecker()
        
    def initialize(self, master_password: str) -> bool:
        if not self._validate_master_password(master_password):
            return False
            
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
        
        self.fernet = Fernet(key)
        self._load_passwords()
        return True
    
    def _validate_master_password(self, password: str) -> bool:
        score, _, _, _ = self.strength_checker.check_strength(password)
        return score >= 50
    
    def _load_passwords(self):
        if os.path.exists(self.password_file):
            try:
                with open(self.password_file, "r") as f:
                    encrypted_data = json.load(f)
                    for service, entry in encrypted_data.items():
                        decrypted_pass = self.fernet.decrypt(entry["password"].encode()).decode()
                        self.password_dict[service] = PasswordEntry(
                            username=entry["username"],
                            password=decrypted_pass,
                            url=entry.get("url", ""),
                            category=entry.get("category", "General"),
                            created_date=entry.get("created_date", time.time()),
                            last_modified=entry.get("last_modified", time.time())
                        )
            except Exception as e:
                print(f"Error loading passwords: {str(e)}")
    
    def _save_passwords(self):
        encrypted_data = {}
        for service, entry in self.password_dict.items():
            encrypted_data[service] = {
                "username": entry.username,
                "password": self.fernet.encrypt(entry.password.encode()).decode(),
                "url": entry.url,
                "category": entry.category,
                "created_date": entry.created_date,
                "last_modified": entry.last_modified
            }
        with open(self.password_file, "w") as f:
            json.dump(encrypted_data, f, indent=4)
    
    def add_password(self, service: str, username: str, password: str, url: str = "", category: str = "General") -> bool:
        try:
            self.password_dict[service] = PasswordEntry(
                username=username,
                password=password,
                url=url,
                category=category
            )
            self._save_passwords()
            return True
        except Exception as e:
            print(f"Error adding password: {str(e)}")
            return False
    
    def get_password_entry(self, service: str) -> Optional[PasswordEntry]:
        return self.password_dict.get(service)
    
    def delete_password(self, service: str) -> bool:
        try:
            if service in self.password_dict:
                del self.password_dict[service]
                self._save_passwords()
                return True
            return False
        except Exception as e:
            print(f"Error deleting password: {str(e)}")
            return False
    
    def generate_password(self, length: int = 16) -> str:
        try:
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            while True:
                password = ''.join(secrets.choice(chars) for _ in range(length))
                score, _, _, _ = self.strength_checker.check_strength(password)
                if score >= 80:  # Only return strong passwords
                    return password
        except Exception as e:
            print(f"Error generating password: {str(e)}")
            return ""
    
    def get_categories(self) -> list:
        return sorted(list(set(entry.category for entry in self.password_dict.values())))
    
    def search_passwords(self, query: str) -> Dict[str, PasswordEntry]:
        query = query.lower()
        return {
            service: entry
            for service, entry in self.password_dict.items()
            if query in service.lower() or
               query in entry.username.lower() or
               query in entry.url.lower() or
               query in entry.category.lower()
        }
