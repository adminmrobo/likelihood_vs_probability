"""실험 ① 그래프 읽는 법 5단계 안내 + 세로축 눈금 (기본판·법정판)"""
CSS='''.guide{display:flex;gap:12px;align-items:center;justify-content:space-between;flex-wrap:wrap;background:var(--amber-soft);border:2px solid #e8c98e;border-radius:12px;padding:12px 14px;margin:8px 0}
.guide .gs{flex:1 1 320px}.guide .gs b{color:var(--amber)}.guide .gs p{margin:.3em 0 0}
.guide .dots{display:flex;gap:5px;margin-top:6px}.guide .dots i{width:9px;height:9px;border-radius:50%;background:#e8c98e}.guide .dots i.on{background:var(--amber)}
'''
HTML='''    <div class="guide" id="g1">
      <div class="gs"><b id="g1n">그래프 읽는 법 1 / 5</b><p id="g1t" aria-live="polite"></p><div class="dots" id="g1d"><i></i><i></i><i></i><i></i><i></i></div></div>
      <div class="group"><button class="bt" id="g1p">◀ 이전</button><button class="bt primary" id="g1x">다음 ▶</button></div>
    </div>
'''
def apply(path):
    s=open(path,encoding='utf-8').read()
    if 'id="g1"' in s: print('already');return
    s=s.replace('.jt{border-bottom',CSS+'.jt{border-bottom',1)
    s=s.replace('<span class="glabel">상자</span>\n        <button class="bt" data-t1="0.3">','<span class="glabel">상자 고르기 (θ = 한 번에 케이크가 나올 확률)</span>\n        <button class="bt" data-t1="0.3">')
    s=s.replace('<label class="glabel" for="t1">θ 직접</label>','<label class="glabel" for="t1">θ 직접 정하기</label>')
    a='    <div class="cwrap"><canvas id="c1"'
    assert a in s; s=s.replace(a,HTML+a,1)
    s=s.replace('<canvas id="c1" height="300"','<canvas id="c1" height="330"')
    # draw: 세로축과 안내 겹그림
    old="function draw(dt){var o=fit(c),x=o.x,W=o.W,H=o.H;grid(x,W,H);var top=70,bot=H-30,l=40,r=W-12,bw=(r-l)/11;\n    var mx=0;for(var k=0;k<=10;k++)mx=Math.max(mx,L(k,th),rounds?cnt[k]/rounds:0);mx=Math.max(mx,.1)*1.1;\n    x.strokeStyle='#d5dbe2';x.beginPath();x.moveTo(l,bot+.5);x.lineTo(r,bot+.5);x.stroke();"
    new="function draw(dt){var o=fit(c),x=o.x,W=o.W,H=o.H;grid(x,W,H);var top=86,bot=H-40,l=46,r=W-12,bw=(r-l)/11;\n    var mx=0;for(var k=0;k<=10;k++)mx=Math.max(mx,L(k,th),rounds?cnt[k]/rounds:0);mx=Math.max(mx,.1)*1.1;\n    x.strokeStyle='#d5dbe2';x.beginPath();x.moveTo(l,bot+.5);x.lineTo(r,bot+.5);x.moveTo(l+.5,top-6);x.lineTo(l+.5,bot);x.stroke();\n    var stp=mx>0.25?0.1:0.05;for(var yv=0;yv<=mx+1e-9;yv+=stp){var yy=bot-(bot-top)*yv/mx;x.strokeStyle='rgba(22,33,43,.08)';x.beginPath();x.moveTo(l,yy+.5);x.lineTo(r,yy+.5);x.stroke();txt(x,yv.toFixed(2),l-5,yy,{a:'right',s:10,c:G1===2?'#a35c00':'#5b6874',b:G1===2})}\n    txt(x,'확률 ↑',l-4,top-16,{a:'left',s:11,c:G1===2?'#a35c00':'#5b6874',b:G1===2});"
    assert old in s; s=s.replace(old,new)
    old="txt(x,String(k2),cx+bw/2,bot+12,{s:12,c:'#5b6874'});"
    new="txt(x,String(k2),cx+bw/2,bot+12,{s:12,c:G1===1?'#a35c00':'#5b6874',b:G1===1});"
    assert old in s; s=s.replace(old,new)
    old="    txt(x,'받은 케이크 개수 →',r,H-8,{a:'right',s:11,c:'#5b6874'});"
    new='''    txt(x,'받은 케이크 개수 →',r,H-8,{a:'right',s:11,c:G1===1?'#a35c00':'#5b6874',b:G1===1});
    if(G1)guide(x,l,r,top,bot,bw,mx,W,H);'''
    assert old in s; s=s.replace(old,new)
    old="  function cake(x,X,Y,g){var p=3;"
    new='''  function Y(v,top,bot,mx){return bot-(bot-top)*v/mx}
  function hl(x,X,Yy,w,h){x.save();x.strokeStyle='#e0a400';x.lineWidth=3;x.setLineDash([6,4]);x.strokeRect(X,Yy,w,h);x.restore()}
  function guide(x,l,r,top,bot,bw,mx,W,H){var pk=0,pv=0;for(var k=0;k<=10;k++)if(L(k,th)>pv){pv=L(k,th);pk=k}
    if(G1===1){hl(x,l-2,bot+2,r-l+4,20)}
    if(G1===2){var v=L(7,th),cx=l+bw*7+bw/2,yy=Y(v,top,bot,mx);hl(x,l+bw*7+2,yy-4,bw-4,bot-yy+4);x.save();x.setLineDash([4,3]);x.strokeStyle='#a35c00';x.beginPath();x.moveTo(l,yy+.5);x.lineTo(cx,yy+.5);x.stroke();x.restore();
      txt(x,'7개가 나올 확률 = '+v.toFixed(3),Math.min(r-80,Math.max(l+80,cx)),top-30,{s:13,b:true,c:'#a35c00'})}
    if(G1===3){var cx2=l+bw*pk+bw/2,yy2=Y(pv,top,bot,mx);txt(x,'▼ 꼭대기: '+pk+'개 (10 × θ = '+(10*th).toFixed(1)+' 근처)',Math.min(r-110,Math.max(l+110,cx2)),yy2-28,{s:13,b:true,c:'#a35c00'});
      var ya=bot-(bot-top)*0.6;txt(x,'← 낮아짐',Math.max(l+30,cx2-bw*2.6),ya,{s:12,c:'#a35c00',b:true});txt(x,'낮아짐 →',Math.min(r-30,cx2+bw*2.6),ya,{s:12,c:'#a35c00',b:true})}
    if(G1===4&&rounds){txt(x,'초록 = 실제로 '+rounds.toLocaleString('ko-KR')+'판 해 본 비율, 테두리 = 공식',(l+r)/2,top-30,{s:13,b:true,c:'#13733a'})}
    if(G1===5){x.save();x.strokeStyle='#a35c00';x.lineWidth=2;x.beginPath();x.moveTo(l+4,top-14);x.lineTo(l+4,top-22);x.lineTo(r-4,top-22);x.lineTo(r-4,top-14);x.stroke();x.restore();
      var s5=0;for(var q=0;q<=10;q++)s5+=L(q,th);txt(x,'막대 11개를 모두 더하면 '+s5.toFixed(3),(l+r)/2,top-34,{s:13,b:true,c:'#a35c00'})}}
  var G1=1,GT=[
    function(){return '가로축은 10번 눌렀을 때 받을 수 있는 케이크 개수예요. 0개부터 10개까지, 결과는 모두 11가지예요.'},
    function(){return '막대 하나의 높이는 “그 개수가 나올 확률”이에요. 왼쪽 세로축 눈금으로 읽어요. 7개 막대의 높이 '+L(7,th).toFixed(3)+'은 “10번 중 정확히 7번 받을 확률”이에요. 준비 ②에서처럼 (순서의 수) × (순서 하나의 확률)로 계산했어요: 120 × '+Math.pow(th,7).toFixed(4)+' × '+Math.pow(1-th,3).toFixed(4)+'.'},
    function(){return '막대가 산 모양인 이유: 7개 근처는 나올 수 있는 순서가 아주 많아요(7개는 120가지). 0개나 10개는 순서가 1가지뿐이라 낮아요. 그래서 꼭대기는 10 × θ 근처에 생겨요. 지금은 '+(10*th).toFixed(1)+'개 근처.'},
    function(){return '초록 막대는 계산이 아니라 실제로 해 본 결과예요. “10번 누르기”를 여러 판 하고, 각 개수가 나온 판의 비율을 그렸어요. 판 수가 많을수록 초록 막대가 테두리 막대(공식값)에 붙어요. 공식이 실제 결과를 잘 맞힌다는 뜻이에요.'},
    function(){return '막대 11개를 모두 더하면 1이에요. 10번 누르면 0~10개 중 하나는 반드시 나오니까요. 위의 상자 버튼으로 0.3 상자로 바꿔 보세요. 산은 3개 근처로 옮겨 가지만, 합은 여전히 1이에요.'}];
  function gset(n){G1=Math.max(1,Math.min(5,n));$('#g1n').textContent='그래프 읽는 법 '+G1+' / 5';$('#g1t').textContent=GT[G1-1]();$$('#g1d i').forEach(function(d,i){d.classList.toggle('on',i<G1)});
    $('#g1p').disabled=G1===1;$('#g1x').textContent=G1===5?'처음으로 ↺':'다음 ▶';if(G1===4&&!rounds){for(var i=0;i<1000;i++){var o=oneRound();cnt[o.k]++;sumK+=o.k}rounds+=1000;upd()}draw(0)}
  function cake(x,X,Y,g){var p=3;'''
    assert old in s; s=s.replace(old,new,1)
    old="  $('#press0').onclick=function(){setT(th)};\n  upd();"
    new="  $('#press0').onclick=function(){setT(th)};\n  $('#g1p').onclick=function(){gset(G1-1)};$('#g1x').onclick=function(){gset(G1===5?1:G1+1)};\n  upd();gset(1);"
    assert old in s; s=s.replace(old,new,1)
    # 상자를 바꿀 때 안내 문장도 갱신
    s=s.replace("cnt.fill(0);rounds=0;sumK=0;anim=null;upd();draw(0)}","cnt.fill(0);rounds=0;sumK=0;anim=null;upd();if($('#g1t'))$('#g1t').textContent=GT[G1-1]();draw(0)}",1)
    # 마지막 10번 위치 아래로
    s=s.replace("txt(x,'마지막 10번:',l,22,","txt(x,'마지막 10번:',l,16,")
    s=s.replace("for(var i=0;i<shown;i++)cake(x,l+86+i*26,14,anim.seq[i]);","for(var i=0;i<shown;i++)cake(x,l+86+i*26,8,anim.seq[i]);")
    open(path,'w',encoding='utf-8').write(s);print('ok',path)
for p in ('build/template.html','build/template_court.html'):apply(p)
