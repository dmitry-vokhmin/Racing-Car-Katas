import unittest

from turn_ticket import TicketDispenser, TurnTicket, TurnNumberSequence


class TicketDispenserTest(unittest.TestCase):

    def test_tickets(self):
        dispenser = TicketDispenser(TurnNumberSequence, TurnTicket)
        second_dispenser = TicketDispenser(TurnNumberSequence, TurnTicket)

        ticket = dispenser.get_turn_ticket()
        second_ticket = second_dispenser.get_turn_ticket()
        third_ticket = dispenser.get_turn_ticket()

        self.assertEqual(ticket.turn_number, 0)
        self.assertEqual(second_ticket.turn_number, 1)
        self.assertEqual(third_ticket.turn_number, 2)


if __name__ == "__main__":
    unittest.main()
