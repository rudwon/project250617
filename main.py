import streamlit as st
import random

# --- 스타일 적용 (CSS) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

    body, .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
        color: #fff;
    }

    .title {
        font-size: 3.2rem;
        font-weight: 700;
        text-align: center;
        margin: 30px 0 10px 0;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.7);
    }

    .subtitle {
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 40px;
        color: #d1c4e9;
        font-weight: 500;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
    }

    .card {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 25px;
        padding: 30px 40px;
        max-width: 650px;
        margin: 0 auto 40px auto;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .question {
        font-size: 1.7rem;
        font-weight: 700;
        margin-bottom: 25px;
        text-align: center;
        letter-spacing: 1.5px;
        text-shadow: 0 0 8px #ffd700;
    }

    input[type="text"] {
        width: 100%;
        max-width: 320px;
        font-size: 1.2rem;
        padding: 12px 15px;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin: 0 auto 25px auto;
        display: block;
        text-align: center;
        font-weight: 600;
        outline: none;
    }

    .btn-primary {
        background: linear-gradient(45deg, #ffba00, #ff6a00);
        border: none;
        padding: 12px 35px;
        font-size: 1.2rem;
        font-weight: 700;
        color: #fff;
        border-radius: 30px;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(255, 105, 0, 0.6);
        transition: all 0.3s ease;
        display: block;
        margin: 0 auto 15px auto;
    }

    .btn-primary:hover {
        box-shadow: 0 0 20px #ffba00;
        transform: scale(1.05);
    }

    .score {
        font-size: 2.5rem;
        font-weight: 900;
        color: #ffd700;
        text-align: center;
        margin-bottom: 35px;
        text-shadow: 0 0 12px #ffd700;
    }

    .message {
        text-align: center;
        font-size: 1.4rem;
        margin-bottom: 20px;
        font-weight: 600;
        text-shadow: 0 0 6px rgba(255, 255, 255, 0.7);
    }

    .hint-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 15px 20px;
        max-width: 500px;
        margin: 15px auto 30px auto;
        font-style: italic;
        font-size: 1.1rem;
        color: #ffe066;
        text-align: center;
        box-shadow: 0 0 10px #ffb700;
    }

    .info-box {
        max-width: 650px;
        background: rgba(255, 255, 255, 0.12);
        padding: 20px 30px;
        margin: 0 auto 40px auto;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(255, 255, 255, 0.15);
        font-size: 1.1rem;
        text-align: center;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 원소 데이터 (20개)
elements = [
    {"name": "수소", "symbol": "H", "atomic_number": 1},
    {"name": "헬륨", "symbol": "He", "atomic_number": 2},
    {"name": "리튬", "symbol": "Li", "atomic_number": 3},
    {"name": "베릴륨", "symbol": "Be", "atomic_number": 4},
    {"name": "붕소", "symbol": "B", "atomic_number": 5},
    {"name": "탄소", "symbol": "C", "atomic_number": 6},
    {"name": "질소", "symbol": "N", "atomic_number": 7},
    {"name": "산소", "symbol": "O", "atomic_number": 8},
    {"name": "플루오린", "symbol": "F", "atomic_number": 9},
    {"name": "네온", "symbol": "Ne", "atomic_number": 10},
    {"name": "나트륨", "symbol": "Na", "atomic_number": 11},
    {"name": "마그네슘", "symbol": "Mg", "atomic_number": 12},
    {"name": "알루미늄", "symbol": "Al", "atomic_number": 13},
    {"name": "규소", "symbol": "Si", "atomic_number": 14},
    {"name": "인", "symbol": "P", "atomic_number": 15},
    {"name": "황", "symbol": "S", "atomic_number": 16},
    {"name": "염소", "symbol": "Cl", "atomic_number": 17},
    {"name": "아르곤", "symbol": "Ar", "atomic_number": 18},
    {"name": "칼륨", "symbol": "K", "atomic_number": 19},
    {"name": "칼슘", "symbol": "Ca", "atomic_number": 20},
]

st.set_page_config(page_title="주기율표 퀴즈 & 탐험", page_icon="🧪", layout="centered")

st.markdown('<div class="title">🔬 주기율표 퀴즈 & 탐험</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">원소의 기호, 이름, 원자번호를 맞춰 보세요!</div>', unsafe_allow_html=True)

# 점수 관리
if "score" not in st.session_state:
    st.session_state.score = 0

# 문제 원소 관리
if "current_element" not in st.session_state:
    st.session_state.current_element = random.choice(elements)

# 문제 유형 관리
if "quiz_type" not in st.session_state:
    st.session_state.quiz_type = random.choice(["symbol", "name", "atomic_number"])

# 사용자 답 입력 상태
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

def new_question():
    st.session_state.current_element = random.choice(elements)
    st.session_state.quiz_type = random.choice(["symbol", "name", "atomic_number"])
    st.session_state.user_answer = ""
    st.session_state.feedback = None
    st.experimental_rerun()

def check_answer(user_answer):
    elem = st.session_state.current_element
    if st.session_state.quiz_type == "symbol":
        return user_answer.strip().capitalize() == elem["symbol"]
    elif st.session_state.quiz_type == "name":
        return user_answer.strip() == elem["name"]
    else:
        return user_answer.strip() == str(elem["atomic_number"])

# 점수판
st.markdown(f'<div class="score">점수: {st.session_state.score}</div>', unsafe_allow_html=True)

# 문제 문구
q = ""
if st.session_state.quiz_type == "symbol":
    q = f"원자번호가 **{st.session_state.current_element['atomic_number']}** 인 원소의 **기호**는?"
elif st.session_state.quiz_type == "name":
    q = f"기호가 **{st.session_state.current_element['symbol']}** 인 원소의 **이름**은?"
else:
    q = f"원소 **{st.session_state.current_element['name']}** 의 원자번호는?"

st.markdown(f'<div class
