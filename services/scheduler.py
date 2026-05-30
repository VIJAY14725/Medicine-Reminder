import threading
from datetime import datetime

from Config.settings import CHECK_INTERVAL_SECONDS
from services.data_services import load_medicines
