import streamlit as st
import random

# ✅ Full question list
questions = [
    ("Aš esu _______ ir kiekvieną dieną einu į universitetą.", ["studentas", "mokytojas", "inžinierius"], "studentas"),
    ("Po paskaitų mes su draugais sėdime ________.", ["bibliotekoje", "parke", "kavinėje"], "bibliotekoje"),
    ("Aš klausau _______ ir užsirašau svarbią informaciją.", ["dėstytojų", "draugų", "studentų"], "dėstytojų"),
    ("Mes kartu _______ dirbame prie grupinių darbų.", ["visi", "abudu", "vienas"], "visi"),
    ("Kartais aš nesuprantu ________, todėl klausiu dėstytojo.", ["užduoties", "muzikos", "žodžių"], "užduoties"),
    ("Jis visada kantriai _______.", ["paaiškina", "skaito", "rašo"], "paaiškina"),
    ("Mes klausome muzikos ______.", ["tyliai", "garsiai", "greitai"], "tyliai"),
    ("Per paskaitas aš klausau ________.", ["dėstytojų", "draugų", "studentų"], "dėstytojų"),
    ("Kartais aš nesuprantu užduoties, todėl klausiu ________.", ["dėstytojo", "draugo", "studento"], "dėstytojo"),
    ("Taip mes vieni kitiems padedame mokytis ________.", ["geriau", "greičiau", "daugiau"], "geriau"),
    ("Kiekvieną dieną aš einu į ________.", ["kavinę", "universitetą", "parduotuvę"], "universitetą"),
    ("Per paskaitas aš dirbu su ________.", ["draugais", "projektas", "įvairiais projektais"], "įvairiais projektais"),
    ("Kartais aš nesuprantu užduoties, todėl klausiu ________.", ["dėstytojo", "mokytojo", "direktoriaus"], "dėstytojo"),
    ("Po paskaitų mes sėdime su draugais ________.", ["bibliotekoje", "kavinėje", "kambaryje"], "bibliotekoje"),
    ("Mes klausome muzikos, bet tyliai arba ________.", ["garsiai", "greitai", "pirmyn"], "garsiai"),
    ("Aš užsirašau ________ informaciją paskaitose.", ["svarbią", "nereikšmingą", "paprastą"], "svarbią"),
    ("Dėstytojas visada ________ užduotis aiškiai.", ["paaiškina", "ignoruoja", "skundžiasi"], "paaiškina"),
    ("Mes kartu dirbame prie ________ darbų.", ["grupinių", "asmeninių", "vieno"], "grupinių"),
    ("Jei kažko nežinome, mes klausinėjame ________.", ["vieni kitų", "mokytojo", "šeimos"], "vieni kitų"),
    ("Taip mes vieni kitiems padedame mokytis ________.", ["geriau", "blogiau", "tikrai"], "geriau"),
]

# Ensure all keys exist every run
st.session_state.setdefault('started', False)
st.session_state.setdefault('questions', random.sample(questions, len(questions)))
st.session_state.setdefault('current', 0)
st.session_state.setdefault('score', 0)
st.session_state.setdefault('show_result', False)
st.session_state.setdefault('answered', False)


# ✅ Title
st.markdown(
    "<h1 style='text-align: center; color: #b30000;'>📚 Mano diena universitete – žaidimas</h1>",
    unsafe_allow_html=True
)

# ✅ Centered start button
if not st.session_state.started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎮 Pradėti žaidimą"):
            st.session_state.started = True
    st.stop()

# ✅ Quiz flow
if not st.session_state.show_result:
    q = st.session_state.questions[st.session_state.current]
    sentence, options, correct = q

    st.markdown(f"### {sentence}")
    selected = st.radio(
        "Pasirink atsakymą:",
        options,
        key=f"q{st.session_state.current}"
    )

    if not st.session_state.answered:
        if st.button("✅ Patikrinti atsakymą"):
            if selected == correct:
                st.session_state.score += 5
                st.success("🎉 Teisingai! Puiku! 😊")
            else:
                st.error(f"❌ Neteisingai. Tinkamas atsakymas: **{correct}**")
            st.session_state.answered = True

    if st.session_state.answered:
        if st.button("➡️ Kitas klausimas"):
            st.session_state.current += 1
            st.session_state.answered = False
            if st.session_state.current >= len(st.session_state.questions):
                st.session_state.show_result = True

    st.write(f"**Progresas:** {st.session_state.current + 1} iš {len(questions)} klausimų – {st.session_state.score} taškų")

else:
    st.markdown(f"## 🎉 Žaidimas baigtas! Tavo rezultatas: {st.session_state.score} / 100 taškų.")
    if st.button("🔄 Žaisti iš naujo"):
        st.session_state.started = False
        st.session_state.questions = random.sample(questions, len(questions))
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.show_result = False
        st.session_state.answered = False

# ✅ Style: radio buttons vertical
st.markdown(
    "<style>div.row-widget.stRadio > div{flex-direction: column;}</style>",
    unsafe_allow_html=True
)
