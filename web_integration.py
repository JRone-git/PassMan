from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time
import pyautogui
import re
import json
import os
from typing import Optional, Dict, Tuple

class WebIntegration:
    def __init__(self):
        self.driver = None
        self.lock = threading.Lock()
        self.known_sites_file = 'known_sites.json'
        self.known_sites = self._load_known_sites()
        
    def _load_known_sites(self) -> Dict[str, Dict]:
        """Load known website login patterns."""
        if os.path.exists(self.known_sites_file):
            with open(self.known_sites_file, 'r') as f:
                return json.load(f)
        return {
            "github.com": {
                "login_url": "https://github.com/login",
                "username_field": {"id": "login_field"},
                "password_field": {"id": "password"},
                "submit_button": {"name": "commit"}
            },
            "google.com": {
                "login_url": "https://accounts.google.com/signin",
                "username_field": {"name": "identifier"},
                "password_field": {"name": "password"},
                "submit_button": {"id": "passwordNext"}
            },
            "facebook.com": {
                "login_url": "https://www.facebook.com/login",
                "username_field": {"id": "email"},
                "password_field": {"id": "pass"},
                "submit_button": {"name": "login"}
            },
            "twitter.com": {
                "login_url": "https://twitter.com/login",
                "username_field": {"name": "text"},
                "password_field": {"name": "password"},
                "submit_button": {"xpath": "//div[@data-testid='LoginForm_Login_Button']"}
            },
            "linkedin.com": {
                "login_url": "https://www.linkedin.com/login",
                "username_field": {"id": "username"},
                "password_field": {"id": "password"},
                "submit_button": {"xpath": "//button[@type='submit']"}
            },
            "instagram.com": {
                "login_url": "https://www.instagram.com/accounts/login",
                "username_field": {"name": "username"},
                "password_field": {"name": "password"},
                "submit_button": {"xpath": "//button[@type='submit']"}
            },
            "amazon.com": {
                "login_url": "https://www.amazon.com/ap/signin",
                "username_field": {"id": "ap_email"},
                "password_field": {"id": "ap_password"},
                "submit_button": {"id": "signInSubmit"}
            },
            "microsoft.com": {
                "login_url": "https://login.live.com",
                "username_field": {"name": "loginfmt"},
                "password_field": {"name": "passwd"},
                "submit_button": {"id": "idSIButton9"}
            },
            "reddit.com": {
                "login_url": "https://www.reddit.com/login",
                "username_field": {"id": "loginUsername"},
                "password_field": {"id": "loginPassword"},
                "submit_button": {"xpath": "//button[@type='submit']"}
            },
            "netflix.com": {
                "login_url": "https://www.netflix.com/login",
                "username_field": {"id": "id_userLoginId"},
                "password_field": {"id": "id_password"},
                "submit_button": {"xpath": "//button[@type='submit']"}
            },
            "spotify.com": {
                "login_url": "https://accounts.spotify.com/login",
                "username_field": {"id": "login-username"},
                "password_field": {"id": "login-password"},
                "submit_button": {"id": "login-button"}
            },
            "dropbox.com": {
                "login_url": "https://www.dropbox.com/login",
                "username_field": {"name": "login_email"},
                "password_field": {"name": "login_password"},
                "submit_button": {"xpath": "//button[@type='submit']"}
            },
            "yahoo.com": {
                "login_url": "https://login.yahoo.com",
                "username_field": {"id": "login-username"},
                "password_field": {"id": "login-passwd"},
                "submit_button": {"id": "login-signin"}
            },
            "twitch.tv": {
                "login_url": "https://www.twitch.tv/login",
                "username_field": {"id": "login-username"},
                "password_field": {"id": "password-input"},
                "submit_button": {"xpath": "//button[@data-a-target='passport-login-button']"}
            },
            "discord.com": {
                "login_url": "https://discord.com/login",
                "username_field": {"name": "email"},
                "password_field": {"name": "password"},
                "submit_button": {"xpath": "//button[@type='submit']"}
            }
        }
    
    def initialize_driver(self):
        """Initialize the web driver with security settings."""
        if not self.driver:
            try:
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')  # Run in headless mode
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                
                service = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service, options=options)
                self.driver.set_page_load_timeout(10)  # Reduced timeout
                return True
            except Exception as e:
                print(f"Failed to initialize driver: {str(e)}")
                return False
        return True
    
    def close_driver(self):
        """Safely close the web driver."""
        with self.lock:
            if self.driver:
                try:
                    self.driver.quit()
                except:
                    pass
                finally:
                    self.driver = None
    
    def learn_website(self, url: str) -> bool:
        """Learn login patterns for a new website."""
        try:
            if not self.initialize_driver():
                return False
                
            with self.lock:
                self.driver.get(url)
                # Look for common login form elements
                found_elements = False
                try:
                    # Check for username/email field
                    username_field = self.driver.find_element(By.CSS_SELECTOR, 
                        'input[type="text"], input[type="email"], input[name="username"], input[name="email"]')
                    # Check for password field
                    password_field = self.driver.find_element(By.CSS_SELECTOR, 
                        'input[type="password"]')
                    # Check for submit button
                    submit_button = self.driver.find_element(By.CSS_SELECTOR, 
                        'button[type="submit"], input[type="submit"]')
                    found_elements = True
                except NoSuchElementException:
                    found_elements = False
                
                self.close_driver()
                return found_elements
                
        except Exception as e:
            print(f"Error learning website: {str(e)}")
            self.close_driver()
            return False
    
    def autofill_login(self, url: str, username: str, password: str) -> bool:
        """Auto-fill login credentials."""
        try:
            if not self.initialize_driver():
                return False
                
            with self.lock:
                self.driver.get(url)
                
                # Find and fill username
                username_field = self.driver.find_element(By.CSS_SELECTOR, 
                    'input[type="text"], input[type="email"], input[name="username"], input[name="email"]')
                username_field.send_keys(username)
                
                # Find and fill password
                password_field = self.driver.find_element(By.CSS_SELECTOR, 
                    'input[type="password"]')
                password_field.send_keys(password)
                
                # Find and click submit button
                submit_button = self.driver.find_element(By.CSS_SELECTOR, 
                    'button[type="submit"], input[type="submit"]')
                submit_button.click()
                
                time.sleep(2)  # Brief wait to ensure form submission
                self.close_driver()
                return True
                
        except Exception as e:
            print(f"Error auto-filling login: {str(e)}")
            self.close_driver()
            return False
    
    def detect_login_fields(self) -> Tuple[Optional[Dict], Optional[Dict], Optional[Dict]]:
        """Detect login fields on the current page."""
        common_username_patterns = [
            'username', 'email', 'login', 'user', 'id', 'phone',
            'account', 'loginid', 'userid', 'user-name', 'username-or-email'
        ]
        common_password_patterns = [
            'password', 'pass', 'pwd', 'passwd'
        ]
        
        try:
            # Try to find username field
            username_field = None
            # Check by type first
            elements = self.driver.find_elements(By.XPATH, "//input[@type='email']")
            if elements:
                username_field = {'xpath': "//input[@type='email']"}
            else:
                for pattern in common_username_patterns:
                    # Try ID
                    elements = self.driver.find_elements(By.ID, pattern)
                    if elements:
                        username_field = {'id': pattern}
                        break
                    # Try name
                    elements = self.driver.find_elements(By.NAME, pattern)
                    if elements:
                        username_field = {'name': pattern}
                        break
                    # Try contains
                    elements = self.driver.find_elements(By.XPATH, 
                        f"//input[contains(@id, '{pattern}') or contains(@name, '{pattern}')]")
                    if elements:
                        username_field = {'xpath': f"//input[contains(@id, '{pattern}') or contains(@name, '{pattern}')]"}
                        break
            
            # Try to find password field
            password_field = None
            # First try type='password'
            elements = self.driver.find_elements(By.XPATH, "//input[@type='password']")
            if elements:
                password_field = {'xpath': "//input[@type='password']"}
            else:
                for pattern in common_password_patterns:
                    elements = self.driver.find_elements(By.XPATH, 
                        f"//input[@type='password' and (contains(@id, '{pattern}') or contains(@name, '{pattern}'))]")
                    if elements:
                        password_field = {'xpath': f"//input[@type='password' and (contains(@id, '{pattern}') or contains(@name, '{pattern}'))]"}
                        break
            
            # Try to find submit button
            submit_button = None
            submit_patterns = [
                "//button[@type='submit']",
                "//input[@type='submit']",
                "//button[contains(@class, 'login')]",
                "//button[contains(@class, 'signin')]",
                "//button[contains(text(), 'Log')]",
                "//button[contains(text(), 'Sign')]"
            ]
            for pattern in submit_patterns:
                elements = self.driver.find_elements(By.XPATH, pattern)
                if elements:
                    submit_button = {'xpath': pattern}
                    break
            
            return username_field, password_field, submit_button
            
        except Exception as e:
            print(f"Error detecting login fields: {str(e)}")
            return None, None, None
    
    def extract_domain(self, url: str) -> str:
        """Extract domain from URL."""
        match = re.search(r'(?:https?://)?(?:www\.)?([^/]+)', url)
        return match.group(1) if match else url
    
    def save_known_sites(self):
        """Save known website patterns."""
        with open(self.known_sites_file, 'w') as f:
            json.dump(self.known_sites, f, indent=4)


