# 클래스

### 상속

- 부모의 정의한 기본값인 init과 부모의 메소드를 상속받은 자식이 사용 가능

### 다중 상속

- 다중으로 상속 받을 수 있으며, 부모는 포괄 자식은 세분화됨

![Untitled](https://github.com/GEON1999/web_scraper/blob/main/python_basic/img/multiple_inheritance.png?raw=true)

![Untitled](https://github.com/GEON1999/web_scraper/blob/main/python_basic/img/multiple_inheritance2.png?raw=true)

### 메소드 오버 라이딩

- 상속을 받으면 자식 클래스는 부모 클래스의 메소드를 사용할 수 있다.
    - 그러나 부모 메소드를 사용할 경우엔, 자식 메소드에서 가지고 있는 기본 값을 호출 시 기입해주어야한다.
    - 아래 이미지를 보면 배틀크루저는 이름 값을 가지고 있음에도 “fly” 라는 부모 메소드를 사용할 때는 name 값을 기입 해주어야한다.
    
    ![Untitled](https://github.com/GEON1999/web_scraper/blob/main/python_basic/img/overriding.png?raw=true)
    
    - 이때 사용할 수 있는 것이 메소드 오버라이딩인데 예시는 아래와 같다.
    
    ![Untitled](https://github.com/GEON1999/web_scraper/blob/main/python_basic/img/overriding2.png?raw=true)
    
    - 자식 클래스에서 메소드를 다시 정의하는데, 부모 메소드를 호출하여 동작하는 건 똑같다.

### pass

- 아무것도 안하고 그냥 넘어간다는 의미

### super

- 단독 상속 시 부모 클래스를 상속 받을 때 사용 가능

![Untitled](https://github.com/GEON1999/web_scraper/blob/main/python_basic/img/super.png?raw=true)

- 다중 상속 시엔 첫번 째 부모만 상속받음 (그럼으로 다중 상속 시엔 super 사용 지양)
- self 없이 사용
