# Genspark 그림 요청서 — 01 초파리의 케이크 상자 (확률 vs 가능도)

| 항목 | 내용 |
|---|---|
| 저장소 | adminmrobo/likelihood_vs_probability |
| 그림체 | **16비트 RPG풍 픽셀아트 (필수)** — 가로 1600 이상에서 직접 그린 작고 촘촘한 픽셀. 작은 그림을 키운 큰 네모 블록, 매끈한 일러스트·벡터·수채화·3D 금지 |
| 배경 | 낮의 연구실 (흰 벽, 큰 창의 자연광). 밤·네온 금지 |
| 그림 안 글자 | 글자·숫자·로고 금지 (표의 숫자도 그리지 않음 — 숫자는 페이지가 씀) |
| 참고 그림 (함께 올리기) | `adminmrobo/fruitfly-lab-expressions`의 박사·조수(하루)·초파리 연구원·주판봇·인턴 시아·인턴 모아 기본 그림 6장 |

## 만드는 순서

1. **표지 `cover_01`** 먼저 받기 → 그림체 확인
2. 마음에 들면 표지를 참고 그림으로 함께 올려 장면 3장(`sc_01_act1`, `sc_01_duel`, `sc_01_act2`)을 요청 (같은 비율 3:2끼리 한 대화에서)
3. 받은 파일 이름을 아래 체크리스트대로 바꿔 저장소 `assets/img/src/`에 올리기 → Claude에게 "표지 반영해 줘"

## 저장 이름 체크리스트

- [ ] `cover_01.png` — 16:9, 1920×1080 이상
- [ ] `sc_01_act1.png` — 3:2, 1536×1024 (선택)
- [ ] `sc_01_duel.png` — 3:2, 1536×1024 (선택)
- [ ] `sc_01_act2.png` — 3:2, 1536×1024 (선택)

---

## 1. 표지 — `cover_01` (16:9)

| 항목 | 내용 |
|---|---|
| 장소 | 햇빛 드는 연구실의 간식 테이블 |
| 주제 은유 | 뚜껑 색이 다른 케이크 상자 네 개(빨강·파랑·초록·보라)와, 벽에 걸린 **글자 없는 색 격자 판**(가로줄 하나와 세로줄 하나가 각각 빛나는 표) |
| 포즈 | 박사: 가운데 뒤에서 턱에 손, 격자 판을 봄 / 조수 하루: 오른쪽 옆에서 클립보드를 들고 세로줄을 가리킴 / 초파리: 왼쪽에서 오른쪽을 보며 케이크 상자 위에 앉아 장난스럽게 상자를 가림 / 주판봇: 오른쪽에서 왼쪽을 보며 주판으로 가로줄을 셈 / 시아·모아: 테이블 끝에서 빈 접시를 들고 기대에 찬 얼굴 |
| 대체 글 (alt) | 케이크 상자 네 개 앞에서 연구실 식구들이 숫자 표를 들여다보는 픽셀아트 표지 |
| 결과 암시 | 없음 (누가 이길지 보이지 않게, 가벼운 장난과 호기심) |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 캐릭터(박사, 조수 하루, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아)를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a sunlit daytime research lab with white walls and big windows, a snack table in the middle, lavender, mint and pink small props.
Characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center with a hand on his chin, looking at a wall board;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the right side holding a clipboard and pointing at one glowing column of the wall board;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, sitting on top of the cake boxes with a playful teasing grin, one hand covering a box;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, counting along one glowing row of the wall board;
  calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, at the far table end holding an empty plate;
  gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, next to her holding an empty plate and smiling hopefully.
Visual metaphor of the topic: four closed cake boxes with different lid colors (red, blue, green, purple) on the table, one small strawberry cake peeking out; on the wall a blank colored grid board (4 rows by 11 columns of blue squares, no numbers) where one horizontal row glows green and one vertical column glows orange.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the cake boxes and the grid board.
Mood: curious, playful teasing, friendly rivalry, the moment before the answer.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

