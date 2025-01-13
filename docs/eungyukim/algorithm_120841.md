# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 점의 위치 구하기         | [점의 위치 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/120841) |

### Source Code
```python
def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] > 0 and dot[1] < 0:
        return 4
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    answer = 0
    return answer
```
