import streamlit as st
import google.generativeai as genai

# ==============================
# 1️⃣ Streamlit 앱 기본 설정
# ==============================
st.set_page_config(
    page_title="Gemini API 테스트",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Gemini API 테스트 페이지")
st.caption("Gemini 모델에 직접 프롬프트를 보내고 응답을 확인합니다.")

# ==============================
# 2️⃣ API 키 설정
# ==============================
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    st.success("✅ GEMINI API Key가 정상 설정되었습니다.")
except Exception as e:
    st.error("🚨 GEMINI API Key가 설정되지 않았습니다.")
    st.stop()

# ==============================
# 3️⃣ 모델 선택
# ==============================
MODEL_NAME = "gemini-1.5-pro-latest"

st.info(f"현재 테스트 모델: `{MODEL_NAME}`")

# ==============================
# 4️⃣ 프롬프트 입력
# ==============================
prompt = st.text_area(
    "💬 프롬프트 입력",
    placeholder="예: 오늘 날씨를 알려줘",
    height=150
)

# ==============================
# 5️⃣ 테스트 실행 버튼
# ==============================
if st.button("🚀 테스트 실행"):
    if not prompt.strip():
        st.warning("프롬프트를 입력하세요.")
    else:
        with st.spinner("Gemini 모델이 응답 중입니다..."):
            try:
                # 모델 객체 생성
                model = genai.GenerativeModel(MODEL_NAME)

                # 콘텐츠 생성
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.7,
                        "max_output_tokens": 512
                    }
                )

                st.success("✅ 응답 도착!")
                st.markdown("**응답 내용:**")
                st.code(response.text)

            except Exception as e:
                st.error(f"오류 발생: {e}")
                st.info("💡 사용 가능한 모델 목록 확인 예시: genai.list_models() 사용")

