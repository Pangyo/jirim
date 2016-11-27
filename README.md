# <font color="green"> <b> Jirim </b> </font>
A forest of knowledge.

## 기능
1. 실시간 네이버 검색어 10개 보여주기
2. 키워드 "A" 입력 -> 연관 검색어 "A'", "A''", "A_" 보여주기.
3. 키워드 "A" 입력 ->  "A"의 연관 검색어 "A'", "A''", "A_"등을 다시 검색

## 청사진
<img src="https://raw.githubusercontent.com/Pangyo/jirim/master/etc/jirim_blueprint.png">

## 데이터 모델
1. Keyword
  * id
  * kind
    * group(단체)
    * person(사람)
    * unknown(처음 추가 시)
    * relation(g-g, p-p, g-p 사이에 존재)
  * name
  * description
  * list<Edge>(인접 keyword)
2. Edge(keyword 사이에 존재)
  * Weight
  * To

### 예시
```
1.kind = person
1.name = 박근혜
1.List<Edge> = { 40년 우정, 구국봉사단, 초기비서실장, 최순실 }
1.description = 대통령

2.kind = person
2.name = 최순실
2.List<Edge> = {40년 우정, 구국봉사단, 비선모임, 정유라 }
2.description = 샤먼

3.kind = group
3.description = 대한민국 청와대
3.name = 청와대
3.List<Edge> = {박근혜, 최순실, 이명박}

4.kind = relation
4.name = 40년 우정
4.List<Edge> = {박근혜, 최순실}
```

## Dependencies
* Web
  * bottle framework
* Persistent
  * bottle framework
  * sqlite3
  * peewee (ORM Framework)
