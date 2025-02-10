# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 삼각형의 완성조건 (1)         | [삼각형의 완성조건 (1)](https://school.programmers.co.kr/learn/courses/30/lessons/120889) |

### Source Code
```python
def solution(sides):
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2
```
