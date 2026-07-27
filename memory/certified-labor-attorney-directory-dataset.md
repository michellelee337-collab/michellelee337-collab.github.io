---
name: certified-labor-attorney-directory-dataset
description: Use for future analysis of the supplied Korean and English certified labor attorney directory, outreach status, regional coverage, specialties, and linkage to the industrial-robots source corpus.
metadata:
  type: reference
---

# Certified labor attorney directory dataset

## Source and evidence status

- Processed on Thursday, July 23, 2026.
- Source workbook: `/Users/mlee/Desktop/노무사_완성 copy.xlsx`.
- This is user-supplied internal data. Names, affiliations, regions, specialties, and response statuses are verified as present in the workbook, but they are not independently verified for publication.
- The workbook contains no phone numbers or street addresses in the extracted data.
- Before publishing any directory entry, verify the current name, affiliation, title, specialty, and location against a primary official source and confirm any necessary consent.

## Workbook structure

- Two sheets and two tables; no formulas.
- Korean sheet `시트1`: `A1:M371`, with 370 populated data rows and 13 columns.
- English sheet `Sheet1`: table range `A1:L423`, with 422 populated data rows and 12 columns. The worksheet used range extends to row 1000 because of formatting below the table.
- Combined sheet-row count: 792. This is not a count of unique people because the sheets overlap and each sheet contains duplicate names.
- Required directory fields were complete: 0 missing values in name, affiliation, region, or specialization across both sheets.
- Formula-error scan: 0 matches.
- Specialization text and the corresponding `O` indicator columns agreed in every populated row on both sheets: 0 mismatches.
- No unexpected status or marker values were found.

## Korean sheet summary

- 370 rows, 367 unique names, and 361 unique affiliations.
- Region counts: 서울 200; 경기남부 67; 경기북부 20; 인천 17; 부산 13; 대전 9; 대구 8; 전북 6; 강원 5; 충북 5; 경북 4; 울산 4; 충남 4; 경남 3; 전남 3; 광주 1; 세종 1.
- Specialty counts: 부당해고 333; 임금체불 280; 괴롭힘/성희롱 271; 인사노무 171; 기업자문 279; 산업재해 156; 산업안전 56; 노사관계 84.
- Status counts: `No Response` 291; `Completed. Form` 21; `Rejected` 20; `Check Again` 15; `Completed. Email` 14; `Completed. Call` 8; `Completed. Visit` 1.
- The 44 named experts from the industrial-robots source corpus account for all completed named entries: 8 calls, 1 visit, 14 emails, and 21 forms.

## English sheet summary

- 422 rows, 417 unique names, and 365 unique affiliations.
- Region counts: Seoul 239; Gyeonggi South 68; Gyeonggi North 25; Incheon 19; Busan 15; Daejeon 10; Daegu 8; Jeonbuk 6; Chungbuk 5; Gangwon 5; Ulsan 5; Chungnam 4; Gyeongbuk 4; Jeonnam 4; Gyeongnam 3; Gwangju 1; Sejong 1.
- Specialty counts: Unfair Dismissal 375; Unpaid Wages 317; Harassment/Sexual Harassment 311; HR & Labor 202; Corporate Advisory 318; Industrial Accident 177; Industrial Safety 60; Labor Relations 89.
- The English sheet has 52 more populated rows than the Korean sheet. A row-level bilingual equivalence or superset relationship was not independently verified.

## Duplicate-name controls

- Korean sheet: three duplicate names, with no exact duplicate rows.
  - 김혜민: 노무법인 굿컴퍼니, 서울; and 어센트 노무컨설팅, 인천.
  - 김민기: 둥지 노무사사무소, 경기남부; and 노동법률사무소 성남, 경기남부.
  - 이지혜: 노무법인 강앤파트너스, 경기남부; and 온힘 노동법률사무소, 경기남부.
- English sheet: five duplicate names, with no exact duplicate rows: Mingi Kim, Jihye Lee, Hyeongu Lee, Hyemin Kim, and Gwangsu Park.
- Always use name plus affiliation, and region when available, to identify a directory entry.
- Critical source disambiguation: the completed email response by 김혜민 belongs to 노무법인 굿컴퍼니 in 서울. The same-name 어센트 노무컨설팅 entry in 인천 has `No Response` status.

