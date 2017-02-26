# <font color="green"> <b> Jirim </b> </font>
A forest of knowledge.

## 기능
1. 실시간 네이버 검색어 10개 보여주기
2. 키워드 "A" 입력 -> 연관 검색어 "A'", "A''", "A_" 보여주기.
3. 키워드 "A" 입력 ->  "A"의 연관 검색어 "A'", "A''", "A_"등을 다시 검색

## 청사진
<img src="https://raw.githubusercontent.com/Pangyo/jirim/master/etc/jirim_blueprint.png">

## Simple Architecture
<img src="https://github.com/Pangyo/jirim/blob/master/etc/jirim_arch2.png?raw=true">

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

## 개발 환경 셋팅
#### Python3 설치
  * Mac
    * 설치 패키지 다운로드 해서 설치 version=3.6.0 [다운](https://www.python.org/ftp/python/3.6.0/python-3.6.0-macosx10.6.pkg)
  * Window
    * exe파일 다운 x86-64 version=3.6.0 : [다운](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe)

#### pip3 설치 (python package manager)
  * [get-pip.py](https://bootstrap.pypa.io/get-pip.py) 다운
  * python3 get-pip.py 실행

#### virtualenv로 python 실행 환경 분리
  * 파이썬3은 venv를 내장하고 있다.
  * python3 -m venv {env name}
    * 위의 명령어를 실행하면 현재 디렉토리 밑에 {env name}의 폴더가 생성됨.
  * . ./{env name}/bin/activate로 activation함.
    * shell 커멘드라인의 가장 앞에 (env)가 표시 되면 활성화 된 것
    * which python, which pip3를 했을때 {env name}밑에 있는 bin의 python 경로가 표시되면 정상적으로 활성화 된 것.
    * 활성화 되었으면 python 명령어는 기본적으로 python 3.6.0버전이다
  * deactivate로 비활성화
  * 모든 python관련 명령어를 실행할때에는 virtualenv가 활성화된 상태에서 해야 한다. (e.g. Shell.py실행, pip3로 패키지 설치 등등)

#### 프로젝트에 필요한 python package를 설치
  * requirements.txt에 dependency들이 작성되어 있음.
  * pip3 install -r requirements.txt 명령어로 한번에 설치.

#### 새로운 dependency를 추가할 때
  * pip3 install {package}로 설치를 하고 난후
  * pip3 freeze > requirements.txt로 requirements.txt 파일을 업데이트 해줘야함.
