import PySimpleGUI as sg
from password_manager_core import PasswordManager
from web_integration import WebAutomation
from languages import Language
from security_questions import SecurityQuestions

def create_security_setup_window(lang: Language):
    """Create window for setting up security questions"""
    # Allow language selection at setup
    layout = [
        [sg.Text(lang.get("select_language"), font=('Helvetica', 10)),
         sg.Radio(lang.get("english"), "LANG", key='-ENGLISH-', default=not lang.is_finnish, 
                 enable_events=True, font=('Helvetica', 10)),
         sg.Radio(lang.get("finnish"), "LANG", key='-FINNISH-', default=lang.is_finnish,
                 enable_events=True, font=('Helvetica', 10))],
        [sg.Text(lang.get("first_time_setup"), font=('Helvetica', 12, 'bold'))],
        [sg.Text(lang.get("setup_questions"), font=('Helvetica', 10))],
        [sg.Text(lang.get("question1"), font=('Helvetica', 10))],
        [sg.Input(key='-ANSWER1-', font=('Helvetica', 10), size=(40, 1))],
        [sg.Text(lang.get("question2"), font=('Helvetica', 10))],
        [sg.Input(key='-ANSWER2-', font=('Helvetica', 10), size=(40, 1))],
        [sg.Text(lang.get("question3"), font=('Helvetica', 10))],
        [sg.Input(key='-ANSWER3-', font=('Helvetica', 10), size=(40, 1))],
        [sg.Button(lang.get("save_answers"), font=('Helvetica', 10))]
    ]
    
    return sg.Window(
        lang.get("title_setup"),
        layout,
        font=('Helvetica', 10),
        margins=(30, 20),
        element_padding=(10, 5),
        finalize=True
    )

def create_reset_window(lang: Language):
    """Create window for resetting master password"""
    layout = [
        [sg.Text(lang.get("answer_questions"), font=('Helvetica', 12, 'bold'))],
        [sg.Text(lang.get("question1"), font=('Helvetica', 10))],
        [sg.Input(key='-ANSWER1-', font=('Helvetica', 10), size=(40, 1))],
        [sg.Text(lang.get("question2"), font=('Helvetica', 10))],
        [sg.Input(key='-ANSWER2-', font=('Helvetica', 10), size=(40, 1))],
        [sg.Text(lang.get("question3"), font=('Helvetica', 10))],
        [sg.Input(key='-ANSWER3-', font=('Helvetica', 10), size=(40, 1))],
        [sg.Text(lang.get("new_password"), font=('Helvetica', 10))],
        [sg.Input(key='-NEW-PASS-', password_char='•', font=('Helvetica', 10), size=(40, 1))],
        [sg.Text(lang.get("confirm_password"), font=('Helvetica', 10))],
        [sg.Input(key='-CONFIRM-PASS-', password_char='•', font=('Helvetica', 10), size=(40, 1))],
        [sg.Button(lang.get("submit_answers"), font=('Helvetica', 10))]
    ]
    
    return sg.Window(
        lang.get("title_reset"),
        layout,
        font=('Helvetica', 10),
        margins=(30, 20),
        element_padding=(10, 5),
        finalize=True
    )

def create_window(lang: Language):
    # Modern dark theme with blue accents
    sg.theme('DarkBlue')
    
    # Custom styling
    title_font = ('Helvetica', 16, 'bold')
    header_font = ('Helvetica', 12, 'bold')
    normal_font = ('Helvetica', 10)
    
    layout = [
        [sg.Text(lang.get("select_language"), font=normal_font),
         sg.Radio(lang.get("english"), "LANG", key='-ENGLISH-', default=not lang.is_finnish, 
                 enable_events=True, font=normal_font),
         sg.Radio(lang.get("finnish"), "LANG", key='-FINNISH-', default=lang.is_finnish,
                 enable_events=True, font=normal_font)],
        [sg.Text(lang.get("master_password"), font=normal_font), 
         sg.Input(key='-MASTER-', password_char='•', font=normal_font,
                 size=(30, 1))],
        [sg.Button(lang.get("login"), font=normal_font, size=(10, 1), 
                  button_color=('#FFFFFF', '#0078D4')),
         sg.Button(lang.get("forgot_password"), font=normal_font)]
    ]
    
    return sg.Window(
        lang.get("title_login"),
        layout,
        font=normal_font,
        margins=(30, 20),
        element_padding=(10, 5),
        finalize=True
    )

