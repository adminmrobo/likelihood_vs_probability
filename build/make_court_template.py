import re
s=open('build/template.html',encoding='utf-8').read()
def between(a,b,new):
    global s
    i=s.index(a); j=s.index(b,i)
    s=s[:i]+new+s[j:]
def rep(a,b,cnt=1):
    global s
    assert a in s, a[:60]
    s=s.replace(a,b,cnt)

# 머리
rep('<title>확률 vs 가능도(우도) — 초파리의 케이크 상자 | 고급통계 연구실</title>','<title>케이크 상자 재판 — 확률과 가능도(우도) 법정편 | 고급통계 연구실</title>')
rep('<meta property="og:title" content="확률 vs 가능도(우도) — 초파리의 케이크 상자">','<meta property="og:title" content="케이크 상자 재판 — 그 확률, 모순입니다!">')
rep('content="같은 숫자 표를 가로로 읽으면 확률, 세로로 읽으면 가능도(우도). 케이크 상자와 야근 판결로 따라가는 통계 입문 연구실 해설."','content="검사 초파리의 증언 속 모순을 증거로 찾아내며 배우는 확률과 가능도(우도). 법정 형식의 통계 입문 연구실 해설."')
# 추가 CSS
rep('.jt{border-bottom','''.court{border:2px solid #2b2d42;border-radius:14px;padding:16px;background:#fff;margin:16px 0}
.court h4{margin:0 0 8px;color:#2b2d42}
.testi{list-style:none;padding:0;margin:8px 0;counter-reset:t}
.testi li{border:1px solid var(--rule);border-radius:10px;padding:10px 12px;margin:6px 0;background:var(--panel);cursor:pointer}
.testi li[aria-pressed=true]{border:2px solid #e0a400;background:#fffbea}
.testi li:before{counter-increment:t;content:"증언 " counter(t) "  ";font-weight:700;color:var(--c-fly)}
.evi{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}
.evi button{border-style:dashed}
.bang{display:none;font-size:clamp(26px,5vw,42px);font-weight:700;color:#fff;background:var(--c-asst);border:4px solid #16212b;border-radius:16px;padding:6px 18px;transform:rotate(-3deg);margin:10px 0;text-align:center;box-shadow:4px 4px 0 #16212b}
.bang.on{display:inline-block}
.seat{font-size:13px;font-weight:700;color:#fff;background:#2b2d42;border-radius:6px;padding:0 6px;margin-left:6px}
.jt{border-bottom''')
# 내비
between('<nav class="top"','</nav>','''<nav class="top" aria-label="페이지 목차">
  <a class="logo" href="#top">고급통계 연구실 · 법정편</a>
  <a href="#intro">사건 개요</a><a href="#cast">법정 배치</a><a href="#map">증거물 1</a>
  <a href="#lv1">제1 증거</a><a href="#lv2">제2 증거</a><a href="#lv3">증언 흔들기</a><a href="#lv4">변호 반론</a>
  <a href="#duel">쟁점</a><a href="#lv5">2막 뒤집힌 법정</a><a href="#sum">정리</a><a href="#outro">폐정</a><a href="index.html">기본판 보기</a>
''')
rep('<span class="cover-chip">고급통계 연구실 · 확률 vs 가능도</span>','<span class="cover-chip">고급통계 연구실 · 케이크 상자 재판</span>')
# 히어로
between('<header class="hero">','<main>','''<header class="hero">
<div class="wrap">
  <div class="kicker">고급통계 연구실 · 법정편 · 확률과 가능도(우도)</div>
  <h1>케이크 상자 재판<br>— 그 확률, 모순입니다!</h1>
  <p class="q">검사 초파리의 증언: “10번 중 7번 나왔으니, 이 상자가 ‘0.7 상자’일 확률은 26.7%다.” 이 증언, 믿어도 될까요?</p>
  <p>연구실 간식 테이블에서 사건이 벌어졌습니다. 초파리 연구원이 케이크 상자를 걸고 인턴 시아·모아에게 숫자 증언을 내밀었어요. 변호인 하루와 감정인 주판봇이 <b>증거(숫자 표)</b>로 그 증언의 <b>모순</b>을 찾아냅니다. 열쇠는 하나, 같은 표를 <b>가로로 읽으면 확률, 세로로 읽으면 가능도</b>라는 것. 2막에서는 법정이 뒤집혀 초파리가 피고석에 앉습니다.</p>
  <div class="kpis">
    <div class="kpi g"><b>1.000</b><span>증거 A · 가로줄(확률) 합</span></div>
    <div class="kpi r"><b>0.450</b><span>증거 B · 세로줄(가능도) 합</span></div>
    <div class="kpi m"><b>1/11</b><span>증거 C · 가능도 곡선 넓이</span></div>
    <div class="kpi a"><b>59.2%</b><span>1막 판결 · 0.7 상자일 확률</span></div>
    <div class="kpi i"><b>93%</b><span>2막 판결 · 야근 사후확률</span></div>
  </div>
  <p class="note">숫자는 모두 이 페이지의 예시값이며, 이항분포 공식으로 다시 계산한 값입니다(소수 셋째 자리 반올림). 등장하는 재판은 연구실 안의 놀이이며 실제 법 절차와 다릅니다.</p>
  <div class="talk">
    <div class="say" data-who="doc"><img class="who" data-who="doc" data-mood="think" alt="" aria-hidden="true"><div><b class="name">박사 <span class="seat">판사</span></b><p>지금부터 ‘케이크 상자 사건’ 재판을 시작합니다. 판결은 숫자로 내립니다.</p></div></div>
    <div class="say" data-who="fly"><img class="who flip" data-who="fly" data-mood="point" alt="" aria-hidden="true"><div><b class="name">초파리 연구원 <span class="seat">검사</span></b><p>약속은 ‘0.7 상자일 확률이 50%를 넘으면 케이크를 준다’였지. 그런데 겨우 26.7%야. 우도로 보면 안 주고, 가능도로 보면… 글쎄?</p></div></div>
    <div class="say" data-who="asst"><img class="who" data-who="asst" data-mood="firm" alt="" aria-hidden="true"><div><b class="name">조수 하루 <span class="seat">변호인</span></b><p>변호인, 준비 완료했습니다. 시아와 모아는 10번 눌러서 7번 받았을 뿐이에요.</p></div></div>
    <div class="say" data-who="robo"><img class="who" data-who="robo" data-mood="calc" alt="" aria-hidden="true"><div><b class="name">주판봇 <span class="seat">감정인</span></b><p>숫자 감정은 내 주판에 맡겨. 표를 가로로 읽을지 세로로 읽을지부터 정리하자.</p></div></div>
  </div>
</div>
</header>

''')
# 사건 개요
between('<section id="intro">','<section id="cast">','''<section id="intro"><div class="wrap">
  <div class="box3">
    <h2 style="font-size:24px">사건 개요 — 이 페이지를 3줄로</h2>
    <ol>
      <li><b>무엇을:</b> 같은 숫자 표를 가로로 읽으면 <span class="jt" data-g="확률">확률</span>, 세로로 읽으면 <span class="jt" data-g="가능도">가능도</span>(우도)입니다. 초파리의 증언은 이 둘을 바꿔 읽었어요.</li>
      <li><b>왜 중요한가:</b> 이 실수는 실제 법정에서도 이름이 붙을 만큼 흔해서 <span class="jt" data-g="검사의 오류">검사의 오류</span>라고 불립니다<sup>[3]</sup>. 보고서와 AI 답변에서도 자주 보여요.</li>
      <li><b>업무에서는:</b> 불량률·클릭률을 데이터로 추정할 때, 머신러닝 모델을 학습시킬 때 쓰는 것이 가능도입니다.</li>
    </ol>
    <p style="margin:.4em 0 0"><b>코드·수식을 몰라도 됩니다.</b> 증거물은 버튼으로 직접 확인하고, 수식 옆에서는 변호인 하루가 대신 질문해요.</p>
    <p style="margin:.4em 0 0"><b>사건의 약속:</b> 초파리가 고른 상자가 ‘0.7 상자’일 확률이 50%를 넘으면, 케이크는 시아·모아에게 갑니다.</p>
    <details class="abbr"><summary>기호·영어 약어 풀이 (접기)</summary>
      <ul>
        <li><b>θ</b>(세타): 상자가 케이크를 줄 확률. 상자의 ‘성격’을 나타내는 숫자(모수)예요.</li>
        <li><b>n, k</b>: 누른 횟수(10)와 케이크를 받은 횟수(7).</li>
        <li><b>P(A | B)</b>: “B라고 정해 두면 A일 확률”. 세로 막대는 나누기가 아니라 ‘조건’이에요.</li>
        <li><b>L(θ)</b>: likelihood(가능도·우도). 결과를 고정하고 θ를 바꿔 가며 보는 점수.</li>
        <li><b>θ̂</b>(세타 햇): 데이터로 추정한 θ. <b>MLE</b>는 Maximum Likelihood Estimation, 최대가능도 추정.</li>
      </ul>
    </details>
  </div>
</div></section>

''')
# 법정 배치
between('<section id="cast">','<section id="why">','''<section id="cast"><div class="wrap">
  <h2>법정 배치와 이 페이지 사용법</h2>
  <div class="cast">
    <div class="card"><img data-who="doc" data-mood="front" alt="" aria-hidden="true"><div><b>박사 · 판사</b><small>판결은 박사만. 기준은 언제나 숫자입니다.</small></div></div>
    <div class="card"><img data-who="asst" data-mood="smile" alt="" aria-hidden="true"><div><b>조수 하루 · 변호인</b><small>증거를 내밀고 모순을 지적해요. 수식도 대신 질문합니다.</small></div></div>
    <div class="card"><img data-who="robo" data-mood="smile" alt="" aria-hidden="true"><div><b>주판봇 · 감정인</b><small>숫자를 감정합니다. 다만 결론이 조금 빠른 편.</small></div></div>
    <div class="card"><img class="flip" data-who="fly" data-mood="clip" alt="" aria-hidden="true"><div><b>초파리 연구원 · 검사</b><small>1막의 증언자. 2막에서는 피고석으로…</small></div></div>
    <div class="card"><img data-who="sia" data-mood="smile" alt="" aria-hidden="true"><div><b>인턴 시아 · 방청석</b><small>케이크를 조용히 기다리다 가끔 졸아요.</small></div></div>
    <div class="card"><img data-who="moa" data-mood="smile" alt="" aria-hidden="true"><div><b>인턴 모아 · 방청석</b><small>응원 담당. 차와 케이크를 챙깁니다.</small></div></div>
  </div>
  <p>재판은 <b>증거 제출(①②) → 증언 흔들기(③) → 변호 반론(④) → 쟁점 정리(대결) → 판결</b> 순서로 갑니다. 노란 점선 밑줄 단어를 누르면 뜻이 나오고, 회색 상자의 버튼과 슬라이더로 증거를 직접 확인할 수 있어요.</p>
</div></section>

''')
# 왜
rep('<h2>왜 이 주제인가</h2>','<h2>왜 이 사건인가</h2>')
rep('<div class="card"><h3>③ 바꿔 읽는 실수가 흔하다</h3><p>“이 결과가 나올 확률”과 “이 원인일 확률”을 바꿔 말하는 실수는 사람도, AI도 자주 합니다. 이번 페이지의 핵심 연습이에요.</p></div>',
    '<div class="card"><h3>③ 실제 법정에서도 생긴 실수</h3><p>“무죄라면 이런 증거가 나올 확률”을 “무죄일 확률”로 바꿔 말하는 실수에는 1987년 논문이 붙인 이름이 있어요. 바로 ‘검사의 오류’입니다<sup>[3]</sup>. 사람도, AI도 자주 합니다.</p></div>')
