    # Patient Examples for Hospital Matching System
# Polish patients with various medical conditions

PATIENT_EXAMPLES = [
    # Cardiovascular Patients
    {
        "name": "Jan",
        "surname": "Kowalski",
        "age": 58,
        "gender": "Mężczyzna",
        "weight": "85 kg",
        "height": "175 cm",
        "location": "Warszawa",
        "complaint": "Ból w klatce piersiowej i duszność",
        "symptoms": ["chest pain", "shortness of breath", "fatigue", "rapid heartbeat"],
        "symptom_duration": "3 dni",
        "matched_diseases": ["Coronary Artery Disease", "Heart Conditions"]
    },
   
    {
        "name": "Anna",
        "surname": "Nowak",
        "age": 65,
        "gender": "Kobieta",
        "weight": "70 kg",
        "height": "162 cm",
        "location": "Gdańsk",
        "complaint": "Obrzęki nóg i zmęczenie",
        "symptoms": ["swelling in legs", "fatigue", "shortness of breath"],
        "symptom_duration": "2 tygodnie",
        "matched_diseases": ["Heart Failure", "Cardiomyopathies"]
    },

    # Respiratory Patients
    {
        "name": "Piotr",
        "surname": "Wiśniewski",
        "age": 45,
        "gender": "Mężczyzna",
        "weight": "78 kg",
        "height": "180 cm",
        "location": "Kraków",
        "complaint": "Przewlekły kaszel i utrata wagi",
        "symptoms": ["persistent cough", "unexplained weight loss", "fever", "night sweats"],
        "symptom_duration": "6 tygodni",
        "matched_diseases": ["Lung Cancer", "Tuberculosis"]
    },
    {
        "name": "Maria",
        "surname": "Wójcik",
        "age": 35,
        "gender": "Kobieta",
        "weight": "65 kg",
        "height": "168 cm",
        "location": "Łódź",
        "complaint": "Duszność i świszczący oddech",
        "symptoms": ["wheezing", "difficulty breathing", "cough"],
        "symptom_duration": "5 dni",
        "matched_diseases": ["Asthma", "Lung Diseases"]
    },

    # Gastrointestinal Patients
    {
        "name": "Tomasz",
        "surname": "Kaczmarek",
        "age": 42,
        "gender": "Mężczyzna",
        "weight": "82 kg",
        "height": "177 cm",
        "location": "Wrocław",
        "complaint": "Ból żołądka i nudności",
        "symptoms": ["stomach pain", "nausea", "vomiting", "heartburn"],
        "symptom_duration": "4 dni",
        "matched_diseases": ["Gastrointestinal Disorders", "Gastritis"]
    },
    {
        "name": "Katarzyna",
        "surname": "Zielińska",
        "age": 28,
        "gender": "Kobieta",
        "weight": "58 kg",
        "height": "165 cm",
        "location": "Poznań",
        "complaint": "Biegunka i ból brzucha",
        "symptoms": ["diarrhea", "abdominal pain", "bloating"],
        "symptom_duration": "3 dni",
        "matched_diseases": ["Gastrointestinal Disorders", "Inflammatory Bowel Disease"]
    },

    # Mental Health Patients
    {
        "name": "Michał",
        "surname": "Szymański",
        "age": 32,
        "gender": "Mężczyzna",
        "weight": "75 kg",
        "height": "183 cm",
        "location": "Białystok",
        "complaint": "Przygnębienie i brak apetytu",
        "symptoms": ["depression", "loss of appetite", "insomnia", "fatigue"],
        "symptom_duration": "3 miesiące",
        "matched_diseases": ["Depression", "Eating Disorders"]
    },
    {
        "name": "Agnieszka",
        "surname": "Dąbrowska",
        "age": 26,
        "gender": "Kobieta",
        "weight": "52 kg",
        "height": "170 cm",
        "location": "Gdańsk",
        "complaint": "Ataki paniki i niepokój",
        "symptoms": ["panic attacks", "anxiety", "rapid heartbeat", "dizziness"],
        "symptom_duration": "2 miesiące",
        "matched_diseases": ["Anxiety Disorders", "Panic Disorders"]
    },

    # Orthopedic Patients
    {
        "name": "Stanisław",
        "surname": "Lewandowski",
        "age": 55,
        "gender": "Mężczyzna",
        "weight": "90 kg",
        "height": "178 cm",
        "location": "Warszawa",
        "complaint": "Ból pleców i ograniczona ruchomość",
        "symptoms": ["back pain", "muscle pain", "morning stiffness"],
        "symptom_duration": "2 tygodnie",
        "matched_diseases": ["Back/neck pain", "Arthritis"]
    },
    {
        "name": "Ewa",
        "surname": "Jankowska",
        "age": 67,
        "gender": "Kobieta",
        "weight": "72 kg",
        "height": "160 cm",
        "location": "Olsztyn",
        "complaint": "Ból stawów i sztywność",
        "symptoms": ["joint pain", "morning stiffness", "swelling"],
        "symptom_duration": "6 miesięcy",
        "matched_diseases": ["Arthritis", "Bone Disorders"]
    },

    # Endocrine Patients
    {
        "name": "Robert",
        "surname": "Mazur",
        "age": 48,
        "gender": "Mężczyzna",
        "weight": "95 kg",
        "height": "175 cm",
        "location": "Kraków",
        "complaint": "Częste oddawanie moczu i pragnienie",
        "symptoms": ["frequent urination", "excessive thirst", "blurred vision", "fatigue"],
        "symptom_duration": "1 miesiąc",
        "matched_diseases": ["Diabetes"]
    },
    {
        "name": "Joanna",
        "surname": "Piotrkowska",
        "age": 39,
        "gender": "Kobieta",
        "weight": "68 kg",
        "height": "166 cm",
        "location": "Łódź",
        "complaint": "Przyrost wagi i zmęczenie",
        "symptoms": ["weight gain", "fatigue", "cold intolerance", "hair loss"],
        "symptom_duration": "3 miesiące",
        "matched_diseases": ["Hypothyroidism", "Thyroid Disorders"]
    },

    # Neurological Patients
    {
        "name": "Marek",
        "surname": "Król",
        "age": 61,
        "gender": "Mężczyzna",
        "weight": "80 kg",
        "height": "172 cm",
        "location": "Wrocław",
        "complaint": "Drżenie rąk i problemy z równowagą",
        "symptoms": ["tremors", "balance problems", "coordination problems"],
        "symptom_duration": "8 miesięcy",
        "matched_diseases": ["Movement Disorders", "Parkinson's disease"]
    },
    {
        "name": "Barbara",
        "surname": "Adamczyk",
        "age": 44,
        "gender": "Kobieta",
        "weight": "63 kg",
        "height": "164 cm",
        "location": "Gdańsk",
        "complaint": "Silne bóle głowy i zawroty",
        "symptoms": ["severe headache", "dizziness", "vision problems"],
        "symptom_duration": "1 tydzień",
        "matched_diseases": ["Brain Disorders", "Neurological Emergencies"]
    },

    # Emergency/Trauma Patients
    {
        "name": "Paweł",
        "surname": "Woźniak",
        "age": 29,
        "gender": "Mężczyzna",
        "weight": "76 kg",
        "height": "181 cm",
        "location": "Warszawa",
        "complaint": "Wypadek samochodowy - ból kręgosłupa",
        "symptoms": ["severe injury", "back pain", "confusion"],
        "symptom_duration": "1 godzina",
        "matched_diseases": ["Trauma Care", "Spinal Disorders"]
    },
    {
        "name": "Magdalena",
        "surname": "Sikora",
        "age": 34,
        "gender": "Kobieta",
        "weight": "61 kg",
        "height": "169 cm",
        "location": "Kraków",
        "complaint": "Złamanie nogi po upadku",
        "symptoms": ["broken bone", "severe pain", "swelling"],
        "symptom_duration": "2 godziny",
        "matched_diseases": ["Fractures", "Orthopedic Surgery"]
    },

    # Infectious Disease Patients
    {
        "name": "Grzegorz",
        "surname": "Bąk",
        "age": 37,
        "gender": "Mężczyzna",
        "weight": "83 kg",
        "height": "179 cm",
        "location": "Białystok",
        "complaint": "Wysoka gorączka i duszność",
        "symptoms": ["high fever", "difficulty breathing", "cough", "fatigue"],
        "symptom_duration": "5 dni",
        "matched_diseases": ["Covid-19", "Bacterial Infections"]
    },
    {
        "name": "Dorota",
        "surname": "Zawadzka",
        "age": 52,
        "gender": "Kobieta",
        "weight": "67 kg",
        "height": "163 cm",
        "location": "Olsztyn",
        "complaint": "Przewlekły kaszel i poty nocne",
        "symptoms": ["chronic cough", "night sweats", "weight loss", "fever"],
        "symptom_duration": "2 miesiące",
        "matched_diseases": ["Tuberculosis", "Lung Diseases"]
    },

    # Skin/Dermatology Patients
    {
        "name": "Krzysztof",
        "surname": "Witkowski",
        "age": 41,
        "gender": "Mężczyzna",
        "weight": "79 kg",
        "height": "176 cm",
        "location": "Poznań",
        "complaint": "Świąd skóry i wysypka",
        "symptoms": ["itchy skin", "skin rash", "red skin"],
        "symptom_duration": "2 tygodnie",
        "matched_diseases": ["Eczema", "Atopic Dermatitis"]
    },
    {
        "name": "Monika",
        "surname": "Grabowska",
        "age": 24,
        "gender": "Kobieta",
        "weight": "55 kg",
        "height": "167 cm",
        "location": "Łódź",
        "complaint": "Pryszcze i zmiany skórne",
        "symptoms": ["pimples", "blackheads", "skin bumps"],
        "symptom_duration": "3 miesiące",
        "matched_diseases": ["Acne", "Skin Disorders"]
    },

    # Eye/Vision Patients
    {
        "name": "Andrzej",
        "surname": "Kaźmierczak",
        "age": 59,
        "gender": "Mężczyzna",
        "weight": "87 kg",
        "height": "174 cm",
        "location": "Wrocław",
        "complaint": "Pogorszenie wzroku i ból oczu",
        "symptoms": ["blurred vision", "eye pain", "vision loss"],
        "symptom_duration": "1 miesiąc",
        "matched_diseases": ["Eye Diseases & Infections", "Retinal Disorders"]
    },

    # Kidney/Urological Patients
    {
        "name": "Teresa",
        "surname": "Kubiak",
        "age": 56,
        "gender": "Kobieta",
        "weight": "74 kg",
        "height": "161 cm",
        "location": "Gdańsk",
        "complaint": "Ból przy oddawaniu moczu i krew w moczu",
        "symptoms": ["painful urination", "blood in urine", "kidney pain"],
        "symptom_duration": "1 tydzień",
        "matched_diseases": ["Kidney Diseases", "Urinary Tract Infections"]
    },

    # Women's Health Patients
    {
        "name": "Beata",
        "surname": "Szczepańska",
        "age": 31,
        "gender": "Kobieta",
        "weight": "62 kg",
        "height": "168 cm",
        "location": "Warszawa",
        "complaint": "Nieregularne miesiączki i ból miednicy",
        "symptoms": ["irregular periods", "pelvic pain", "heavy bleeding"],
        "symptom_duration": "3 miesiące",
        "matched_diseases": ["Menstrual Irregularities", "Pelvic Inflammatory Disease"]
    },

    # Allergy Patients
    {
        "name": "Jacek",
        "surname": "Borkowski",
        "age": 33,
        "gender": "Mężczyzna",
        "weight": "71 kg",
        "height": "182 cm",
        "location": "Kraków",
        "complaint": "Katar sienny i świąd oczu",
        "symptoms": ["sneezing", "itchy eyes", "runny nose", "blocked nose"],
        "symptom_duration": "2 tygodnie",
        "matched_diseases": ["Allergic Rhinitis", "Seasonal Allergies"]
    },

    # Obesity/Metabolic Patients
    {
        "name": "Henryk",
        "surname": "Górski",
        "age": 47,
        "gender": "Mężczyzna",
        "weight": "110 kg",
        "height": "173 cm",
        "location": "Olsztyn",
        "complaint": "Nadwaga i wysokie ciśnienie",
        "symptoms": ["overweight", "high blood pressure", "fatigue"],
        "symptom_duration": "2 lata",
        "matched_diseases": ["Obesity", "Hypertension"]
    },

     # --- Additional Patients (Polish and Foreign, some with same diseases) ---
    {"name": "John", "surname": "Smith", "age": 60, "gender": "Male", "weight": "90 kg", "height": "180 cm", "location": "London", "complaint": "Chest pain and shortness of breath", "symptoms": ["chest pain", "shortness of breath", "fatigue"], "symptom_duration": "2 days", "matched_diseases": ["Coronary Artery Disease", "Heart Conditions"]},
    {"name": "Maria", "surname": "Garcia", "age": 54, "gender": "Female", "weight": "68 kg", "height": "165 cm", "location": "Madrid", "complaint": "Fatigue and leg swelling", "symptoms": ["fatigue", "swelling in legs"], "symptom_duration": "1 week", "matched_diseases": ["Heart Failure", "Cardiomyopathies"]},
    {"name": "Ahmed", "surname": "Hassan", "age": 47, "gender": "Male", "weight": "82 kg", "height": "178 cm", "location": "Cairo", "complaint": "Persistent cough and weight loss", "symptoms": ["persistent cough", "unexplained weight loss"], "symptom_duration": "3 weeks", "matched_diseases": ["Lung Cancer", "Tuberculosis"]},
    {"name": "Sophie", "surname": "Dubois", "age": 38, "gender": "Female", "weight": "60 kg", "height": "168 cm", "location": "Paris", "complaint": "Wheezing and cough", "symptoms": ["wheezing", "cough"], "symptom_duration": "4 days", "matched_diseases": ["Asthma", "Lung Diseases"]},
    {"name": "Luca", "surname": "Rossi", "age": 50, "gender": "Male", "weight": "85 kg", "height": "175 cm", "location": "Rome", "complaint": "Stomach pain and nausea", "symptoms": ["stomach pain", "nausea"], "symptom_duration": "2 days", "matched_diseases": ["Gastrointestinal Disorders", "Gastritis"]},
    {"name": "Olga", "surname": "Ivanova", "age": 29, "gender": "Female", "weight": "57 kg", "height": "162 cm", "location": "Moscow", "complaint": "Diarrhea and abdominal pain", "symptoms": ["diarrhea", "abdominal pain"], "symptom_duration": "1 day", "matched_diseases": ["Gastrointestinal Disorders", "Inflammatory Bowel Disease"]},
    {"name": "Ali", "surname": "Yılmaz", "age": 36, "gender": "Male", "weight": "80 kg", "height": "176 cm", "location": "Istanbul", "complaint": "Depression and insomnia", "symptoms": ["depression", "insomnia"], "symptom_duration": "2 months", "matched_diseases": ["Depression", "Eating Disorders"]},
    {"name": "Emily", "surname": "Johnson", "age": 27, "gender": "Female", "weight": "59 kg", "height": "170 cm", "location": "New York", "complaint": "Panic attacks and anxiety", "symptoms": ["panic attacks", "anxiety"], "symptom_duration": "1 month", "matched_diseases": ["Anxiety Disorders", "Panic Disorders"]},
    {"name": "Marek", "surname": "Nowicki", "age": 52, "gender": "Mężczyzna", "weight": "88 kg", "height": "179 cm", "location": "Poznań", "complaint": "Back pain and muscle pain", "symptoms": ["back pain", "muscle pain"], "symptom_duration": "3 weeks", "matched_diseases": ["Back/neck pain", "Arthritis"]},
    {"name": "Julia", "surname": "Müller", "age": 63, "gender": "Female", "weight": "70 kg", "height": "164 cm", "location": "Berlin", "complaint": "Joint pain and swelling", "symptoms": ["joint pain", "swelling"], "symptom_duration": "5 months", "matched_diseases": ["Arthritis", "Bone Disorders"]},
    {"name": "Carlos", "surname": "Santos", "age": 44, "gender": "Male", "weight": "92 kg", "height": "182 cm", "location": "Lisbon", "complaint": "Frequent urination and thirst", "symptoms": ["frequent urination", "excessive thirst"], "symptom_duration": "2 weeks", "matched_diseases": ["Diabetes"]},
    {"name": "Anna", "surname": "Petrova", "age": 41, "gender": "Female", "weight": "66 kg", "height": "167 cm", "location": "Kyiv", "complaint": "Weight gain and fatigue", "symptoms": ["weight gain", "fatigue"], "symptom_duration": "4 months", "matched_diseases": ["Hypothyroidism", "Thyroid Disorders"]},
    {"name": "David", "surname": "Brown", "age": 58, "gender": "Male", "weight": "83 kg", "height": "180 cm", "location": "Dublin", "complaint": "Tremors and balance problems", "symptoms": ["tremors", "balance problems"], "symptom_duration": "6 months", "matched_diseases": ["Movement Disorders", "Parkinson's disease"]},
    {"name": "Isabella", "surname": "Martinez", "age": 39, "gender": "Female", "weight": "61 kg", "height": "163 cm", "location": "Barcelona", "complaint": "Severe headache and dizziness", "symptoms": ["severe headache", "dizziness"], "symptom_duration": "2 weeks", "matched_diseases": ["Brain Disorders", "Neurological Emergencies"]},
    {"name": "Tomasz", "surname": "Lewicki", "age": 33, "gender": "Mężczyzna", "weight": "77 kg", "height": "174 cm", "location": "Gdańsk", "complaint": "Severe injury and back pain", "symptoms": ["severe injury", "back pain"], "symptom_duration": "2 hours", "matched_diseases": ["Trauma Care", "Spinal Disorders"]},
    {"name": "Sven", "surname": "Andersson", "age": 46, "gender": "Male", "weight": "85 kg", "height": "181 cm", "location": "Stockholm", "complaint": "Broken bone and swelling", "symptoms": ["broken bone", "swelling"], "symptom_duration": "3 hours", "matched_diseases": ["Fractures", "Orthopedic Surgery"]},
    {"name": "Fatima", "surname": "Al-Farsi", "age": 49, "gender": "Female", "weight": "69 kg", "height": "160 cm", "location": "Muscat", "complaint": "High fever and cough", "symptoms": ["high fever", "cough"], "symptom_duration": "4 days", "matched_diseases": ["Covid-19", "Bacterial Infections"]},
    {"name": "Lucas", "surname": "Silva", "age": 35, "gender": "Male", "weight": "81 kg", "height": "177 cm", "location": "Sao Paulo", "complaint": "Chronic cough and night sweats", "symptoms": ["chronic cough", "night sweats"], "symptom_duration": "1 month", "matched_diseases": ["Tuberculosis", "Lung Diseases"]},
    {"name": "Elena", "surname": "Popescu", "age": 40, "gender": "Female", "weight": "64 kg", "height": "165 cm", "location": "Bucharest", "complaint": "Itchy skin and rash", "symptoms": ["itchy skin", "skin rash"], "symptom_duration": "2 weeks", "matched_diseases": ["Eczema", "Atopic Dermatitis"]},
    {"name": "George", "surname": "Williams", "age": 30, "gender": "Male", "weight": "75 kg", "height": "172 cm", "location": "Sydney", "complaint": "Pimples and skin bumps", "symptoms": ["pimples", "skin bumps"], "symptom_duration": "2 months", "matched_diseases": ["Acne", "Skin Disorders"]},
    {"name": "Yuki", "surname": "Tanaka", "age": 28, "gender": "Female", "weight": "53 kg", "height": "158 cm", "location": "Tokyo", "complaint": "Blurred vision and eye pain", "symptoms": ["blurred vision", "eye pain"], "symptom_duration": "3 weeks", "matched_diseases": ["Eye Diseases & Infections", "Retinal Disorders"]},
    {"name": "Mateusz", "surname": "Wójcik", "age": 55, "gender": "Mężczyzna", "weight": "86 kg", "height": "178 cm", "location": "Kraków", "complaint": "Painful urination and blood in urine", "symptoms": ["painful urination", "blood in urine"], "symptom_duration": "5 days", "matched_diseases": ["Kidney Diseases", "Urinary Tract Infections"]},
    {"name": "Sara", "surname": "Eriksen", "age": 34, "gender": "Female", "weight": "60 kg", "height": "166 cm", "location": "Oslo", "complaint": "Irregular periods and pelvic pain", "symptoms": ["irregular periods", "pelvic pain"], "symptom_duration": "2 months", "matched_diseases": ["Menstrual Irregularities", "Pelvic Inflammatory Disease"]},
    {"name": "Mohammed", "surname": "Ali", "age": 42, "gender": "Male", "weight": "90 kg", "height": "180 cm", "location": "Dubai", "complaint": "Sneezing and itchy eyes", "symptoms": ["sneezing", "itchy eyes"], "symptom_duration": "1 week", "matched_diseases": ["Allergic Rhinitis", "Seasonal Allergies"]},
    {"name": "Natalia", "surname": "Kowalczyk", "age": 39, "gender": "Kobieta", "weight": "72 kg", "height": "170 cm", "location": "Wrocław", "complaint": "Overweight and high blood pressure", "symptoms": ["overweight", "high blood pressure"], "symptom_duration": "1 year", "matched_diseases": ["Obesity", "Hypertension"]},
    {"name": "Victor", "surname": "Nguyen", "age": 37, "gender": "Male", "weight": "78 kg", "height": "173 cm", "location": "Hanoi", "complaint": "Chest pain and shortness of breath", "symptoms": ["chest pain", "shortness of breath"], "symptom_duration": "2 days", "matched_diseases": ["Coronary Artery Disease", "Heart Conditions"]},
    {"name": "Alicja", "surname": "Szymańska", "age": 48, "gender": "Kobieta", "weight": "65 kg", "height": "168 cm", "location": "Lublin", "complaint": "Fatigue and leg swelling", "symptoms": ["fatigue", "swelling in legs"], "symptom_duration": "2 weeks", "matched_diseases": ["Heart Failure", "Cardiomyopathies"]},
    {"name": "Omar", "surname": "Abdullah", "age": 51, "gender": "Male", "weight": "88 kg", "height": "182 cm", "location": "Amman", "complaint": "Persistent cough and weight loss", "symptoms": ["persistent cough", "unexplained weight loss"], "symptom_duration": "4 weeks", "matched_diseases": ["Lung Cancer", "Tuberculosis"]},
    {"name": "Samantha", "surname": "Lee", "age": 32, "gender": "Female", "weight": "58 kg", "height": "162 cm", "location": "Toronto", "complaint": "Wheezing and cough", "symptoms": ["wheezing", "cough"], "symptom_duration": "3 days", "matched_diseases": ["Asthma", "Lung Diseases"]},

    # --- 30 New Patients with Rare Diseases ---
    {"name": "Mikołaj", "surname": "Czarnecki", "age": 62, "gender": "Mężczyzna", "weight": "81 kg", "height": "176 cm", "location": "Warszawa", "complaint": "Podejrzenie raka skóry", "symptoms": ["skin lesion", "unusual moles", "itchy skin"], "symptom_duration": "2 miesiące", "matched_diseases": ["Skin Cancer"]},
    {"name": "Elżbieta", "surname": "Majewska", "age": 70, "gender": "Kobieta", "weight": "68 kg", "height": "162 cm", "location": "Łódź", "complaint": "Zabieg pomostowania aortalno-wieńcowego (bypass surgery)", "symptoms": ["chest pain", "shortness of breath"], "symptom_duration": "1 miesiąc", "matched_diseases": ["Bypass Surgeries"]},
    {"name": "Andreas", "surname": "Schmidt", "age": 59, "gender": "Male", "weight": "90 kg", "height": "180 cm", "location": "Berlin", "complaint": "Aortic aneurysm", "symptoms": ["abdominal pain", "pulsating mass"], "symptom_duration": "3 tygodnie", "matched_diseases": ["Aortic Aneurysms"]},
    {"name": "Svetlana", "surname": "Kuznetsova", "age": 48, "gender": "Female", "weight": "74 kg", "height": "168 cm", "location": "Moscow", "complaint": "Soft tissue sarcoma", "symptoms": ["growing mass under skin", "pain"], "symptom_duration": "4 miesiące", "matched_diseases": ["Soft Tissue Sarcomas"]},
    {"name": "Olivier", "surname": "Moreau", "age": 53, "gender": "Male", "weight": "85 kg", "height": "178 cm", "location": "Paris", "complaint": "Paraneoplastic syndrome", "symptoms": ["unexplained weight loss", "fatigue"], "symptom_duration": "2 miesiące", "matched_diseases": ["Cancer"]},
    {"name": "Agnieszka", "surname": "Lis", "age": 44, "gender": "Kobieta", "weight": "60 kg", "height": "165 cm", "location": "Kraków", "complaint": "Zespół Cushinga", "symptoms": ["weight gain", "purple striae", "hypertension"], "symptom_duration": "6 miesięcy", "matched_diseases": ["Endocrine Cancers"]},
    {"name": "Ravi", "surname": "Patel", "age": 51, "gender": "Male", "weight": "77 kg", "height": "172 cm", "location": "Delhi", "complaint": "Parathyroid tumor", "symptoms": ["bone pain", "kidney stones"], "symptom_duration": "5 miesięcy", "matched_diseases": ["Thyroid/Parathyroid Tumors"]},
    {"name": "Anna", "surname": "Svensson", "age": 36, "gender": "Female", "weight": "62 kg", "height": "170 cm", "location": "Stockholm", "complaint": "Liver transplant recipient", "symptoms": ["jaundice", "fatigue"], "symptom_duration": "1 rok", "matched_diseases": ["Liver Transplants"]},
    {"name": "Piotr", "surname": "Baran", "age": 67, "gender": "Mężczyzna", "weight": "79 kg", "height": "174 cm", "location": "Poznań", "complaint": "Przeszczep nerki", "symptoms": ["swelling", "fatigue"], "symptom_duration": "8 miesięcy", "matched_diseases": ["Kidney Transplants"]},
    {"name": "Fatima", "surname": "El Amrani", "age": 42, "gender": "Female", "weight": "70 kg", "height": "168 cm", "location": "Casablanca", "complaint": "Pancreas transplant", "symptoms": ["abdominal pain", "nausea"], "symptom_duration": "3 miesiące", "matched_diseases": ["Pancreas Transplants"]},
    {"name": "Mateusz", "surname": "Duda", "age": 39, "gender": "Mężczyzna", "weight": "82 kg", "height": "180 cm", "location": "Wrocław", "complaint": "HIV infection", "symptoms": ["weight loss", "night sweats"], "symptom_duration": "6 miesięcy", "matched_diseases": ["HIV"]},
    {"name": "Julia", "surname": "Nowak", "age": 29, "gender": "Kobieta", "weight": "58 kg", "height": "164 cm", "location": "Gdańsk", "complaint": "AIDS", "symptoms": ["recurrent infections", "weight loss"], "symptom_duration": "1 rok", "matched_diseases": ["AIDS"]},
    {"name": "Carlos", "surname": "Gomez", "age": 56, "gender": "Male", "weight": "88 kg", "height": "175 cm", "location": "Mexico City", "complaint": "Hepatitis B", "symptoms": ["jaundice", "fatigue"], "symptom_duration": "2 miesiące", "matched_diseases": ["Hepatitis"]},
    {"name": "Marta", "surname": "Kwiatkowska", "age": 47, "gender": "Kobieta", "weight": "65 kg", "height": "167 cm", "location": "Szczecin", "complaint": "Tropical disease (malaria)", "symptoms": ["fever", "chills", "sweating"], "symptom_duration": "1 tydzień", "matched_diseases": ["Tropical Diseases"]},
    {"name": "Yusuf", "surname": "Demir", "age": 40, "gender": "Male", "weight": "80 kg", "height": "178 cm", "location": "Istanbul", "complaint": "Parasitic infection", "symptoms": ["abdominal pain", "diarrhea"], "symptom_duration": "2 tygodnie", "matched_diseases": ["Parasitic Infections"]},
    {"name": "Natalia", "surname": "Wasilewska", "age": 34, "gender": "Kobieta", "weight": "60 kg", "height": "165 cm", "location": "Lublin", "complaint": "Collapsed lung", "symptoms": ["chest pain", "shortness of breath"], "symptom_duration": "1 dzień", "matched_diseases": ["Collapsed Lung"]},
    {"name": "Liam", "surname": "O'Connor", "age": 45, "gender": "Male", "weight": "85 kg", "height": "180 cm", "location": "Dublin", "complaint": "Dialysis access surgery", "symptoms": ["swelling", "fatigue"], "symptom_duration": "2 tygodnie", "matched_diseases": ["Dialysis Access"]},
    {"name": "Katarzyna", "surname": "Pawlak", "age": 61, "gender": "Kobieta", "weight": "72 kg", "height": "168 cm", "location": "Bydgoszcz", "complaint": "Bypass surgery", "symptoms": ["chest pain", "shortness of breath"], "symptom_duration": "3 tygodnie", "matched_diseases": ["Bypass Surgeries"]},
    {"name": "Zhang", "surname": "Wei", "age": 50, "gender": "Male", "weight": "78 kg", "height": "175 cm", "location": "Shanghai", "complaint": "Aortic aneurysm", "symptoms": ["abdominal pain", "pulsating mass"], "symptom_duration": "1 miesiąc", "matched_diseases": ["Aortic Aneurysms"]},
    {"name": "Ewa", "surname": "Sikorska", "age": 37, "gender": "Kobieta", "weight": "63 kg", "height": "160 cm", "location": "Katowice", "complaint": "Soft tissue sarcoma", "symptoms": ["growing mass under skin", "pain"], "symptom_duration": "5 miesięcy", "matched_diseases": ["Soft Tissue Sarcomas"]},
    {"name": "Mohammed", "surname": "Salah", "age": 52, "gender": "Male", "weight": "82 kg", "height": "179 cm", "location": "Cairo", "complaint": "Paraneoplastic syndrome", "symptoms": ["unexplained weight loss", "fatigue"], "symptom_duration": "3 miesiące", "matched_diseases": ["Cancer"]},
    {"name": "Helena", "surname": "Nowicka", "age": 58, "gender": "Kobieta", "weight": "70 kg", "height": "166 cm", "location": "Gdynia", "complaint": "Cushing's syndrome", "symptoms": ["weight gain", "purple striae", "hypertension"], "symptom_duration": "7 miesięcy", "matched_diseases": ["Endocrine Cancers"]},
    {"name": "Ivan", "surname": "Petrov", "age": 49, "gender": "Male", "weight": "86 kg", "height": "182 cm", "location": "St. Petersburg", "complaint": "Parathyroid tumor", "symptoms": ["bone pain", "kidney stones"], "symptom_duration": "6 miesięcy", "matched_diseases": ["Thyroid/Parathyroid Tumors"]},
    {"name": "Magdalena", "surname": "Rutkowska", "age": 43, "gender": "Kobieta", "weight": "64 kg", "height": "163 cm", "location": "Toruń", "complaint": "Liver transplant recipient", "symptoms": ["jaundice", "fatigue"], "symptom_duration": "2 lata", "matched_diseases": ["Liver Transplants"]},
    {"name": "Stefan", "surname": "Kowal", "age": 65, "gender": "Mężczyzna", "weight": "83 kg", "height": "178 cm", "location": "Rzeszów", "complaint": "Kidney transplant", "symptoms": ["swelling", "fatigue"], "symptom_duration": "1 rok", "matched_diseases": ["Kidney Transplants"]},
    {"name": "Aisha", "surname": "Abdi", "age": 38, "gender": "Female", "weight": "68 kg", "height": "165 cm", "location": "Nairobi", "complaint": "Pancreas transplant", "symptoms": ["abdominal pain", "nausea"], "symptom_duration": "4 miesiące", "matched_diseases": ["Pancreas Transplants"]},
    {"name": "Marek", "surname": "Szymański", "age": 55, "gender": "Mężczyzna", "weight": "80 kg", "height": "176 cm", "location": "Opole", "complaint": "HIV infection", "symptoms": ["weight loss", "night sweats"], "symptom_duration": "8 miesięcy", "matched_diseases": ["HIV"]},
    {"name": "Patrycja", "surname": "Wójcik", "age": 31, "gender": "Kobieta", "weight": "59 kg", "height": "161 cm", "location": "Radom", "complaint": "AIDS", "symptoms": ["recurrent infections", "weight loss"], "symptom_duration": "1,5 roku", "matched_diseases": ["AIDS"]},
    {"name": "Lucas", "surname": "Fernandez", "age": 60, "gender": "Male", "weight": "90 kg", "height": "180 cm", "location": "Buenos Aires", "complaint": "Hepatitis C", "symptoms": ["jaundice", "fatigue"], "symptom_duration": "3 miesiące", "matched_diseases": ["Hepatitis"]},
    {"name": "Zofia", "surname": "Lewandowska", "age": 50, "gender": "Kobieta", "weight": "67 kg", "height": "164 cm", "location": "Kielce", "complaint": "Malaria (tropical disease)", "symptoms": ["fever", "chills", "sweating"], "symptom_duration": "2 tygodnie", "matched_diseases": ["Tropical Diseases"]},
    {"name": "Ali", "surname": "Rahman", "age": 41, "gender": "Male", "weight": "79 kg", "height": "177 cm", "location": "Tehran", "complaint": "Parasitic infection", "symptoms": ["abdominal pain", "diarrhea"], "symptom_duration": "3 tygodnie", "matched_diseases": ["Parasitic Infections"]},

    # --- 20 Additional Patients with Previously Unmentioned Diseases ---
    {"name": "Marianna", "surname": "Kowalik", "age": 28, "gender": "Kobieta", "weight": "65 kg", "height": "167 cm", "location": "Warszawa", "complaint": "Ciąża - badania kontrolne", "symptoms": ["pregnancy symptoms", "morning sickness"], "symptom_duration": "3 miesiące", "matched_diseases": ["Pregnancy"]},
    {"name": "Isabella", "surname": "Rodriguez", "age": 32, "gender": "Female", "weight": "60 kg", "height": "165 cm", "location": "Madrid", "complaint": "Childbirth complications", "symptoms": ["severe pain", "bleeding"], "symptom_duration": "1 dzień", "matched_diseases": ["Childbirth"]},
    {"name": "Krzysztof", "surname": "Adamczyk", "age": 45, "gender": "Mężczyzna", "weight": "82 kg", "height": "178 cm", "location": "Gdańsk", "complaint": "Severe burns from accident", "symptoms": ["burns", "severe burns", "damaged skin"], "symptom_duration": "2 godziny", "matched_diseases": ["Burns"]},
    {"name": "Emma", "surname": "Taylor", "age": 22, "gender": "Female", "weight": "56 kg", "height": "163 cm", "location": "London", "complaint": "Drug overdose", "symptoms": ["seizures", "dilated pupils", "confusion"], "symptom_duration": "1 godzina", "matched_diseases": ["Poisoning/Overdose"]},
    {"name": "Jakub", "surname": "Nowicki", "age": 38, "gender": "Mężczyzna", "weight": "75 kg", "height": "175 cm", "location": "Kraków", "complaint": "Jaw fracture after accident", "symptoms": ["jaw pain", "difficulty chewing"], "symptom_duration": "3 godziny", "matched_diseases": ["Jaw Disorders"]},
    {"name": "Chen", "surname": "Li", "age": 19, "gender": "Male", "weight": "68 kg", "height": "170 cm", "location": "Beijing", "complaint": "Dental abscess", "symptoms": ["tooth pain", "swelling", "fever"], "symptom_duration": "4 dni", "matched_diseases": ["Abscesses"]},
    {"name": "Agata", "surname": "Zawadzka", "age": 54, "gender": "Kobieta", "weight": "71 kg", "height": "164 cm", "location": "Poznań", "complaint": "Gout attack", "symptoms": ["joint pain", "swelling", "redness"], "symptom_duration": "2 dni", "matched_diseases": ["Gout"]},
    {"name": "Pierre", "surname": "Martin", "age": 48, "gender": "Male", "weight": "89 kg", "height": "180 cm", "location": "Lyon", "complaint": "Varicose veins", "symptoms": ["leg pain", "visible veins", "swelling"], "symptom_duration": "6 miesięcy", "matched_diseases": ["Varicose Veins"]},
    {"name": "Beata", "surname": "Kamińska", "age": 41, "gender": "Kobieta", "weight": "63 kg", "height": "166 cm", "location": "Wrocław", "complaint": "Endometriosis", "symptoms": ["pelvic pain", "irregular periods", "heavy bleeding"], "symptom_duration": "8 miesięcy", "matched_diseases": ["Pelvic Inflammatory Disease"]},
    {"name": "Ahmed", "surname": "Omar", "age": 27, "gender": "Male", "weight": "74 kg", "height": "176 cm", "location": "Alexandria", "complaint": "Appendicitis", "symptoms": ["abdominal pain", "nausea", "fever"], "symptom_duration": "1 dzień", "matched_diseases": ["Appendicitis"]},
    {"name": "Karolina", "surname": "Lis", "age": 35, "gender": "Kobieta", "weight": "58 kg", "height": "162 cm", "location": "Łódź", "complaint": "Hair loss (alopecia)", "symptoms": ["hair loss", "bald patches"], "symptom_duration": "4 miesiące", "matched_diseases": ["Hair & Nail Disorders"]},
    {"name": "Dmitri", "surname": "Volkov", "age": 52, "gender": "Male", "weight": "85 kg", "height": "179 cm", "location": "Moscow", "complaint": "Prostate enlargement", "symptoms": ["frequent urination", "difficulty urinating"], "symptom_duration": "3 miesiące", "matched_diseases": ["Prostate Diseases"]},
    {"name": "Sofia", "surname": "Andersson", "age": 24, "gender": "Female", "weight": "55 kg", "height": "168 cm", "location": "Stockholm", "complaint": "Gallstones", "symptoms": ["abdominal pain", "nausea", "indigestion"], "symptom_duration": "2 tygodnie", "matched_diseases": ["Gallstones"]},
    {"name": "Maciej", "surname": "Wiśniewski", "age": 43, "gender": "Mężczyzna", "weight": "78 kg", "height": "174 cm", "location": "Katowice", "complaint": "Celiac disease", "symptoms": ["diarrhea", "bloating", "weight loss"], "symptom_duration": "6 miesięcy", "matched_diseases": ["Celiac disease"]},
    {"name": "Lucia", "surname": "Fernandez", "age": 37, "gender": "Female", "weight": "62 kg", "height": "161 cm", "location": "Barcelona", "complaint": "Inflammatory bowel disease", "symptoms": ["abdominal pain", "diarrhea", "blood in stool"], "symptom_duration": "3 miesiące", "matched_diseases": ["Inflammatory Bowel Disease"]},
    {"name": "Paweł", "surname": "Zieliński", "age": 59, "gender": "Mężczyzna", "weight": "81 kg", "height": "177 cm", "location": "Bydgoszcz", "complaint": "Osteoporosis", "symptoms": ["bone pain", "fractures", "height loss"], "symptom_duration": "1 rok", "matched_diseases": ["Osteoporosis"]},
    {"name": "Yuki", "surname": "Yamamoto", "age": 31, "gender": "Female", "weight": "52 kg", "height": "157 cm", "location": "Tokyo", "complaint": "Sleep apnea", "symptoms": ["snoring", "sleep interruption", "fatigue"], "symptom_duration": "5 miesięcy", "matched_diseases": ["Sleep Disorders"]},
    {"name": "Hassan", "surname": "Al-Rashid", "age": 46, "gender": "Male", "weight": "88 kg", "height": "181 cm", "location": "Dubai", "complaint": "Peripheral artery disease", "symptoms": ["leg pain", "poor circulation", "numbness"], "symptom_duration": "4 miesiące", "matched_diseases": ["Peripheral Artery Disease"]},
    {"name": "Aleksandra", "surname": "Górska", "age": 26, "gender": "Kobieta", "weight": "59 kg", "height": "169 cm", "location": "Szczecin", "complaint": "Infertility treatment", "symptoms": ["irregular periods", "difficulty conceiving"], "symptom_duration": "2 lata", "matched_diseases": ["Infertility"]},
    {"name": "Marco", "surname": "Bianchi", "age": 33, "gender": "Male", "weight": "76 kg", "height": "173 cm", "location": "Milan", "complaint": "Testicular pain", "symptoms": ["testicular pain", "swelling"], "symptom_duration": "1 tydzień", "matched_diseases": ["Testicular Conditions"]}
]

