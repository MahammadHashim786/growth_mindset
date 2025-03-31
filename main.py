import streamlit as st

def main():
    st.set_page_config(page_title="Growth Mindset", page_icon="🌱")
    
    st.title("🌱 Growth Mindset")  
    st.write("*Apni qabliyat ko barhane ka tareeqa*")
    
    tab1, tab2 = st.tabs(["Basic Info", "Daily Challenge"])  
    
    with tab1:
        st.header("Growth Mindset kya hai?")  
        st.write("""
        - Yaqeen  ke sath aap ki salahiyaten barh sakti hain 
        - Mehnat se behtar ho sakte hain 
        - Mushkilat ko mauqa samjhein 
        - Ghaltiyon se seekhein 
        """)
        
    with tab2:
        st.header("Aaj ka Challenge")  
        option = st.selectbox("Apna option select kare:", [  
            "Apne comfort zone se bahar kuch seekhein", 
            "Ghalti ko seekhne ka mauqa dein",  
            "Apne kaam par feedback lein"  
        ])
        
        if st.button("accept"):  
            st.success(f"your choice: {option}")
            st.balloons()
            
main()