# 큰 그림
rep('<h2>큰 그림 — 표는 하나, 읽는 방향은 둘</h2>','<h2>증거물 1 — 케이크 표: 표는 하나, 읽는 방향은 둘</h2>')
rep('<span class="tag">① 확률: 상자 고정</span><span class="tag">→ ② 가능도: 결과 고정</span><span class="tag">→ ③ 바꿔 읽는 함정</span><span class="tag">→ ④ 가능도로 비교하기</span><span class="tag">→ ⑤ 사전 × 가능도 = 사후</span>',
    '<span class="tag">제1 증거: 가로줄 = 확률</span><span class="tag">→ 제2 증거: 세로줄 = 가능도</span><span class="tag">→ 증언 흔들기: 모순 지적</span><span class="tag">→ 변호 반론: 가능도로 비교</span><span class="tag">→ 2막: 사전 × 가능도 = 사후</span>')
# 단계 제목
rep('<span class="hexn">1</span>상자를 고정하면 — 확률</h2>','<span class="hexn">1</span>제1 증거 · 감정인의 가로줄 — 확률</h2>')
rep('<span class="hexn">2</span>결과를 고정하면 — 가능도(우도)</h2>','<span class="hexn">2</span>제2 증거 · 변호인의 세로줄 — 가능도(우도)</h2>')
rep('<span class="hexn">3</span>바꿔 읽는 함정 — 26.7%의 정체</h2>','<span class="hexn">3</span>증언 흔들기 — 그 26.7%, 모순입니다!</h2>')
rep('<span class="hexn">4</span>가능도로 할 수 있는 일 — 비교와 최대가능도</h2>','<span class="hexn">4</span>변호인의 반론 — 가능도로 할 수 있는 일</h2>')
rep('<h2>대결 — 세로줄을 1로 맞추면 ‘상자의 확률’이 될까?</h2>','<h2>쟁점 정리 — 세로줄을 1로 맞추면 ‘상자의 확률’이 될까?</h2>')
rep('<span class="hexn">5</span>2막: 역습 — 사전 × 가능도 = 사후, 그리고 야근</h2>','<span class="hexn">5</span>2막 뒤집힌 법정 — 피고석의 초파리, 사전 × 가능도 = 사후</h2>')
rep('<h4>실험 ① 상자를 정하고 10번 조르기</h4>','<h4>증거 확인 ① 상자를 정하고 10번 조르기</h4>')
rep('<h4>실험 ② 결과를 고정하고 상자 후보 심문하기</h4>','<h4>증거 확인 ② 결과를 고정하고 상자 후보 심문하기</h4>')
rep('<h4>실험 ③ 가능도 곡선 아래 넓이 재기</h4>','<h4>증거 확인 ③ 가능도 곡선 아래 넓이 재기 (증거 C)</h4>')
rep('<h4>실험 ④ 두 상자 맞대기</h4>','<h4>증거 확인 ④ 두 상자 맞대기</h4>')
rep('<h4>실험 ⑤ 야근 판결기</h4>','<h4>2막 판결기 — 야근인가, 퇴근인가</h4>')
# 단계 대화 이름표에 법정 자리
for who,seat in [('박사','판사'),('조수 하루','변호인'),('주판봇','감정인'),('초파리 연구원','검사')]:
    s=s.replace('<b class="name">'+who+'</b>','<b class="name">'+who+' <span class="seat">'+seat+'</span></b>')