def get_patient_by_disease(disease_name):
    """Return patients that match a specific disease"""
    matching_patients = []
    for patient in PATIENT_EXAMPLES:
        if any(disease_name.lower() in disease.lower() for disease in patient["matched_diseases"]):
            matching_patients.append(patient)
    return matching_patients

def get_patient_by_symptom(symptom):
    """Return patients that have a specific symptom"""
    matching_patients = []
    for patient in PATIENT_EXAMPLES:
        if any(symptom.lower() in s.lower() for s in patient["symptoms"]):
            matching_patients.append(patient)
    return matching_patients

def display_patient(patient):
    """Display patient information in a formatted way"""
    print(f"\n--- PACJENT ---")
    print(f"Imię i nazwisko: {patient['name']} {patient['surname']}")
    print(f"Wiek: {patient['age']} lat")
    print(f"Płeć: {patient['gender']}")
    print(f"Waga: {patient['weight']}")
    print(f"Wzrost: {patient['height']}")
    print(f"Lokalizacja: {patient['location']}")
    print(f"Główna skarga: {patient['complaint']}")
    print(f"Objawy: {', '.join(patient['symptoms'])}")
    print(f"Czas trwania objawów: {patient['symptom_duration']}")
    print(f"Możliwe diagnozy: {', '.join(patient['matched_diseases'])}")
    print("-" * 50)

def display_all_patients():
    """Display all patient examples"""
    for i, patient in enumerate(PATIENT_EXAMPLES, 1):
        print(f"\nPACJENT #{i}")
        display_patient(patient)

if __name__ == "__main__":
    print("PRZYKŁADY PACJENTÓW DLA SYSTEMU DOPASOWYWANIA SZPITALI")
    print("=" * 60)
    
    # Display all patients
    display_all_patients()
    
    # Example searches
    print("\n\nPRZYKŁADY WYSZUKIWANIA:")
    print("=" * 30)
    
    print("\nPacjenci z chorobami serca:")
    heart_patients = get_patient_by_disease("Heart")
    for patient in heart_patients[:3]:  # Show first 3
        display_patient(patient)
    
    print("\nPacjenci z bólem w klatce piersiowej:")
    chest_pain_patients = get_patient_by_symptom("chest pain")
    for patient in chest_pain_patients:
        display_patient(patient)
