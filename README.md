# Jump-up
# 국립한밭대학교 컴퓨터공학과 Hyeum팀

**팀 구성**
- 국립한밭대학교 컴퓨터공학과 옥주용
- 국립한밭대학교 컴퓨터공학과 김영권
- 국립한밭대학교 컴퓨터공학과 길지훈
- 국립한밭대학교 컴퓨터공학과 채성수
- 국립한밭대학교 컴퓨터공학과 육종범
<ul>
  <li>백엔드 개발자: 채성수 (API 설계 및 데이터 처리)</li>
  <li>백엔드 개발자: 육종범 (서버 최적화 및 데이터베이스 설계)</li>
  <li>WEB 및 안드로이드 프론트엔드 개발자: 옥주용 (UI/UX 설계)</li>
  <li>WEB 및 안드로이드 프론트엔드 개발자: 김영권 (기능 구현 및 디버깅)</li>
  <li>IOS 개발자: 길지훈 (iOS 플랫폼 연동 및 최적화)</li>
</ul>

## Project Background
<p><strong>일기 작성의 중요성:</strong> 연구에 따르면 일기는 스트레스와 불안을 관리하고 감정을 조절하며, 자아 성찰의 기회를 제공합니다. 그러나 현대인들이 일기를 쓰는 비율은 매우 낮습니다.</p>

<h4>문제점:</h4>
<ul>
  <li><strong>시간 부족:</strong> 바쁜 일상 속에서 일기를 쓸 여유가 부족함.</li>
  <li><strong>습관화 어려움:</strong> 일기를 꾸준히 작성하는 것이 쉽지 않음.</li>
  <li><strong>표현의 부담:</strong> 자신의 감정을 글로 옮기는 데 어려움을 느낌.</li>
</ul>

<h4>HyeEum의 솔루션:</h4>
<ul>
  <li><strong>대화형 일기 작성:</strong> ChatGPT를 활용하여 사용자에게 자연스러운 대화 경험 제공.</li>
  <li><strong>시각적 표현:</strong> DALL·E API를 통해 하루를 이미지로 표현.</li>
  <li><strong>감정 분석:</strong> 사용자의 감정을 수치화하고 시각화하여 정신 건강 상태를 파악.</li>
</ul>

<hr/>

## System Model
<h4>사용 기술스택</h4>
<ul>
  <li><strong>React:</strong> 컴포넌트 기반의 사용자 인터페이스(UI) 개발.</li>
  <li><strong>OpenAI API:</strong> ChatGPT를 활용한 대화형 기능과 DALL·E를 이용한 이미지 생성.</li>
  <li><strong>Spring:</strong> 서버와의 데이터 통신 및 API 개발.</li>
  <li><strong>PWA:</strong> 모바일 환경에서 네이티브 앱과 같은 경험 제공.</li>
  <li><strong>Module CSS:</strong> 컴포넌트 스타일링을 효율적이고 유지보수 가능하게 구현.</li>
</ul>

<h3>기술 개발에 필요했던 요구사항</h3>

<h4>주요 기술적 요구사항</h4>
<ul>
  <li><strong>대화형 인터페이스:</strong> ChatGPT API를 활용하여 자연스러운 대화 흐름 제공.</li>
  <li><strong>일기 요약 및 시각화:</strong> DALL·E API를 통해 일기를 이미지로 표현.</li>
  <li><strong>감정 분석 알고리즘:</strong> 사용자 감정을 분석하고 통계를 시각화.</li>
  <li><strong>PWA 구현:</strong> 다양한 디바이스에서 네이티브 앱과 유사한 사용자 경험 제공.</li>
</ul>

<h4>데이터베이스 설계</h4>
<img src="./Images/image03.png" alt="데이터베이스 설계도" style="width:100%; margin-top:10px;">
<p>
데이터베이스는 <strong>사용자(User)</strong>, <strong>일기(Book)</strong>, <strong>라이브러리(Library)</strong>, <strong>통계(Statistics)</strong>로 구성됩니다.
</p>
<ul>
  <li><strong>Library:</strong> 5개의 Book을 모아 저장하며, GPT API를 통해 통계 코멘트를 생성.</li>
  <li><strong>Book:</strong> 사용자가 작성한 일기 데이터, GPT API를 통한 감정(emotion), DALL·E로 생성된 이미지 URL 저장.</li>
  <li><strong>Statistics:</strong> 감정 데이터를 기반으로 사용자의 심리 상태를 시각화.</li>
</ul>

<h4>시스템 설계도</h4>
<img src="./Images/image04.png" alt="시스템 설계도" style="width:100%; margin-top:10px;">
<p>
백엔드는 HTTP 요청을 처리하며, 데이터는 Sqlite 데이터베이스에서 관리됩니다. OpenAI GPT API를 활용하여 질문 생성, 응답 처리, 통계 분석을 수행합니다. 프론트엔드는 CSR(Client Side Rendering) 방식으로 구성되어 사용자 경험을 강화합니다.
</p>

## Conclusion
<h3>4. 앱 화면 및 주요 기능</h3>

<h4>초기 화면</h4>
<img src="./Images/image08.png" alt="초기 화면" style="width:100%; margin-top:10px;">
<p>앱 설치 시 초기 설정 화면이 표시됩니다. 데이터베이스 조회를 통해 사용자의 존재 여부를 확인하여 첫 화면을 결정합니다.</p>

<h4>메인 페이지</h4>
<img src="./Images/image09.png" alt="메인 페이지" style="width:100%; margin-top:10px;">
<p>사용자가 기록한 일기와 생성된 이미지를 한눈에 볼 수 있습니다. 플러스 버튼을 눌러 새로운 일기를 작성할 수 있습니다.</p>

<h4>일기 작성 플로우</h4>
<img src="./Images/image10.png" alt="일기 작성" style="width:100%; margin-top:10px;">
<p>사용자의 성향과 기존 데이터를 기반으로 질문을 생성하여 GPT API에 요청합니다. 사용자는 응답을 통해 AI와 상호작용하며 일기를 완성합니다.</p>

<h4>통계 페이지</h4>
<img src="./Images/image11.png" alt="통계 페이지" style="width:100%; margin-top:10px;">
<p>사용자의 감정을 바탕으로 통계를 시각화합니다. 5회분의 일기를 기반으로 GPT API를 통해 심리 분석 코멘트를 제공합니다.</p>

<hr/>

## Project Outcome
<ul>
  <li><strong>대화형 일기 작성 UI:</strong> React 기반의 사용자 친화적 인터페이스.</li>
  <li><strong>일기 요약 및 시각적 표현:</strong> ChatGPT 및 DALL·E API를 통해 생성된 일기 요약과 이미지.</li>
  <li><strong>감정 분석 및 통계:</strong> 사용자의 심리 데이터를 분석하고 시각화.</li>
  <li><strong>모바일 최적화:</strong> PWA 기술을 활용한 접근성 강화.</li>
</ul>
<p>HyeEum은 단순한 기록 도구를 넘어, 사용자가 자신의 감정을 관리하고 긍정적인 정신 건강을 유지할 수 있도록 돕는 혁신적인 솔루션입니다.</p>
