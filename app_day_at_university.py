import streamlit as st
import random

# Questions
questions = [
    ("Aš esu _______ ir kiekvieną dieną einu į universitetą.", ["studentas", "mokytojas", "inžinierius"], "studentas"),
    # (same list of questions as before) ...
    ("Taip mes vieni kitiems padedame mokytis ________.", ["geriau", "blogiau", "tikrai"], "geriau"),
]

# Init state
if 'started' not in st.session_state:
    st.session_state.started = False
    st.session_state.questions = random.sample(questions, len(questions))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.show_result = False

st.markdown("<h1 style='text-align: center; color: #b30000;'>📚 Mano diena universitete – žaidimas</h1>", unsafe_allow_html=True)

if not st.session_state.started:
    if st.button("Pradėti žaidimą 🎮"):
        st.session_state.started = True
    st.stop()

# Show question or result
if not st.session_state.show_result:
    q = st.session_state.questions[st.session_state.current]
    sentence, options, correct = q

    st.markdown(f"## {sentence}")
    selected = st.radio("Pasirink atsakymą:", options, key=st.session_state.current)

    if st.button("Patikrinti"):
        if selected == correct:
            st.session_state.score += 5
            st.success("🎉 Teisingai! Puiku! 😊")
        else:
            st.error(f"❌ Neteisingai. Tinkamas atsakymas: **{correct}**")

        st.session_state.current += 1

        if st.session_state.current >= len(st.session_state.questions):
            st.session_state.show_result = True

    st.markdown(f"**Progresas:** {st.session_state.current} iš {len(questions)} klausimų – {st.session_state.score} taškų")

else:
    st.markdown(f"## 🎉 Žaidimas baigtas! Tavo rezultatas: {st.session_state.score} / 100 taškų.")
    if st.button("🔄 Žaisti iš naujo"):
        st.session_state.started = False
        st.session_state.questions = random.sample(questions, len(questions))
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.show_result = False

st.markdown("<style>div.row-widget.stRadio > div{flex-direction: column;}</style>", unsafe_allow_html=True)
