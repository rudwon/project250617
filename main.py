import streamlit as st
import random

# 원소 데이터 (기본 20개 정도만 예시)
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

st.title("🔬 주기율표 퀴즈 & 탐험")

# 점수 상태 관리
if "score" not in st.session_state:
    st.session_state.score = 0

# 문제 원소 상태 관리
if "current_element" not in st.session_state:
    st.session_state.current_element = random.choice(elements)

# 문제 유형 (기호, 이름, 원자번호 중 하나 선택)
if "quiz_type" not in st.session_state:
    st.session_state.quiz_type = random.choice(["symbol", "name", "atomic_number"])

def new_question():
    st.session_state.current_element = random.choice(elements)
    st.session_state.quiz_type = random.choice(["symbol", "name", "atomic_number"])
    st.session_state.user_answer = ""

def check_answer(user_answer):
    elem = st.session_state.current_element
    correct = False
    # 정답 확인
    if st.session_state.quiz_type == "symbol":
        correct = user_answer.strip().capitalize() == elem["symbol"]
    elif st.session_state.quiz_type == "name":
        correct = user_answer.strip() == elem["name"]
    else:  # atomic_number
        correct = user_answer.strip() == str(elem["atomic_number"])
    return correct

st.write(f"현재 점수: **{st.session_state.score}**")

# 문제 보여주기
question = ""
if st.session_state.quiz_type == "symbol":
    question = f"원자번호가 **{st.session_state.current_element['atomic_number']}** 인 원소의 **기호**는?"
elif st.session_state.quiz_type == "name":
    question = f"기호가 **{st.session_state.current_element['symbol']}** 인 원소의 **이름**은?"
else:
    question = f"원소 **{st.session_state.current_element['name']}** 의 원자번호는?"

st.markdown(f"### {question}")

# 사용자 답변 입력
user_answer = st.text_input("정답을 입력하세요", key="user_answer")

# 정답 확인 버튼
if st.button("정답 확인"):
    if check_answer(user_answer):
        st.success("🎉 정답입니다!")
        st.session_state.score += 1
        st.button("다음 문제", on_click=new_question)
    else:
        st.error("❌ 틀렸어요. 다시 시도해 보세요.")
        # 힌트 보여주기
        hint = ""
        elem = st.session_state.current_element
        if st.session_state.quiz_type == "symbol":
            hint = f"힌트: 원소 이름은 '{elem['name']}' 입니다."
        elif st.session_state.quiz_type == "name":
            hint = f"힌트: 원자번호는 {elem['atomic_number']} 입니다."
        else:
            hint = f"힌트: 원소 기호는 '{elem['symbol']}' 입니다."
        st.info(hint)

# 원소 간단 정보 카드
st.markdown("---")
st.markdown("### 현재 문제 원소 정보 (힌트 참고용)")
st.write(f"- 이름: {st.session_state.current_element['name']}")
st.write(f"- 기호: {st.session_state.current_element['symbol']}")
st.write(f"- 원자번호: {st.session_state.current_element['atomic_number']}")

# 다음 문제 버튼 (언제나 눌러서 넘어갈 수 있음)
if st.button("다음 문제"):
    new_question()
    st.experimental_rerun()