# lv3: 증언 흔들기 게임 (실험 패널 앞)
rep('''  <div class="panel">
    <h4>증거 확인 ③''','''  <div class="court" id="trial">
    <h4>법정 — 검사 초파리의 증언</h4>
    <p class="note">증언 하나를 누르고, 그 증언과 맞지 않는 증거를 내밀어 보세요. 맞는 증언과 증거를 고르면 모순이 드러납니다.</p>
    <ol class="testi" id="testi">
      <li tabindex="0" role="button" aria-pressed="false" data-s="0">시아·모아는 상자 넷 중 하나를 10번 눌렀고, 케이크가 7번 나왔다.</li>
      <li tabindex="0" role="button" aria-pressed="false" data-s="1">0.7 상자라면, 10번 중 7번 나올 확률은 0.267이다.</li>
      <li tabindex="0" role="button" aria-pressed="false" data-s="2">그러므로 이 상자가 0.7 상자일 확률은 26.7%다. 케이크는 못 준다.</li>
    </ol>
    <div class="evi" role="group" aria-label="증거 고르기">
      <button class="bt" data-ev="A">증거 A · 가로줄 합 1.000</button>
      <button class="bt" data-ev="B">증거 B · 세로줄 합 0.450</button>
      <button class="bt" data-ev="C">증거 C · 곡선 넓이 1/11</button>
    </div>
    <div class="bang" id="bang" aria-hidden="true">그 증언, 모순입니다!</div>
    <div class="mini"><img id="trialImg" data-who="asst" data-mood="firm" alt="" aria-hidden="true"><p id="trialFb" aria-live="polite">변호인 하루: 증언을 먼저 골라 주세요.</p></div>
  </div>
  <div class="panel">
    <h4>증거 확인 ③''')
