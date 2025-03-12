# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 제곱수 판별하기         | [제곱수 판별하기](https://school.programmers.co.kr/learn/courses/30/lessons/120909) |

### Source Code
```python
import math

def solution(n):
    root = math.sqrt(n)
    
    answer = 0
    if root.is_integer():
        answer = 1
    else:
        answer = 2
    
    return answer
```
