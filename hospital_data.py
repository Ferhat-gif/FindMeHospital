# Fuzzy matching
from fuzzywuzzy import fuzz
# Example hospital data for matching diseases to hospitals
HOSPITALS = [
    {
        "name": "Hospital Bielański Warszawa",
        "website": "https://www.bielanski.med.pl/",
        "diseases": [
            "Hypothyroidism", "Hyperthyroidism", "Thyroid nodules", "Thyroid cancer", "Thyroid Eye Disease",
            "Bone Disorders", "Heart Conditions", "Kidney Diseases", "Lung Diseases", "Tumors", "monitor diseases",
            "Autoimmune & Inflammatory Disorders","Genetic & Metabolic Disorders", "Blood Disorders","Fractures", "internal bleeding",
            "Cancer", "Strokes", "aneurysms", "spinal cord injuries", "Blocked arteries", "aortic aneurysms"," Pneumonia"," COPD", " pulmonary embolism",
            "Gallstones", "appendicitis", "kidney stones","Arthritis", "osteoporosis", "torn ligaments","Back/neck pain", "Arthritis","Post-fracture rehabilitation",
            "torn ligaments", "muscle strains", "motor function re-education", "Multiple sclerosis (MS)", "Parkinson's disease","Spinal cord injuries","Joint replacements ",
            "Post-cardiac surgery ", "Recovery from orthopedic surgeries", "Patients requiring blood transfusions","unexplained anemia or jaundice ","Transplant recipients/donors",
            "acid reflux", "Strictures or tumors", "Gastritis", "ulcers", "Stomach cancer", "Inflammatory Bowel Disease", "Colon polyps/cancer", "Celiac disease", "Liver Diseases", 
            "Lung Cancer"
        ]
    },
    {
        "name": "Hospital Czerniakowski Warszawa",
        "website": "https://www.szpitalczerniakowski.waw.pl/",
        "diseases": [
            "Digestive System Cancers", "Breast Cancers", "Endocrine Cancers", "Soft Tissue Cancers", "Skin Cancers",
            "Gastrointestinal Disorders", "Acute Abdominal Emergencies", "Benign Tumors", "Cysts","Diabetes", "Adrenal Disorders", "Tumors", "Bone Diseases","Kidney Diseases",
            "Obesity", "Hypertension", "Complex multisystem diseases", "Fractures", "Dislocations", "Severe injuries", "Orthopedic Surgery", "Bone infections", "Ear Disorders",
            "Nose & Sinus Conditions", "Throat & Voice Disorders", "Head & Neck Surgery", "Pediatric ENT", "Refractive Errors", "Eye Diseases & Infections", "Retinal Disorders",
            "Pediatric & Congenital Issues", "Trauma & Emergencies", "Brain Disorders", "Spinal Cord & Nerve Disorders", "Muscle & Neuromuscular Diseases", "Infections & Inflammation",
            "Movement Disorders"

        ]
    },
    {"name": "Uniwersyteckie Centrum Kliniczne, Gdansk",
        "website": "https://uck.pl/",
        "diseases": [
            "Coronary Artery Disease", "Heart Failure", "Heart Diseases", "Cardiomyopathies", "Inflammatory/Infectious Conditions","Allergic Rhinitis", "Atopic Dermatitis",
            "Food Allergies", "Drug Allergies ", "Contact Dermatitis ", "Chronic Urticaria", "Insect Venom Allergies", "Anaphylaxis", "Acute Respiratory Failure", "Sepsis & Septic Shock",
            "Post-Surgical Critical Care ", "Trauma Care", "Organ Failure ", "Poisoning/Overdose ", "Burns", "Neurological Emergencies ", "Lung Cancer", "Pleural Diseases", "Chest Trauma",
            "Diaphragm Hernias ", "Hyperhidrosis", "Tuberculosis", "lung abscesses","Aortic Aneurysms", "Dialysis Access", "Breast Cancer", "Thyroid/Parathyroid Tumors", "Liver Transplants",
            "Kidney Transplants", "Pancreas Transplants", "Appendicitis", "Soft Tissue Sarcomas"
]
    },
    {
        "name": "Copernicus Hospital, Gdansk",
        "website": "https://copernicus.gda.pl/",
        "diseases": ["Acute Respiratory Failure","Sepsis & Septic Shock", "Post-Surgical Critical Care", "Trauma Care", "Organ Failure", "Poisoning/Overdose", "Burns", "Neurological Emergencies", "Lung Cancer", "Fractures","Dislocations",
                 "Severe injuries", "Orthopedic Surgery", "Bone infections", "Tumors","Diabetes","Obesity", "Hypertension", "Complex multisystem diseases","Genetic & Metabolic Disorders","Eczema","Acne",
                 "Skin Cancer", "Hair & Nail Disorders", "Acid reflux", "Gastritis", "ulcers", "Stomach cancer" ,"Coronary Artery Disease", "Heart Failure", "Heart Diseases", "Cardiomyopathies",
                 "Vascular Diseases", "Inflammatory/Infectious Conditions","Low Birth Weight", "Infant Feeding difficulties","Brain Disorders", "Spinal Cord & Nerve Disorders", "Muscle & Neuromuscular Diseases", "Infections & Inflammation",
                 "Movement Disorders"
                 ]
     },
     {"name": "Uniwersytet Szpital Kliniczny, Olsztyn",
      "website":"https://szpital.uwm.edu.pl/",
      "diseases": ["Obesity","Gout","Genetic & Metabolic Disorders", "Hypertension","Complex multisystem diseases", "Diabetes","Asthma","Heart Failure",
                   "Coronary Artery Disease", "ulcers", "Thyroid Eye Disease","Kidney Diseases", "Anemia", "Clotting Disorders", "Bleeding Disorders",
                   "Facial Fracture", "Facial Trauma", "Dental Abnormalities", "Jaw Disorders", "Infections", "Abscesses", "Cosmetic Surgery","Reconstructive Surgery",
                    "Ear Disorders", "Nose & Sinus Conditions", "Throat & Voice Disorders", "Head & Neck Surgery","Breast Cancer", "Gastrointestinal Cancers",
                    "Thyroid/Parathyroid Tumors","Soft Tissue Sarcomas", "Liver Transplants", "Kidney Transplants", "Pancreas Transplants","Appendicitis",
                    "Prostate Diseases", "Testicular Conditions", "Acute Respiratory Failure", "Sepsis & Septic Shock", "Post-Surgical Critical Care", "Trauma Care",
                    "Organ Failure", "Poisoning/Overdose", "Burns", "Neurological Emergencies"
                     
                      ]

     },
        {"name": "Szpital Wojewódzki, Olsztyn",
        "website":"https://www.szpital.olsztyn.pl/",
        "diseases": ["Pregnancy", "Childbirth", "Menstrual Irregularities","Pelvic Inflammatory Disease", "Pelvic Organ Prolapse","Gynecologic Oncology","Infertility",
                     "Hormone Therapy", "Minimally Invasive Surgery","Eczema", "Acne", "Skin Cancer", "Hair & Nail Disorders", "Infections", "Coronary Artery Disease",
                     "Heart Failure", "Heart Diseases", "Cardiomyopathies", "Vascular Diseases", "Inflammatory/Infectious Conditions","Joint Damage","Morning Stiffness",
                     "Butterfly Rash", "Spinal Inflammation", "Tissue Diseases", "Bone Disorders","Ear Disorders", "Nose & Sinus Conditions", "Throat & Voice Disorders",
                     "Head & Neck", "Refractive Errors", "Eye Diseases & Infections", "Retinal Disorders", "Facial Fracture", "Facial Trauma", "Dental Abnormalities",
                     "Jaw Disorders", "Infections", "Abscesses", "Cosmetic Surgery"
                        ]
        },
        {"name": "Uniwersytecki Szpital Kliniczny, Białystok",
         "website":"https://uskwb.pl/",
         "diseases": ["Depression", "Anxiety Disorders", "Bipolar Disorder", "Schizophrenia", "Personality Disorders","ADHD", "Addiction", "Sleep Disorders", 
                      "Eating Disorders", "Post-Traumatic Stress Disorder (PTSD)", "Orthopedic Disorders", "Fractures", "Dislocations", "Hand & Wrist Conditions",
                      "Spinal Disorders","Sport Injuries","Pregnancy", "Fetal Medicine", "Prematurity Care", "Critical Newborn Conditions", "Vascular Diseases",
                      "Kidney Transplants", "Liver Transplants", "Pancreas Transplants", "Dialysis Access", "Bypass Surgeries", "Lung Cancer","Collapsed Lung", 
                      "Pleural Diseases", "Tumors", "Cysts","Blood Disorders", "Anemia", "Clotting Disorders", "Bleeding Disorders","Lymphatic Disorders",
                      "Diabetes", "Aortic Aneurysms", "Arterial Diseases", "Venous Diseases", "Peripheral Artery Disease", "Varicose Veins", "Heart Conditions",
                      "Coronary Artery Disease", "Heart Failure", "Cardiomyopathies", "Inflammatory/Infectious Conditions"
                      ]
         },
         {"name": "Centralny Szpital Kliniczny Uniwersytetu Medycznego, Łódź",
          "website": "https://csk.umed.pl/",
          "diseases": ["Eating Disorders", "Childbirth","Asthma", "Diabetes", "Epilepsy", "ADHD", "Autism","Eczema", "Food Allergies", "Morning Stiffness",
                       "Butterfly Rash", "Autoimmune Disorders", "Spinal Disorders", "Ear Disorders", "Nose & Sinus Conditions", "Throat & Voice Disorders",
                       "Sleep Disorders", "Tuberculosis", "Lung Diseases", "Apnea","Refractive Errors", "Eye Diseases & Infections", "Retinal Disorders",
                       "Acute Respiratory Failure", "Sepsis & Septic Shock", "Post-Surgical Critical Care", "Trauma Care", "Organ Failure", "Poisoning/Overdose",
                       "Burns", "Neurological Emergencies", "Lung Cancer", "Pleural Diseases", "Chest Trauma", "Diaphragm Hernias", "Hypothyroidism", "Hyperthyroidism",
                       "Thyroid nodules", "Thyroid cancer", "Thyroid Eye Disease", "Bone Disorders", "Heart Conditions", "Kidney Diseases", "Lung Diseases","Back/neck pain",
                       "Fractures", "Arthritis", "Sport Injuries", "Stroke", "Post-fracture rehabilitation", "torn ligaments", "muscle strains", "motor function re-education",

              

          ]},
          {"name": "Szpital Jana Pawla II, Kraków",
           "website": "https://www.szpitaljp2.krakow.pl/",
           "diseases": ["Bypass Surgeries", "Coronary Artery Disease", "Heart Failure", "Heart Diseases", "Vascular Diseases", "Cardiomyopathies", "Inflammatory/Infectious Conditions",
                        "Lung Transplants", "Liver Diseases", "Brain Disorders", "Spinal Cord & Nerve Disorders", "Muscle & Neuromuscular Diseases", "Movement Disorders", "Back/neck pain",
                        "Fractures", "Dislocations", "Severe injuries", "Orthopedic Surgery", "Bone infections","Acute Respiratory Failure", "Sepsis & Septic Shock", "Post-Surgical Critical Care", 
                        "Trauma Care", "Organ Failure", "Poisoning/Overdose", "Burns", "Aortic Aneurysms", "Dialysis Access", "Covid-19", "HIV", "AIDS", "Hepatitis", "Tuberculosis",
                        "Bacterial Infections", "Tropical Diseases", "Parasitic Infections"

           
           ]

           },
           {"name": "Wojewódzki Szpital Specjalistyczny im. J. Gromkowskiego",
            "website": "https://www.szpital.wroc.pl/",
            "diseases": [ "Covid-19", "HIV", "AIDS", "Hepatitis", "Tuberculosis", "Bacterial Infections", "Tropical Diseases", "Parasitic Infections", "Brain Disorders", "Spinal Cord & Nerve Disorders",
                           "Muscle & Neuromuscular Diseases", "Movement Disorders", "Infections & Inflammation", "Acute Respiratory Failure","Sepsis & Septic Shock", "Post-Surgical Critical Care", 
                           "Trauma Care", "Organ Failure", "Poisoning/Overdose", "Burns", "Neurological Emergencies","Digestive System Cancers", "Breast Cancers", "Endocrine Cancers", "Soft Tissue Cancers", 
                           "Skin Cancers", "Diabetes",  "Hypothyroidism", "Hyperthyroidism", "Thyroid nodules", "Thyroid cancer", "Thyroid Eye Disease", "Tumors", "Bone Diseases", "Kidney Diseases", "Gout",
                           "Metabolic Disorders", "Liver Diseases", "Back/neck pain", "Arthritis","Post-fracture rehabilitation","Fractures", "Dislocations", "Severe injuries", "Orthopedic Surgery",
                           "Hypothyroidism", "Hyperthyroidism", "Thyroid nodules", "Thyroid cancer", "Thyroid Eye Disease"

                        ]

           }
        
        ]