rep('<h4>AI 판단 코너 — 이 답변, 그대로 믿어도 될까?</h4>','<h4>AI 판단 코너 — 법정 밖의 같은 증언: 이 AI 답변, 믿어도 될까?</h4>')
# lv3 현장 상자 추가(풀이 앞)
rep('''  <div class="explain">
    <h4>풀이</h4>
    <ol>
      <li>0.267 = P(7개 | 0.7 상자).''','''  <div class="bridge field"><h4>현장에 옮기면 — 진짜 법정의 ‘검사의 오류’</h4><p>Thompson과 Schumann(1987)은 형사재판에서 “무죄인 사람에게서 이런 증거가 나올 확률”을 “피고가 무죄일 확률”로 바꿔 말하는 실수를 ‘검사의 오류’라고 이름 붙였어요<sup>[3]</sup>. 요즘 법과학에서는 이 실수를 피하려고 결론을 가능도 비율로 보고하자는 논의가 이어집니다<sup>[4]</sup>. 바로 ④에서 다룰 도구예요.</p><p class="lm">비유의 한계: 이 페이지의 재판은 놀이입니다. 실제 재판의 증거 평가는 법과 절차를 따릅니다.</p></div>
  <div class="explain">
    <h4>풀이</h4>
    <ol>
      <li>0.267 = P(7개 | 0.7 상자).''')
