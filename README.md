# 확률 vs 가능도(우도) — 초파리의 케이크 상자

고급통계 연구실 해설 페이지. 같은 숫자 표를 **가로로 읽으면 확률, 세로로 읽으면 가능도(우도)**라는 것을 케이크 상자 이야기(1막)와 야근 판결(2막)로 따라갑니다. 통계를 처음 접하는 분을 위한 입문 페이지입니다.

- 페이지: `index.html` (단일 파일, 외부 요청은 글꼴 하나)
- 구성: ① 확률(상자 고정) → ② 가능도(결과 고정) → ③ 바꿔 읽는 함정(넓이 1/11) → ④ 가능도 비율·최대가능도 → 대결(조건부) → ⑤ 사전 × 가능도 = 사후(야근 판결)
- 지식 색인·온톨로지·서지 꾸러미 포함 (`kg/`)
- 그림 요청서: `docs/GENSPARK_01_likelihood_vs_probability.md`
- 페르소나 평가: `docs/persona_review_01.md`

## 다시 만들기

```sh
python3 build/build.py                         # template + 캐릭터 팩 → index.html
sh build/kg.sh ../ahnboat_lab_explainer        # 지식 색인(#kg)·꾸러미(#export) 붙이기
```

## 함께 보기

- [베이지안 통계 연구실](https://github.com/adminmrobo/bayesian-statistics-for-data-scientists)
- [확률분포 딕셔너리](https://github.com/adminmrobo/probability_distribution_dictionary)
- [Stochastic_labs](https://github.com/adminmrobo/Stochastic_labs) (마르코프 행렬)

## 출처

1. Muhammad Almas, “Likelihood Is Not a Probability” (LinkedIn) — 구성 아이디어. 숫자는 이 페이지에서 다시 계산.
2. 박선용·윤형석 (2016). 우도원리에 대한 분석과 그에 따른 교육적 시사점에 대한 연구. 수학교육 55(2), 193–208.

글 · 안상선 (https://adminmrobo.github.io/who_am_i/who_am_i.html) · (주)M-Robo 대표
캐릭터 이름·설정·그림의 저작권은 안상선에게 있습니다.
