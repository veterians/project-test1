import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date

# 페이지 설정
st.set_page_config(
    page_title="PetWellbeing - 반려동물 웰다이닝 가이드",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 네비게이션
st.sidebar.title("🐾 PetWellbeing")
st.sidebar.markdown("*반려동물을 웰다이닝 가이드*")

menu = st.sidebar.selectbox(
    "기능 선택",
    ["🏠 홈", "🌱 생애 케어 & 커뮤니티", "📖 디지털 자서전 & 아바타", 
     "⚰️ 장례 준비 & 시설 매칭", "📱 모바일 장례식 웹페이지", 
     "💝 사후 추모 & 심리 케어", "🏡 새 가족 매칭"]
)

# 메인 홈페이지
if menu == "🏠 홈":
    st.title("🐾 PetWellbeing")
    st.markdown("### 반려동물을 위한 종합 웰다이닝 가이드")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("등록된 반려동물", "1,234마리", "12↗")
        
    with col2:
        st.metric("커뮤니티 회원", "5,678명", "45↗")
        
    with col3:
        st.metric("매칭 성공률", "89%", "3%↗")
    
    st.markdown("---")
    
    # 기능 소개 카드
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌱 생애 케어")
        st.write("노견·노묘 전문 관리 가이드와 커뮤니티")
        
        st.subheader("⚰️ 장례 서비스")
        st.write("위치 기반 시설 추천 및 예약")
        
        st.subheader("💝 사후 추모")
        st.write("디지털 추모관 및 심리 상담")
    
    with col2:
        st.subheader("📖 디지털 자서전")
        st.write("AI 기반 스토리텔링 및 아바타 생성")
        
        st.subheader("📱 모바일 웹페이지")
        st.write("부고장 및 추모 페이지 제작")
        
        st.subheader("🏡 새 가족 매칭")
        st.write("성향 분석 기반 입양/분양 매칭")

# 1. 생애 케어 & 커뮤니티
elif menu == "🌱 생애 케어 & 커뮤니티":
    st.title("🌱 생애 케어 & 커뮤니티")
    
    tab1, tab2 = st.tabs(["📋 케어 가이드", "💬 커뮤니티"])
    
    with tab1:
        st.subheader("반려동물 생애 단계별 케어 가이드")
        
        pet_type = st.selectbox("반려동물 종류", ["강아지", "고양이", "기타"])
        age_group = st.selectbox("연령대", ["새끼(0-1년)", "성견/성묘(1-7년)", "노견/노묘(7년+)"])
        
        if age_group == "노견/노묘(7년+)":
            st.warning("⚠️ 노령 반려동물 전용 케어 가이드")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **건강 관리 체크리스트**
                - [ ] 정기 건강검진 (6개월마다)
                - [ ] 관절 건강 보조제 급여
                - [ ] 저칼로리 사료로 변경
                - [ ] 운동량 조절
                """)
                
            with col2:
                st.markdown("""
                **주의사항**
                - 급격한 체중 변화 모니터링
                - 호흡 패턴 관찰
                - 식욕 변화 체크
                - 행동 변화 기록
                """)
    
    with tab2:
        st.subheader("커뮤니티 게시판")
        
        # 글쓰기 폼
        with st.expander("새 글 작성하기"):
            title = st.text_input("제목")
            content = st.text_area("내용", height=150)
            category = st.selectbox("카테고리", ["건강상담", "행동교정", "일상공유", "질문/답변"])
            
            if st.button("게시글 등록"):
                st.success("게시글이 등록되었습니다!")
        
        # 샘플 게시글
        posts = [
            {"title": "13살 강아지 관절 관리 팁 공유", "author": "멍멍맘", "category": "건강상담", "likes": 15},
            {"title": "노묘 식단 추천 부탁드립니다", "author": "냥이아빠", "category": "질문/답변", "likes": 8},
            {"title": "우리 댕댕이 마지막 여행 후기", "author": "골든사랑", "category": "일상공유", "likes": 32}
        ]
        
        for post in posts:
            with st.container():
                col1, col2, col3 = st.columns([6, 2, 1])
                with col1:
                    st.markdown(f"**{post['title']}**")
                    st.caption(f"by {post['author']} | {post['category']}")
                with col2:
                    st.caption("2시간 전")
                with col3:
                    st.caption(f"❤️ {post['likes']}")
                st.divider()

# 2. 디지털 자서전 & 아바타
elif menu == "📖 디지털 자서전 & 아바타":
    st.title("📖 디지털 자서전 & 아바타")
    
    tab1, tab2 = st.tabs(["📚 자서전 작성", "🎭 아바타 생성"])
    
    with tab1:
        st.subheader("반려동물 디지털 자서전 만들기")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            pet_name = st.text_input("반려동물 이름", "코코")
            pet_birth = st.date_input("생년월일")
            pet_breed = st.text_input("품종", "골든 리트리버")
            
        with col2:
            uploaded_file = st.file_uploader("대표 사진 업로드", type=['png', 'jpg', 'jpeg'])
            if uploaded_file:
                st.image(uploaded_file, width=200)
        
        st.markdown("### 추억의 순간들")
        memories = st.text_area("특별한 추억을 적어주세요", height=150, 
                               placeholder="우리가 함께한 소중한 순간들...")
        
        personality = st.multiselect(
            "성격 특성",
            ["활발한", "온순한", "장난꾸러기", "똑똑한", "애교많은", "용감한", "수줍은"]
        )
        
        if st.button("AI 자서전 생성하기"):
            st.success("AI가 자서전을 생성 중입니다...")
            st.info("💡 AI 스트리밍으로 개인화된 스토리를 만들어드립니다!")
    
    with tab2:
        st.subheader("AI 아바타 생성")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**아바타 스타일 선택**")
            avatar_style = st.radio("스타일", ["사실적", "만화풍", "픽사 스타일"])
            
            expression = st.selectbox("표정", ["기본", "웃는", "졸린", "장난스러운"])
            
            if st.button("아바타 생성"):
                st.success("아바타가 생성되었습니다!")
        
        with col2:
            st.info("📸 사진을 업로드하시면 AI가 귀여운 아바타로 변환해드립니다!")

# 3. 장례 준비 & 시설 매칭
elif menu == "⚰️ 장례 준비 & 시설 매칭":
    st.title("⚰️ 장례 준비 & 시설 매칭")
    
    tab1, tab2 = st.tabs(["🗺️ 시설 찾기", "📅 예약 관리"])
    
    with tab1:
        st.subheader("위치 기반 장례 시설 검색")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            location = st.selectbox("지역 선택", ["서울", "경기", "부산", "대구", "인천", "광주", "대전", "울산"])
            service_type = st.multiselect("서비스 종류", ["화장", "매장", "납골당", "추도식"])
            budget = st.slider("예산 범위 (만원)", 50, 500, (100, 300))
        
        with col2:
            # 지도 시뮬레이션
            map_data = pd.DataFrame({
                'lat': [37.5665, 37.5025, 37.4979, 37.5172],
                'lon': [126.9780, 127.0266, 127.0276, 126.8506],
                'name': ['서울펫장례식장', '강남동물장례식장', '한강펫메모리얼', '김포펫휴먼'],
                'rating': [4.8, 4.6, 4.7, 4.5],
                'price': [150, 220, 180, 130]
            })
            
            st.map(map_data[['lat', 'lon']])
        
        st.subheader("추천 시설")
        for _, facility in map_data.iterrows():
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                with col1:
                    st.markdown(f"**{facility['name']}**")
                with col2:
                    st.metric("평점", f"{facility['rating']}★")
                with col3:
                    st.metric("가격", f"{facility['price']}만원")
                with col4:
                    st.button("예약", key=f"book_{facility['name']}")
                st.divider()
    
    with tab2:
        st.subheader("예약 현황")
        
        booking_data = pd.DataFrame({
            '날짜': ['2024-03-15', '2024-03-18', '2024-03-22'],
            '시설명': ['서울펫장례식장', '강남동물장례식장', '한강펫메모리얼'],
            '서비스': ['화장 + 추도식', '화장', '납골당'],
            '상태': ['확정', '대기', '확정']
        })
        
        st.dataframe(booking_data, use_container_width=True)

# 4. 모바일 장례식 웹페이지
elif menu == "📱 모바일 장례식 웹페이지":
    st.title("📱 모바일 장례식 웹페이지")
    
    tab1, tab2 = st.tabs(["🎨 페이지 제작", "👀 미리보기"])
    
    with tab1:
        st.subheader("추모 웹페이지 제작")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**기본 정보**")
            memorial_name = st.text_input("반려동물 이름")
            memorial_dates = st.text_input("생존 기간", "2015.03.12 - 2024.02.28")
            memorial_message = st.text_area("추모 메시지", height=100)
            
            st.markdown("**디자인 설정**")
            theme = st.selectbox("테마", ["클래식", "모던", "자연", "따뜻함"])
            color = st.color_picker("대표 색상", "#FFB6C1")
        
        with col2:
            st.markdown("**사진 갤러리**")
            uploaded_photos = st.file_uploader("추모 사진들", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
            
            if uploaded_photos:
                cols = st.columns(3)
                for idx, photo in enumerate(uploaded_photos[:6]):
                    with cols[idx % 3]:
                        st.image(photo, width=100)
    
    with tab2:
        st.subheader("웹페이지 미리보기")
        
        # 미리보기 시뮬레이션
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background: {color if 'color' in locals() else '#FFB6C1'}20; border-radius: 10px;'>
            <h2>🌈 {memorial_name if memorial_name else '사랑하는 반려동물'}</h2>
            <p>{memorial_dates if memorial_dates else '2015.03.12 - 2024.02.28'}</p>
            <p style='font-style: italic;'>{memorial_message if memorial_message else '영원히 기억될 소중한 친구'}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("웹페이지 생성 및 공유"):
            st.success("추모 웹페이지가 생성되었습니다!")
            st.info("🔗 공유 링크: https://petwellbeing.com/memorial/abc123")

# 5. 사후 추모 & 심리 케어
elif menu == "💝 사후 추모 & 심리 케어":
    st.title("💝 사후 추모 & 심리 케어")
    
    tab1, tab2 = st.tabs(["🏛️ 디지털 추모관", "🤝 심리 상담"])
    
    with tab1:
        st.subheader("디지털 추모관")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 추모 메시지 남기기")
            message = st.text_area("마음을 전하는 메시지", height=100)
            message_author = st.text_input("작성자")
            
            if st.button("메시지 남기기"):
                st.success("추모 메시지가 등록되었습니다.")
            
            st.markdown("### 최근 추모 메시지")
            messages = [
                {"author": "김○○", "message": "코코야, 하늘에서 건강하게 지내길...", "date": "2024-03-10"},
                {"author": "이○○", "message": "너무 그리워요. 좋은 곳에서 편히 쉬세요.", "date": "2024-03-09"},
                {"author": "박○○", "message": "영원히 잊지 않을게요.", "date": "2024-03-08"}
            ]
            
            for msg in messages:
                st.info(f"**{msg['author']}** ({msg['date']})\n{msg['message']}")
        
        with col2:
            st.markdown("### 추모 통계")
            st.metric("방문자 수", "234명")
            st.metric("추모 메시지", "18개")
            st.metric("공유 횟수", "12회")
    
    with tab2:
        st.subheader("반려동물 상실 심리 상담")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**상담 신청**")
            counsel_type = st.selectbox("상담 방식", ["화상 상담", "전화 상담", "채팅 상담"])
            prefer_time = st.selectbox("희망 시간대", ["오전", "오후", "저녁", "심야"])
            urgency = st.select_slider("긴급도", ["보통", "빠른", "긴급"])
            
            concern = st.text_area("상담 내용", height=100, 
                                 placeholder="어떤 마음으로 상담을 받고 싶으신가요?")
            
            if st.button("상담 신청하기"):
                st.success("상담 신청이 완료되었습니다. 24시간 내 연락드리겠습니다.")
        
        with col2:
            st.markdown("**자가 진단 체크리스트**")
            
            symptoms = [
                "식욕이나 수면 패턴의 변화",
                "집중력 저하나 일상생활 어려움",
                "극도의 슬픔이나 우울감",
                "죄책감이나 후회",
                "사회적 위축"
            ]
            
            checked_symptoms = []
            for symptom in symptoms:
                if st.checkbox(symptom):
                    checked_symptoms.append(symptom)
            
            if len(checked_symptoms) >= 3:
                st.warning("⚠️ 전문 상담을 권장합니다.")
            elif len(checked_symptoms) >= 1:
                st.info("💙 자연스러운 반응입니다. 필요시 상담받으세요.")

# 6. 새 가족 매칭
elif menu == "🏡 새 가족 매칭":
    st.title("🏡 새 가족 매칭")
    
    tab1, tab2, tab3 = st.tabs(["🔍 매칭 찾기", "📋 등록하기", "📊 매칭 현황"])
    
    with tab1:
        st.subheader("성향 분석 기반 매칭")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**희망 조건**")
            desired_pet = st.selectbox("반려동물 종류", ["강아지", "고양이", "기타"])
            desired_age = st.selectbox("희망 나이", ["새끼", "성견/성묘", "노견/노묘", "상관없음"])
            desired_size = st.selectbox("크기", ["소형", "중형", "대형", "상관없음"])
            
            lifestyle = st.multiselect("생활 패턴", 
                                     ["활동적", "조용함", "규칙적", "자유로운", "가족 중심"])
            
            experience = st.radio("반려동물 경험", ["초보", "경험있음", "전문가급"])
            
            if st.button("매칭 검색"):
                st.success("조건에 맞는 반려동물을 찾았습니다!")
        
        with col2:
            st.markdown("**추천 매칭 결과**")
            
            # 매칭 결과 시뮬레이션
            matches = [
                {"name": "바둑이", "age": "2살", "breed": "믹스", "location": "서울 강남", "match": 95},
                {"name": "나비", "age": "3살", "breed": "코리아 숏헤어", "location": "서울 홍대", "match": 88},
                {"name": "몽이", "age": "1살", "breed": "포메라니안", "location": "경기 성남", "match": 82}
            ]
            
            for match in matches:
                with st.container():
                    col_a, col_b, col_c = st.columns([2, 2, 1])
                    with col_a:
                        st.markdown(f"**{match['name']}** ({match['age']})")
                        st.caption(f"{match['breed']} | {match['location']}")
                    with col_b:
                        st.progress(match['match']/100)
                        st.caption(f"매칭률: {match['match']}%")
                    with col_c:
                        st.button("연락하기", key=f"contact_{match['name']}")
                    st.divider()
    
    with tab2:
        st.subheader("분양/입양 동물 등록")
        
        col1, col2 = st.columns(2)
        
        with col1:
            reg_name = st.text_input("동물 이름")
            reg_breed = st.text_input("품종")
            reg_age = st.number_input("나이", min_value=0, max_value=20)
            reg_gender = st.selectbox("성별", ["수컷", "암컷"])
            
        with col2:
            reg_personality = st.multiselect("성격", 
                                           ["활발한", "온순한", "사교적", "독립적", "애교많은"])
            reg_health = st.selectbox("건강 상태", ["매우 좋음", "좋음", "보통", "주의 필요"])
            reg_vaccination = st.checkbox("예방접종 완료")
            reg_neutering = st.checkbox("중성화 수술 완료")
        
        reg_description = st.text_area("상세 설명", height=100)
        reg_photos = st.file_uploader("사진 업로드", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
        
        contact_info = st.text_input("연락처")
        
        if st.button("등록하기"):
            st.success("등록이 완료되었습니다!")
    
    with tab3:
        st.subheader("매칭 성과 대시보드")
        
        # 매칭 통계 차트
        col1, col2 = st.columns(2)
        
        with col1:
            # 월별 매칭 성공률 - 간단한 bar chart
            months = ['1월', '2월', '3월']
            success_rate = [85, 89, 92]
            
            chart_data = pd.DataFrame({
                '월': months,
                '매칭 성공률(%)': success_rate
            })
            
            st.subheader("월별 매칭 성공률")
            st.bar_chart(chart_data.set_index('월'))
        
        with col2:
            # 동물 종류별 분포 - 간단한 표
            st.subheader("등록 동물 분포")
            pet_data = pd.DataFrame({
                '동물 종류': ['강아지', '고양이', '기타'],
                '등록 수': [45, 32, 8]
            })
            st.dataframe(pet_data, use_container_width=True)
        
        # 최근 성공 매칭
        st.subheader("최근 성공 매칭")
        success_matches = pd.DataFrame({
            '날짜': ['2024-03-10', '2024-03-09', '2024-03-08'],
            '동물명': ['코코', '나비', '몽실이'],
            '새 가족': ['김○○님', '이○○님', '박○○님'],
            '지역': ['서울', '경기', '부산']
        })
        
        st.dataframe(success_matches, use_container_width=True)

# 푸터
st.sidebar.markdown("---")
st.sidebar.info("PetWellbeing v1.0\n고객 지원: help@petwellbeing.com")