---

## 2. 장면 — `sc_01_act1` (3:2) · 1막 케이크 놀림 (선택)

```
3:2 scene illustration, 1536x1024, same 16-bit high-resolution pixel-art style and same characters as the attached cover image.
Scene: daytime lab snack table. The fruit fly researcher (left, facing right) stands on a stack of four colored cake boxes, holding one strawberry cake high out of reach with a teasing grin. The two maid interns (right side) look up at the cake — the black-haired one patient and slightly sleepy, the ash-beige one pouting cutely with clasped hands. Ten small plates on the table: seven with a slice of cake, three empty, arranged in a row.
No text, no letters, no numbers. Faces and hands away from the edges.
```

## 3. 장면 — `sc_01_duel` (3:2) · 대결 (선택)

```
3:2 scene illustration, 1536x1024, same 16-bit high-resolution pixel-art style and same characters as the attached cover image.
Scene: a friendly duel in the lab. Fruit fly researcher on the left facing right, holding a magnifying glass over a small stack of record cards. Boxy beige CRT robot on the right facing left, proudly lifting a wooden abacus. Between them a tall glass jar being poured from four small cups into one, the liquid level stopping halfway (a visual of "normalizing", no numbers). The chibi scientist stands at the back center with a hand on his chin, undecided. The pink-haired girl researcher holds a clipboard at the side.
Mood: curious rivalry, result not yet shown. No text, no letters, no numbers.
```

## 4. 장면 — `sc_01_act2` (3:2) · 2막 야근 크리티컬 (선택)

```
3:2 scene illustration, 1536x1024, same 16-bit high-resolution pixel-art style and same characters as the attached cover image, plus three small silhouette helpers.
Scene: evening light just starting in the lab window (still bright, not night). The chibi scientist (left) raises both hands with purple sparks, casting a harmless glowing wave toward the right. The fruit fly researcher (right) is comically knocked back into an office chair in front of a tall pile of paper work, with waterfall tears and a cartoon "critical hit" star burst made of shapes only. Three cute solid dark navy-black silhouettes with a thin purple rim light and round white dot eyes stand behind the scientist: one with a pink ribbon holding an old record book, one with teal glasses reflection holding a magnifier, one with a small yellow bell. The ash-beige maid intern brings a cup of tea and a slice of cake to the fly's desk; the black-haired maid intern dozes standing up.
Funny, not scary, no injury. No text, no letters, no numbers.
```

## 5. 받은 뒤 처리 (Claude가 함)

- 그림체 점검: 2배로 확대해 얼굴·손이 세밀한지(큰 네모 블록이면 다시 받기)
- 표지: `LANCZOS` 1600×900 WebP(220 KB 이하) → `assets/img/cover_01.webp`, 공유 미리보기 `og_01.jpg`(1200×630), 썸네일 `thumb_01.webp`(600×400)
- 장면: 1200×800 WebP(180 KB 이하) → 해당 단계 위에 배치
- `python3 build/build.py` → `sh build/kg.sh` → `cover_manifest.json`의 `status`를 `ok`로

---

# 법정판 (`court.html`) 그림

**주의:** 특정 법정 게임·작품의 캐릭터, 말풍선 디자인, 손가락 포즈 구도, 로고를 닮지 않게 합니다. 우리 연구실 식구가 연구실 안에 꾸민 장난스러운 모의 법정입니다.

## 저장 이름 체크리스트

- [ ] `cover_01b.png` — 16:9, 1920×1080 이상
- [ ] `sc_01b_trial.png` — 3:2, 1536×1024 (선택) · 증언 흔들기 장면
- [ ] `sc_01b_act2.png` — 3:2, 1536×1024 (선택) · 2막 피고석의 초파리

## 6. 법정판 표지 — `cover_01b` (16:9)