# Symptom-to-disease mapping
SYMPTOM_TO_DISEASE = {
    "heartburn": "Gastrointestinal Disorders",
    "nausea": "Gastrointestinal Disorders",
    "vomiting": ["Gastrointestinal Disorders","Food Allergies"],
    "vomitting": "Gastrointestinal Disorders",  # Common misspelling
    "vomit": "Gastrointestinal Disorders",
    "throw up": "Gastrointestinal Disorders",
    "stomach pain": "Gastrointestinal Disorders",
    "stomach ache": "Gastrointestinal Disorders",
    "rapid heartbeat": ["Heart Conditions", "Sepsis & Septic Shock"],
    "fast heartbeat": ["Heart Conditions", "Sepsis & Septic Shock"],  
    "bone pain": "Bone Disorders",
    "joint pain": ["Bone Disorders","Arthritis"],
    "muscle pain": "Bone Disorders",
    "muscle pains": "Bone Disorders",
    "muscle ache": "Bone Disorders",
    "muscle aches": "Bone Disorders",
    "sore muscles": "Bone Disorders",
    "cough": ["Lung Diseases","Lung Cancer"],
    "coughing": ["Lung Diseases","Lung Cancer"],  
    "wheezing": "Lung Diseases",
    "Leukemia": "Blood Disorders",
    "Anemia": "Blood Disorders",
    "lymphoma": "Blood Disorders",
    "overweight": "Obesity",
    "obese": "Obesity",
    "high blood pressure": "Hypertension",
    "high cholesterol": "Hypertension",
    "broken bone": "Fractures",
    "fractured bone": "Fractures",
    "back pain": "Back/neck pain",
    "neck pain": "Back/neck pain",
    "tightness in chest": "Coronary Artery Disease",
    "pressure in chest": "Coronary Artery Disease",
    "poor blood flow": "Coronary Artery Disease",
    "unexplained exhaustion": "Coronary Artery Disease",
    
    # Examples of symptoms that can indicate multiple diseases
    "shortness of breath": ["Heart Conditions", "Heart Failure", "Lung Diseases", "Cardiomyopathies","Trauma Care","Lung Cancer","Pleural Diseases","Chest Trauma"],
    "difficulty breathing": ["Heart Conditions", "Heart Failure", "Lung Diseases", "Cardiomyopathies","Trauma Care", "Pleural Diseases","Chest Trauma"],
    "chest pain": ["Heart Conditions", "Coronary Artery Disease", "Lung Diseases"],
    "fatigue": ["Heart Conditions", "Blood Disorders", "Anemia","Cardiomyopathies"],
    "swelling in legs": "Cardiomyopathies",
    "Fever & Chills ": "Inflammatory/Infectious Conditions",
    "Sneezing": "Allergic Rhinitis",
    "Itchy Eyes": "Allergic Rhinitis",
    "Itchy Nose": "Allergic Rhinitis",
    "Itchy Throat": "Allergic Rhinitis",
    "Runny Nose": "Allergic Rhinitis",
    "Blocked Nose": "Allergic Rhinitis",
    "Intense Itching": "Atopic Dermatitis",
    "Dry,red patchy skin": "Atopic Dermatitis",
    "Oozing sores": "Atopic Dermatitis",
    "Crusting skin": "Atopic Dermatitis",
    "Hive skin": ["Food Allergies","Drug Allergies"],
    "Swelling": ["Food Allergies","Contact Dermatitis","Insect Venom Allergies","Anaphylaxis","Organ Failure"],
    "abdominal pain": ["Food Allergies","Diaphragm Hernias"],
    "difficulty breathing": "Food Allergies",
    "Rash": "Drug Allergies",
    "sudden wheezing": "Drug Allergies",
    "drop in blood pressure": ["Drug Allergies","Anaphylaxis"],
    "loss of consciousness": "Drug Allergies",
    "Red rash": "Contact Dermatitis",
    "Blistering skin": "Contact Dermatitis",
    "Dry skin": "Contact Dermatitis",
    "Cracked skin": "Contact Dermatitis",
    "Raised, Itchy Welts": "Chronic Urticaria",
    "swelling lips": "Chronic Urticaria",
    "swelling eyelids": "Chronic Urticaria",
    "swelling hands": "Chronic Urticaria",
    "hives": "Insect Venom Allergies",
    "throat swelling": "Insect Venom Allergies",
    "Dizziness": "Insect Venom Allergies",
    "Bee Stings": "Insect Venom Allergies",
    "Wasp Stings": "Insect Venom Allergies",
    "Difficulty Breathing": "Anaphylaxis",
    "Bluish skin":"Acute Respiratory Failure",
    "Bluish lips": "Acute Respiratory Failure",
    "Urine output reduction": "Sepsis & Septic Shock",
    "Pale or cold skin": ["Sepsis & Septic Shock","Chest Trauma"],
    "confusion": ["Sepsis & Septic Shock","Trauma Care","Organ Failure"],
    "disorientation": ["Sepsis & Septic Shock","Trauma Care"],
    "Bleeding/swelling at the surgical site": "Post-Surgical Critical Care",
    "No urine output": "Kidney Diseases",
    "Altered Mental Status": "Post-Surgical Critical Care",
    "Uncontrolled Pain": "Post-Surgical Critical Care",
    "Uncontrolled Bleeding": ["Post-Surgical Critical Care","Trauma Care"],
    "Irregular Pulse": ["Organ Failure", "Post-Surgical Critical Care"],
    "yellowing of skin/eyes": "Organ Failure",
    "Seizures": ["Organ Failure","poisoning/overdose"],
    "Dilated pupils": ["Organ Failure","poisoning/overdose","Neurological Emergencies"],
    "snake bites": "poisoning/overdose",
    "chemical exposure": "poisoning/overdose",
    "burns": "Burns",
    "severe burns": "Burns",
    "damaged skin": "Burns",
    "burned skin": "Burns",
    "Sudden Severe Headache": "Neurological Emergencies",
    "Stroke Signs ": "Neurological Emergencies",
    "Unexplained Weight Loss": ["Lung Cancer","Tuberculosis"],
    "persistent cough": "Lung Cancer",
    "fever": ["Lung Cancer","Pleural Diseases","Tuberculosis"],
    "weak pulse": ["Pleural Diseases","Chest Trauma"],
    "Heartburn" :"Diaphragm Hernias",
    "rapid breathing": ["Pleural Diseases","Diaphragm Hernias"],
    "uncontrollable sweating": "Hyperhidrosis",
    "white skin": "Hyperhidrosis",
    "intereference with daily activities": "Hyperhidrosis",
    "night sweats": ["Hyperhidrosis","Tuberculosis"],
    "Neck Lump/Nodule": ["Thyroid Disorders","Thyroid Cancer"],
    "Voice Changes/Hoarseness":["Thyroid Disorders","Thyroid Cancer"],
    "Swollen Lymph Nodes":["Thyroid Disorders","Thyroid Cancer"],
    "Myopia": "Eye Disorders",
    "astigmatic":"Eye Disorders",
    "hypermetropia":"Eye Disorders",
    "Yellow skin": "Liver Diseases",
    "Bug bites":"Poisoning/Overdose",
    "Eating Problems": "Eating Disorders",
    "Restricted Mobility":"Movement Disorders",
    "Growing mass under skin": "Soft Tissue Cancer",
    "Can't sleep at night": "Sleep Disorders",
    "Airway Obstruction": "Trauma Care",
    "Head Injury": "Trauma Care",
    
    # Mental Health Symptoms
    "depression": "Depression",
    "sadness": "Depression",
    "hopelessness": "Depression",
    "anxiety": "Anxiety Disorders",
    "panic attacks": "Anxiety Disorders",
    "panic": "Anxiety Disorders",
    "worry": "Anxiety Disorders",
    "mood swings": "Bipolar Disorder",
    "mania": "Bipolar Disorder",
    "hearing voices": "Schizophrenia",
    "hallucinations": "Schizophrenia",
    "delusions": "Schizophrenia",
    "paranoia": "Schizophrenia",
    "hyperactivity": "ADHD",
    "attention problems": "ADHD",
    "can't focus": "ADHD",
    "concentration problems": "ADHD",
    "substance abuse": "Addiction",
    "drug addiction": "Addiction",
    "alcohol addiction": "Addiction",
    "insomnia": "Sleep Disorders",
    "can't fall asleep": "Sleep Disorders",
    "nightmares": ["Sleep Disorders", "Post-Traumatic Stress Disorder (PTSD)"],
    "flashbacks": "Post-Traumatic Stress Disorder (PTSD)",
    "traumatic memories": "Post-Traumatic Stress Disorder (PTSD)",
    "loss of appetite": "Eating Disorders",
    "overeating": "Eating Disorders",
    "bulimia": "Eating Disorders",
    "anorexia": "Eating Disorders",
    
    # Neurological Symptoms
    "headache": ["Brain Disorders", "Neurological Emergencies"],
    "severe headache": "Neurological Emergencies",
    "migraine": "Brain Disorders",
    "dizziness": ["Brain Disorders", "Neurological Emergencies"],
    "vertigo": "Brain Disorders",
    "memory loss": "Brain Disorders",
    "forgetfulness": "Brain Disorders",
    "tremors": ["Movement Disorders", "Parkinson's disease"],
    "shaking": ["Movement Disorders", "Parkinson's disease"],
    "numbness": "Spinal Cord & Nerve Disorders",
    "tingling": "Spinal Cord & Nerve Disorders",
    "weakness": ["Spinal Cord & Nerve Disorders", "Muscle & Neuromuscular Diseases"],
    "paralysis": "Spinal Cord & Nerve Disorders",
    "balance problems": "Movement Disorders",
    "coordination problems": "Movement Disorders",
    "speech problems": ["Brain Disorders", "Stroke"],
    "slurred speech": ["Brain Disorders", "Stroke"],
    
    # Diabetes and Endocrine Symptoms
    "frequent urination": "Diabetes",
    "excessive thirst": "Diabetes",
    "blurred vision": ["Diabetes", "Eye Diseases & Infections"],
    "weight loss": ["Diabetes", "Hyperthyroidism"],
    "weight gain": ["Hypothyroidism", "Obesity"],
    "cold intolerance": "Hypothyroidism",
    "heat intolerance": "Hyperthyroidism",
    "hair loss": ["Hypothyroidism", "Hair & Nail Disorders"],
    "brittle nails": "Hair & Nail Disorders",
    
    # Skin Conditions
    "itchy skin": ["Eczema", "Atopic Dermatitis", "Skin Cancer"],
    "skin rash": ["Eczema", "Contact Dermatitis", "Drug Allergies"],
    "red skin": ["Eczema", "Contact Dermatitis"],
    "scaly skin": "Eczema",
    "pimples": "Acne",
    "blackheads": "Acne",
    "skin bumps": "Acne",
    "moles": "Skin Cancer",
    "skin lesions": "Skin Cancer",
    "unusual moles": "Skin Cancer",
    
    # Eye and Vision Problems
    "eye pain": "Eye Diseases & Infections",
    "red eyes": "Eye Diseases & Infections",
    "itchy eyes": ["Eye Diseases & Infections", "Allergic Rhinitis"],
    "watery eyes": ["Eye Diseases & Infections", "Allergic Rhinitis"],
    "double vision": "Eye Diseases & Infections",
    "vision loss": ["Eye Diseases & Infections", "Retinal Disorders"],
    "night blindness": "Retinal Disorders",
    "flashing lights": "Retinal Disorders",
    "floaters": "Retinal Disorders",
    
    # Ear and Hearing Problems
    "ear pain": "Ear Disorders",
    "hearing loss": "Ear Disorders",
    "ear infection": "Ear Disorders",
    "ringing in ears": "Ear Disorders",
    "tinnitus": "Ear Disorders",
    "ear discharge": "Ear Disorders",
    
    # Respiratory Symptoms
    "asthma": "Asthma",
    "breathing problems": ["Asthma", "Lung Diseases"],
    "wheezing": ["Asthma", "Lung Diseases"],
    "chronic cough": ["Lung Diseases", "Tuberculosis"],
    "coughing blood": ["Lung Cancer", "Tuberculosis"],
    "sore throat": "Throat & Voice Disorders",
    "voice hoarseness": "Throat & Voice Disorders",
    "snoring": "Sleep Disorders",
    "sleep apnea": "Sleep Disorders",
    
    # Cardiovascular Symptoms
    "palpitations": "Heart Conditions",
    "irregular heartbeat": "Heart Conditions",
    "heart palpitations": "Heart Conditions",
    "swollen ankles": ["Heart Failure", "Kidney Diseases"],
    "leg swelling": ["Heart Failure", "Vascular Diseases"],
    "high heart rate": "Heart Conditions",
    "low blood pressure": "Heart Conditions",
    "blood clots": "Vascular Diseases",
    "varicose veins": "Varicose Veins",
    
    # Gastrointestinal Symptoms
    "diarrhea": "Gastrointestinal Disorders",
    "constipation": "Gastrointestinal Disorders",
    "bloating": "Gastrointestinal Disorders",
    "gas": "Gastrointestinal Disorders",
    "indigestion": "Gastrointestinal Disorders",
    "acid reflux": "Gastrointestinal Disorders",
    "blood in stool": ["Gastrointestinal Disorders", "Colon polyps/cancer"],
    "black stool": "Gastrointestinal Disorders",
    "yellow stool": "Liver Diseases",
    "pale stool": "Liver Diseases",
    
    # Kidney and Urinary Symptoms
    "blood in urine": "Kidney Diseases",
    "painful urination": "Kidney Diseases",
    "kidney pain": "Kidney Diseases",
    "kidney stones": "Kidney Diseases",
    "urinary incontinence": "Kidney Diseases",
    "dark urine": "Kidney Diseases",
    "foamy urine": "Kidney Diseases",
    
    # Bone and Joint Symptoms
    "arthritis": "Arthritis",
    "joint swelling": "Arthritis",
    "morning stiffness": "Arthritis",
    "hip pain": ["Arthritis", "Fractures"],
    "knee pain": ["Arthritis", "Fractures"],
    "shoulder pain": ["Arthritis", "Fractures"],
    "osteoporosis": "Bone Disorders",
    "bone fractures": "Fractures",
    "sports injury": "Sport Injuries",
    "sprained ankle": "Sport Injuries",
    "torn muscle": "Sport Injuries",
    
    # Women's Health Symptoms
    "irregular periods": "Menstrual Irregularities",
    "heavy bleeding": "Menstrual Irregularities",
    "missed periods": ["Menstrual Irregularities", "Pregnancy"],
    "pelvic pain": "Pelvic Inflammatory Disease",
    "pregnancy symptoms": "Pregnancy",
    "morning sickness": "Pregnancy",
    "breast lumps": "Breast Cancer",
    "breast pain": "Breast Cancer",
    
    # Infectious Disease Symptoms
    "covid symptoms": "Covid-19",
    "loss of taste": "Covid-19",
    "loss of smell": "Covid-19",
    "flu symptoms": "Bacterial Infections",
    "high fever": ["Bacterial Infections", "Tuberculosis"],
    "chills": "Bacterial Infections",
    "body aches": "Bacterial Infections",
    "swollen glands": "Bacterial Infections",
    "rash with fever": "Tropical Diseases",
    
    # Cancer-related Symptoms
    "unexplained lumps": ["Breast Cancer", "Soft Tissue Cancer"],
    "persistent pain": "Cancer",
    "unusual bleeding": ["Cancer", "Gynecologic Oncology"],
    "changes in moles": "Skin Cancer",
    "difficulty swallowing": ["Throat & Voice Disorders", "Cancer"],
    
    # Emergency Symptoms
    "severe bleeding": "Trauma Care",
    "unconsciousness": ["Trauma Care", "Neurological Emergencies"],
    "severe injury": "Trauma Care",
    "car accident": "Trauma Care",
    "fall injury": "Trauma Care",
    "broken bones": "Fractures",
    "dislocated joint": "Dislocations",
    "emergency": "Trauma Care"

}

