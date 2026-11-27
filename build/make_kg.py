#!/usr/bin/env python3
"""지식 색인·꾸러미용 kg.json / refs.json / meta.json 생성"""
import json,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
COURT='court' in sys.argv
PG='01b_likelihood_court' if COURT else '01_likelihood_vs_probability'
OUT=os.path.join(R,'kg','court') if COURT else os.path.join(R,'kg')
os.makedirs(OUT,exist_ok=True)
N=[];E=[]
def node(id,type,ko,en,anchor,level=2,family=None,defn=None,cov='explained',conf='high',dom=('stats',),alt=None,src=None):
    n={"id":id,"type":type,"label":{"ko":ko,"en":en},"page":PG,"anchor":anchor,"level":level,"status":"known","confidence":conf,"coverage":cov,"match":[],"domain":list(dom)}
    if family:n["family"]=family
    if defn:n["definition"]={"ko":defn}
    if alt:n["altLabel"]={"ko":alt}
    if src:n["source"]=src
    N.append(n);return id
def edge(s,p,o,a,c="high"):E.append({"s":s,"p":"lab:"+p,"o":o,"anchor":a,"confidence":c})
c=lambda x:'lab:concept/'+x; m=lambda x:'lab:method/'+x; t=lambda x:'lab:topic/'+x
# 핵심 개념
P=node(c('probability'),'Concept','확률','Probability','#lv1',1,'probability','상자(θ)를 고정했을 때 각 결과가 나올 정도. 가능한 모든 결과의 확률을 더하면 1이다.')
TH=node(c('parameter'),'Concept','모수 θ','Parameter (theta)','#lv1',1,'probability','분포의 모양을 정하는 숫자. 여기서는 상자가 케이크를 줄 확률.')
IND=node(c('independent-trials'),'Concept','독립시행','Independent trials','#lv1',1,'probability','한 번의 결과가 다른 번의 결과에 영향을 주지 않는 시행.')
BIN=node('lab:distribution/binomial','Distribution','이항분포','Binomial distribution','#lv1',1,'distributions','성공 확률 θ인 독립시행을 n번 했을 때 성공 횟수의 분포.')
LIK=node(c('likelihood'),'Concept','가능도(우도)','Likelihood','#lv2',2,'estimation','결과(데이터)를 고정하고 모수 θ를 바꿔 가며 본 값. θ가 데이터를 얼마나 잘 설명하는지 나타내며 합이 1일 필요가 없다.',alt=['우도','가능도 함수','L(θ)'])
SWAP=node('lab:limitation/condition-swap','Limitation','조건 뒤집기 오류','Transposed conditional','#lv3',2,'probability','P(데이터|θ)를 P(θ|데이터)로 바꿔 읽는 실수.')
AREA=node(c('likelihood-area'),'Concept','가능도 곡선 넓이 1/11','Area under the likelihood curve','#lv3',2,'estimation','n=10 이항 가능도 곡선 아래 넓이는 k와 상관없이 1/11로, 1이 아니므로 θ에 대한 확률분포가 아니다.')
LR=node(m('likelihood-ratio'),'Method','가능도 비율','Likelihood ratio','#lv4',2,'estimation','두 후보의 가능도를 나눈 값. 한 후보가 다른 후보보다 데이터를 몇 배 더 잘 설명하는지 뜻한다.')
MLE=node(m('maximum-likelihood-estimation'),'Method','최대가능도 추정','Maximum likelihood estimation (MLE)','#lv4',2,'estimation','가능도를 가장 크게 만드는 θ를 추정값으로 고르는 방법. 이항분포에서는 k/n.',alt=['최대우도 추정','MLE'])
PRI=node(c('prior-distribution'),'Concept','사전분포','Prior distribution','#lv5',3,'bayes','데이터를 보기 전에 θ 후보들에 매겨 둔 확률.')
POS=node(c('posterior-distribution'),'Concept','사후분포','Posterior distribution','#lv5',3,'bayes','사전분포 × 가능도를 합이 1이 되게 나눈 결과. 데이터를 본 뒤 θ에 대한 확률.')
BAY=node(m('bayes-theorem'),'Method','베이즈 정리','Bayes\' theorem','#lv5',3,'bayes','P(θ|데이터) = P(데이터|θ)×P(θ) ÷ 전체 합.')
NORM=node(c('normalization'),'Concept','정규화','Normalization','#lv5',2,'bayes','값들을 모두 더한 값으로 나눠 합을 1로 맞추는 일.')
COND=node(c('conditional-probability'),'Concept','조건부확률 P(A|B)','Conditional probability','#intro',1,'probability','B라고 정해 두었을 때 A일 확률. 세로 막대는 조건 표시.')
# 한계
L1=node('lab:limitation/theta-must-be-known','Limitation','확률 계산은 θ를 알아야 한다','Probability requires a known parameter','#lv1',1,'probability')
L2=node('lab:limitation/likelihood-not-probability','Limitation','가능도는 θ의 확률이 아니다','Likelihood is not a probability over θ','#lv2',2,'estimation')
L4=node('lab:limitation/mle-no-probability','Limitation','최대가능도는 θ의 확률을 말하지 못한다','MLE gives no probability statement','#lv4',2,'estimation')
L5=node('lab:limitation/prior-sensitivity','Limitation','사전분포에 따라 결과가 달라질 수 있다','Prior sensitivity','#lv5',3,'bayes')
# 대결
D1=node(m('normalize-likelihood-column'),'Method','세로줄을 1로 나눠 확률로 읽기','Normalize the likelihood column','#duel',3,'bayes','가능도를 합으로 나눈 값을 θ의 확률로 읽는 방법. 균등 사전분포를 가정한 것과 같다.')
D2=node(m('require-prior-information'),'Method','사전 정보를 먼저 정하기','Specify the prior first','#duel',3,'bayes','θ의 확률을 말하기 전에 사전분포를 밝히는 방법.')
MET=node('lab:metric/posterior-probability-0p7','Metric','0.7 상자의 사후확률','Posterior probability of θ=0.7','#duel',3,'bayes')
# 주장
C1=node('lab:claim/column-sum-045','Claim','결과 7개일 때 θ=0.3·0.5·0.7·0.9의 가능도 합은 약 0.450이다','Likelihoods of 7 heads over four θ values sum to about 0.450','#map',2,'estimation',src=[{"ref":"almas2026likelihood","loc":""}])
C2=node('lab:claim/likelihood-area-one-eleventh','Claim','10번 중 7번의 가능도 곡선 넓이는 1/11이다','The likelihood curve for 7 of 10 has area 1/11','#lv3',2,'estimation',src=[{"ref":"almas2026likelihood","loc":""}])
C3=node('lab:claim/likelihood-translated-udo','Claim','통계학계에서는 likelihood를 흔히 우도로 번역한다','Likelihood is commonly translated as udo in Korean statistics','#why',1,'estimation',src=[{"ref":"park2016likelihood","loc":"각주 1"}])
# 문헌
W1=node('lab:work/almas2026likelihood','Work','Almas, Likelihood Is Not a Probability (LinkedIn)','Likelihood Is Not a Probability','#export',2)
W2=node('lab:work/park2016likelihood','Work','박선용·윤형석 (2016) 수학교육','A Study on Analysis of Likelihood Principle and its Educational Implications','#export',2)
# 질문
Q1=node('lab:question/is-267-prob-of-box','Question','7번 받았으면 0.7 상자일 확률은 26.7%일까?','Is 0.267 the probability of θ=0.7?','#top',1,'estimation')
Q2=node('lab:question/normalize-equals-probability','Question','세로줄을 1로 맞추면 상자의 확률이 될까?','Does normalizing the likelihood give a probability?','#duel',3,'bayes')
# 비유
A1=node('lab:analogy/cake-box','Analogy','케이크 상자','Cake box','#lv1',1,'probability',cov='explained')
A2=node('lab:analogy/footprint-suspect','Analogy','발자국과 용의자','Footprints and suspects','#lv3',1,'probability')
A3=node('lab:analogy/attendance-record','Analogy','평소 출근 기록과 지각 한 번','Usual record and one late day','#lv5',2,'bayes')
A4=node('lab:analogy/audition-score','Analogy','오디션 점수의 격차','Audition score gaps','#lv4',1,'estimation')
# 시뮬레이션
S=[node('lab:simulation/p01-heat-table','Simulation','케이크 표 가로·세로 읽기','Row/column reading table','#map',1,'probability'),
   node('lab:simulation/p01-binomial-presses','Simulation','상자 정하고 10번 조르기','Binomial presses','#lv1',1,'probability'),
   node('lab:simulation/p01-column-likelihood','Simulation','결과 고정 상자 심문','Fixed-outcome likelihood bars','#lv2',2,'estimation'),
   node('lab:simulation/p01-likelihood-area','Simulation','가능도 곡선 넓이 재기','Likelihood curve area','#lv3',2,'estimation'),
   node('lab:simulation/p01-ratio-mle','Simulation','두 상자 맞대기','Likelihood ratio and MLE','#lv4',2,'estimation'),
   node('lab:simulation/p01-overtime-verdict','Simulation','야근 판결기','Prior × likelihood verdict','#lv5',3,'bayes')]
