# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideTeacherInfo(Action):

    def name(self) -> Text:
        return "action_provide_teacher_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        teacher_info = {
            "yasir mehmood": "Dr. Yasir Mehmood is the Coordinator of the Computer Science and Information Technology department...",
            "faisal riaz": "Prof. Dr. Faisal Riaz is a Professor in the Computer Science and Information Technology department...",
            "syed yasser arafat": "Dr. Syed Yasser Arafat is an Assistant Professor in the Computer Science and Information Technology department...",
            "muhammad mohsin ansari": "Muhammad Mohsin Ansari is a Lecturer in the Computer Science and Information Technology department...",
            "iftikhar ahmed": "Dr. Iftikhar Ahmed is an Assistant Professor in the Computer Science and Information Technology department...",
            "samreen ayaz": "Samreen Ayaz is an Assistant Professor in the Computer Science and Information Technology department...",
            "fakhra riaz": "Fakhra Riaz is a Lecturer in the Computer Science and Information Technology department...",
            "farzana riaz": "Farzana Riaz is a Lecturer in the Computer Science and Information Technology department...",
            "ghias hamid": "Ghias Hamid is a Lecturer in the Computer Science and Information Technology department...",
            "mehreen shakoor": "Mehreen Shakoor is a Lecturer in the Computer Science and Information Technology department...",
            "muhammad adnan": "Muhammad Adnan is a Lecturer in the Computer Science and Information Technology department...",
            "somyyia akram": "Somyyia Akram is a Lecturer in the Computer Science and Information Technology department...",
            "sommaiya akram": "Somyyia Akram is a Lecturer in the Computer Science and Information Technology department...",  
            "rabia rauf": "Rabia Rauf is a Lecturer in the Computer Science and Information Technology department...",
            "sania khadim": "Sania Khadim is a Lecturer in the Computer Science and Information Technology department...",
            "sofia ghafoor": "Sofia Ghafoor is a Lecturer in the Computer Science and Information Technology department...",
            "abdul sami": "Mr. Abdul Sami is a Lecturer at Kotli University and currently at MUST...",
            "abdul": "Mr. Abdul Sami is a Lecturer at Kotli University and currently at MUST...",  # Variation without last name
            "sami": "Mr. Abdul Sami is a Lecturer at Kotli University and currently at MUST...",   # 
            "adnan": "Muhammad Adnan is a Lecturer in the Computer Science and Information Technology department...",
            "rabia": "Rabia Rauf is a Lecturer in the Computer Science and Information Technology department..."
        }
        
        
        teacher_name = tracker.get_slot("teacher")
        
       
        if teacher_name:
            teacher_name = teacher_name.lower().replace("dr. ", "").replace("mr. ", "").replace("ms. ", "").replace("mrs. ", "").strip()

        
            print(f"Processed teacher name: '{teacher_name}'")
            
            
            if teacher_name in teacher_info:
                response = teacher_info[teacher_name]
            else:
                response = "I'm sorry, I don't have information on that teacher."
        else:
            response = "I'm sorry, I didn't catch the teacher's name. Could you please repeat?"

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        
        return []
