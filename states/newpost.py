from aiogram.dispatcher.filters.state import StatesGroup, State


class AccountData(StatesGroup):
    accountImage = State()
    sellingType = State()
    allPlayersCount = State()
    ftPlayersCount = State()
    imPlayersCount = State()
    legendPlayersCount = State()
    coinsCount = State()
    price = State()
    contact = State()
    finishPost = State()
