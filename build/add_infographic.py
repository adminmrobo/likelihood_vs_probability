"""인포그래픽 스타일: 준비 ② 확률 나무 + 단계마다 '한눈에 보기' 카드 (기본판·법정판)"""
CSS='''.glance{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:8px;align-items:stretch;margin:6px 0 18px;padding:14px;border-radius:16px;border:2px solid var(--rule);background:#fff}
.glance .gh{grid-column:1/-1;font-size:13px;font-weight:700;color:var(--muted);letter-spacing:.04em}
.gt{border-radius:12px;padding:12px 10px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:4px;justify-content:center}
.gt .gl{font-size:12px;font-weight:700;padding:1px 10px;border-radius:999px;background:#fff;border:1px solid currentColor}
.gt b{font-size:17px;line-height:1.35}
.gt small{font-size:13px;color:var(--muted);line-height:1.4}
.gt .num{font-size:clamp(30px,5vw,44px);line-height:1;font-variant-numeric:tabular-nums}
.ga{display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700;color:var(--muted)}
.gt i[data-ic]{display:block;height:44px}
.gt i[data-ic] svg{height:44px;width:auto;max-width:100%}
.gt i[data-ic=seven],.gt i[data-ic=seven] svg{height:20px}.gt i[data-ic=boxes],.gt i[data-ic=boxes] svg{height:34px}.glance>*{min-width:0}
.c-fix{background:#eef2f6;color:#2b2d42}.c-move{background:var(--amber-soft);color:var(--amber)}
.c-prob{background:var(--gfp-soft);color:var(--gfp)}.c-lik{background:#fdeee2;color:#b4531a}.c-post{background:var(--stain-soft);color:var(--stain)}.c-bad{background:var(--eye-soft);color:var(--eye)}
@media (max-width:640px){.glance{grid-template-columns:1fr}.ga{font-size:22px;height:24px}}
.tree svg{width:100%;height:auto;display:block}
.tree{background:#fff;border:1px solid var(--rule);border-radius:12px;padding:8px}
'''
ICONS_JS=r'''/* ── 픽셀 아이콘 · 한눈에 카드 · 확률 나무 ── */
var PXI=(function(){var O='#1d1a22';
  function svg(w,h,body){return '<svg viewBox="0 0 '+w+' '+h+'" shape-rendering="crispEdges" aria-hidden="true">'+body+'</svg>'}
  function r(x,y,w,h,c){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+c+'"/>'}
  function box(x,lid){return r(x,3,10,9,O)+r(x+1,4,8,7,'#f4e7d0')+r(x,1,10,3,O)+r(x+1,2,8,1,lid)+r(x+3,6,4,3,O)+r(x+4,7,2,1,'#ffd54a')}
  function cake(x,y){return r(x,y+2,8,5,O)+r(x+1,y+3,6,3,'#ffe1ec')+r(x+1,y+3,6,1,'#c42a6e')+r(x+3,y,2,2,'#ffd54a')}
  function plate(x,y){return r(x,y+5,8,2,O)+r(x+1,y+5,6,1,'#eef2f6')}
  var I={
    box:function(c){return svg(10,12,box(0,c||'#13733a'))},
    boxes:function(){return svg(46,12,box(0,'#c9302c')+box(12,'#4a6a96')+box(24,'#13733a')+box(36,'#9b3fb5'))},
    cake:function(){return svg(8,8,cake(0,0))},
    cakes:function(){return svg(30,8,cake(0,0)+plate(11,0)+cake(22,0))},
    seven:function(){var b='';for(var i=0;i<10;i++)b+=i<7?cake(i*9,0):plate(i*9,0);return svg(89,8,b)},
    book:function(){return svg(12,12,r(1,1,10,10,O)+r(2,2,8,8,'#e6eefb')+r(3,4,6,1,'#4a6a96')+r(3,6,6,1,'#4a6a96')+r(3,8,4,1,'#4a6a96'))},
    curve:function(){return svg(24,12,r(0,11,24,1,O)+r(2,10,2,1,'#4a6a96')+r(4,9,2,1,'#4a6a96')+r(6,7,2,2,'#4a6a96')+r(8,5,2,2,'#4a6a96')+r(10,3,2,2,'#4a6a96')+r(12,2,3,1,'#4a6a96')+r(15,3,2,2,'#4a6a96')+r(17,6,2,2,'#4a6a96')+r(19,9,2,1,'#4a6a96')+r(21,10,2,1,'#4a6a96'))},
    scale:function(){return svg(16,12,r(7,1,2,10,O)+r(2,3,12,1,O)+r(1,4,4,1,'#13733a')+r(0,5,6,2,'#13733a')+r(11,6,4,1,'#9b3fb5')+r(10,7,6,2,'#9b3fb5')+r(4,11,8,1,O))},
    gavel:function(){return svg(14,12,r(1,1,7,4,O)+r(2,2,5,2,'#a35c00')+r(6,4,2,6,O)+r(2,10,10,2,O))}
  };
  function fill(root){(root||document).querySelectorAll('i[data-ic]').forEach(function(e){var f=I[e.dataset.ic];if(f)e.innerHTML=f(e.dataset.c)})}
  return {fill:fill,cake:cake,plate:plate,r:r,svg:svg};
})();
PXI.fill();
function drawTree(th){var el=document.getElementById('wTree');if(!el)return;var T=th,F=1-th;
  var W=360,rowH=30,top=26,H=top+8*rowH+10,x0=14,dx=46,leafX=x0+dx*3+8;var o='';var R=PXI.r;
  var cols=['#9aa5b1','#4a6a96','#c42a6e','#13733a'];
  function node(x,y){o+=R(x-3,y-3,6,6,'#1d1a22')}
  o+='<text x="'+x0+'" y="14" font-size="10" fill="#5b6874">1번째</text><text x="'+(x0+dx)+'" y="14" font-size="10" fill="#5b6874">2번째</text><text x="'+(x0+dx*2)+'" y="14" font-size="10" fill="#5b6874">3번째</text>';
  function yLeaf(i){return top+rowH*i+rowH/2}
  for(var lvl=0;lvl<3;lvl++){var n=1<<lvl,span=8/n;for(var j=0;j<n;j++){var yc=(yLeaf(j*span)+yLeaf(j*span+span-1))/2;var xa=x0+dx*lvl;
      for(var b=0;b<2;b++){var cs=span/2,yb=(yLeaf(j*span+b*cs)+yLeaf(j*span+b*cs+cs-1))/2,xb=xa+dx;var isC=b===0;
        o+='<path d="M'+xa+' '+yc+' H'+(xa+8)+' V'+yb+' H'+xb+'" fill="none" stroke="'+(isC?'#e8a3bf':'#c9d3e3')+'" stroke-width="3"/>';
        o+='<text x="'+(xa+12)+'" y="'+(yb-4)+'" font-size="9" fill="'+(isC?'#c42a6e':'#5b6874')+'">'+(isC?T:F).toFixed(1)+'</text>'}
      node(xa,yc)}}
  var S=[];for(var m=0;m<8;m++){var a=[1-((m>>2)&1),1-((m>>1)&1),1-(m&1)];S.push(a)}
  S.forEach(function(a,i){var y=yLeaf(i),k=a[0]+a[1]+a[2],p=Math.pow(T,k)*Math.pow(F,3-k);var g='';a.forEach(function(v,q){g+=v?PXI.cake(q*9,0):PXI.plate(q*9,0)});
    o+='<g transform="translate('+leafX+','+(y-7)+') scale(1.6)">'+g+'</g>';o+='<text x="'+(leafX+48)+'" y="'+(y+4)+'" font-size="11" fill="#16212b">= '+p.toFixed(3)+'</text>';
    o+=R(leafX+92,y-9,4,18,cols[k])});
  var groups=[[0,0,3],[1,3,2],[4,6,1],[7,7,0]];var bx=leafX+104;
  [[3,[0]],[2,[1,2,4]],[1,[3,5,6]],[0,[7]]].forEach(function(gr){var k=gr[0],idx=gr[1];var ys=idx.map(yLeaf),ym=(Math.min.apply(null,ys)+Math.max.apply(null,ys))/2;
    var tot=idx.length*Math.pow(T,k)*Math.pow(F,3-k);ys.forEach(function(y){o+='<path d="M'+(leafX+96)+' '+y+' H'+(bx+4)+' V'+ym+' H'+(bx+12)+'" fill="none" stroke="'+cols[k]+'" stroke-width="2"/>'});
    o+=R(bx+12,ym-12,W-bx-14,24,cols[k]);o+='<text x="'+(bx+18)+'" y="'+(ym+4)+'" font-size="11" font-weight="700" fill="#fff">'+k+'개 '+tot.toFixed(3)+'</text>'});
  el.innerHTML='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="세 번 누르기 확률 나무: 순서 8가지를 케이크 개수로 묶은 그림" font-family="IBM Plex Sans KR, sans-serif">'+o+'</svg>'}
'''
G={
 'lv1':('c-prob','''<div class="gt c-fix"><span class="gl">고정</span><i data-ic="box"></i><b>상자 하나 (θ = 0.7)</b></div><div class="ga">→</div><div class="gt c-move"><span class="gl">움직임</span><i data-ic="cakes"></i><b>받는 개수 0~10</b></div><div class="ga">→</div><div class="gt c-prob"><span class="gl">다 더하면</span><b class="num">1</b><small>그래서 ‘확률’</small></div>'''),
 'lv2':('c-lik','''<div class="gt c-fix"><span class="gl">고정</span><i data-ic="seven"></i><b>받은 결과 7개</b></div><div class="ga">→</div><div class="gt c-move"><span class="gl">움직임</span><i data-ic="boxes"></i><b>상자 후보 넷</b></div><div class="ga">→</div><div class="gt c-lik"><span class="gl">다 더하면</span><b class="num">0.450</b><small>1이 아니라서 ‘가능도’</small></div>'''),
 'map':('c-fix','''<div class="gt c-prob"><span class="gl">가로로 →</span><i data-ic="box"></i><b>상자 고정</b><small>합 1 · 확률</small></div><div class="ga">＋</div><div class="gt c-lik"><span class="gl">세로로 ↓</span><i data-ic="seven"></i><b>결과 고정</b><small>합 0.450 · 가능도</small></div><div class="ga">=</div><div class="gt c-fix"><span class="gl">한 표</span><b class="num">4 × 11</b><small>읽는 방향만 다르다</small></div>'''),
 'lv3':('c-bad','''<div class="gt c-bad"><span class="gl">✗ 틀린 읽기</span><b>“0.7 상자일 확률 26.7%”</b><small>상자가 움직이는데 확률처럼 말함</small></div><div class="ga">≠</div><div class="gt c-prob"><span class="gl">✓ 바른 읽기</span><b>“0.7 상자라면 7개 나올 확률 26.7%”</b><small>상자를 고정한 확률</small></div><div class="ga">∵</div><div class="gt c-lik"><span class="gl">증거</span><i data-ic="curve"></i><b class="num">1/11</b><small>곡선 넓이가 1이 아님</small></div>'''),
 'lv4':('c-lik','''<div class="gt c-lik"><span class="gl">0.7 상자</span><i data-ic="box" data-c="#13733a"></i><b>0.267</b></div><div class="ga">÷</div><div class="gt c-lik"><span class="gl">0.5 상자</span><i data-ic="box" data-c="#4a6a96"></i><b>0.117</b></div><div class="ga">=</div><div class="gt c-move"><span class="gl">비교</span><i data-ic="scale"></i><b class="num">2.28배</b><small>더 잘 설명함 · 꼭대기 θ̂ = 0.7</small></div>'''),
 'lv5':('c-post','''<div class="gt c-fix"><span class="gl">평소 (사전)</span><i data-ic="book"></i><b>느긋 30%</b><small>지난달 기록</small></div><div class="ga">×</div><div class="gt c-lik"><span class="gl">이번 주 (가능도)</span><i data-ic="curve"></i><b>10개 중 3개</b><small>느긋 쪽이 3만 배 그럴듯</small></div><div class="ga">=</div><div class="gt c-post"><span class="gl">판결 (사후)</span><i data-ic="gavel"></i><b class="num">93%</b><small>90% 넘음 → 야근</small></div>'''),
}
def card(key):
    cls,body=G[key]
    return '<div class="glance" role="group" aria-label="한눈에 보기"><div class="gh">한눈에 보기</div>'+body+'</div>\n'
