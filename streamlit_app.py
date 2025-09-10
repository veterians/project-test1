import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date

# 페이지 설정
st.set_page_config(
    page_title="Welldying - 반려동물 AI 장례 서비스",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS 스타일
st.markdown("""
<style>
    .main > div {
        padding: 0rem 1rem;
    }
    
    .header-container {
        background: linear-gradient(135deg, #C4A484 0%, #D4B898 100%);
        padding: 2rem 1rem;
        margin: -1rem -1rem 2rem -1rem;
        text-align: center;
        color: white;
    }
    
    .header-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    .welcome-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .service-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .service-card {
        background: #F5F5F5;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .service-card:hover {
        background: #E8E8E8;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .service-card.active {
        background: #C4A484;
        color: white;
        border: 2px solid #A08661;
    }
    
    .service-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        background: white;
        width: 60px;
        height: 60px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem auto;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .service-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 0.3rem;
    }
    
    .service-desc {
        font-size: 0.9rem;
        opacity: 0.8;
    }
    
    .mobile-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        padding: 1rem;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        z-index: 1000;
    }
    
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #C4A484 0%, #D4B898 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #A08661 0%, #B8956F 100%);
        transform: translateY(-1px);
    }
    
    @media (max-width: 768px) {
        .service-grid {
            grid-template-columns: 1fr;
        }
        
        .header-title {
            font-size: 2rem;
        }
        
        .main > div {
            padding: 0rem 0.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# 세션 스테이트 초기화
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

# 헤더
st.markdown("""
<div class="header-container">
    <div class="header-title">Welldying</div>
    <div class="header-subtitle">반려동물 AI 장례 서비스</div>
</div>
""", unsafe_allow_html=True)

# 홈페이지
if st.session_state.current_page == "home":
    # 환영 메시지
    st.markdown("""
    <div class="welcome-card">
        <h2>안녕하세요!</h2>
        <p style="margin-top: 1rem; color: #666;">반려동물과의 소중한 추억을 기록해보세요.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 서비스 메뉴
    st.markdown("## 서비스 메뉴")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🐾\n\n생애 케어\n& 커뮤니티", key="care", help="반려동물 전문 관리 가이드"):
            st.session_state.current_page = "care"
            st.rerun()
            
        if st.button("📋\n\n장례 준비\n& 시설 예약", key="funeral", help="위치 기반 시설 추천"):
            st.session_state.current_page = "funeral"
            st.rerun()
            
        if st.button("💝\n\n사후 추모\n& 심리 케어", key="memorial", help="디지털 추모관 및 상담"):
            st.session_state.current_page = "memorial_care"
            st.rerun()
    
    with col2:
        if st.button("📖\n\n디지털 자서전\n& 아바타", key="digital", help="AI 기반 스토리텔링"):
            st.session_state.current_page = "digital"
            st.rerun()
            
        if st.button("📱\n\n모바일 장례식\n플랫폼", key="mobile", help="추모 웹페이지 제작"):
            st.session_state.current_page = "mobile_platform"
            st.rerun()
            
        if st.button("👥\n\n새 가족 매칭\n& 서비스", key="matching", help="성향 분석 기반 매칭"):
            st.session_state.current_page = "matching"
            st.rerun()

# 생애 케어 & 커뮤니티
elif st.session_state.current_page == "care":
    st.markdown("# 🐾 생애 케어 & 커뮤니티")
    
    # 뒤로가기 버튼
    if st.button("← 홈으로", key="back_care"):
        st.session_state.current_page = "home"
        st.rerun()
    
    tab1, tab2 = st.tabs(["📋 케어 가이드", "💬 커뮤니티"])
    
    with tab1:
        st.markdown("""
        <div class="form-container">
            <h3>🌱 반려동물 생애 단계별 케어</h3>
        </div>
        """, unsafe_allow_html=True)
        
        pet_type = st.selectbox("🐕 반려동물 종류", ["강아지", "고양이", "기타"], key="pet_type_care")
        age_group = st.selectbox("📅 연령대", ["새끼(0-1년)", "성견/성묘(1-7년)", "노견/노묘(7년+)"], key="age_care")
        
        if age_group == "노견/노묘(7년+)":
            st.error("⚠️ 노령 반려동물 전용 케어 가이드")
            
            st.markdown("""
            <div style="background: #FFF3CD; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                <h4>🏥 건강 관리 체크리스트</h4>
                <ul style="margin-left: 1rem;">
                    <li>정기 건강검진 (6개월마다)</li>
                    <li>관절 건강 보조제 급여</li>
                    <li>저칼로리 사료로 변경</li>
                    <li>운동량 조절 및 관찰</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: #F8D7DA; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
                <h4>⚠️ 주의사항</h4>
                <ul style="margin-left: 1rem;">
                    <li>급격한 체중 변화 모니터링</li>
                    <li>호흡 패턴 및 행동 관찰</li>
                    <li>식욕 변화 체크</li>
                    <li>일상 행동 변화 기록</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="form-container">
            <h3>💬 커뮤니티 게시판</h3>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("✏️ 새 글 작성하기", expanded=False):
            title = st.text_input("제목", key="post_title")
            category = st.selectbox("카테고리", ["건강상담", "행동교정", "일상공유", "질문/답변"], key="post_category")
            content = st.text_area("내용", height=120, key="post_content")
            
            if st.button("게시글 등록", key="submit_post"):
                st.success("✅ 게시글이 등록되었습니다!")
        
        st.markdown("### 📝 최근 게시글")
        
        posts = [
            {"title": "13살 강아지 관절 관리 팁 공유", "author": "멍멍맘", "category": "건강상담", "likes": 15, "time": "2시간 전"},
            {"title": "노묘 식단 추천 부탁드립니다", "author": "냥이아빠", "category": "질문/답변", "likes": 8, "time": "4시간 전"},
            {"title": "우리 댕댕이 마지막 여행 후기", "author": "골든사랑", "category": "일상공유", "likes": 32, "time": "6시간 전"}
        ]
        
        for post in posts:
            st.markdown(f"""
            <div style="background: white; padding: 1rem; border-radius: 10px; margin: 0.5rem 0; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div style="flex: 1;">
                        <h4 style="margin: 0 0 0.5rem 0;">{post['title']}</h4>
                        <p style="color: #666; font-size: 0.9rem; margin: 0;">
                            by {post['author']} | {post['category']} | {post['time']}
                        </p>
                    </div>
                    <div style="color: #C4A484; font-weight: bold;">
                        ❤️ {post['likes']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# 디지털 자서전 & 아바타
elif st.session_state.current_page == "digital":
    st.markdown("# 📖 디지털 자서전 & 아바타")
    
    if st.button("← 홈으로", key="back_digital"):
        st.session_state.current_page = "home"
        st.rerun()
    
    tab1, tab2 = st.tabs(["📚 자서전 작성", "🎭 아바타 생성"])
    
    with tab1:
        st.markdown("""
        <div class="form-container">
            <h3>📖 반려동물 디지털 자서전 만들기</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            pet_name = st.text_input("🐕 반려동물 이름", placeholder="예: 코코", key="pet_name_digital")
            pet_birth = st.date_input("📅 생년월일", key="pet_birth_digital")
            pet_breed = st.text_input("🏷️ 품종", placeholder="예: 골든 리트리버", key="pet_breed_digital")
            
        with col2:
            uploaded_file = st.file_uploader("📸 대표 사진", type=['png', 'jpg', 'jpeg'], key="pet_photo_digital")
            if uploaded_file:
                st.image(uploaded_file, width=150, caption="대표 사진")
        
        memories = st.text_area("💭 특별한 추억", height=120, 
                               placeholder="우리가 함께한 소중한 순간들을 적어주세요...", key="memories_digital")
        
        personality = st.multiselect("🎭 성격 특성", 
                                   ["활발한", "온순한", "장난꾸러기", "똑똑한", "애교많은", "용감한", "수줍은"],
                                   key="personality_digital")
        
        if st.button("🤖 AI 자서전 생성하기", key="generate_bio"):
            with st.spinner("AI가 자서전을 생성 중입니다..."):
                st.success("✅ AI 자서전이 생성되었습니다!")
                st.info("💡 개인화된 스토리가 완성되었습니다. 편집하여 더욱 특별하게 만들어보세요!")
    
    with tab2:
        st.markdown("""
        <div class="form-container">
            <h3>🎭 AI 아바타 생성</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            avatar_style = st.radio("🎨 아바타 스타일", ["사실적", "만화풍", "픽사 스타일"], key="avatar_style")
            expression = st.selectbox("😊 표정", ["기본", "웃는", "졸린", "장난스러운"], key="avatar_expression")
            
        with col2:
            st.markdown("""
            <div style="background: #E3F2FD; padding: 1rem; border-radius: 10px; text-align: center;">
                <p style="margin: 0;">📸 사진을 업로드하시면</p>
                <p style="margin: 0;"><strong>AI가 귀여운 아바타로 변환</strong>해드립니다!</p>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("🎨 아바타 생성", key="generate_avatar"):
            with st.spinner("아바타를 생성 중입니다..."):
                st.success("✅ 아바타가 생성되었습니다!")

# 장례 준비 & 시설 매칭
elif st.session_state.current_page == "funeral":
    st.markdown("# ⚰️ 장례 준비 & 시설 매칭")
    
    if st.button("← 홈으로", key="back_funeral"):
        st.session_state.current_page = "home"
        st.rerun()
    
    tab1, tab2 = st.tabs(["🗺️ 시설 찾기", "📅 예약 관리"])
    
    with tab1:
        st.markdown("""
        <div class="form-container">
            <h3>🔍 위치 기반 장례 시설 검색</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            location = st.selectbox("📍 지역", ["서울", "경기", "부산", "대구", "인천"], key="funeral_location")
            service_type = st.multiselect("🛠️ 서비스", ["화장", "매장", "납골당", "추도식"], key="funeral_service")
            budget_min, budget_max = st.slider("💰 예산 (만원)", 50, 500, (100, 300), key="funeral_budget")
            
            if st.button("🔍 시설 검색", key="search_funeral"):
                st.success("조건에 맞는 시설을 찾았습니다!")
        
        with col2:
            # 지도 데이터
            map_data = pd.DataFrame({
                'lat': [37.5665, 37.5025, 37.4979],
                'lon': [126.9780, 127.0266, 127.0276]
            })
            st.map(map_data, zoom=10)
        
        # 추천 시설
        st.markdown("### 🏢 추천 시설")
        facilities = [
            {"name": "서울펫장례식장", "rating": 4.8, "price": 150, "address": "서울시 강남구"},
            {"name": "강남동물장례식장", "rating": 4.6, "price": 220, "address": "서울시 서초구"},
            {"name": "한강펫메모리얼", "rating": 4.7, "price": 180, "address": "서울시 마포구"}
        ]
        
        for facility in facilities:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; margin: 0.5rem 0; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0;">{facility['name']}</h4>
                        <p style="color: #666; margin: 0.5rem 0;">{facility['address']}</p>
                        <p style="color: #C4A484; margin: 0;">⭐ {facility['rating']} | 💰 {facility['price']}만원</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 📋 예약 현황")
        booking_data = pd.DataFrame({
            '날짜': ['2024-03-15', '2024-03-18', '2024-03-22'],
            '시설명': ['서울펫장례식장', '강남동물장례식장', '한강펫메모리얼'],
            '서비스': ['화장 + 추도식', '화장', '납골당'],
            '상태': ['✅ 확정', '⏳ 대기', '✅ 확정']
        })
        st.dataframe(booking_data, use_container_width=True, hide_index=True)

# 모바일 장례식 웹페이지
elif st.session_state.current_page == "mobile_platform":
    st.markdown("# 📱 모바일 장례식 플랫폼")
    
    if st.button("← 홈으로", key="back_mobile"):
        st.session_state.current_page = "home"
        st.rerun()
    
    tab1, tab2 = st.tabs(["🎨 페이지 제작", "👀 미리보기"])
    
    with tab1:
        st.markdown("""
        <div class="form-container">
            <h3>💐 추모 웹페이지 제작</h3>
        </div>
        """, unsafe_allow_html=True)
        
        memorial_name = st.text_input("🐕 반려동물 이름", key="memorial_name")
        memorial_dates = st.text_input("📅 생존 기간", value="2015.03.12 - 2024.02.28", key="memorial_dates")
        memorial_message = st.text_area("💭 추모 메시지", height=100, key="memorial_message")
        
        col1, col2 = st.columns(2)
        with col1:
            theme = st.selectbox("🎨 테마", ["클래식", "모던", "자연", "따뜻함"], key="memorial_theme")
        with col2:
            color = st.color_picker("🎨 대표 색상", "#FFB6C1", key="memorial_color")
        
        uploaded_photos = st.file_uploader("📸 추모 사진", accept_multiple_files=True, 
                                         type=['png', 'jpg', 'jpeg'], key="memorial_photos")
        
        if uploaded_photos:
            cols = st.columns(3)
            for idx, photo in enumerate(uploaded_photos[:6]):
                with cols[idx % 3]:
                    st.image(photo, width=100)
    
    with tab2:
        st.markdown("### 👀 웹페이지 미리보기")
        
        preview_name = memorial_name if memorial_name else "사랑하는 반려동물"
        preview_dates = memorial_dates if memorial_dates else "2015.03.12 - 2024.02.28"
        preview_message = memorial_message if memorial_message else "영원히 기억될 소중한 친구"
        
        st.markdown(f"""
        <div style='text-align: center; padding: 2rem; background: {color}20; border-radius: 15px; margin: 1rem 0;'>
            <h2 style='color: {color}; margin-bottom: 1rem;'>🌈 {preview_name}</h2>
            <p style='font-size: 1.1rem; color: #666; margin-bottom: 1rem;'>{preview_dates}</p>
            <p style='font-style: italic; color: #888;'>{preview_message}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🌐 웹페이지 생성 및 공유", key="create_memorial_page"):
            st.success("✅ 추모 웹페이지가 생성되었습니다!")
            st.info("🔗 공유 링크: https://welldying.com/memorial/abc123")

# 사후 추모 & 심리 케어
elif st.session_state.current_page == "memorial_care":
    st.markdown("# 💝 사후 추모 & 심리 케어")
    
    if st.button("← 홈으로", key="back_memorial"):
        st.session_state.current_page = "home"
        st.rerun()
    
    tab1, tab2 = st.tabs(["🏛️ 디지털 추모관", "🤝 심리 상담"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="form-container">
                <h3>💌 추모 메시지 남기기</h3>
            </div>
            """, unsafe_allow_html=True)
            
            message = st.text_area("마음을 전하는 메시지", height=100, key="memorial_msg")
            message_author = st.text_input("작성자", key="memorial_author")
            
            if st.button("💝 메시지 남기기", key="submit_memorial"):
                st.success("✅ 추모 메시지가 등록되었습니다.")
            
            st.markdown("### 💬 최근 추모 메시지")
            messages = [
                {"author": "김○○", "message": "코코야, 하늘에서 건강하게 지내길...", "date": "2024-03-10"},
                {"author": "이○○", "message": "너무 그리워요. 좋은 곳에서 편히 쉬세요.", "date": "2024-03-09"}
            ]
            
            for msg in messages:
                st.markdown(f"""
                <div style="background: #F8F9FA; padding: 1rem; border-left: 4px solid #C4A484; margin: 0.5rem 0; border-radius: 5px;">
                    <strong>{msg['author']}</strong> <span style="color: #666;">({msg['date']})</span><br>
                    {msg['message']}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 📊 추모 통계")
            st.metric("👥 방문자", "234명")
            st.metric("💌 추모 메시지", "18개")
            st.metric("📤 공유 횟수", "12회")
    
    with tab2:
        st.markdown("""
        <div class="form-container">
            <h3>🤝 반려동물 상실 심리 상담</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📞 상담 신청**")
            counsel_type = st.selectbox("상담 방식", ["화상 상담", "전화 상담", "채팅 상담"], key="counsel_type")
            prefer_time = st.selectbox("희망 시간", ["오전", "오후", "저녁", "심야"], key="counsel_time")
            urgency = st.select_slider("긴급도", ["보통", "빠른", "긴급"], key="counsel_urgency")
            
            concern = st.text_area("상담 내용", height=100, 
                                 placeholder="어떤 마음으로 상담을 받고 싶으신가요?", key="counsel_content")
            
            if st.button("📞 상담 신청하기", key="request_counsel"):
                st.success("✅ 상담 신청 완료! 24시간 내 연락드리겠습니다.")
        
        with col2:
            st.markdown("**🏥 자가 진단**")
            symptoms = [
                "식욕/수면 패턴 변화",
                "집중력 저하",
                "극도의 슬픔/우울감",
                "죄책감이나 후회",
                "사회적 위축"
            ]
            
            checked_count = 0
            for symptom in symptoms:
                if st.checkbox(symptom, key=f"symptom_{symptom}"):
                    checked_count += 1
            
            if checked_count >= 3:
                st.error("⚠️ 전문 상담을 권장합니다.")
            elif checked_count >= 1:
                st.info("💙 자연스러운 반응입니다.")

# 새 가족 매칭
elif st.session_state.current_page == "matching":
    st.markdown("# 🏡 새 가족 매칭 & 서비스")
    
    if st.button("← 홈으로", key="back_matching"):
        st.session_state.current_page = "home"
        st.rerun()
    
    tab1, tab2, tab3 = st.tabs(["🔍 매칭 찾기", "📋 등록하기", "📊 현황"])
    
    with tab1:
        st.markdown("""
        <div class="form-container">
            <h3>🎯 성향 분석 기반 매칭</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            desired_pet = st.selectbox("🐕 동물 종류", ["강아지", "고양이", "기타"], key="desired_pet")
            desired_age = st.selectbox("📅 희망 나이", ["새끼", "성견/성묘", "노견/노묘", "상관없음"], key="desired_age")
            desired_size = st.selectbox("📏 크기", ["소형", "중형", "대형", "상관없음"], key="desired_size")
            
            lifestyle = st.multiselect("🏠 생활 패턴", 
                                     ["활동적", "조용함", "규칙적", "자유로운", "가족 중심"], key="lifestyle")
            
            experience = st.radio("🎓 경험", ["초보", "경험있음", "전문가급"], key="experience")
            
            if st.button("🔍 매칭 검색", key="search_matching"):
                st.success("✅ 조건에 맞는 반려동물을 찾았습니다!")
        
        with col2:
            st.markdown("### 🎯 추천 매칭 결과")
            
            matches = [
                {"name": "바둑이", "age": "2살", "breed": "믹스", "location": "서울 강남", "match": 95},
                {"name": "나비", "age": "3살", "breed": "코리아 숏헤어", "location": "서울 홍대", "match": 88},
                {"name": "몽이", "age": "1살", "breed": "포메라니안", "location": "경기 성남", "match": 82}
            ]
            
            for match in matches:
                st.markdown(f"""
                <div style="background: white; padding: 1rem; border-radius: 10px; margin: 0.5rem 0; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="margin: 0;">{match['name']} ({match['age']})</h4>
                            <p style="color: #666; margin: 0.5rem 0;">{match['breed']} | {match['location']}</p>
                            <div style="background: #E8F5E8; padding: 0.2rem 0.5rem; border-radius: 15px; display: inline-block;">
                                <small>매칭률: {match['match']}%</small>
                            </div>
                        </div>
                        <div style="background: #C4A484; color: white; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer;">
                            📞 연락
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="form-container">
            <h3>📝 분양/입양 동물 등록</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            reg_name = st.text_input("🐕 이름", key="reg_name")
            reg_breed = st.text_input("🏷️ 품종", key="reg_breed")
            reg_age = st.number_input("📅 나이", min_value=0, max_value=20, key="reg_age")
            reg_gender = st.selectbox("⚥ 성별", ["수컷", "암컷"], key="reg_gender")
            
        with col2:
            reg_personality = st.multiselect("🎭 성격", 
                                           ["활발한", "온순한", "사교적", "독립적", "애교많은"], key="reg_personality")
            reg_health = st.selectbox("🏥 건강 상태", ["매우 좋음", "좋음", "보통", "주의 필요"], key="reg_health")
            reg_vaccination = st.checkbox("💉 예방접종 완료", key="reg_vaccination")
            reg_neutering = st.checkbox("✂️ 중성화 완료", key="reg_neutering")
        
        reg_description = st.text_area("📝 상세 설명", height=100, key="reg_description")
        reg_photos = st.file_uploader("📸 사진", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'], key="reg_photos")
        contact_info = st.text_input("📞 연락처", key="reg_contact")
        
        if st.button("📋 등록하기", key="submit_registration"):
            st.success("✅ 등록이 완료되었습니다!")
    
    with tab3:
        st.markdown("### 📊 매칭 성과 대시보드")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📈 월별 매칭 성공률")
            chart_data = pd.DataFrame({
                '월': ['1월', '2월', '3월'],
                '성공률(%)': [85, 89, 92]
            })
            st.bar_chart(chart_data.set_index('월'))
        
        with col2:
            st.markdown("#### 🐾 등록 동물 분포")
            pet_data = pd.DataFrame({
                '동물 종류': ['강아지', '고양이', '기타'],
                '등록 수': [45, 32, 8]
            })
            st.dataframe(pet_data, use_container_width=True, hide_index=True)
        
        st.markdown("### 🎉 최근 성공 매칭")
        success_data = pd.DataFrame({
            '날짜': ['2024-03-10', '2024-03-09', '2024-03-08'],
            '동물명': ['코코', '나비', '몽실이'],
            '새 가족': ['김○○님', '이○○님', '박○○님'],
            '지역': ['서울', '경기', '부산'],
            '상태': ['✅ 완료', '✅ 완료', '✅ 완료']
        })
        st.dataframe(success_data, use_container_width=True, hide_index=True)

# 푸터 (모든 페이지 공통)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #999; padding: 2rem 0; border-top: 1px solid #eee; margin-top: 2rem;">
    <p style="margin: 0;">🐾 Welldying v1.0</p>
    <p style="margin: 0.5rem 0 0 0;">고객 지원: help@welldying.com</p>
</div>
""", unsafe_allow_html=True)