class WebAutomation:
    def __init__(self):
        self.driver = None
        self.lock = threading.Lock()
    
    def _create_driver(self):
        """Create a new browser instance with optimal settings."""
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless=new')  # Modern headless mode
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-notifications')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.set_page_load_timeout(10)
            driver.implicitly_wait(5)
            return driver
        except Exception as e:
            print(f"Failed to create driver: {str(e)}")
            return None
    
    def _ensure_driver(self):
        """Ensure we have a working driver."""
        if not self.driver:
            self.driver = self._create_driver()
        return self.driver is not None
    
    def _quit_driver(self):
        """Safely quit the driver."""
        try:
            if self.driver:
                self.driver.quit()
        except:
            pass
        finally:
            self.driver = None
    
    def fill_login_form(self, url: str, username: str, password: str) -> tuple[bool, str]:
        """
        Attempt to fill a login form on a webpage.
        Returns: (success, message)
        """
        with self.lock:
            try:
                if not self._ensure_driver():
                    return False, "Failed to initialize browser"
                
                # Load the page
                self.driver.get(url)
                time.sleep(2)  # Let the page load completely
                
                # Common selectors for login forms
                username_selectors = [
                    "input[type='email']",
                    "input[type='text']",
                    "input[name*='email']",
                    "input[name*='user']",
                    "input[id*='email']",
                    "input[id*='user']"
                ]
                
                password_selectors = [
                    "input[type='password']",
                    "input[name*='pass']",
                    "input[id*='pass']"
                ]
                
                submit_selectors = [
                    "button[type='submit']",
                    "input[type='submit']",
                    "button[contains(text(), 'Sign')]",
                    "button[contains(text(), 'Log')]"
                ]
                
                # Try to find username field
                username_field = None
                for selector in username_selectors:
                    try:
                        username_field = self.driver.find_element(By.CSS_SELECTOR, selector)
                        if username_field.is_displayed():
                            break
                    except:
                        continue
                
                if not username_field:
                    return False, "Could not find username field"
                
                # Try to find password field
                password_field = None
                for selector in password_selectors:
                    try:
                        password_field = self.driver.find_element(By.CSS_SELECTOR, selector)
                        if password_field.is_displayed():
                            break
                    except:
                        continue
                
                if not password_field:
                    return False, "Could not find password field"
                
                # Fill in the credentials
                username_field.clear()
                username_field.send_keys(username)
                time.sleep(0.5)
                
                password_field.clear()
                password_field.send_keys(password)
                time.sleep(0.5)
                
                # Try to find and click submit button
                submit_button = None
                for selector in submit_selectors:
                    try:
                        submit_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                        if submit_button.is_displayed():
                            break
                    except:
                        continue
                
                if submit_button:
                    submit_button.click()
                    time.sleep(2)  # Wait for form submission
                    return True, "Login form filled successfully"
                else:
                    return True, "Form filled, but submit button not found"
                
            except Exception as e:
                return False, f"Error filling login form: {str(e)}"
            finally:
                self._quit_driver()
    
    def test_login_form(self, url: str) -> tuple[bool, str]:
        """
        Test if a login form exists on the webpage.
        Returns: (success, message)
        """
        with self.lock:
            try:
                if not self._ensure_driver():
                    return False, "Failed to initialize browser"
                
                self.driver.get(url)
                time.sleep(2)
                
                # Check for password field as it's most distinctive
                password_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
                if password_field and password_field.is_displayed():
                    return True, "Login form found"
                return False, "No login form found"
                
            except NoSuchElementException:
                return False, "No login form found"
            except Exception as e:
                return False, f"Error testing login form: {str(e)}"
            finally:
                self._quit_driver()
