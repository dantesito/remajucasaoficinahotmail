set -o errexit
pip install -r requirements.txt
crawl4ai-setup
crawl4ai-doctor
python manage.py collectstatic --no--input
python manage.py migrate