# 더 알아보기
M1=node(c('markov-matrix'),'Concept','마르코프 행렬','Markov transition matrix','#sum',3,'probability','지금 상태를 고정했을 때 다음 상태의 분포를 가로줄로 적은 표. 가로줄 합이 1이다.',cov='mentioned',dom=('stats','math'))
M2=node(c('negative-log-likelihood'),'Concept','음의 로그가능도(교차 엔트로피)','Negative log-likelihood','#sum',3,'estimation','분류 모델 손실. 학습은 가능도 최대화와 같다.',cov='mentioned',dom=('stats','ai'))
M3=node(c('hidden-markov-model'),'Concept','은닉 마르코프 모델','Hidden Markov model','#sum',4,'timeseries',cov='mentioned',dom=('stats','ai'))
M4=node(c('llm-pretraining-likelihood'),'Concept','LLM 사전학습과 가능도','LLM pretraining as maximum likelihood','#sum',4,'estimation',cov='mentioned',dom=('ai','llm'))
# 법정판 추가
if COURT:
    PF=node(c('prosecutors-fallacy'),'Concept','검사의 오류','Prosecutor\'s fallacy','#lv3',2,'probability','P(증거|무죄)를 P(무죄|증거)로 바꿔 읽는 실수.',alt=['prosecutor\'s fallacy'])
    C4=node('lab:claim/prosecutors-fallacy-named-1987','Claim','검사의 오류라는 이름은 Thompson과 Schumann(1987)이 붙였다','The term prosecutor\'s fallacy was coined by Thompson and Schumann (1987)','#lv3',2,'probability',src=[{"ref":"thompson1987interpretation","loc":""}])
    C5=node('lab:claim/forensic-likelihood-ratio-reporting','Claim','법과학 보고에서 가능도 비율로 결론을 쓰자는 논의가 있다','Forensic reporting using likelihood ratios is discussed to avoid the fallacy','#lv3',3,'estimation',src=[{"ref":"arxiv2025prosecutor","loc":""}])
    W3=node('lab:work/thompson1987interpretation','Work','Thompson·Schumann (1987) Law and Human Behavior','Interpretation of statistical evidence in criminal trials','#export',2)
    W4=node('lab:work/arxiv2025prosecutor','Work','arXiv:2502.03217 (2025)','The Prosecutor\'s Fallacy and Expert Testimony: A Modern Take Using Likelihood Ratios','#export',3)
    TG=node('lab:simulation/p01b-testimony','Simulation','증언 흔들기','Testimony cross-examination game','#lv3',2,'probability')
    edge(PF,'broader',t('conditional-probability'),'#lv3');edge(SWAP,'relatedTo',PF,'#lv3');edge(C4,'supports',PF,'#lv3');edge(C4,'assertedIn',W3,'#lv3');edge(C5,'supports',LR,'#lv3');edge(C5,'assertedIn',W4,'#lv3');edge(PF,'demonstratedBy',TG,'#lv3');edge(PF,'addressedBy',LR,'#lv3')