def create_main_window(lang: Language):
    # Modern dark theme with blue accents
    sg.theme('DarkBlue')
    
    # Custom styling
    title_font = ('Helvetica', 16, 'bold')
    header_font = ('Helvetica', 12, 'bold')
    normal_font = ('Helvetica', 10)
    
    # Categories
    categories = [
        lang.get("all"),
        lang.get("general"),
        lang.get("work"),
        lang.get("personal"),
        lang.get("social"),
        lang.get("finance")
    ]
    
    # Create tabs
    search_frame = [
        [sg.Text(lang.get("search"), font=normal_font), 
         sg.Input(key='-SEARCH-', enable_events=True, font=normal_font,
                 size=(30, 1))],
        [sg.Text(lang.get("category"), font=normal_font), 
         sg.Combo(categories, default_value=lang.get("all"), 
                 key='-CATEGORY-', enable_events=True, font=normal_font,
                 size=(20, 1))],
        [sg.Listbox(values=[], size=(45, 8), key='-LIST-', 
                   enable_events=True, font=normal_font)]
    ]
    
    password_frame = [
        [sg.Text(lang.get("service"), font=normal_font), 
         sg.Input(key='-SERVICE-', font=normal_font, size=(30, 1))],
        [sg.Text(lang.get("username"), font=normal_font), 
         sg.Input(key='-USERNAME-', font=normal_font, size=(30, 1))],
        [sg.Text(lang.get("password"), font=normal_font), 
         sg.Input(key='-PASSWORD-', password_char='•', font=normal_font,
                 size=(30, 1)),
         sg.Button('👁', key='-TOGGLE-PASS-', font=normal_font),
         sg.Button(lang.get("generate"), font=normal_font)],
        [sg.Text(lang.get("strength"), font=normal_font), 
         sg.Text('', key='-STRENGTH-', size=(12, 1), font=normal_font),
         sg.ProgressBar(100, orientation='h', size=(20, 20), key='-STRENGTH-BAR-',
                       bar_color=('#0078D4', '#3D3D3D'))],
        [sg.Text('', key='-FEEDBACK-', size=(40, 1), font=normal_font, 
                text_color='#FFB900')],
        [sg.Text(lang.get("url"), font=normal_font), 
         sg.Input(key='-URL-', font=normal_font, size=(40, 1))],
        [sg.Text(lang.get("category"), font=normal_font), 
         sg.Combo(categories[1:], default_value=lang.get("general"),
                 key='-NEW-CATEGORY-', font=normal_font,
                 size=(20, 1))]
    ]
    
    button_frame = [
        [sg.Button(lang.get("add"), font=normal_font),
         sg.Button(lang.get("update"), font=normal_font),
         sg.Button(lang.get("delete"), font=normal_font, button_color=('#FFFFFF', '#D83B01')),
         sg.VSeparator(),
         sg.Button(lang.get("copy_user"), font=normal_font),
         sg.Button(lang.get("copy_pass"), font=normal_font),
         sg.VSeparator(),
         sg.Button(lang.get("auto_fill"), font=normal_font),
         sg.Button(lang.get("test_url"), font=normal_font)]
    ]
    
    layout = [
        [sg.Text(lang.get("title_main"), font=title_font, pad=(0, 10))],
        [sg.Frame(lang.get("search_filter"), search_frame, font=header_font, 
                 pad=(0, 10))],
        [sg.Frame(lang.get("password_details"), password_frame, font=header_font,
                 pad=(0, 10))],
        [sg.Frame(lang.get("actions"), button_frame, font=header_font,
                 pad=(0, 10))],
        [sg.Button(lang.get("export"), font=normal_font),
         sg.Button(lang.get("import"), font=normal_font),
         sg.Button(lang.get("logout"), font=normal_font, button_color=('#FFFFFF', '#D83B01'))],
        [sg.Text(lang.get("status"), font=normal_font), 
         sg.Text('', key='-STATUS-', size=(50, 1), font=normal_font,
                text_color='#0078D4')]
    ]
    
    return sg.Window(
        lang.get("title_main"),
        layout,
        font=normal_font,
        margins=(30, 20),
        element_padding=(10, 5),
        finalize=True
    )

