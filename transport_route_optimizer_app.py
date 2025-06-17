import streamlit as st

# Diesel Cost Calculator
st.set_page_config(page_title="Diesel Cost Calculator", page_icon="⛽")
st.title("⛽ Diesel Cost & Usage Manager")

# Section: Calculate consumption rate or input directly
mode = st.radio("Fuel consumption mode:", ["Calculate rate from usage", "Enter rate directly"], index=0)

if mode == "Calculate rate from usage":
    ... # existing diesel section
# Reminders for vehicle documents
st.header("📅 Vehicle Document Expiry Reminders")
with st.form("doc_reminders_form"):
    vehicle_id = st.text_input("Vehicle ID (e.g. DMM-01)")
    insp_date = st.date_input("Inspection expiry date")
    reg_date = st.date_input("Registration expiry date")
    op_date = st.date_input("Operating card expiry date")
    btn = st.form_submit_button("Schedule Document Reminders")
if btn and vehicle_id:
    # Reminder one month before each expiry
    for doc_name, expiry in [("Inspection", insp_date), ("Registration", reg_date), ("Operating Card", op_date)]:
        # Title and prompt for automation
        title = f"Remind {doc_name} for {vehicle_id}"
        prompt = f"Tell me to remind that vehicle {vehicle_id} {doc_name.lower()} expires on {expiry}."
        # Schedule one month prior
        reminder_date = expiry - pd.DateOffset(months=1)
        dt = reminder_date.strftime("%Y%m%dT090000")
        schedule = (
            "BEGIN:VEVENT
"
            f"DTSTART:{dt}
"
            "END:VEVENT"
        )
        automations.create(title=title, prompt=prompt, schedule=schedule)
    st.success("✅ Document reminders scheduled via email!")
else:
    st.info("Fill in all fields to schedule reminders.")
