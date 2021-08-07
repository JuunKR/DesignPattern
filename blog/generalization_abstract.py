'''
상속은 부모에서 자식으로 !
자식클래스가 부모클래스의 기능과 속성에 접근이 가능하다.
자식크래스에서 부모클래스의 기능과 속성을 재정의할 경우 오버라이딩이라하고 기존의 내용에 새로운 내용을 덮어쓴다.
'''
# 부모 클래스
from abc import ABCMeta, abstractmethod


class Parents(object):
    def __init__(self):
        self.mother ='mother'
        self.father = 'father'
    
    def my_family(self):
        return (f'우리 가족의 구성원은 {self.mother}, {self.father} 입니다')
        
# 부모클래스 상속받음
class Child(Parents):
    
    def __init__(self):
        # 부모클래스의 생성자를 가져옴(상속)
        super().__init__()
        self.child = 'child'
        # mother을 자식클래스에서 재정의(오버라이딩)
        self.mother = 'new_mother'

    # 부모클래스에 있는 메소드를 재정의
    def my_family(self):
        return (f'우리 가족의 구성원은 {self.mother}, {self.father}, {self.child} 입니다')


if __name__ == '__main__':
    parents = Parents()
    child = Child()

    # 부모클래스의 mother와 자식클래스의 mother가 다름
    print(parents.mother)
    # mother
    print(child.mother)
    # new_mother

    #자식 클래스에서 생성하지 않은 father을 부모에서 상속받아 사용 가능
    print(child.father)
    # father
    
    # 부모클래스와 자식클래스의 메소드 결과가 다름(오버라이딩)
    # 자식클래스에서 정의를 안한 father을 자식클래스에서도 사용가능(상속)
    print(parents.my_family())
    # 우리 가족의 구성원은 mother, father 입니다
    print(child.my_family())
    # 우리 가족의 구성원은 new_mother, father,  child입니다

'''
추상클래스

추상클래스는 설계도와 비슷하다. 
추상클래스는 구현메서드와 추상메서드가 동시적으로 존재할 수 있다.
구현메서드는 실제 구현 내용을 포함한 메서드이다.
추상메서드는 선언만 된 메서드이다.
추상클래스는 단독으로  객체를 생성할 수 없고 구현 내용을 추가하는 자식클래스에서의 오버라이딩을 통해 객체를 생성
'''


# abc = abstract base class 의 약자
import abc
class Abstract_family(metaclass=ABCMeta):
    
    # 구현 메서드
    def __init__(self):
        self.mother = 'mother'
        self.father = 'father'
    
    #추상메서드로 지정 - 기능구현을 하지 않는다.
    @abstractmethod
    def my_family(self):
        pass

# 추상 클래스를 상속받는다.
class Myfamily(Abstract_family):
    def __init__(self):
        super().__init__()

    # 추상메서드를 구현해주지 않으면 오류가 걸린다.
    # 오버라이딩을 통해 추상메서드 구현
    def my_family(self):
        return (f'우리 {self.mother}, {self.father} 최고')


if __name__ == '__main__':
    
    myfamily = Myfamily()
    
    print(myfamily.my_family())
    # 우리 mother, father 최고