def run_main_window(window, lang, master_password):
    password_manager = PasswordManager()
    web_auto = WebAutomation()
    show_password = False
    current_service = None
    
    def update_status(message, is_error=False):
        """Update status message with color"""
        color = '#FF0000' if is_error else '#0078D4'
        window['-STATUS-'].update(message, text_color=color)
    
    def update_list(filter_text="", category=None):
        """Update password list with optional filtering"""
        if filter_text:
            filtered = password_manager.search_passwords(filter_text)
            update_status(lang.get("search_results").format(len(filtered)))
        else:
            filtered = password_manager.password_dict
        
        if category and category != lang.get("all"):
            filtered = {k: v for k, v in filtered.items() if v.category == category}
            update_status(lang.get("category_filter").format(len(filtered), category))
        
        window['-LIST-'].update(values=list(filtered.keys()))
    
    def get_strength_text(score: int, lang: Language = None) -> str:
        """Get password strength text based on score"""
        if not lang:
            # Default to English if no language provided
            if score >= 80:
                return "Very Strong"
            elif score >= 60:
                return "Strong"
            elif score >= 40:
                return "Moderate"
            elif score >= 20:
                return "Weak"
            else:
                return "Very Weak"
        
        # Use language-specific text
        if score >= 80:
            return lang.get("very_strong")
        elif score >= 60:
            return lang.get("strong")
        elif score >= 40:
            return lang.get("moderate")
        elif score >= 20:
            return lang.get("weak")
        else:
            return lang.get("very_weak")

    while True:
        try:
            event, values = window.read(timeout=100)
            
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
                
            elif event == '-SEARCH-' or event == '-CATEGORY-':
                search_query = values['-SEARCH-']
                category = values['-CATEGORY-']
                update_list(search_query, category)
            
            elif event == '-LIST-':
                if values['-LIST-']:
                    current_service = values['-LIST-'][0]
                    entry = password_manager.get_password_entry(current_service)
                    if entry:
                        window['-SERVICE-'].update(current_service)
                        window['-USERNAME-'].update(entry.username)
                        window['-PASSWORD-'].update(entry.password)
                        window['-URL-'].update(entry.url)
                        window['-NEW-CATEGORY-'].update(entry.category)
                        
                        # Update password strength
                        score, _, _, feedback = password_manager.strength_checker.check_strength(entry.password)
                        window['-STRENGTH-BAR-'].update(score)
                        window['-STRENGTH-'].update(get_strength_text(score, lang))
                        window['-FEEDBACK-'].update(feedback)
            
            elif event == lang.get("generate"):
                password = password_manager.generate_password()
                window['-PASSWORD-'].update(password)
                update_status(lang.get("password_generated"))
                
                # Update strength for generated password
                score, _, _, feedback = password_manager.strength_checker.check_strength(password)
                window['-STRENGTH-BAR-'].update(score)
                window['-STRENGTH-'].update(get_strength_text(score, lang))
                window['-FEEDBACK-'].update(feedback)
            
            elif event == '-TOGGLE-PASS-':
                show_password = not show_password
                window['-PASSWORD-'].update(password_char='' if show_password else '•')
            
            elif event == lang.get("add"):
                service = values['-SERVICE-']
                username = values['-USERNAME-']
                password = values['-PASSWORD-']
                url = values['-URL-']
                category = values['-NEW-CATEGORY-']
                
                if not all([service, username, password]):
                    update_status(lang.get("fill_required"), True)
                    continue
                
                if service in password_manager.password_dict:
                    update_status(lang.get("service_exists").format(service), True)
                    continue
                
                if password_manager.add_password(service, username, password, url, category):
                    update_status(lang.get("password_added").format(service))
                    update_list()
                    window['-SERVICE-'].update('')
                    window['-USERNAME-'].update('')
                    window['-PASSWORD-'].update('')
                    window['-URL-'].update('')
                else:
                    update_status(lang.get("error_occurred"), True)
            
            elif event == lang.get("update"):
                if not current_service:
                    update_status(lang.get("select_service"), True)
                    continue
                
                service = values['-SERVICE-']
                username = values['-USERNAME-']
                password = values['-PASSWORD-']
                url = values['-URL-']
                category = values['-NEW-CATEGORY-']
                
                if not all([service, username, password]):
                    update_status(lang.get("fill_required"), True)
                    continue
                
                if password_manager.delete_password(current_service):
                    if password_manager.add_password(service, username, password, url, category):
                        update_status(lang.get("password_updated").format(service))
                        current_service = service
                        update_list()
            
            elif event == lang.get("delete"):
                if not current_service:
                    update_status(lang.get("select_service"), True)
                    continue
                
                if sg.popup_yes_no(lang.get("confirm_delete").format(current_service),
                                 title=lang.get("confirm_delete")) == 'Yes':
                    if password_manager.delete_password(current_service):
                        update_status(lang.get("password_deleted").format(current_service))
                        update_list()
                        window['-SERVICE-'].update('')
                        window['-USERNAME-'].update('')
                        window['-PASSWORD-'].update('')
                        window['-URL-'].update('')
                        current_service = None
            
            elif event == lang.get("copy_user"):
                if not values['-USERNAME-']:
                    update_status(lang.get("nothing_to_copy"), True)
                    continue
                pyperclip.copy(values['-USERNAME-'])
                update_status(lang.get("copied_to_clipboard").format(lang.get("username")))
            
            elif event == lang.get("copy_pass"):
                if not values['-PASSWORD-']:
                    update_status(lang.get("nothing_to_copy"), True)
                    continue
                pyperclip.copy(values['-PASSWORD-'])
                update_status(lang.get("copied_to_clipboard").format(lang.get("password")))
            
            elif event == lang.get("test_url"):
                if not values['-URL-']:
                    update_status(lang.get("enter_url"), True)
                    continue
                update_status(lang.get("url_opened").format(current_service))
                web_auto.open_url(values['-URL-'])
            
            elif event == lang.get("auto_fill"):
                if not current_service or not values['-URL-']:
                    update_status(lang.get("select_service_url"), True)
                    continue
                
                entry = password_manager.get_password_entry(current_service)
                if entry:
                    update_status(lang.get("auto_fill_started").format(current_service))
                    web_auto.auto_fill(entry.url, entry.username, entry.password)
                else:
                    update_status(lang.get("service_not_found"), True)
            
            elif event == lang.get("logout"):
                if sg.popup_yes_no(lang.get("confirm_logout"), title=lang.get("logout")) == 'Yes':
                    update_status(lang.get("logout_successful"))
                    window.close()
                    main()
            
            # Update password strength when typing
            if values.get('-PASSWORD-'):
                password = values['-PASSWORD-']
                score, _, _, feedback = password_manager.strength_checker.check_strength(password)
                window['-STRENGTH-BAR-'].update(score)
                window['-STRENGTH-'].update(get_strength_text(score, lang))
                window['-FEEDBACK-'].update(feedback)
        
        except Exception as e:
            sg.popup_error(f'{lang.get("error_occurred")} {str(e)}')
            continue
    
    window.close()

