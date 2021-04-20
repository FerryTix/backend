#
#{
#  "from": "Bislich",
#  "issuedAt": "2021-04-11T15:45:57.643Z",
#  "issuedBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
#  "payment": {
#    "amount": 0,
#    "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
#  },
#  "positions": [
#    {
#      "count": 0,
#      "fare": {
#        "fare": 5,
#        "ticketClass": {
#          "bicycle": true,
#          "reduced": true,
#          "return": true,
#          "staff": true
#        }
#      }
#    }
#  ],
#  "returnValid": true,
#  "saleCounter": 0,
#  "signature": "string",
#  "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
#}

#["FährCard", "Cash", "ECCard", "BankTransfer", "PayPal"]
from uuid import uuid4

from dataclasses import asdict
from typing import Optional

from swagger_server.models import FaehrCardPayment, TicketSaleFaehrCard, TicketSaleCash, CashPayment
from swagger_server.dao import payment_dao as PaymentDao
from swagger_server.dao import faehrcard_dao as FaehrcardDao
from swagger_server.dao import ticket_sale_dao as TicketSaleDao


def create_ticket_sale_faehrcard(ticket_sale_faehrcard: TicketSaleFaehrCard):
    uuid = create_faehrcard_payment(ticket_sale_faehrcard.faehr_card_payment)
    if uuid:
        ticket_sale_faehrcard.faehr_card_payment = uuid
        TicketSaleDao.insert_faehrcard(ticket_sale_faehrcard)


def create_ticket_sale_cash(ticket_sale_cash: TicketSaleCash):
    uuid = create_cash_payment(ticket_sale_cash.cash_payment)
    if uuid:
        TicketSaleDao.insert()


def create_faehrcard_payment(faehrcard_payment: FaehrCardPayment) -> Optional[str]:
    if not faehrcard_payment.payment.uuid:
        faehrcard_payment.payment.uuid = uuid4()
    uuid = faehrcard_payment.payment.uuid
    faehr_card = FaehrcardDao.find_by_uuid(faehrcard_payment.uuid)
    if faehr_card:
        faehr_card_bal = faehr_card.balance
        if faehr_card_bal >= faehrcard_payment.payment.amount:
            result = PaymentDao.insert(faehrcard_payment.payment)
            if result:
                faehr_card.balance = faehr_card.balance - faehrcard_payment.payment.amount
                FaehrcardDao.update(faehr_card)
                return uuid
    return None


def create_cash_payment(cash_payment: CashPayment) -> Optional[str]:
    if not cash_payment.payment.uuid:
        cash_payment.payment.uuid = uuid4()
    uuid = cash_payment.payment.uuid
    result = PaymentDao.insert(cash_payment.payment)
    if result:
        return uuid
    else:
        return None

