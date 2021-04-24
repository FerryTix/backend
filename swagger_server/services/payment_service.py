from uuid import uuid4

from typing import Optional

from swagger_server.models import FaehrCardPayment, TicketSaleFaehrCard, TicketSaleCash, CashPayment, TopUp
from swagger_server.dao import payment_dao as PaymentDao
from swagger_server.dao import faehrcard_dao as FaehrcardDao
from swagger_server.dao import ticket_sale_dao as TicketSaleDao
from swagger_server.dao import top_up_dao as TopUpDao


def create_ticket_sale_faehrcard(ticket_sale_faehrcard: TicketSaleFaehrCard):
    uuid = create_faehrcard_payment(ticket_sale_faehrcard.faehr_card_payment)
    if uuid:
        ticket_sale_faehrcard.faehr_card_payment = uuid
        TicketSaleDao.insert_faehrcard(ticket_sale_faehrcard)
        return None, 201


def create_ticket_sale_cash(ticket_sale_cash: TicketSaleCash):
    uuid = create_cash_payment(ticket_sale_cash.cash_payment)
    if uuid:
        ticket_sale_cash.cash_payment = uuid
        TicketSaleDao.insert_cash(ticket_sale_cash)
        return None, 201


def top_up_faehrcard(top_up: TopUp):
    faehr_card = FaehrcardDao.find_by_uuid(top_up.card)
    if faehr_card:
        uuid = create_cash_payment(top_up.payment)
        if uuid:
            top_up.payment = uuid
            TopUpDao.insert_cash(top_up)
            faehr_card.balance = faehr_card.balance + top_up.amount
            TopUpDao.insert_cash(top_up)
            FaehrcardDao.update(faehr_card)
            return {"newbalance": faehr_card.balance}, 201
    else:
        return 'no FaehrCard with given uuid found', 404
    return None


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