| 항목 | 내용 |
|---|---|
| 장소 | 연구실 회의실을 책상·상자로 꾸민 모의 법정 (낮, 큰 창) |
| 주제 은유 | 높은 책상 뒤 판사석, 양쪽 마주 보는 두 책상, 가운데 증거 탁자 위 케이크 상자 넷과 글자 없는 색 격자 판 |
| 포즈 | 박사: 가운데 높은 책상 뒤 판사석, 나무 망치를 들고 생각하는 얼굴 / 초파리: 왼쪽 책상(검사석)에서 오른쪽을 보며 서류를 흔듦 / 하루: 오른쪽 책상(변호인석)에서 왼쪽을 보며 격자 판을 들어 올림 / 주판봇: 하루 옆 감정인석, 주판을 튕김 / 시아·모아: 뒤쪽 방청석, 빈 접시를 든 채 |
| 대체 글 (alt) | 연구실 모의 법정에서 판사 박사와 검사 초파리, 변호인 하루가 케이크 상자 증거를 두고 마주 선 픽셀아트 표지 |
| 결과 암시 | 없음 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 캐릭터(박사, 조수 하루, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아)를 같은 외형으로 등장
- 특정 게임·만화의 법정 장면이나 캐릭터를 닮지 않게, 그림 안에 글자·숫자·로고 금지
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a playful mock courtroom built inside a bright daytime research lab meeting room, big windows, white walls, desks and stacked boxes arranged as a judge's bench, two facing tables and a small public gallery; lavender, mint and pink props. Original design, not resembling any existing game or anime courtroom.
Characters:
  chibi scientist (thin teal rectangular glasses, spiky black hair with one white streak, small ponytail, white lab coat over black vest and tie) sitting behind the high bench at the back center as the judge, holding a small wooden gavel, thoughtful face;
  anthropomorphic fruit fly researcher (black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings) at the left table, facing right, confidently waving a sheet of paper;
  girl researcher (long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans) at the right table, facing left, holding up a blank colored grid board (blue squares, one glowing row, one glowing column, no numbers);
  boxy beige retro CRT-monitor robot (dark green screen face with mint pixel eyes, abacus-bead antenna, gray segmented arms, tank treads) beside her, facing left, flicking beads on a wooden abacus;
  two maid interns (one with long straight jet-black hair and charcoal maid dress, one with long ash-beige wavy hair, white frilled headband and camel cardigan) sitting in the gallery at the back, holding empty plates.
Visual metaphor: a small evidence table in the center with four closed cake boxes of different lid colors (red, blue, green, purple).
Composition: faces and hands inside the central safe area (12% margin left and right, 10% top, 18% bottom); bottom-left corner plain and bright; light falls on the evidence table.
Mood: playful, curious, the moment before the contradiction is revealed.
No text, no letters, no numbers, no logos, no speech bubbles, no weapons, no real brands.
```

## 7. 장면 — `sc_01b_trial` (3:2, 선택)
```
3:2 scene, 1536x1024, same 16-bit high-resolution pixel-art style and characters as the attached cover. The pink-haired girl researcher at the right table, facing left, thrusts a blank grid board forward with determination; small shape-only impact lines around the board (no text, no speech bubble). The fruit fly researcher at the left table, facing right, recoils in surprise, sweat drops, papers flying. The chibi judge at the back raises his eyebrows. Bright daytime lab mock courtroom. No text, no letters, no numbers.
```

## 8. 장면 — `sc_01b_act2` (3:2, 선택)
```
3:2 scene, 1536x1024, same 16-bit high-resolution pixel-art style and characters as the attached cover. Roles reversed: the fruit fly researcher now sits small at a defendant's stool in the middle, clutching a tall pile of work papers. Three cute solid dark navy-black silhouettes with a thin purple rim light and round white dot eyes stand as witnesses: one with a pink ribbon holding an old record book, one with teal glasses reflection holding a magnifier, one with a small yellow bell. The chibi judge brings down the gavel with harmless purple sparks. The ash-beige maid intern quietly brings tea and a slice of cake to the fly. Funny, not scary. No text, no letters, no numbers.
```
