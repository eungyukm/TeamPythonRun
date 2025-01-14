# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 문자열안에 문자열         | [문자열안에 문자열](https://school.programmers.co.kr/learn/courses/30/lessons/120908) |

### Source Code
```python
def solution(str1, str2):
    index = str1.find(str2)
    if index != -1:
        return 1
    else:
        return 2
```
