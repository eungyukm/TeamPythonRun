# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 중복된 숫자 개수         | [중복된 숫자 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120583?language=python3) |

### Source Code
```python
def solution(array, n):
    answer = 0
    for x in array:
        if n == x:
            answer+= 1
    return answer
```
