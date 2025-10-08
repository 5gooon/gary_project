
# Git & GitHub 완전 입문 가이드

## 1. Git이란?
버전 관리 시스템(Version Control System)으로, 코드나 문서의 변경 이력을 기록하고 협업을 쉽게 도와주는 도구입니다.

## 2. Git의 3가지 공간
- Working Directory : 실제로 파일을 수정하는 공간
- Staging Area : 커밋할 파일을 선택해두는 공간
- Repository : 커밋되어 버전으로 저장된 공간

## 3. Git 기본 설정
```
git config --global user.name "이름"
git config --global user.email "이메일"
```

## 4. 기본 작업 흐름
```
작업 → git add → git commit → git push
```
예시:
```
git init
git add .
git commit -m "첫 커밋"
git push origin main
```

## 5. GitHub 연결
```
git remote add origin https://github.com/username/repository.git
git push -u origin main
```
GitHub는 온라인 원격 저장소로, 다른 사람과 협업하거나 백업할 때 사용합니다.

## 6. VS Code에서 Git 보기
- 왼쪽 Source Control 아이콘 (Ctrl + Shift + G)
- “+” 버튼 : git add
- “✔️” 버튼 : git commit
- 하단 브랜치 이름 클릭 → 브랜치 변경 가능

## 7. 브랜치 기본 명령어
```
git branch           # 브랜치 목록 보기
git switch -c dev    # 새 브랜치 생성 후 이동
git switch main      # main 브랜치로 돌아가기
```

## 8. 자주 쓰는 명령어 요약
| 명령어 | 설명 |
|---------|------|
| git status | 변경된 파일 상태 확인 |
| git log --oneline | 커밋 기록 요약 보기 |
| git diff | 수정된 내용 비교 |
| git pull | 원격 저장소에서 변경사항 가져오기 |
| git push | 변경사항 업로드 |

## 9. 문제 해결
- push 실패 시 (rejected):
```
git pull origin main --rebase
git push origin main
```
- 강제로 덮어쓰기:
```
git push origin main --force
```

## 10. 연습 예시
```
mkdir git-practice
cd git-practice
git init
echo "hello git" > readme.txt
git add readme.txt
git commit -m "첫 커밋"
git log --oneline
```

---
**Tip:** Git은 ‘변경 이력을 기록하는 타임머신’이다. 커밋을 자주 남겨라!
