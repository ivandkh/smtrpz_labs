from cards import CardType, TimeDuration
from register import Register
from turnstile import Turnstile


def test_ban():
	reg = Register('Metropoliten1')
	time = TimeDuration.OneMonth
	c2 = reg.create_card(CardType.TimeLimit, time)
	reg.ban_card(c2.id)

	assert c2.id in reg.banned.keys()

def test_creation():
	reg = Register('Metropoliten2')
	time = TimeDuration.OneMonth
	c1 = reg.create_card(CardType.TimeLimit, time)
	assert c1.id in reg.cardsID

def test_logs():
	reg = Register('Metropoliten3')
	t = Turnstile(reg, id_=1, fare = 8.0)
	c3 = reg.create_card(CardType.BalanceLimit, 12)
	c4 = reg.create_card(CardType.BalanceLimit, 3)
	
	t(c3.id)
	t(c4.id)

	log = [ID for ID, _, _ in reg.log]	
	assert c3.id in log and c4.id in log