# 퀴즈
QZ={'q1':['#lv1',[P,BIN]],'q2':['#lv2',[LIK,LIK]],'q3':['#lv3',[SWAP,AREA]],'q4':['#lv4',[LR,MLE]],'q5':['#lv5',[POS,PRI]]}
qlab={'q1':['가로줄 합은 1','0.5 상자 7개 확률'],'q2':['우도와 가능도의 관계','후보 추가 시 세로줄 합'],'q3':['0.267의 바른 해석','넓이 1/11 ×11'],'q4':['가능도 비율의 뜻','θ̂ = 14/20'],'q5':['사후분포의 합','데이터가 많을 때 사전의 영향']}
for q,(a,tg) in QZ.items():
    for i in range(2):
        qi=node(f'lab:quiz/{"p01b" if COURT else "p01"}-{q}-{i+1}','QuizItem',qlab[q][i],qlab[q][i],a,2); edge(qi,'assesses',tg[i],a)
# 관계
edge(P,'prerequisiteOf',LIK,'#lv2');edge(LIK,'prerequisiteOf',SWAP,'#lv3');edge(LIK,'prerequisiteOf',LR,'#lv4');edge(LR,'prerequisiteOf',MLE,'#lv4');edge(LIK,'prerequisiteOf',BAY,'#lv5')
edge(PRI,'prerequisiteOf',POS,'#lv5');edge(NORM,'partOf',BAY,'#lv5');edge(COND,'prerequisiteOf',BAY,'#lv5');edge(IND,'prerequisiteOf',BIN,'#lv1');edge(TH,'partOf',BIN,'#lv1');edge(BIN,'prerequisiteOf',P,'#lv1')
edge(P,'hasLimitation',L1,'#lv1');edge(L1,'addressedBy',LIK,'#lv2')
edge(LIK,'hasLimitation',L2,'#lv2');edge(L2,'addressedBy',BAY,'#lv5');edge(L2,'raises',Q1,'#lv3')
edge(SWAP,'addressedBy',BAY,'#lv5');edge(AREA,'supports',L2,'#lv3')
edge(MLE,'hasLimitation',L4,'#lv4');edge(L4,'addressedBy',BAY,'#lv5')
edge(BAY,'hasLimitation',L5,'#lv5');edge(POS,'derivedFrom',LIK,'#lv5');edge(POS,'derivedFrom',PRI,'#lv5');edge(BAY,'solves',Q1,'#lv5')
edge(P,'contrastsWith',LIK,'#sum')
edge(D1,'contrastsWith',D2,'#duel');edge(D1,'evaluatedBy',MET,'#duel');edge(D2,'evaluatedBy',MET,'#duel');edge(D1,'assumes',PRI,'#duel');edge(LIK,'raises',Q2,'#duel');edge(D2,'broader',t('prior-posterior'),'#duel');edge(D1,'broader',t('prior-posterior'),'#duel')
edge(C1,'supports',LIK,'#map');edge(C1,'assertedIn',W1,'#map');edge(C2,'supports',AREA,'#lv3');edge(C2,'assertedIn',W1,'#lv3');edge(C3,'supports',LIK,'#why');edge(C3,'assertedIn',W2,'#why')
edge(A1,'analogyOf',BIN,'#lv1');edge(A2,'analogyOf',SWAP,'#lv3');edge(A3,'analogyOf',BAY,'#lv5');edge(A4,'analogyOf',LR,'#lv4')
for s_,o_ in zip(S,[LIK,BIN,LIK,AREA,MLE,POS]):edge(o_,'demonstratedBy',s_,s_ and N[[n['id'] for n in N].index(s_)]['anchor'])
edge(M1,'relatedTo',P,'#sum');edge(M2,'derivedFrom',LIK,'#sum');edge(M3,'derivedFrom',M1,'#sum');edge(M3,'relatedTo',LIK,'#sum');edge(M4,'derivedFrom',MLE,'#sum')
# 뼈대에 걸기
for a,b in [(P,'probability-rules'),(COND,'conditional-probability'),(BIN,'discrete-distributions'),(TH,'discrete-distributions'),(IND,'probability-rules'),(LIK,'maximum-likelihood'),(AREA,'maximum-likelihood'),(LR,'maximum-likelihood'),(MLE,'maximum-likelihood'),(L4,'maximum-likelihood'),(L2,'maximum-likelihood'),(L1,'discrete-distributions'),(SWAP,'conditional-probability'),(PRI,'prior-posterior'),(POS,'prior-posterior'),(L5,'prior-posterior'),(BAY,'bayes-theorem'),(NORM,'bayes-theorem')]:
    edge(a,'broader',t(b),N[[n['id'] for n in N].index(a)]['anchor'])
