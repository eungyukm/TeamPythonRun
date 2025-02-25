# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 짝수는 싫어요         | [짝수는 싫어요](https://school.programmers.co.kr/learn/courses/30/lessons/120813) |

### Source Code
```python
def solution(n):
    answer = []
    for x in range(1, n + 1):
        if x % 2 == 1:
            answer.append(x)
    
    return answer
```
