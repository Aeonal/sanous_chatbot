
import streamlit as st
import requests

st.set_page_config(page_title="چت‌بات سلامت‌یار | Sanous", page_icon="🧠")
st.title("🧠 چت‌بات سلامت‌یار")
st.markdown("""
🔸 به چت‌بات سلامت‌یار خوش آمدید. سوالات خود درباره‌ی داروها، بیماری‌ها، تغذیه، سلامت روان و دیگر موضوعات مرتبط با سلامت را بپرسید.
""")

# کادر ورودی کاربر
user_input = st.text_input("✍️ سوال خود را اینجا وارد کنید:")

# دکمه ارسال
if st.button("ارسال سوال"):
    if user_input.strip() == "":
        st.warning("لطفاً یک سوال وارد کنید.")
    else:
        # اینجا پاسخ از مدل RAG یا API باید بیاد — فعلاً پاسخ تستی قرار می‌دیم
        answer = "این یک پاسخ تستی است به سوال شما: '" + user_input + "'"

        # نمایش پاسخ
        st.success("پاسخ چت‌بات:")
        st.write(answer)

# پاورقی
st.markdown("---")
st.markdown("ساخته شده با ❤️ توسط تیم Sanous")
