#!/usr/bin/env python3
"""template.html + 캐릭터 팩(sprites96.js) + 동작 팩(motion.js) → index.html (단일 파일)
다시 만들기: python3 build/build.py  →  그다음 kg 꼬리표: build/kg.sh"""
import os,re
B=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(B)
import sys
srcn,outn=('template_court.html','court.html') if 'court' in sys.argv else ('template.html','index.html')
t=open(os.path.join(B,srcn),encoding='utf-8').read()
sp=open(os.path.join(B,'sprites96.js'),encoding='utf-8').read()
mo=open(os.path.join(B,'motion.js'),encoding='utf-8').read()
cid='cover_01b' if 'court' in sys.argv else 'cover_01'
cover=os.path.join(R,'assets/img/'+cid+'.webp')
if os.path.exists(cover):
    t=t.replace('<!--COVERIMG-->','<img class="cv" src="assets/img/'+cid+'.webp" width="1600" height="900" alt="케이크 상자 네 개 앞에서 연구실 식구들이 숫자 표를 들여다보는 픽셀아트 표지" fetchpriority="high" decoding="async"><style>.cover .alt{display:none}.cover{max-height:72vh}</style>')
    t=t.replace('<!--OGIMAGE-->','<meta property="og:image" content="https://adminmrobo.github.io/likelihood_vs_probability/assets/img/og_'+cid[6:]+'.jpg">')
t=t.replace('/*SPRITES*/',sp).replace('/*MOTION*/',mo)
open(os.path.join(R,outn),'w',encoding='utf-8').write(t)
print(outn,len(t.encode())//1024,'KB')