def apply(path):
    s=open(path,encoding='utf-8').read()
    if 'class="glance"' in s: print('already',path);return
    s=s.replace('.jt{border-bottom',CSS+'.jt{border-bottom',1)
    for key in ('lv1','lv2','lv3','lv4','lv5'):
        i=s.index('<section class="level" id="'+key+'">');j=s.index('<div class="tags">',i);j=s.index('</div>',j)+6
        s=s[:j]+'\n  '+card(key)+s[j:]
    i=s.index('<section id="map">');j=s.index('</h2>',i)+5;s=s[:j]+'\n  '+card('map')+s[j:]
    # 준비 ②: 나무 그림 + 표는 접기
    s=s.replace('<div class="tw"><table class="tb" id="wSeq" aria-label="세 번 누를 때 나올 수 있는 순서와 확률"></table></div>',
      '<div class="tree" id="wTree"></div>\n    <p class="note">왼쪽에서 오른쪽으로 갈수록 한 번씩 더 누른 것. 분홍 가지는 케이크, 회색 가지는 빈 접시. 끝의 숫자는 그 순서의 확률(가지의 숫자를 모두 곱한 값)이고, 오른쪽 색 띠가 케이크 개수별 묶음 합이에요.</p>\n    <details class="code"><summary>숫자 표로 보기</summary><div class="tw"><table class="tb" id="wSeq" aria-label="세 번 누를 때 나올 수 있는 순서와 확률"></table></div></details>')
    s=s.replace('/* ── 준비: 한 번·세 번·작은 표 ── */',ICONS_JS+'\n/* ── 준비: 한 번·세 번·작은 표 ── */',1)
    s=s.replace("$('#wSeq').innerHTML=h;","$('#wSeq').innerHTML=h;drawTree(th);",1)
    open(path,'w',encoding='utf-8').write(s);print('ok',path)
for p in ('build/template.html','build/template_court.html'):apply(p)
