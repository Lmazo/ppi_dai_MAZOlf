import streamlit as st

def main():
    
    menu = ["Inicio", "Inicio de sesion", "Registrarse", "Sobre nosotros"]
    choice = st.sidebar.selectbox("Selecciona una opción", menu)
    
    
    if choice == "Inicio":
        st.subheader("Inicio")
        st.image('images/CA.jfif')
        st.write("Haz click para ver la calidad del aire hoy")
        if st.button("Calidad del aire hoy"):
            st.write("¡Botón presionado!") 
    
    
    elif choice == "Inicio de sesion":
        st.subheader("Inicio de sesion")
        username = st.text_input("Correo electronico")
        password = st.text_input("Contraseña", type="password")
        if st.button("Iniciar sesion"):
            st.write("¡Botón presionado!")
            #sing_in(username, password)
    
    elif choice == "Registrarse":
        st.subheader("Registrarse")
        username = st.text_input("Correo Electronico")
        city = st.text_input("Ciudad")
        date = st.text_input("Fecha de nacimiento")
        first_password = st.text_input("Contraseña ", type="password")
        st.checkbox("Politica tratamiento de datos personales")
        if st.button("Registrarse"):
            st.write("¡Botón presionado!")
            #sing_up(username, city, date, first_password)
            
    elif choice == "Sobre nosotros":
        st.subheader("Sobre nosotros")
        st.write("Esta aplicacion fue creada por Luisa Fernanda Mazo Perez.")
        st.write("Estudiante de Ingenieria de sistemas e informatica de la universidad nacional de colombia.")
        st.write("Mi objetivo es crear una aplicacion que provea datos y permita estar informado hacerca de la calidad del aire e informar sobre el impacto de la contaminacion en la salud \n")
        
        st.write("📞 Contactanos : ")
        linkedin_url = "https://www.linkedin.com/in/luisa-fernanda-mazo-perez-815b5b248/"
        if st.button('🔗 Conectar en LinkedIn'):
            st.write(f"Visita mi perfil en LinkedIn: [LinkedIn]({linkedin_url})")
        

    
if __name__ == "__main__":
    main()