## Link to the industrial-robots source corpus

- All 44 named experts in the calls, visit, emails, and survey were found by exact Korean-name match in the Korean directory sheet: 44 of 44 matched.
- The anonymous telephone-labeled call source is intentionally excluded from name matching and remains `anonymous certified labor attorney A`.
- Directory status aligned with the source inventory: 8 `Completed. Call`, 1 `Completed. Visit`, 14 `Completed. Email`, and 21 `Completed. Form`.
- Detailed source views and substantive findings remain in [Industrial robots and worker protection source corpus](industrial-robots-worker-protection-source-corpus.md).

### Completed calls and visit

- 김희연, 제일인사노무법인 (평택지사), 경기남부: `Completed. Call`.
- 모승재, 공인노무사 로앤HR컨설팅, 경기남부: `Completed. Call`.
- 박한울, 노동법률사무소 동감, 세종: `Completed. Call`.
- 송준규, 가우 노동법률사무소, 서울: `Completed. Call`.
- 안찬호, 포스원 노무법인, 서울: `Completed. Call`.
- 임창근, 노동법률사무소 필립, 경기남부: `Completed. Call`.
- 정시현, 노무법인 청인 서울본사, 서울: `Completed. Visit`.
- 정재혁, 대선노무사사무소, 서울: `Completed. Call`.
- 홍난의, 의진 노무사 사무소, 인천: `Completed. Call`.

### Completed emails

- 고병일, 미래노무법인, 서울.
- 권현애, 노무법인 정권, 경기남부.
- 김록영, 라라 노무법인, 서울.
- 김서하, 노동법률사무소 해오름, 서울.
- 김수경, 노무법인 가치 서울지사, 서울.
- 김혜민, 노무법인 굿컴퍼니, 서울.
- 박도제, 지무 노동법률사무소, 서울.
- 박채원, 노동법률사무소 모간, 서울.
- 신욱철, 노무법인 예인, 대구.
- 이수인, 노무법인 정성인사노무컨설팅, 서울.
- 이준구, 노무법인 해성, 서울.
- 정구현, 노무법인 한그루, 서울.
- 조서연, 선율노무법인 서울경인지사, 서울.
- 한현정, 노무법인 리원, 서울.

### Completed forms

- 강영조, 노무법인 이산 원주지사, 강원.
- 윤정토, 노무법인 종로 안산지사, 경기남부.
- 박준우, 노무사사무소 강인, 경기남부.
- 박천조, Xp노사관계컨설팅, 경기북부.
- 이성흠, 이성흠노무컨설팅, 경기남부.
- 박우균, 노무법인 나래, 부산.
- 김세원, 노동법률사무소 우상, 서울.
- 김우현, 노무법인 성공 산재보상센터, 서울.
- 이상협, 노무법인 지음, 서울.
- 신희지, 노무법인아테네, 서울.
- 유리나, 노무법인 유연, 서울.
- 정혜영, 온기 공인노무사 사무소, 서울.
- 신호순, 노무법인 서해, 인천.
- 지정은, 노무법인 더보상 전남여수지사, 전남.
- 최준호, 노무법인 태영, 서울.
- 최정호, 노무법인 마루, 전북.
- 유용호, 근본 노동법률사무소, 인천.
- 이동진, 노무법인 당찬, 충남.
- 박은중, 노동법률자문 법제, 서울.
- 김나희, 노무법인 우린인사컨설팅, 경기남부.
- 김가을, 노무법인 가온, 경기남부.

## Still open before use or publication

1. Do not treat 792 sheet rows as 792 unique people. The bilingual sheets overlap, and their exact row-level relationship remains unverified.
2. Resolve duplicate names by affiliation and region before attribution, outreach, or analysis.
3. Verify all directory facts against current primary official sources before publication.
4. Confirm consent before publishing names in connection with interview content or direct quotations.
5. Keep anonymous certified labor attorney A unnamed and exclude the telephone number embedded in the original source filename.
