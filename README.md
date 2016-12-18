# <font color="green"> <b> Jirim </b> </font>
A forest of knowledge.
 
## 기능
1. 실시간 네이버 검색어 10개 보여주기
2. 키워드 "A" 입력 -> 연관 검색어 "A'", "A''", "A_" 보여주기.
3. 키워드 "A" 입력 ->  "A"의 연관 검색어 "A'", "A''", "A_"등을 다시 검색

## 청사진
<img src="https://raw.githubusercontent.com/Pangyo/jirim/master/etc/jirim_blueprint.png">

## Simple Architecture
<img src="https://github.com/Pangyo/jirim/blob/master/etc/jirim_arch.png?raw=true">

## 데이터 모델
1. Keyword - strng
  * name - String
  * link - String
  * list<Keyword>

### 예시
```
박근혜.name = "박근혜"
박근혜.link = {url}
박근혜.list = [청와대, 최순실]

```

## Dependencies
* Web
  * bottle framework
* Persistent
  * bottle framework
  * sqlite3
  * peewee (ORM Framework)
