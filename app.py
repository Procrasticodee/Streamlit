import streamlit as st
from automation import yookalo, pookalo, mookalo
import time

if not st.session_state.get("form_submitted", False):
    st.session_state.is_posting = False
# Initialize session state cleanly
if "initialized" not in st.session_state:
    st.session_state.is_posting = False
    st.session_state.form_submitted = False
    st.session_state.initialized = True



st.title("One-Click Blog Automation")
st.markdown("### Enter all blog details manually. Nothing is auto-generated.")

# 💡 User inputs inside a form
with st.form("blog_form"):
    title = st.text_input("Enter Blog Title")
    description = st.text_area("Enter Blog Description")
    keyword = st.text_input("Enter Blog Keyword")
    target_url = st.text_input("Enter Target URL (e.g., https://posts.yookalo.com/list-an-ad-steps.php)")

    # 🟨 FUNCTION CHOICE DROPDOWN
    function_choice = st.selectbox("Select Platform", ["Yookalo", "Pookalo", "Mookalo"])


    #Buttons
    col1, col2 = st.columns(2)
    submit = col1.form_submit_button("Post Blog")
    cancel = col2.form_submit_button("Cancel Posting")

# Handle cancel button
if cancel:
    st.session_state.is_posting = False
    st.session_state.form_submitted = False



# Placeholder to show status
status_placeholder = st.empty()

# 🟢 When user clicks Post Blog
if submit:
    if title and description and keyword and target_url:
        st.session_state.is_posting = True
        st.session_state.form_submitted = True
    else:
        st.warning("Please fill out all fields before posting.")

# 🚀 Handle blog posting
if st.session_state.is_posting:
    status_placeholder.info("⏳ Posting blog... (Click 'Cancel Posting' to stop)")

    try:
        for i in range(5):
            time.sleep(1)
            if not st.session_state.is_posting:
                status_placeholder.warning("⚠️ Posting canceled.")
                break
        else:
            # ✅ CALL THE SELECTED FUNCTION
            if function_choice == "Yookalo":
                yookalo(title, description, keyword, target_url)
            elif function_choice == "Pookalo":
                pookalo(title, description, keyword, target_url)
            elif function_choice == "Mookalo":
                mookalo(title, description, keyword, target_url)

            st.session_state.is_posting = False
            status_placeholder.success("✅ Blog posted successfully!")
            st.markdown(f"**Title:** {title}")
            st.markdown(f"**Description:** {description}")
            st.markdown(f"**Keyword:** {keyword}")
            st.markdown(f"**URL:** {target_url}")

    except Exception as e:
        st.session_state.is_posting = False
        st.error(f"❌ Error: {e}")
