from typing import TypeVar, Type

T = TypeVar('T', bound='Friend')

class Friend:
    other: "Friend" = None

    @classmethod
    def make_pair(cls: Type[T]) -> tuple[T, T]:
        a, b = cls(), cls()
        a.other = b
        b.other = a
        return a, b

class SuperFriend(Friend):
    pass

a, b = SuperFriend.make_pair()
print(f"a: {a}, b: {b}")