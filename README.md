# test-project

간단한 Hello World 파이썬 예제 프로젝트입니다.

## 구조

- `src/hello.py`: 메시지 함수 + 실행 엔트리포인트
- `tests/test_hello.py`: 기본 단위 테스트

## 실행

```bash
python3 src/hello.py
```

## 테스트

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```
