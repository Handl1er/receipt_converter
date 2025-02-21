# Receipt Converter
Django-сервис для распознавания чеков и конвертации в Excel.

## 🚀 Функционал:
- Загрузка чеков (JPG, PNG, PDF)
- OCR-распознавание текста
- Экспорт в Excel
- API и Telegram-бот (в разработке)

## 🛠 Установка
```bash
git clone https://github.com/Handl1er/receipt_converter.git
cd receipt_converter
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
