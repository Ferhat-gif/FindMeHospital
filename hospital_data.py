# Fuzzy matching
from fuzzywuzzy import fuzz
# Example hospital data for matching diseases to hospitals
HOSPITALS = [
    {
        "name": "Hospital Bielański Warszawa",
        "website": "https://www.bielanski.med.pl/",
        "diseases": [
            "Hypothyroidism", "Hyperthyroidism", "Thyroid nodules", "Thyroid cancer", "Thyroid Eye Disease",
            "Bone Disorders", "Heart Conditions", "Kidney Diseases", "Lung Diseases", "tumors", "monitor diseases"
        ]
    },
    {
        "name": "Hospital Czerniakowski Warszawa",
        "website": "https://www.szpitalczerniakowski.waw.pl/",
        "diseases": [
            "Digestive System Cancers", "Breast Cancers", "Endocrine Cancers", "Soft Tissue Cancers", "Skin Cancers",
            "Gastrointestinal Disorders", "Acute Abdominal Emergencies", "Benign Tumors", "Cysts"
        ]
    }
]

# Symptom-to-disease mapping
SYMPTOM_TO_DISEASE = {
    "acid reflux": "Gastrointestinal Disorders",
    "heartburn": "Gastrointestinal Disorders",
    "nausea": "Gastrointestinal Disorders",
    "vomiting": "Gastrointestinal Disorders",
    "vomitting": "Gastrointestinal Disorders",  # Common misspelling
    "vomit": "Gastrointestinal Disorders",
    "throw up": "Gastrointestinal Disorders",
    "stomach pain": "Gastrointestinal Disorders",
    "stomach ache": "Gastrointestinal Disorders",
    "shortness of breath": "Heart Conditions",
    "chest pain": "Heart Conditions",
    "rapid heartbeat": "Heart Conditions",
    "fatigue": "Heart Conditions",
    "bone pain": "Bone Disorders",
    "joint pain": "Bone Disorders",
    "muscle pain": "Bone Disorders",
    "muscle pains": "Bone Disorders",
    "muscle ache": "Bone Disorders",
    "muscle aches": "Bone Disorders",
    "sore muscles": "Bone Disorders",
    "cough": "Lung Diseases",
    "wheezing": "Lung Diseases"
}

def find_hospitals_for_disease(disease):
    matches = []
    disease_lower = disease.lower()
    
    # Fuzzy symptom-to-disease mapping
    mapped_diseases = []
    for symptom, mapped_disease in SYMPTOM_TO_DISEASE.items():
        if fuzz.partial_ratio(symptom, disease_lower) > 80 or fuzz.partial_ratio(disease_lower, symptom) > 80:
            mapped_diseases.append(mapped_disease)

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
