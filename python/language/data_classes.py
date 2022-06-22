import random
import string
from dataclasses import dataclass, field


@dataclass(slots=True, kw_only=True)  # (frozen=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    _id: str = field(init=False, default_factory=lambda: "".join(random.choices(string.ascii_uppercase, k=12)))
    _search_string: str = field(repr=False, init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, '_search_string', f'{self.name} and {self.address}')


def main() -> None:
    person = Person(name='John', address='123 Main St')
    print(person)


if __name__ == "__main__":
    main()
