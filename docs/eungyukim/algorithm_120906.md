# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 자릿수 더하기         | [자릿수 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/120906?language=python3) |

### Source Code
```python
def solution(n):
    sum = 0
    while(n > 0):
        sum = sum + (n % 10)
        n = n // 10
        
    return sum
```
