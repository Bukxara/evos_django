from environs import Env

# environs kutubxonasidan  foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
SECRET_KEY = env.str("SECRET_KEY")  # Django Secret-Key
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
