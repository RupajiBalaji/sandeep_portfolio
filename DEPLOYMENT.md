# 🚀 Deployment Guide

## Local Development Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git (optional, for version control)

### Setup Steps

1. **Clone/Download Project**
   ```bash
   cd "e:\Django portfolio\myportfolio"
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate Data**
   ```bash
   python manage.py populate_portfolio
   ```

7. **Run Server**
   ```bash
   python manage.py runserver
   ```

---

## Deployment Options

### Option 1: Heroku (Recommended for Beginners)

#### Setup:
1. **Create Heroku Account** - https://www.heroku.com
2. **Install Heroku CLI** - https://devcenter.heroku.com/articles/heroku-cli

#### Deployment Steps:
```bash
# 1. Create requirements file
pip freeze > requirements.txt

# 2. Create Procfile in project root
echo web: gunicorn myportfolio.wsgi > Procfile

# 3. Create runtime.txt
echo python-3.11.7 > runtime.txt

# 4. Configure Django settings
# Edit settings.py:
DEBUG = False
ALLOWED_HOSTS = ['your-app-name.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

# 5. Add environment variables
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com

# 6. Login and deploy
heroku login
heroku create your-app-name
git init
git add .
git commit -m "Initial commit"
git push heroku main

# 7. Run migrations on Heroku
heroku run python manage.py migrate

# 8. Create superuser on Heroku
heroku run python manage.py createsuperuser

# 9. Populate portfolio
heroku run python manage.py populate_portfolio

# 10. Visit your app
heroku open
```

#### Environment Variables:
```bash
heroku config:set SECRET_KEY='your-secret-key-here'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='your-domain.com'
```

---

### Option 2: PythonAnywhere

#### Setup:
1. **Create Account** - https://www.pythonanywhere.com
2. **Upload Project** - Via web console

#### Steps:
1. Go to Dashboard > Web apps
2. Create new web app (select Django + Python 3.10)
3. Upload your project files
4. Configure WSGI file
5. Set up static files
6. Reload web app

#### Configuration:
1. Edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`
2. Point to your Django project
3. Set virtual environment path

---

### Option 3: DigitalOcean (VPS)

#### Prerequisites:
- DigitalOcean account
- SSH knowledge
- Linux basic commands

#### Deployment:
```bash
# 1. Create Droplet (Ubuntu 20.04)
# 2. SSH into droplet
ssh root@your_droplet_ip

# 3. Update system
apt update && apt upgrade -y

# 4. Install dependencies
apt install -y python3-pip python3-venv postgresql nginx

# 5. Clone project
git clone your-repo-url
cd myportfolio

# 6. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 7. Install Python dependencies
pip install -r requirements-production.txt

# 8. Configure PostgreSQL
sudo -u postgres psql
CREATE DATABASE portfolio_db;
CREATE USER portfolio_user WITH PASSWORD 'strong_password';
ALTER ROLE portfolio_user SET client_encoding TO 'utf8';
ALTER ROLE portfolio_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE portfolio_user SET default_transaction_deferrable TO on;
ALTER ROLE portfolio_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;

# 9. Update Django settings
# Edit settings.py with PostgreSQL config:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'portfolio_user',
        'PASSWORD': 'strong_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# 10. Run migrations
python manage.py migrate

# 11. Create superuser
python manage.py createsuperuser

# 12. Collect static files
python manage.py collectstatic --noinput

# 13. Configure Gunicorn
# Create gunicorn_config.py
pip install gunicorn

# 14. Configure Nginx
# Create /etc/nginx/sites-available/portfolio
# Configure as reverse proxy to Gunicorn

# 15. Enable site
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/

# 16. Test Nginx
sudo nginx -t
sudo systemctl restart nginx

# 17. Create systemd service for Gunicorn
# Create /etc/systemd/system/gunicorn.service

# 18. Enable and start service
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
```

---

### Option 4: AWS EC2

#### Instance Setup:
1. Launch Ubuntu 20.04 instance
2. Configure security groups
3. Associate Elastic IP

#### Installation:
Similar to DigitalOcean, but with AWS specifics:
- Use AWS RDS for database
- Use S3 for static/media files
- Use CloudFront for CDN
- Use Route 53 for DNS

---

## Production Checklist

Before deploying, ensure:

- [ ] `DEBUG = False` in settings.py
- [ ] `SECRET_KEY` is secure and not hardcoded
- [ ] `ALLOWED_HOSTS` properly configured
- [ ] Database password changed
- [ ] Static files collected
- [ ] Media files directory created
- [ ] HTTPS/SSL configured
- [ ] Email settings configured
- [ ] Backup strategy in place
- [ ] Logging configured
- [ ] Error monitoring setup (Sentry)
- [ ] Performance monitoring enabled
- [ ] Admin username changed from 'admin'

---

## Security Configuration

### settings.py Production Settings:
```python
import os
from pathlib import Path

# Security
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

---

## Monitoring & Maintenance

### Daily Tasks:
- Monitor server health
- Check error logs
- Verify backups

### Weekly Tasks:
- Review analytics
- Check contact form messages
- Update content if needed

### Monthly Tasks:
- Review security logs
- Update dependencies
- Perform database optimization
- Check SSL certificate expiration

---

## Troubleshooting Deployment

### Issue: Static files not loading
```bash
python manage.py collectstatic --noinput --clear
```

### Issue: Database migration errors
```bash
python manage.py migrate --verbosity 2
```

### Issue: Permission denied errors
```bash
chmod -R 755 staticfiles/
chmod -R 755 media/
```

### Issue: 502 Bad Gateway (Nginx)
Check Gunicorn logs:
```bash
sudo systemctl status gunicorn
sudo journalctl -u gunicorn -n 50
```

---

## Performance Optimization

### Database:
- Add database indexes
- Use connection pooling
- Enable query caching

### Static Files:
- Enable gzip compression
- Use CDN
- Minify CSS/JS

### Caching:
- Implement Redis caching
- Cache template fragments
- Use browser caching headers

---

## Backup Strategy

### Daily Backups:
```bash
# Database backup
pg_dump -U portfolio_user portfolio_db > backup.sql

# Media files backup
tar -czf media_backup.tar.gz /path/to/media/

# Full backup
tar -czf full_backup.tar.gz /var/www/portfolio/
```

### Automated Backups:
```bash
# Add to crontab
0 2 * * * /path/to/backup.sh  # 2 AM daily
```

---

## Support & Resources

- Django Docs: https://docs.djangoproject.com/
- Deployment: https://docs.djangoproject.com/en/6.0/howto/deployment/
- Heroku Django: https://devcenter.heroku.com/articles/deploying-python
- Security: https://docs.djangoproject.com/en/6.0/topics/security/

---

**Deployment successful? Congratulations! 🎉**
