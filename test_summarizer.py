from summarizer import summarize_note

SAMPLE_NOTE = """
DISCHARGE SUMMARY

Patient: John D.
DOB: 03/15/1958
Admission Date: 04/10/2026
Discharge Date: 04/14/2026
Attending Physician: Dr. Sarah Mitchell, MD
Primary Service: Internal Medicine

CHIEF COMPLAINT:
Chest pain and shortness of breath x 2 days

HISTORY OF PRESENT ILLNESS:
68-year-old male with PMH significant for HTN, T2DM, and HLD who presented
to the ED with 2 days of progressively worsening chest pain radiating to
the left arm, associated with diaphoresis and dyspnea on exertion. Initial
EKG showed ST depression in leads V4-V6. Troponin I peaked at 2.8 ng/mL.
Patient was started on heparin drip and taken for urgent cardiac
catheterization which revealed 85% stenosis of the LAD. Drug eluting stent
placed without complication. Post-procedure course unremarkable.

PAST MEDICAL HISTORY:
1. Hypertension - on lisinopril 10mg daily
2. Type 2 Diabetes Mellitus - on metformin 1000mg BID
3. Hyperlipidemia - on atorvastatin 40mg daily
4. Former smoker - quit 2015

HOSPITAL COURSE:
Patient admitted to cardiac ICU post-catheterization. Monitored for 48
hours without arrhythmia. Echo showed EF of 45%. Started on dual
antiplatelet therapy with aspirin 81mg and clopidogrel 75mg daily.
Lisinopril dose increased to 20mg for cardiac remodeling. Diabetes well
controlled during admission. Transferred to step-down unit on HD2.
Ambulating independently by HD3. Discharged home in stable condition.

DISCHARGE DIAGNOSES:
1. Non-ST elevation myocardial infarction (NSTEMI)
2. Coronary artery disease - single vessel, LAD
3. Hypertension
4. Type 2 Diabetes Mellitus
5. Hyperlipidemia

DISCHARGE MEDICATIONS:
1. Aspirin 81mg daily - NEW
2. Clopidogrel 75mg daily - NEW
3. Lisinopril 20mg daily - DOSE CHANGED from 10mg
4. Metformin 1000mg twice daily - CONTINUED
5. Atorvastatin 40mg daily - CONTINUED
6. Nitroglycerin 0.4mg SL PRN chest pain - NEW

FOLLOW UP:
1. Cardiology with Dr. Mitchell in 1 week
2. Primary Care in 2 weeks
3. Cardiac rehab referral placed
4. Repeat echo in 6 weeks

DIET: Low sodium, cardiac diet
ACTIVITY: No heavy lifting for 2 weeks. Walk 10-15 minutes daily.

Electronically signed: Dr. Sarah Mitchell, MD
04/14/2026 14:32
"""

if __name__ == "__main__":
    print("Summarizing discharge note...\n")
    result = summarize_note(SAMPLE_NOTE)

    print(f"Chief Complaint:     {result.chief_complaint}")
    print(f"Primary Diagnosis:   {result.primary_diagnosis}")
    print(f"Hospital Days:       {result.hospital_days}")
    print(f"Discharge Condition: {result.discharge_condition}")
    print(f"\nAll Diagnoses:")
    for d in result.all_diagnoses:
        print(f"  - {d}")
    print(f"\nDischarge Medications:")
    for m in result.discharge_medications:
        print(f"  - {m}")
    print(f"\nNew Medications:")
    for m in result.new_medications:
        print(f"  - {m}")
    print(f"\nChanged Medications:")
    for m in result.changed_medications:
        print(f"  - {m}")
    print(f"\nFollow Up:")
    for f in result.follow_up:
        print(f"  - {f}")
    print(f"\nClinical Summary:")
    print(f"  {result.clinical_summary}")