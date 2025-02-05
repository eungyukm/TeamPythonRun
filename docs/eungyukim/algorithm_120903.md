# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 배열의 유사도          | [배열의 유사도](https://school.programmers.co.kr/learn/courses/30/lessons/120903) |

### Source Code
```python
def solution(s1, s2):
    answer = 0
    for x in s1:
        for y in s2:
            if x == y:
                answer += 1
    return answer
```
