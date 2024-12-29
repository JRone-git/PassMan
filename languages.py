class Language:
    def __init__(self, is_finnish=False):
        self.is_finnish = is_finnish
        self.translations = {
            # Language selection
            "select_language": "Select Language:" if not is_finnish else "Valitse kieli:",
            "english": "English" if not is_finnish else "Englanti",
            "finnish": "Finnish" if not is_finnish else "Suomi",
            
            # Window titles
            "title_login": "Password Manager - Login" if not is_finnish else "Salasanojen Hallinta - Kirjautuminen",
            "title_main": "Password Manager" if not is_finnish else "Salasanojen Hallinta",
            "title_reset": "Reset Master Password" if not is_finnish else "Palauta Pääsalasana",
            "title_setup": "First Time Setup" if not is_finnish else "Ensimmäinen Asennus",
            
            # Login window
            "master_password": "Master Password:" if not is_finnish else "Pääsalasana:",
            "login": "Login" if not is_finnish else "Kirjaudu",
            "forgot_password": "Forgot Password?" if not is_finnish else "Unohditko salasanan?",
            "reset_password": "Reset Password" if not is_finnish else "Palauta Salasana",
            
            # Security questions
            "setup_questions": "Set up security questions:" if not is_finnish else "Määritä turvallisuuskysymykset:",
            "answer_questions": "Answer security questions:" if not is_finnish else "Vastaa turvallisuuskysymyksiin:",
            "question1": "What was your first pet's name?" if not is_finnish else "Mikä oli ensimmäisen lemmikkisi nimi?",
            "question2": "In which city were you born?" if not is_finnish else "Missä kaupungissa synnyit?",
            "question3": "What was your childhood nickname?" if not is_finnish else "Mikä oli lapsuuden lempinimesi?",
            "new_password": "New Master Password:" if not is_finnish else "Uusi pääsalasana:",
            "confirm_password": "Confirm Password:" if not is_finnish else "Vahvista salasana:",
            "save_answers": "Save Answers" if not is_finnish else "Tallenna vastaukset",
            "submit_answers": "Submit Answers" if not is_finnish else "Lähetä vastaukset",
            "passwords_dont_match": "Passwords don't match!" if not is_finnish else "Salasanat eivät täsmää!",
            "answer_required": "All security questions must be answered!" if not is_finnish else "Kaikkiin turvallisuuskysymyksiin on vastattava!",
            "incorrect_answers": "Incorrect security answers!" if not is_finnish else "Väärät turvallisuusvastaukset!",
            "password_reset_success": "Master password reset successfully!" if not is_finnish else "Pääsalasana palautettu onnistuneesti!",
            "first_time_setup": "First time setup - please set security questions" if not is_finnish else "Ensimmäinen asennus - määritä turvallisuuskysymykset",
            
            # Main window sections
            "search_filter": "Search & Filter" if not is_finnish else "Haku & Suodatus",
            "password_details": "Password Details" if not is_finnish else "Salasanan Tiedot",
            "actions": "Actions" if not is_finnish else "Toiminnot",
            
            # Search and filter
            "search": "Search:" if not is_finnish else "Haku:",
            "category": "Category:" if not is_finnish else "Kategoria:",
            "all": "All" if not is_finnish else "Kaikki",
            
            # Categories
            "general": "General" if not is_finnish else "Yleinen",
            "work": "Work" if not is_finnish else "Työ",
            "personal": "Personal" if not is_finnish else "Henkilökohtainen",
            "social": "Social" if not is_finnish else "Sosiaalinen",
            "finance": "Finance" if not is_finnish else "Talous",
            
            # Password fields
            "service": "Service:" if not is_finnish else "Palvelu:",
            "username": "Username:" if not is_finnish else "Käyttäjänimi:",
            "password": "Password:" if not is_finnish else "Salasana:",
            "url": "URL:" if not is_finnish else "Verkko-osoite:",
            "strength": "Strength:" if not is_finnish else "Vahvuus:",
            
            # Buttons
            "generate": "Generate" if not is_finnish else "Luo",
            "add": "Add" if not is_finnish else "Lisää",
            "update": "Update" if not is_finnish else "Päivitä",
            "delete": "Delete" if not is_finnish else "Poista",
            "copy_user": "Copy User" if not is_finnish else "Kopioi Käyttäjä",
            "copy_pass": "Copy Pass" if not is_finnish else "Kopioi Salasana",
            "auto_fill": "Auto-Fill" if not is_finnish else "Automaattinen Täyttö",
            "test_url": "Test URL" if not is_finnish else "Testaa Osoite",
            "export": "Export" if not is_finnish else "Vie",
            "import": "Import" if not is_finnish else "Tuo",
            "logout": "Logout" if not is_finnish else "Kirjaudu Ulos",
            
            # Status and messages
            "status": "Status:" if not is_finnish else "Tila:",
            "password_added": "Password added successfully for {}" if not is_finnish else "Salasana lisätty onnistuneesti palvelulle {}",
            "password_updated": "Password updated successfully for {}" if not is_finnish else "Salasana päivitetty onnistuneesti palvelulle {}",
            "password_deleted": "Password deleted successfully for {}" if not is_finnish else "Salasana poistettu onnistuneesti palvelulta {}",
            "password_generated": "New password generated" if not is_finnish else "Uusi salasana luotu",
            "copied_to_clipboard": "{} copied to clipboard" if not is_finnish else "{} kopioitu leikepöydälle",
            "url_opened": "Opening URL for {}" if not is_finnish else "Avataan osoite palvelulle {}",
            "auto_fill_started": "Starting auto-fill for {}" if not is_finnish else "Aloitetaan automaattinen täyttö palvelulle {}",
            "search_results": "Found {} matches" if not is_finnish else "Löydettiin {} osumaa",
            "category_filter": "Showing {} passwords in category {}" if not is_finnish else "Näytetään {} salasanaa kategoriassa {}",
            "fill_required": "Please fill in all required fields!" if not is_finnish else "Täytä kaikki pakolliset kentät!",
            "select_service": "Please select a service first!" if not is_finnish else "Valitse ensin palvelu!",
            "confirm_delete": "Are you sure you want to delete password for {}?" if not is_finnish else "Haluatko varmasti poistaa salasanan palvelulta {}?",
            "nothing_to_copy": "Nothing to copy!" if not is_finnish else "Ei mitään kopioitavaa!",
            "enter_url": "Please enter a URL!" if not is_finnish else "Anna verkko-osoite!",
            "service_exists": "Service {} already exists!" if not is_finnish else "Palvelu {} on jo olemassa!",
            "service_not_found": "Service not found!" if not is_finnish else "Palvelua ei löydy!",
            "select_service_url": "Please select a service and enter a URL!" if not is_finnish else "Valitse palvelu ja anna verkko-osoite!",
            "login_successful": "Login successful!" if not is_finnish else "Kirjautuminen onnistui!",
            "logout_successful": "Logout successful!" if not is_finnish else "Uloskirjautuminen onnistui!",
            
            # Password strength levels
            "very_strong": "Very Strong" if not is_finnish else "Erittäin Vahva",
            "strong": "Strong" if not is_finnish else "Vahva",
            "moderate": "Moderate" if not is_finnish else "Kohtalainen",
            "weak": "Weak" if not is_finnish else "Heikko",
            "very_weak": "Very Weak" if not is_finnish else "Erittäin Heikko",
            
            # Password feedback
            "add_numbers": "Add numbers" if not is_finnish else "Lisää numeroita",
            "add_lowercase": "Add lowercase letters" if not is_finnish else "Lisää pieniä kirjaimia",
            "add_uppercase": "Add uppercase letters" if not is_finnish else "Lisää isoja kirjaimia",
            "add_special": "Add special characters" if not is_finnish else "Lisää erikoismerkkejä",
            "password_good": "Password is good!" if not is_finnish else "Salasana on hyvä!",
            
            # Error messages
            "master_password_weak": "Master password too weak! Must contain uppercase, lowercase, numbers, and special characters." \
                if not is_finnish else "Pääsalasana liian heikko! Täytyy sisältää isoja ja pieniä kirjaimia, numeroita ja erikoismerkkejä.",
            "error_occurred": "An error occurred:" if not is_finnish else "Tapahtui virhe:"
        }
    
    def get(self, key: str, *args) -> str:
        """Get translation with optional format arguments"""
        text = self.translations.get(key, key)
        if args:
            return text.format(*args)
        return text
