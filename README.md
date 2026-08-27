# mode-matrix

[English](README.en.md)

디렉터리 트리의 POSIX 권한 모드를 요약.

한 가지 일을 명확하게 수행하는 가벼운 Python 명령줄 도구입니다:
**파일 권한 모드 요약**.

## 주요 특징

- 예측 가능한 텍스트 출력을 제공하는 단일 목적 CLI
- 실행 시 Python 표준 라이브러리만 사용
- 다른 스크립트에서 재사용할 수 있는 핵심 함수
- 단위 테스트와 GitHub Actions CI 포함

## 요구 사항

Python 3.11 이상이 필요합니다.

## 설치

~~~bash
git clone https://github.com/Kwondh0321/mode-matrix.git
cd mode-matrix
python -m pip install .
~~~

격리된 명령줄 환경에서는 pipx install .도 사용할 수 있습니다.

## 빠른 시작

~~~bash
mode-matrix .
~~~

모든 옵션은 mode-matrix --help에서 확인할 수 있습니다.

## 개발

~~~bash
python -m unittest discover -s tests -v
python mode_matrix.py --help
~~~

## 범위

이 저장소는 의도적으로 작게 유지합니다. 큰 의존성 트리나 대화형
인터페이스보다 투명한 동작, 표준 형식, 셸 파이프라인과의 조합을
우선합니다.

## 라이선스

MIT
