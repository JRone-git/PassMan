import json
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class SecurityQuestions:
    def __init__(self):
        self.questions_file = 'security_answers.bin'
        self.salt_file = 'security_salt.bin'
        
    def _generate_key(self, answers: list) -> bytes:
        """Generate encryption key from security answers"""
        # Combine all answers into one string
        combined = ''.join(answers).encode()
        
        # Load or create salt
        if os.path.exists(self.salt_file):
            with open(self.salt_file, 'rb') as f:
                salt = f.read()
        else:
            salt = os.urandom(16)
            with open(self.salt_file, 'wb') as f:
                f.write(salt)
        
        # Generate key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(combined))
        return key
        
    def save_answers(self, answers: list) -> bool:
        """Save encrypted security question answers"""
        try:
            # Generate key from answers
            key = self._generate_key(answers)
            fernet = Fernet(key)
            
            # Encrypt the answers themselves
            encrypted_data = fernet.encrypt(json.dumps(answers).encode())
            
            # Save encrypted answers
            with open(self.questions_file, 'wb') as f:
                f.write(encrypted_data)
                
            return True
        except Exception:
            return False
            
    def verify_answers(self, answers: list) -> bool:
        """Verify if provided answers match stored answers"""
        try:
            if not os.path.exists(self.questions_file):
                return False
                
            # Generate key from provided answers
            key = self._generate_key(answers)
            fernet = Fernet(key)
            
            # Read encrypted answers
            with open(self.questions_file, 'rb') as f:
                encrypted_data = f.read()
            
            # Try to decrypt - if successful, answers are correct
            decrypted = fernet.decrypt(encrypted_data)
            stored_answers = json.loads(decrypted.decode())
            
            return stored_answers == answers
        except Exception:
            return False
            
    def is_setup_needed(self) -> bool:
        """Check if security questions need to be set up"""
        return not os.path.exists(self.questions_file)
