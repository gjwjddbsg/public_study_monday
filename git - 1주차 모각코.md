# Git - 1주차 모각코 



- 발표 장소 : 큐브동
- 참석인원 : 한승민, 허정윤, 김채영, 최근휘 홍진백, 이문현, 이재규 총 7명

- 발표자 : 홍진백
- 발표자료 : 이재규

## git, github 를 쓰는 이유

프로그래밍 만드는것이 힘든 일인데 중간 중간마다 버전을 두어 기능을 추가할때 문제가 생기면 버전을 다시 되돌아가기 위해 쓴다.

ex ) 과제_ 최종_ 최종_ 최종.py 이런 상황을 없앨 수 있다. ( 버전 관리 )

​       포트폴리오가 될 수 있다.

## git 설치 하기

- windows 사용자는 git bash 

- mac 사용자는 brew install git

## GitHub 가입하기

- 과기대모각코 organization 가입

## repository

- 레포지토리란?
  - 일종의 원격 저장소
  - README를 통해 문서화 가능
  - Code 를 업로드할 수 있음

- 개인 리포지토리 만들어보기

## git user email , name 추가

git config —global user.email "your email"

git config —global user.name "your name"



## git init

만들고자 하는 리포지토리에 git init

## git status

변경사항 확인

버전이 다른 것 확인

## git add

git add . 현재 변경사항 있는 것 모두 스테이징 ( 커밋하기 전 상태 )

## git commit

커밋 버전관리 하는용도 

git commit -m "제목"

제목이 바로 커밋제목으로 올라감

## git push

하기전에 remote repository 를 추가해줘야하는데

## git remote add origin "git repository url"

해당 명령을 치면 원격 리포지토리와 연결이 된다.

origin 이 url의 별명

## git push origin master

원격 리포지토리에 올리기

git push [리포지토리 별명] [브랜치 이름]

## Branch 

쓰는 이유 !

마스터와는 다른 버전을 생성하여 마스터에는 완전한 코드를 올리고 다른 브랜치에서는 기능 추가 등 다른 기능을 만들기 위해서 사용!

## Branch 생성

git checkout 브랜치명

브랜치 변경

git checkout -b 브랜치명

브랜치명으로 브랜치 생성후 그 브랜치로 이동



## git pull

pull은 원격리포지토리와 로컬 리포지토리를 같게 만드는 명령어!

원격리포지토리에 커밋이 더 있는 경우에 로컬에 리포지토리에 커밋을 가져와서 적용해준다.

쓰는 법 : git pull [리포지토리 별명] [브랜치명]

ex) git pull origin master

## 가장 기본적인 git 명령어는 끝!

이후 더 쓰고 싶은 기능은

[더 알아보기](https://rogerdudler.github.io/git-guide/index.ko.html)

여기서 공부합시다~