def check_master_password(password: str) -> bool:
    """Check if master password meets security requirements"""
    if len(password) < 8:
        return False
        
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    return has_upper and has_lower and has_digit and has_special

def main():
    # Initialize language and security
    lang = Language(is_finnish=False)
    security = SecurityQuestions()
    
    # Check if first time setup is needed
    if security.is_setup_needed():
        setup_window = create_security_setup_window(lang)
        while True:
            event, values = setup_window.read()
            
            if event == sg.WIN_CLOSED:
                setup_window.close()
                return
                
            # Handle language change in setup
            if event in ['-ENGLISH-', '-FINNISH-']:
                is_finnish = values['-FINNISH-']
                lang = Language(is_finnish=is_finnish)
                setup_window.close()
                setup_window = create_security_setup_window(lang)
                continue
                
            if event == lang.get("save_answers"):
                answers = [values['-ANSWER1-'], values['-ANSWER2-'], values['-ANSWER3-']]
                if not all(answers):
                    sg.popup(lang.get("answer_required"), title=lang.get("error_occurred"))
                    continue
                    
                if security.save_answers(answers):
                    setup_window.close()
                    break
                else:
                    sg.popup(lang.get("error_occurred"), title=lang.get("error_occurred"))
                    continue
    
    window = create_window(lang)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
            
        # Handle language change
        if event in ['-ENGLISH-', '-FINNISH-']:
            is_finnish = values['-FINNISH-']
            lang = Language(is_finnish=is_finnish)
            window.close()
            window = create_window(lang)
            continue
            
        if event == lang.get("forgot_password"):
            window.hide()
            reset_window = create_reset_window(lang)
            
            while True:
                reset_event, reset_values = reset_window.read()
                
                if reset_event == sg.WIN_CLOSED:
                    reset_window.close()
                    window.un_hide()
                    break
                    
                if reset_event == lang.get("submit_answers"):
                    answers = [
                        reset_values['-ANSWER1-'],
                        reset_values['-ANSWER2-'],
                        reset_values['-ANSWER3-']
                    ]
                    
                    if not all(answers):
                        sg.popup(lang.get("answer_required"), title=lang.get("error_occurred"))
                        continue
                        
                    new_pass = reset_values['-NEW-PASS-']
                    confirm_pass = reset_values['-CONFIRM-PASS-']
                    
                    if new_pass != confirm_pass:
                        sg.popup(lang.get("passwords_dont_match"), title=lang.get("error_occurred"))
                        continue
                        
                    if not check_master_password(new_pass):
                        sg.popup(lang.get("master_password_weak"), title=lang.get("error_occurred"))
                        continue
                        
                    if security.verify_answers(answers):
                        # Initialize password manager with new password
                        password_manager = PasswordManager()
                        if password_manager.initialize(new_pass):
                            sg.popup(lang.get("password_reset_success"))
                            reset_window.close()
                            window.un_hide()
                            break
                    else:
                        sg.popup(lang.get("incorrect_answers"), title=lang.get("error_occurred"))
            
            continue
            
        if event == lang.get("login"):
            master_password = values['-MASTER-']
            if not master_password:
                sg.popup(lang.get("fill_required"), title=lang.get("error_occurred"))
                continue
                
            if not check_master_password(master_password):
                sg.popup(lang.get("master_password_weak"), title=lang.get("error_occurred"))
                continue
            
            # Initialize password manager
            password_manager = PasswordManager()
            if not password_manager.initialize(master_password):
                sg.popup(lang.get("master_password_weak"), title=lang.get("error_occurred"))
                continue
            
            window.close()
            main_window = create_main_window(lang)
            run_main_window(main_window, lang, master_password)
            break
    
    window.close()

if __name__ == '__main__':
    main()