# 대결 → 쟁점 정리 문구
rep('<p>세로줄 합이 0.450이니, 각 값을 0.450으로 나누면 합이 1이 됩니다. 그러면 0.267 ÷ 0.450 ≈ 59%를 “0.7 상자일 확률”이라고 불러도 될까요?</p>',
    '<p>증언이 무너지자 감정인 주판봇이 새 계산을 내밉니다. 세로줄 합이 0.450이니, 각 값을 0.450으로 나누면 합이 1이 된다는 것. 그러면 0.267 ÷ 0.450 ≈ 59%를 “0.7 상자일 확률”이라고 불러도 될까요? 판사 박사가 쟁점으로 올립니다.</p>')
# 쟁점 뒤 1막 판결
rep('''<!-- ⑤ -->''','''<section id="verdict1"><div class="wrap">
  <div class="court">
    <h4>1막 판결</h4>
    <div class="talk">
      <div class="say" data-who="fly"><img class="who flip" data-who="fly" data-mood="coffee" alt="" aria-hidden="true"><div><b class="name">초파리 연구원 <span class="seat">검사</span></b><p>…상자는 주사위로 골랐어. 넷 다 똑같이.</p></div></div>
      <div class="say" data-who="doc"><img class="who" data-who="doc" data-mood="judge" alt="" aria-hidden="true"><div><b class="name">박사 <span class="seat">판사</span></b><p>그렇다면 가정 A가 성립한다. 0.7 상자일 확률은 59.2%, 약속한 50%를 넘었다. 케이크는 시아·모아에게 간다.</p></div></div>
      <div class="say" data-who="moa"><img class="who" data-who="moa" data-mood="sparkle" alt="" aria-hidden="true"><div><b class="name">인턴 모아 <span class="seat">방청석</span></b><p>와아, 감사합니다! 시아, 일어나요. 케이크예요!</p></div></div>
    </div>
  </div>
</div></section>

<!-- ⑤ -->''')
# 2막 도입
rep('<p>초파리가 상자를 주사위로 골랐다고 실토했어요. 그러니 가정 A, 0.7 상자일 확률은 59.2%. 약속한 50%를 넘었으니 케이크는 시아·모아 몫입니다. 그런데 초파리, 이번 주 일감 10개 중 3개만 끝냈더군요?</p>',
    '<p>휴정 뒤 2막을 엽니다. 이번 피고는 초파리 연구원. 이번 주 일감 10개 중 3개만 끝냈다는 기록이 들어왔습니다.</p>')
