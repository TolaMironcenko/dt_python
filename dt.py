from database.models.UserModel import User
from database.models.ChetModel import Chet
from database.models.TransactionModel import Transaction
from database.base import conn
from repositories.UserRepository import UserRepository
from repositories.ChetRepository import ChetRepository

conn.create_tables([User, Chet, Transaction])

print(UserRepository.create_user(username='tolik', email='tolamironcenko@gmail.com', password='2808'))

# print(ChetRepository.create_chet(user=UserRepository.get_user_by_id(1), name='mom'))

for i in UserRepository.get_chets(user=UserRepository.get_user_by_id(id=1)):
    print(i)
