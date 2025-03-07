# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 문자 반복 출력하기          | [문자 반복 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/120825) |

### Source Code
```python
def solution(my_string, n):
    answer = ""
    for char in my_string:
        answer += char * n
    return answer
```