rep('<p>가능도는 확률이 아니잖아! 그걸로는 나를 판결 못 해!</p>','<p>변론하겠습니다! 가능도는 확률이 아니잖아! 그걸로는 나를 판결 못 해!</p>')
rep('<p>맞아요, 잘 배웠네요. 그래서 지원군을 불렀습니다. 평소 기록을 함께 보면 확률로 말할 수 있거든요.</p>','<p>그 주장, 인정합니다. 1막에서 잘 배웠군요. 그래서 증인을 불렀습니다. 평소 기록을 함께 보면 확률로 판결할 수 있어요.</p>')
s=s.replace('<b class="name">초파리 연구원 <span class="seat">검사</span></b><p>변론하겠습니다!','<b class="name">초파리 연구원 <span class="seat">피고</span></b><p>변론하겠습니다!')
rep('>지원군 부르기</button>','>비공개 증인 부르기</button>')
rep("this.textContent=on?'지원군 숨기기':'지원군 부르기'","this.textContent=on?'증인 돌려보내기':'비공개 증인 부르기'")
rep('<small>(…) 지난달 근무 기록을 내민다 → <b>사전분포</b></small>','<small>(…) 증거로 지난달 근무 기록 제출 → <b>사전분포</b></small>')
rep('<small>(반짝) 이번 주 기록을 읽는다 → <b>가능도</b></small>','<small>(반짝) 이번 주 기록을 감정 → <b>가능도</b></small>')
rep('<small>(딸랑) 곱해서 합 1로 맞춘다 → <b>사후분포</b></small>','<small>(딸랑) 곱해서 합 1로 맞춤 → <b>사후분포</b></small>')
rep('<p>여기서 θ는 초파리의 <b>일 처리 모드</b>','<p class="explain" style="background:var(--info-soft);border-left-color:var(--info)"><b>이 재판의 판결 방식:</b> 가설검정을 재판에 빗댈 때는 “무죄 추정(귀무가설)에서 출발해 증거가 충분하면 유죄”로 설명하곤 해요. 이 2막은 그것과 다릅니다. 사전분포와 가능도로 <b>사후확률</b>을 계산하고, 그 확률이 기준(90%)을 넘는지로 판결하는 베이즈 방식이에요. p값은 쓰지 않습니다.</p>\n  <p>여기서 θ는 초파리의 <b>일 처리 모드</b>')
# 2막 대화 재배치 (피고)
s=s.replace('<p>내 평소 기록은 훌륭하다고! ‘초파리 주장’ 기록으로 바꿔 봐.</p>','<p>이의를 제기합니다! 내 평소 기록은 훌륭하다고. ‘초파리 주장’ 기록으로 바꿔 봐.</p>')
# 2막 좌석
i=s.index('<!-- ⑤ -->');j=s.index('<!-- 정리 -->')
s=s[:i]+s[i:j].replace('<span class="seat">검사</span>','<span class="seat">피고</span>')+s[j:]
# 폐정
between('<section id="outro">','</main>','''<section id="outro"><div class="wrap">
  <h2>폐정</h2>
  <div class="talk">
    <div class="say" data-who="doc"><img class="who" data-who="doc" data-mood="judge" alt="" aria-hidden="true"><div><b class="name">박사 <span class="seat">판사</span></b><p>이것으로 폐정합니다. 판결 요지 세 줄. ① 가로줄은 확률, 세로줄은 가능도. ② 가능도는 비교 점수라 합이 1일 이유가 없다. ③ 확률로 말하려면 사전 정보를 곱해 사후분포를 만든다.</p></div></div>
    <div class="say" data-who="robo"><img class="who" data-who="robo" data-mood="happy" alt="" aria-hidden="true"><div><b class="name">주판봇 <span class="seat">감정인</span></b><p>세로줄 나누기는 주사위 가정 덕에 통했어. 가정 없이는 감정서를 못 쓴다는 것도 배웠고. 반만 본전이야.</p></div></div>
    <div class="say" data-who="fly"><img class="who flip" data-who="fly" data-mood="cry" alt="" aria-hidden="true"><div><b class="name">초파리 연구원 <span class="seat">피고</span></b><p>…검사로 이길 줄 알았는데 피고로 야근이라니. 인정.</p></div></div>
    <div class="say" data-who="asst"><img class="who" data-who="asst" data-mood="proud" alt="" aria-hidden="true"><div><b class="name">조수 하루 <span class="seat">변호인</span></b><p>다음에 “○○일 확률”이라는 증언을 들으면, 무엇을 고정했는지부터 물어봐 주세요. 그게 가장 강한 증거예요.</p></div></div>
  </div>
  <p class="note">같은 내용을 법정 형식 없이 보려면 <a href="index.html">기본판</a>을 보세요.</p>
</div></section>
''')
# 출처 추가
rep('''<tr><td>[2]</td>''','''<tr><td>[3]</td><td style="text-align:left">Thompson, W. C., &amp; Schumann, E. L. (1987). Interpretation of statistical evidence in criminal trials: The prosecutor's fallacy and the defense attorney's fallacy. Law and Human Behavior, 11(3), 167–187.</td><td style="text-align:left">‘검사의 오류’라는 이름과 뜻</td></tr>
    <tr><td>[4]</td><td style="text-align:left">The Prosecutor's Fallacy and Expert Testimony: A Modern Take Using Likelihood Ratios. arXiv:2502.03217 (2025). <a href="https://arxiv.org/abs/2502.03217">링크</a></td><td style="text-align:left">법과학 보고에서 가능도 비율 사용 논의</td></tr>
    <tr><td>[2]</td>''')
