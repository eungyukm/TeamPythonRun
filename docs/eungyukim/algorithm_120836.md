# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 순서쌍의 개수         | [순서쌍의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120836) |

### Source Code
```python
def solution(n):
    answer = 0
    for x in range(1, n+1):
        if n % x == 0:
            answer += 1
    
    return answer
```
