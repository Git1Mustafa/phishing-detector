import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('phishing_model.pkl')

# Title
st.title("🔐 Phishing Website Detector")
st.markdown("Developed by Mohammed Mustafa Shaikh   \nFinal Year Project")
st.write("Enter website features to check if it's **Phishing** or **Legitimate**.")

# Input fields for all 30 features
having_ip_address = st.selectbox("1. Having IP Address", [-1, 0, 1])
url_length = st.selectbox("2. URL Length", [-1, 0, 1])
shortining_service = st.selectbox("3. Using URL Shortening Service", [-1, 0, 1])
having_at_symbol = st.selectbox("4. Has '@' Symbol", [-1, 0, 1])
double_slash_redirecting = st.selectbox("5. Double Slash Redirecting", [-1, 0, 1])
prefix_suffix = st.selectbox("6. Prefix-Suffix in Domain", [-1, 0, 1])
having_sub_domain = st.selectbox("7. Having Sub Domain", [-1, 0, 1])
sslfinal_state = st.selectbox("8. SSL Final State", [-1, 0, 1])
domain_registration_length = st.selectbox("9. Domain Registration Length", [-1, 0, 1])
favicon = st.selectbox("10. Suspicious Favicon", [-1, 0, 1])
port = st.selectbox("11. Unusual Ports", [-1, 0, 1])
https_token = st.selectbox("12. HTTPS Token in Domain", [-1, 0, 1])
request_url = st.selectbox("13. Request URL Behavior", [-1, 0, 1])
url_of_anchor = st.selectbox("14. URL of Anchor", [-1, 0, 1])
links_in_tags = st.selectbox("15. Links in <meta>, <script>, <link>", [-1, 0, 1])
sfh = st.selectbox("16. SFH (Server Form Handler)", [-1, 0, 1])
submitting_to_email = st.selectbox("17. Submitting to Email", [-1, 0, 1])
abnormal_url = st.selectbox("18. Abnormal URL", [-1, 0, 1])
redirect = st.selectbox("19. Redirects", [-1, 0, 1])
on_mouseover = st.selectbox("20. On Mouseover Behavior", [-1, 0, 1])
rightclick = st.selectbox("21. Right Click Disabled", [-1, 0, 1])
popupwindow = st.selectbox("22. Has Pop-up Window", [-1, 0, 1])
iframe = st.selectbox("23. Using Iframe", [-1, 0, 1])
age_of_domain = st.selectbox("24. Age of Domain", [-1, 0, 1])
dnsrecord = st.selectbox("25. DNS Record", [-1, 0, 1])
web_traffic = st.selectbox("26. Website Traffic", [-1, 0, 1])
page_rank = st.selectbox("27. Page Rank", [-1, 0, 1])
google_index = st.selectbox("28. Indexed by Google", [-1, 0, 1])
links_pointing_to_page = st.selectbox("29. Links Pointing to Page", [-1, 0, 1])
statistical_report = st.selectbox("30. Statistical Report", [-1, 0, 1])

# Predict button
if st.button("✅ Check"):
    # Create input with exact feature names used during training
    input_data = pd.DataFrame([{
        'having_ip_address': having_ip_address,
        'url_length': url_length,
        'shortining_service': shortining_service,
        'having_at_symbol': having_at_symbol,
        'double_slash_redirecting': double_slash_redirecting,
        'prefix_suffix': prefix_suffix,
        'having_sub_domain': having_sub_domain,
        'sslfinal_state': sslfinal_state,
        'domain_registration_length': domain_registration_length,
        'favicon': favicon,
        'port': port,
        'https_token': https_token,
        'request_url': request_url,
        'url_of_anchor': url_of_anchor,
        'links_in_tags': links_in_tags,
        'sfh': sfh,
        'submitting_to_email': submitting_to_email,
        'abnormal_url': abnormal_url,
        'redirect': redirect,
        'on_mouseover': on_mouseover,
        'rightclick': rightclick,
        'popupwindow': popupwindow,
        'iframe': iframe,
        'age_of_domain': age_of_domain,
        'dnsrecord': dnsrecord,
        'web_traffic': web_traffic,
        'page_rank': page_rank,
        'google_index': google_index,
        'links_pointing_to_page': links_pointing_to_page,
        'statistical_report': statistical_report
    }])

    # Predict and show result
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ This website is **Legitimate**.")
    else:
        st.error("🚨 This website is **Phishing**.")
