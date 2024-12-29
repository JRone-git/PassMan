import re
from typing import Tuple

class PasswordStrengthChecker:
    def __init__(self):
        self.min_length = 8
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def check_strength(self, password: str) -> Tuple[int, str, str]:
        """
        Check password strength and return a score (0-100), strength level, and feedback.
        """
        score = 0
        feedback = []
        
        # Length check (up to 30 points)
        length_score = min(len(password) * 3, 30)
        score += length_score
        if len(password) < self.min_length:
            feedback.append(f"Password should be at least {self.min_length} characters")
        
        # Complexity checks (up to 70 points)
        if re.search(r"\d", password):
            score += 15
        else:
            feedback.append("Add numbers")
            
        if re.search(r"[a-z]", password):
            score += 15
        else:
            feedback.append("Add lowercase letters")
            
        if re.search(r"[A-Z]", password):
            score += 15
        else:
            feedback.append("Add uppercase letters")
            
        if any(c in self.special_chars for c in password):
            score += 15
        else:
            feedback.append("Add special characters")
            
        # Variety bonus (up to 10 points)
        unique_chars = len(set(password))
        variety_score = min(unique_chars, 10)
        score += variety_score
        
        # Determine strength level
        if score >= 90:
            strength = "Very Strong"
            color = "#00FF00"  # Green
        elif score >= 70:
            strength = "Strong"
            color = "#90EE90"  # Light Green
        elif score >= 50:
            strength = "Moderate"
            color = "#FFD700"  # Gold
        elif score >= 30:
            strength = "Weak"
            color = "#FFA500"  # Orange
        else:
            strength = "Very Weak"
            color = "#FF0000"  # Red
        
        # Create feedback string
        feedback_str = ", ".join(feedback) if feedback else "Password is good!"
        
        return score, strength, color, feedback_str

    def get_strength_bar(self, score: int, width: int = 20) -> str:
        """
        Create a text-based strength bar.
        """
        filled = int((score / 100) * width)
        bar = "█" * filled + "░" * (width - filled)
        return bar
