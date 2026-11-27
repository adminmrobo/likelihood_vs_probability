"""큰 표(#map)를 ②와 ③ 사이로 옮겨 '모아 보기'로 쓰게 한다 (기본판·법정판)"""
import sys
for path,court in (('build/template.html',False),('build/template_court.html',True)):
    s=open(path,encoding='utf-8').read()
    i=s.index('<section id="map">');j=s.index('</section>',i)+len('</section>')
    blk=s[i:j];s=s[:i]+s[j:].lstrip('\n')
    k=s.index('<!-- ③ -->');s=s[:k]+blk+'\n\n'+s[k:]
    if court:
        s=s.replace('<h2>증거물 1 — 케이크 표: 표는 하나, 읽는 방향은 둘</h2>','<h2>증거물 1 — 제1·제2 증거를 한 표에</h2>')
        s=s.replace('<a href="#warm">증거물 0</a><a href="#map">증거물 1</a>\n  <a href="#lv1">제1 증거</a><a href="#lv2">제2 증거</a>','<a href="#warm">증거물 0</a>\n  <a href="#lv1">제1 증거</a><a href="#lv2">제2 증거</a><a href="#map">증거물 1</a>')
        big='증거물 1'
    else:
        s=s.replace('<h2>큰 그림 — 표는 하나, 읽는 방향은 둘</h2>','<h2>모아 보기 — 큰 표 하나, 읽는 방향 둘</h2>')
        s=s.replace('<a href="#warm">준비</a><a href="#map">큰 그림</a>\n  <a href="#lv1">① 확률</a><a href="#lv2">② 가능도</a>','<a href="#warm">준비</a>\n  <a href="#lv1">① 확률</a><a href="#lv2">② 가능도</a><a href="#map">모아 보기</a>')
        big='큰 표'
    old=s[s.index('<p>방금 본 작은 표(상자 2개 × 3번)를 그대로 키웠어요.'):]
    old=old[:old.index('</p>')+4]
    s=s.replace(old,'<p>①에서 본 가로줄(상자 하나의 확률)과 ②에서 본 세로줄(결과 7개의 가능도)을 한 표에 모았어요. 준비 단계의 작은 표를 상자 네 개, 10번으로 키운 것입니다. 읽는 법은 똑같아요. 가로줄은 합이 1, 세로줄은 아무 값. 7개 세로줄을 눌러 ②의 0.450이 여기서 나온 것인지 확인해 보세요.</p>')
    s=s.replace('아래 '+big+'는 이 작은 표를 상자 네 개, 10번으로 키운 것뿐이에요.','이제 ①에서 상자 하나를 10번 누르는 가로줄을, ②에서 세로줄을 차례로 키워 볼게요.')
    s=s.replace('아래 '+big+'는 이 작은 표를 상자 네 개, 10번으로 키운 것뿐이에요.','')
    open(path,'w',encoding='utf-8').write(s);print('ok',path,s.index('id="map"')>s.index('id="lv2"'))
