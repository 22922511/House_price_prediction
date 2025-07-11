import streamlit as st
import requests
from PIL import Image
API_URL = "http://127.0.0.1:8000/predict" 
 

st.title("Predict House Price in Bengaluru")
st.markdown("Enter your details below:")

# Input fields
total_sqft = st.number_input("Enter Total Requied Square Feet Area",min_value=300)
No_Bathroom = st.slider("Enter No of Bathroom ", min_value=1, value=2,max_value=17)
BHK= st.slider("Enter BHK ", min_value=1, max_value=16)
Location =st.selectbox("Select location in Bengalaru ",["1st phase jp nagar", "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar", "amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", "attibele", "babusapalaya", "balagere", "banashankari", "banashankari stage ii", "banashankari stage iii", "banashankari stage vi", "banaswadi", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", "battarahalli", "begur", "begur road", "bellandur", "benson town", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra", "bommasandra industrial area", "brookefield", "btm 2nd stage", "btm layout", "budigere", "chandapura", "channasandra", "chikka tirupathi", "chikkalasandra", "choodasandra", "cooke town", "cv raman nagar", "dasanapura", "dasarahalli", "devanahalli", "dodda nekkundi", "doddathoguru", "domlur", "electronic city", "electronic city phase ii", "electronics city phase 1", "epip zone", "frazer town", "garudachar palya", "gottigere", "green glen layout", "gubbalala", "gunjur", "haralur road", "harlur", "hbr layout", "hebbal", "hebbal kempapura", "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli", "hoskote", "hosur road", "hrbr layout", "hsr layout", "hulimavu", "iblur village", "indira nagar", "jakkur", "jalahalli", "jigani", "jp nagar", "judicial layout", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura", "kanakpura road", "kannamangala", "kasavanhalli", "kasturi nagar", "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", "kereguddadahalli", "kodichikkanahalli", "kodihalli", "kogilu", "koramangala", "kothannur", "kothanur", "kr puram", "kudlu", "kudlu gate", "kumaraswami layout", "kundalahalli", "lakshminarayana pura", "lingadheeranahalli", "magadi road", "mahadevpura", "mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "munnekollal", "mysore road", "nagarbhavi", "nagavara", "nagavarapalya", "old airport road", "old madras road", "ombr layout", "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "poorna pragna layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", "sanjay nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", "seegehalli", "singasandra", "somasundara palya", "sonnenahalli", "subramanyapura", "talaghattapura", "tc palaya", "thanisandra", "thigalarapalya", "thubarahalli", "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road", "vidyaranyapura", "vijayanagar", "vittasandra", "whitefield", "yelachenahalli", "yelahanka", "yelahanka new town", "yeshwanthpur"])

img=Image.open(r'C:\Users\DELL\Desktop\House_price_prediction\images\skyscraper.png')
st.image(img,width=100)

if st.button("Predict House Price In Lakh"):
    input_data = {
        "total_sqft": total_sqft,
        "bath": No_Bathroom,
        "BHK": BHK,
        "location": Location
    }
    #st.write(input_data)
    try:
     response = requests.post(API_URL, json=input_data)
     result = response.json()

     ##st.write("Raw Response:", result) 

     if response.status_code == 200 and "predicted_category" in result:
        prediction = result["predicted_category"]
        st.success(f"Expected Price: **{round(prediction,2)} Lakh**")
     else:
        st.error(f"API Error: {response.status_code}")
        st.write("Response content:", result)

    except requests.exceptions.ConnectionError:
     st.error("Could not connect to the server. Make sure it's working.")
