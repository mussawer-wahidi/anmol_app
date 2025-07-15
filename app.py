import streamlit as st
import random

st.set_page_config(page_title="For Anmol 💖", layout="centered")

# 🌸 Background + Cute CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #ffe6f0, #ffccf9, #ffe6f0);
        animation: bgFlow 15s ease infinite;
        background-size: 400% 400%;
    }

    @keyframes bgFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .rainbow-text {
        font-size: 120px;
        font-weight: bold;
        background: linear-gradient(to right, #ff6ec4, #7873f5, #42e695, #fddb92);
        -webkit-background-clip: text;
        color: transparent;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        margin-top: 70px;
        text-shadow: 2px 2px 10px #ffffff70;
    }

    .fade-text {
        font-size: 38px;
        color: #fff0f5;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        margin-bottom: 40px;
    }

    .hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: -1;
    }

    .heart {
        position: absolute;
        width: 20px;
        height: 20px;
        background: pink;
        animation: float 12s linear infinite;
        border-radius: 50%;
        transform: rotate(45deg);
    }

    .heart::before,
    .heart::after {
        content: "";
        position: absolute;
        width: 20px;
        height: 20px;
        background: pink;
        border-radius: 50%;
    }

    .heart::before {
        top: -10px;
        left: 0;
    }

    .heart::after {
        left: -10px;
        top: 0;
    }

    @keyframes float {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(-10vh) rotate(360deg);
            opacity: 0;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 💖 Floating hearts (20)
st.markdown('<div class="hearts">' + ''.join([
    f'<div class="heart" style="left: {random.randint(0, 100)}%; animation-delay: {random.uniform(0, 8)}s;"></div>'
    for _ in range(20)
]) + '</div>', unsafe_allow_html=True)

# 🌈 Main name
st.markdown('<div class="rainbow-text">ANMOL</div>', unsafe_allow_html=True)

# 💬 One random cute compliment
phrases = [
    "YOUUUU THE BEST 💕",
    "YOUUU THE CUTEST 💫",
    "YOU'RE MY HAPPINESS 🌼",
    "YOU MAKE MY HEART SMILE 🐣",
    "MY UNIVERSE IN A HUMAN 🌙"
]
st.markdown(f'<div class="fade-text">{random.choice(phrases)}</div>', unsafe_allow_html=True)

# 🎁 Cute surprise buttons
st.markdown("### 💌 Click a Button for a Surprise!")

col1, col2, col3 = st.columns(3)

if col1.button("💖 Why I Love You"):
    st.success("Because you're magic in motion ✨ and I adore everything about you!")
    st.balloons()

if col2.button("🎁 Compliment Time!"):
    compliments = [
        "Your laugh is my favorite sound 💓",
        "You make ordinary moments extraordinary 💐",
        "You're my forever kind of person 🌟",
        "You're prettier than a thousand sunsets 🌅",
    ]
    st.info(random.choice(compliments))
    st.toast("Awww 🥺💘")

if col3.button("🎀 Open a Tiny Love Note"):
    st.toast("🌸 I’d choose you over and over again. Forever starts with you.")
    st.snow()

# 💗 Sweet footer
st.markdown("---")
st.markdown("#### 🌷 Made with infinite love, just for **you** Anmol 💞")