kg={"version":"1.0","page":PG,"nodes":N,"edges":E}
json.dump(kg,open(os.path.join(OUT,'kg.json'),'w'),ensure_ascii=False,indent=1)
refs=[{"id":"almas2026likelihood","type":"webpage","title":"Likelihood Is Not a Probability","author":[{"family":"Almas","given":"Muhammad"}],"container-title":"LinkedIn","URL":"https://www.linkedin.com/pulse/likelihood-probability-muhammad-almas-es7bf/","accessed":{"date-parts":[[2026,11,27]]},
 "lab":{"work":W1,"role":"primary","supports":[C1,C2],"locs":[],"verified":{"title":True,"author":True,"year":False,"container":True,"pages":False,"doi":False},"checkedBy":"사용자가 준 글과 그림에서 옮김, 숫자는 이 페이지에서 다시 계산 (2026-11-27)","checkedSource":"user"}},
 {"id":"park2016likelihood","type":"article-journal","title":"우도원리에 대한 분석과 그에 따른 교육적 시사점에 대한 연구","author":[{"literal":"박선용"},{"literal":"윤형석"}],"issued":{"date-parts":[[2016]]},"container-title":"수학교육 (The Mathematical Education)","volume":"55","issue":"2","page":"193-208","DOI":"10.7468/mathedu.2016.55.2.193",
 "lab":{"work":W2,"role":"background","supports":[C3],"locs":[{"claim":C3,"loc":"각주 1"}],"verified":{"title":True,"author":True,"year":True,"container":True,"pages":True,"doi":True},"checkedBy":"웹 검색(koreascience.kr) 2026-11-27","checkedSource":"web"}}]
