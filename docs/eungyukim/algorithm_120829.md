# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 각도기          | [각도기](https://school.programmers.co.kr/learn/courses/30/lessons/120829) |

### Source Code
```python
def solution(angle):
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle < 180:
        answer = 3
    else:
        answer = 4
    return answer
```
