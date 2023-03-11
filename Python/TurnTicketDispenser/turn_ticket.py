from typing import Type, Protocol


class Ticket(Protocol):
    def __init__(self, number: int):
        ...


class TurnTicket:
    def __init__(self, turn_number):
        self.turn_number = turn_number


class Sequence(Protocol):
    @classmethod
    def next_turn_number(cls) -> int:
        ...


class TurnNumberSequence:
    _turn_number = -1

    @classmethod
    def next_turn_number(cls):
        cls._turn_number += 1
        return cls._turn_number


class TicketDispenser:
    def __init__(self, sequence: Type[Sequence], ticket: Type[Ticket]):
        self._ticket = ticket
        self._sequence = sequence

    def get_turn_ticket(self):
        new_turn_number = self._sequence.next_turn_number()
        new_turn_ticket = self._ticket(new_turn_number)
        return new_turn_ticket