rep('<p><b>예시값·설명용 모형인 것:</b>','<p><b>재판에 대해:</b> 이 페이지의 재판은 연구실 안의 놀이 형식이며, 특정 게임·작품의 등장인물이나 장면과 관계가 없고, 실제 법 절차와 다릅니다.</p>\n  <p><b>예시값·설명용 모형인 것:</b>')
# 용어 추가
rep("'정규화':['정규화','계산','값들을 모두 더한 값으로 나눠 합을 1로 맞추는 일.',0]","'정규화':['정규화','계산','값들을 모두 더한 값으로 나눠 합을 1로 맞추는 일.',0],\n '검사의 오류':['검사의 오류 (prosecutor\\'s fallacy)','오류','“무죄라면 이 증거가 나올 확률”을 “무죄일 확률”로 바꿔 읽는 실수. P(증거|무죄)와 P(무죄|증거)를 혼동하는 것.',1]")
# 증언 게임 스크립트
rep("/* ── 용어 말풍선 ── */","""/* ── 증언 흔들기 ── */
(function(){var sel=null,done=false;var FB={
  '0':'증언 1은 사실 그대로예요. 시아·모아도 10번 중 7번을 인정해요. 다른 증언을 흔들어 보세요.',
  '1':'증언 2는 감정 결과와 같아요. 0.7 상자를 고정했을 때 7번의 확률이 0.267인 건 맞습니다. 모순은 다른 곳에 있어요.',
  '2A':'증거 A(가로줄 합 1)는 상자를 고정했을 때의 이야기라, 이 증언을 직접 무너뜨리지는 못해요. 상자 쪽을 움직인 증거를 찾아보세요.'};
  function say(t,m){$('#trialFb').textContent='변호인 하루: '+t;Cast.set($('#trialImg'),'asst',m||'report')}
  $$('#testi li').forEach(function(li){function pick(){$$('#testi li').forEach(function(z){z.setAttribute('aria-pressed','false')});li.setAttribute('aria-pressed','true');sel=li.dataset.s;if(!done)say('증언 '+(+sel+1)+'을 골랐어요. 이제 맞지 않는 증거를 내밀어 보세요.','firm')}
    li.addEventListener('click',pick);li.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();pick()}})});
  $$('[data-ev]').forEach(function(b){b.onclick=function(){if(sel===null){say('증언을 먼저 골라 주세요.','firm');return}var ev=b.dataset.ev;
    if(sel!=='2'){say(FB[sel],'smile');return}
    if(ev==='A'){say(FB['2A'],'smile');return}
    done=true;$('#bang').classList.add('on');say(ev==='B'?'세로줄 합은 0.450이에요. 상자 후보의 값을 더해도 1이 안 되니, 0.267은 ‘상자의 확률’이 될 수 없어요. 0.267은 0.7 상자라면 7번이 나올 확률일 뿐이에요!':'가능도 곡선 넓이는 1/11이에요. θ에 대한 확률분포라면 넓이가 1이어야 하죠. 0.267을 ‘0.7 상자일 확률’로 읽은 증언은 모순입니다!','spark');
    var fi=$$('#lv3 .say[data-who=fly] img.who')[0];if(fi)Cast.set(fi,'fly','cry')}});
})();

/* ── 용어 말풍선 ── */""")
open('build/template_court.html','w',encoding='utf-8').write(s)
print('ok')