def find_hospitals_for_disease(disease):
    matches = []
    disease_lower = disease.lower()
    
    # Fuzzy symptom-to-disease mapping
    mapped_diseases = []
    for symptom, mapped_disease in SYMPTOM_TO_DISEASE.items():
        if fuzz.partial_ratio(symptom, disease_lower) > 80 or fuzz.partial_ratio(disease_lower, symptom) > 80:
            # Handle both single diseases (strings) and multiple diseases (lists)
            if isinstance(mapped_disease, list):
                mapped_diseases.extend(mapped_disease)  # Add all diseases from the list
            else:
                mapped_diseases.append(mapped_disease)  # Add single disease

    # Add mapped diseases to the search
    all_search_terms = [disease_lower] + [d.lower() for d in mapped_diseases]

    for hospital in HOSPITALS:
        for search_term in all_search_terms:
            for d in hospital["diseases"]:
                # Fuzzy match for hospital diseases
                if (
                    search_term in d.lower() or d.lower() in search_term or
                    fuzz.partial_ratio(search_term, d.lower()) > 80 or fuzz.partial_ratio(d.lower(), search_term) > 80
                ):
                    if hospital not in matches:  # Avoid duplicates
                        matches.append(hospital)
                    break
            if hospital in matches:  # Break outer loop if already matched
                break
    return matches
