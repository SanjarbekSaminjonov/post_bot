from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn

ADMINS = env.list("ADMINS")  # adminlar ro'yxati

IP = env.str("IP")  # Xosting ip manzili

CHANNELS = env.list("CHANNELS")  # kanallar ro'yxati

FORCED_CHANNELS = env.list("FORCED_CHANNELS")  # obuna shart kanallar ro'yxati
