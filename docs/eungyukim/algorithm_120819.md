# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 아이스 아메리카노         | [아이스 아메리카노](https://school.programmers.co.kr/learn/courses/30/lessons/120819) |

### Source Code
```python
def solution(money):
    answer = []
    answer.append((int)(money / 5500))
    answer.append((int)(money % 5500))
    return answer
```
