import threading 

class Account():
	def __init__(self, owner, balance):
		self.owner = owner
		self._balance = balance
		self._lock = threading.Lock()


	def change_balance(self, change):
		if not self._balance + change >= 0:
			raise Exception
		else: 
			self._balance += change


class Bank():
	def __init__(self):
		self.accounts = []


	def transfer(self, source, target, amount):
		if source in self.accounts and target in self.accounts:
			try:
				
				source._lock.acquire()
				target._lock.acquire()
				source.change_balance(-amount)
				target.change_balance(amount)
			except:
				print("Not enough money!")

			finally:
				source._lock.release()
				target._lock.release()

		else : 
			print('Account not found.')

	def create_acc(self, owner, balance):
		acc = Account('owner', balance)
		self.accounts.append(acc)

		return acc



if __name__ == '__main__':
	bank = Bank()
	main_acc = bank.create_acc('Name', 0)
	#acc = Account('Name', 100)

	def tranfer_from_minors(amount):
		minor_acc = bank.create_acc('Name', amount)
		bank.transfer(minor_acc, main_acc, amount)


	threads = []
	for i in range(100):
		thread = threading.Thread(target = tranfer_from_minors, args=(100,))
		threads.append(thread)

		thread.start()

	for th in threads:
		th.join()

	print('Total money now:', main_acc._balance)