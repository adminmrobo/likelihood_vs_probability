import sys
WARM_HTML='''<section id="warm"><div class="wrap">
  <h2>__H2__</h2>
  <p>큰 표를 보기 전에, 아주 작은 경우부터 손으로 세어 봅니다. 상자 하나를 <b>딱 한 번</b> 누르는 것에서 시작해요.</p>
  <div class="mini"><img data-who="robo" data-mood="calc" alt="" aria-hidden="true"><p><b>주판봇__SR__:</b> 한 번에 하나씩. 주판도 첫 알부터 튕기는 거야.</p></div>
  <div class="panel">
    <h4>준비 ① 한 번 누르기</h4>
    <div class="ctrl"><div class="group" role="group" aria-label="상자 고르기"><span class="glabel">상자</span>
      <button class="bt" data-w="0.3" aria-pressed="false">0.3 상자</button><button class="bt" data-w="0.7" aria-pressed="true">0.7 상자</button></div></div>
    <p id="w1" aria-live="polite"></p>
    <p class="note">θ(세타)는 “한 번 눌렀을 때 케이크가 나올 확률”이에요. 0.7 상자는 10번에 7번꼴로 케이크를 줍니다.</p>
  </div>
  <div class="panel">
    <h4>준비 ② 세 번 누르기 — 나올 수 있는 순서 8가지</h4>
    <p>세 번 누르면 케이크(<span class="ck">케</span>)와 빈 접시(<span class="pl">빈</span>)가 나오는 순서는 2 × 2 × 2 = 8가지예요. 순서마다 나온 차례대로 확률을 곱하고, 케이크 개수가 같은 순서끼리 묶어 더합니다.</p>
    <div class="tw"><table class="tb" id="wSeq" aria-label="세 번 누를 때 나올 수 있는 순서와 확률"></table></div>
    <div class="insight" aria-live="polite"><p class="g" id="w2"></p></div>
  </div>
  <div class="panel">
    <h4>준비 ③ 작은 표 — 상자 두 개 × 세 번</h4>
    <p>준비 ②의 맨 아래 줄을 두 상자에 대해 나란히 적으면 작은 표가 됩니다. 이 표를 가로로도, 세로로도 읽어 보세요.</p>
    <div class="ctrl"><div class="group" role="group" aria-label="작은 표 읽는 방향">
      <button class="bt" id="wRow" aria-pressed="true">가로로 읽기 (확률)</button>
      <button class="bt" id="wCol" aria-pressed="false">세로로 읽기 (가능도)</button></div></div>
    <div class="tw"><table class="tb" id="wTab" aria-label="상자 두 개, 세 번 누를 때의 작은 표"></table></div>
    <div class="insight" aria-live="polite"><p class="g" id="w3"></p></div>
  </div>
  <div class="mini"><img data-who="asst" data-mood="spark" alt="" aria-hidden="true"><p><b>__AN__:</b> 가로줄은 상자를 정해 두고 결과를 훑으니 합이 1, 세로줄은 결과를 정해 두고 상자를 훑으니 합이 아무 값이에요. 아래 __BIG__는 이 작은 표를 상자 네 개, 10번으로 키운 것뿐이에요.</p></div>
</div></section>

'''
WARM_CSS='''.ck,.pl{display:inline-block;min-width:1.6em;padding:0 4px;border-radius:4px;font-size:13px;font-weight:700;text-align:center;line-height:1.6}
.ck{background:#ffe1ec;color:#c42a6e;border:1px solid #e8a3bf}.pl{background:#eef2f6;color:#5b6874;border:1px solid #d5dbe2}
#wSeq td{min-width:64px}@media (max-width:520px){#wSeq .sq small{display:block;margin-bottom:4px}#wSeq th{font-size:13px}}
#wSeq td:last-child{min-width:96px;text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}#wSeq .sq{white-space:nowrap;display:inline-block;margin:2px 6px 2px 0}
#wTab td.c{cursor:pointer;min-width:60px}
#wTab td.c.hl{outline:3px solid var(--gfp);outline-offset:-3px;font-weight:700}
#wTab td.c.hc{outline:3px solid #e07a2c;outline-offset:-3px;font-weight:700}
'''
WARM_JS='''/* ── 준비: 한 번·세 번·작은 표 ── */
(function(){var th=0.7,mode='row',selR=1,selC=2,W2=[0.3,0.7];
  function seqs(){var o=[];for(var m=0;m<8;m++){var a=[(m>>2)&1,(m>>1)&1,m&1];o.push(a)}return o}
  function p3(k,t){return L(k,t,3)}
  function draw(){$$('[data-w]').forEach(function(b){b.setAttribute('aria-pressed',+b.dataset.w===th?'true':'false')});
    $('#w1').innerHTML='<span class="ck">케</span> 케이크: <b>'+th.toFixed(1)+'</b> &nbsp; · &nbsp; <span class="pl">빈</span> 빈 접시: <b>'+(1-th).toFixed(1)+'</b> &nbsp; → 둘을 더하면 1';
    var S=seqs(),h='<tr><th>케이크 개수</th><th>나올 수 있는 순서와 그 확률 (나온 순서대로 곱하기)</th><th>묶음 합 (순서 상관없이 더하기)</th></tr>';
    var T=th.toFixed(1),F=(1-th).toFixed(1);
    for(var k=0;k<=3;k++){var g=S.filter(function(a){return a[0]+a[1]+a[2]===k});var one=Math.pow(th,k)*Math.pow(1-th,3-k);
      var cells=g.map(function(a){return '<span class="sq">'+a.map(function(v){return v?'<span class="ck">케</span>':'<span class="pl">빈</span>'}).join('')+' <small>'+a.map(function(v){return v?T:F}).join('×')+' = '+one.toFixed(3)+'</small></span>'}).join('<br>');
      var sum=g.map(function(){return one.toFixed(3)}).join('<br>+ ')+'<br>= <b>'+p3(k,th).toFixed(3)+'</b>'+(g.length>1?'<br><small>(= '+g.length+' × '+one.toFixed(3)+')</small>':'');
      h+='<tr><td>'+k+'개</td><td style="text-align:left">'+cells+'</td><td>'+sum+'</td></tr>'}
    h+='<tr><th colspan="2">네 묶음을 모두 더하면</th><th>1.000</th></tr>';$('#wSeq').innerHTML=h;
    $('#w2').textContent='케이크 개수가 같은 순서들은 곱하는 순서만 다를 뿐 값이 같아요(빈빈케 = 빈케빈 = 케빈빈). 그래서 묶음 합은 “순서 상관없이 그 개수가 나올 확률”이고, 같은 값을 순서 수만큼 더한 것 = 순서 수 × 한 순서의 확률이에요. 이 순서 수(3)가 큰 표 공식의 ₁₀C₇ 자리에 들어가요.';
    var t='<tr><th>상자 \\\\ 케이크 개수</th><th>0개</th><th>1개</th><th>2개</th><th>3개</th><th>가로줄 합</th></tr>';
    W2.forEach(function(tt,i){t+='<tr><th>'+tt+' 상자</th>';for(var k=0;k<=3;k++)t+='<td class="c" data-r="'+i+'" data-k="'+k+'">'+p3(k,tt).toFixed(3)+'</td>';t+='<td><b>1.000</b></td></tr>'});
    t+='<tr><th>세로줄 합</th>';for(var k2=0;k2<=3;k2++)t+='<td><b>'+(p3(k2,.3)+p3(k2,.7)).toFixed(3)+'</b></td>';t+='<td></td></tr>';$('#wTab').innerHTML=t;
    $$('#wTab td.c').forEach(function(td){td.onclick=function(){if(mode==='row')selR=+td.dataset.r;else selC=+td.dataset.k;paint()}});paint()}
  function paint(){$$('#wTab td.c').forEach(function(td){td.classList.remove('hl','hc');if(mode==='row'&&+td.dataset.r===selR)td.classList.add('hl');if(mode==='col'&&+td.dataset.k===selC)td.classList.add('hc')});
    var n=$('#w3');if(mode==='row'){n.className='g';n.textContent='가로로 읽기: '+W2[selR]+' 상자를 정해 두고 0~3개를 훑으면 합이 1.000. 이것이 확률이에요. (다른 줄을 눌러 보세요)'}
    else{n.className='r';n.textContent='세로로 읽기: 케이크 '+selC+'개를 정해 두고 두 상자를 훑으면 '+p3(selC,.3).toFixed(3)+' + '+p3(selC,.7).toFixed(3)+' = '+(p3(selC,.3)+p3(selC,.7)).toFixed(3)+'. 1이 아니에요. 이것이 가능도예요. (다른 세로줄을 눌러 보세요)'}}
  $$('[data-w]').forEach(function(b){b.onclick=function(){th=+b.dataset.w;draw()}});
  $('#wRow').onclick=function(){mode='row';this.setAttribute('aria-pressed','true');$('#wCol').setAttribute('aria-pressed','false');paint()};
  $('#wCol').onclick=function(){mode='col';this.setAttribute('aria-pressed','true');$('#wRow').setAttribute('aria-pressed','false');paint()};
  draw();
})();

/* ── 큰 그림 표 ── */'''
def apply(path,court):
    s=open(path,encoding='utf-8').read()
    if 'id="warm"' in s: print('already',path);return
    h2='증거물 0 — 먼저 상자 하나, 세 번만 눌러 보기' if court else '준비 — 상자 하나, 세 번만 눌러 보기'
    html=WARM_HTML.replace('__H2__',h2).replace('__SR__',' <span class="seat">감정인</span>' if court else '').replace('__AN__','조수 하루 <span class="seat">변호인</span>' if court else '조수 하루').replace('__BIG__','증거물 1' if court else '큰 표')
    s=s.replace('<section id="map">',html+'<section id="map">',1)
    s=s.replace('.jt{border-bottom',WARM_CSS+'.jt{border-bottom',1)
    s=s.replace('/* ── 큰 그림 표 ── */',WARM_JS,1)
    old='<p>상자 네 개(θ = 0.3, 0.5, 0.7, 0.9)를 각각 10번 눌렀을 때, 케이크를 0~10번 받을 확률을 모두 계산한 표입니다. 아래 버튼으로 읽는 방향을 바꾸고, 줄을 눌러 보세요.</p>'
    new='<p>방금 본 작은 표(상자 2개 × 3번)를 그대로 키웠어요. 상자는 네 개(θ = 0.3, 0.5, 0.7, 0.9), 누르는 횟수는 10번, 케이크 개수는 0~10개입니다. 읽는 법은 똑같아요. 가로줄은 합이 1, 세로줄은 아무 값. 시아·모아가 실제로 받은 것은 <b>7개</b>이니 7개 세로줄을 눌러 보세요.</p>'
    assert old in s; s=s.replace(old,new)
    if court: s=s.replace('<a href="#map">증거물 1</a>','<a href="#warm">증거물 0</a><a href="#map">증거물 1</a>')
    else: s=s.replace('<a href="#map">큰 그림</a>','<a href="#warm">준비</a><a href="#map">큰 그림</a>')
    open(path,'w',encoding='utf-8').write(s);print('ok',path)
apply('build/template.html',False);apply('build/template_court.html',True)
