# programmers

| 문제 플랫폼   | 문제 이름           | 링크                                   |
|---------------|--------------------|----------------------------------------|
| 프로그래머스          | 머쓱이보다 키 큰 사람          | [머쓱이보다 키 큰 사람](https://school.programmers.co.kr/learn/courses/30/lessons/120585) |

### Source Code
```python
def solution(array, height):
    count = 0
    for h in array:
        if h > height:
            count += 1
    answer = count
    return answer
```
