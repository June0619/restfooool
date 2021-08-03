# RESTfooool

> To be a RESTGenius from a RESTFooool


## Dependencies
    django 3.2.5
    djangorestframework 3.12.4


## Goals
  - Create restful api
  - Structure
    - POST
    - MEMBER
  - It will return only JSON
  - Practice atomic commit

<br>

---
## 기록

### 2021-07-31
- 경솔한 커밋으로 에러를 유발하는 소스가 커밋 되었음 9aec2d24
    - 일관성 있는 커밋을 유지하기 위해서는 커밋 전 테스트가 항상 동반되어야 함
- 앱은 세개로 구성
    - 리소스 단위 앱
        - members
        - post
    - 리소스 전반적으로 다루는 공용 로직이 들어갈 앱
        - common