# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 세균 증식        | [세균 증식](https://school.programmers.co.kr/learn/courses/30/lessons/120910) |

### Source Code
```python
def solution(n, t):
    answer = n
    for _ in range(t):
        answer *= 2
    return answer
```
