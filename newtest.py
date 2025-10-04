import streamlit as st
import google.generativeai as genai

# --- 기본 설정 ---
st.set_page_config(page_title="Gemini API 테스트", page_icon="🤖", layout="centered")

# --- API 키 불러오기 ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("🚨 API Key가 설정되지 않았습니다. Streamlit Secrets에서 GEMINI_API_KEY를 등록하세요.")
    st.stop()

# --- 페이지 제목 ---
st.title("🤖 Gemini API 직접 테스트 페이지")

st.markdown("""
이 페이지는 Google **Gemini 모델**을 직접 호출해 테스트할 수 있는 간단한 예제입니다.  
아래 입력창에 질문을 입력하고 **[테스트 실행]** 버튼을 눌러보세요.
""")

# --- 입력창 ---
prompt = st.text_area("💬 프롬프트 입력", placeholder="예: 한국의 인공지능 산업 동향을 요약해줘", height=150)

# --- 옵션 설정 ---
with st.expander("⚙️ 고급 설정"):
    model_name = st.selectbox("모델 선택", ["gemini-1.5-flash", "gemini-1.5-pro"])
    temperature = st.slider("창의성 (temperature)", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.number_input("최대 출력 토큰 수", 100, 2048, 512)

# --- 실행 버튼 ---
if st.button("🚀 테스트 실행"):
    if not prompt.strip():
        st.warning("프롬프트를 입력하세요.")
    else:
        with st.spinner("Gemini가 응답 중입니다..."):
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "max_output_tokens": max_tokens
                    }
                )
                st.success("✅ 응답이 도착했습니다!")
                st.markdown("### 🧠 Gemini의 응답")
                st.write(response.text)

            except Exception as e:
                st.error(f"오류 발생: {e}")
