# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 짝수의 합          | [짝수의 합](https://school.programmers.co.kr/learn/courses/30/lessons/120831) |

### Source Code
```python
def solution(n):
    sum = 0
    for a in range(n+1):
        if a % 2 == 0:
            sum += a
    answer = sum
    return answer
```