if COURT:
    refs+=[{"id":"thompson1987interpretation","type":"article-journal","title":"Interpretation of statistical evidence in criminal trials: The prosecutor's fallacy and the defense attorney's fallacy","author":[{"family":"Thompson","given":"William C."},{"family":"Schumann","given":"Edward L."}],"issued":{"date-parts":[[1987]]},"container-title":"Law and Human Behavior","volume":"11","issue":"3","page":"167-187",
      "lab":{"work":"lab:work/thompson1987interpretation","role":"background","supports":["lab:claim/prosecutors-fallacy-named-1987"],"locs":[],"verified":{"title":True,"author":True,"year":True,"container":True,"pages":True,"doi":False},"checkedBy":"웹 검색 2026-11-27","checkedSource":"web"}},
     {"id":"arxiv2025prosecutor","type":"article-journal","title":"The Prosecutor's Fallacy and Expert Testimony: A Modern Take Using Likelihood Ratios","author":[{"literal":"(저자 확인 필요)"}],"issued":{"date-parts":[[2025]]},"container-title":"arXiv","URL":"https://arxiv.org/abs/2502.03217",
      "lab":{"work":"lab:work/arxiv2025prosecutor","role":"background","supports":["lab:claim/forensic-likelihood-ratio-reporting"],"locs":[],"verified":{"title":True,"author":False,"year":True,"container":True,"pages":False,"doi":False},"checkedBy":"웹 검색 2026-11-27","checkedSource":"web"}}]
json.dump(refs,open(os.path.join(OUT,'refs.json'),'w'),ensure_ascii=False,indent=1)
meta={"title":"초파리의 케이크 상자 — 확률과 가능도는 왜 다를까","number":"01","series":"고급통계 연구실 · 확률 vs 가능도","about":[P,LIK,MLE,BAY,POS],"basedOn":["almas2026likelihood"],"educationalLevel":"입문",
 "creator":[{"name":"안상선","role":"author"}],"contributor":[{"name":"AI 보조 제작","role":"assistant"}],"date":"2026-11-27","version":"1.0","language":["ko"],"license":"","url":"https://adminmrobo.github.io/likelihood_vs_probability/","registry":"KG_00_registry 0.2","learningResourceType":"interactive explainer","seeAlso":"",
 "suggestedCitation":"안상선 (2026). 초파리의 케이크 상자 — 확률과 가능도는 왜 다를까. 고급통계 연구실 · 확률 vs 가능도 01, v1.0."}
if COURT:
    meta.update({"title":"케이크 상자 재판 — 그 확률, 모순입니다!","number":"01b","series":"고급통계 연구실 · 확률 vs 가능도 (법정편)","url":"https://adminmrobo.github.io/likelihood_vs_probability/court.html","basedOn":["almas2026likelihood","thompson1987interpretation"],
      "suggestedCitation":"안상선 (2026). 케이크 상자 재판 — 그 확률, 모순입니다!. 고급통계 연구실 · 확률 vs 가능도 (법정편) 01b, v1.0."})
json.dump(meta,open(os.path.join(OUT,'meta.json'),'w'),ensure_ascii=False,indent=1)
print(len(N),'nodes',len(E),'edges')
