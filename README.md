# 🎨 Shalem Sandeep - AI Developer Portfolio

A modern, professional, and attractive Django-based portfolio website designed to showcase AI/ML projects and expertise to top product-based companies.

## ✨ Features

- **Modern Design**: Sleek, gradient-based UI with smooth animations
- **Responsive**: Fully responsive across all devices (mobile, tablet, desktop)
- **Projects Showcase**: Beautiful project cards with technology tags, links, and detailed descriptions
- **Skills Management**: Organized skill categories with proficiency levels
- **Experience Timeline**: Professional timeline of work experience
- **Education & Certifications**: Complete educational background and certifications
- **Contact Form**: Professional contact form with message storage
- **Admin Panel**: Easy-to-use Django admin interface to manage all content
- **Performance Optimized**: Fast loading, lazy loading images, smooth animations

## 🚀 Quick Start

### 1. **Install Dependencies**

```bash
# Navigate to project directory
cd "e:\Django portfolio\myportfolio"

# Install required packages
pip install -r ../requirements.txt
```

### 2. **Set Up Database**

```bash
# Run migrations
python manage.py migrate
```

### 3. **Create Admin User**

```bash
python manage.py createsuperuser
# Follow the prompts to create your admin account
```

### 4. **Populate Portfolio with Data**

```bash
# Load your resume data into the portfolio
python manage.py populate_portfolio
```

### 5. **Run Development Server**

```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

## 📁 Project Structure

```
myportfolio/
├── portfolio/                 # Main portfolio app
│   ├── migrations/           # Database migrations
│   ├── management/           # Management commands
│   ├── templatetags/         # Custom template filters
│   ├── static/               # CSS, JavaScript, Images
│   │   └── portfolio/
│   │       ├── css/
│   │       │   └── style.css # Main styling
│   │       ├── js/
│   │       │   └── main.js   # JavaScript interactions
│   │       └── images/
│   ├── templates/            # HTML templates
│   │   └── portfolio/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── portfolio.html
│   │       ├── about.html
│   │       ├── contact.html
│   │       └── project_detail.html
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # App configuration
│   ├── forms.py             # Contact form
│   ├── models.py            # Database models
│   ├── urls.py              # App URLs
│   └── views.py             # Views logic
├── myportfolio/             # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URLs
│   ├── wsgi.py
│   └── asgi.py
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

## 🎯 Pages Overview

### 1. **Home** (`/`)
- Hero section with introduction
- Featured projects showcase
- Technical skills overview
- Recent experience highlights
- Call-to-action sections

### 2. **Portfolio** (`/portfolio/`)
- All projects in a grid layout
- Filter-friendly technology tags
- Links to live demos and GitHub repos
- Complete technical stack display

### 3. **About** (`/about/`)
- Personal introduction
- Complete work experience timeline
- Educational background
- Certifications display
- Comprehensive skills breakdown

### 4. **Project Detail** (`/project/<id>/`)
- Full project information
- Detailed description
- Technologies used with badges
- Related projects sidebar
- Links to live site and GitHub

### 5. **Contact** (`/contact/`)
- Professional contact form
- Direct contact information
- Social media links
- Quick response information

## 🛠️ Admin Panel

Access the admin panel at: `http://localhost:8000/admin`

### Manage:
- **Skills**: Add/edit skills with categories and proficiency levels
- **Projects**: Add projects with images, descriptions, and links
- **Experience**: Manage work experience entries
- **Education**: Track educational background
- **Certifications**: Add certifications and achievements
- **Messages**: View and manage contact form submissions

## 🎨 Customization

### 1. **Update Your Information**

Edit through the admin panel or modify `populate_portfolio.py`:

```bash
python manage.py populate_portfolio  # Re-runs with updated data
```

### 2. **Customize Colors**

Edit CSS variables in `portfolio/static/portfolio/css/style.css`:

```css
:root {
    --primary-color: #6366f1;           /* Primary brand color */
    --secondary-color: #ec4899;         /* Accent color */
    --dark-bg: #0f172a;                 /* Dark backgrounds */
    /* ... other colors ... */
}
```

### 3. **Add Project Images**

1. Go to Admin Panel
2. Click "Projects"
3. Click on a project
4. Upload an image in the "Image" field
5. Save

### 4. **Update Social Links**

Edit in `portfolio/templates/portfolio/base.html` and `contact.html`:

```html
<a href="https://your-linkedin-url" target="_blank">
    <i class="fab fa-linkedin"></i>
</a>
```

## 📱 Responsive Design

The portfolio is fully responsive with breakpoints for:
- **Desktop** (1200px+)
- **Tablet** (768px - 1199px)
- **Mobile** (320px - 767px)

All images scale automatically, and layouts adapt for smaller screens.

## 🚀 Deployment

### **Deploy to Heroku**

1. **Create Procfile**:
```
web: gunicorn myportfolio.wsgi
```

2. **Create runtime.txt**:
```
python-3.11.7
```

3. **Install dependencies**:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

4. **Deploy**:
```bash
heroku create your-app-name
heroku config:set DEBUG=False
git push heroku main
```

### **Deploy to PythonAnywhere**

1. Upload project files
2. Configure virtual environment
3. Set up WSGI configuration
4. Configure static files
5. Reload web app

## 📊 Performance Tips

1. **Enable Compression**: Install `django-compressor`
2. **Database**: Use PostgreSQL for production instead of SQLite
3. **Static Files**: Collect and serve from CDN
4. **Caching**: Implement Redis caching
5. **Images**: Optimize images before uploading

## 🔒 Security Checklist

- [ ] Set `DEBUG = False` in production
- [ ] Update `SECRET_KEY` in settings
- [ ] Set secure `ALLOWED_HOSTS`
- [ ] Use HTTPS
- [ ] Set `CSRF_COOKIE_SECURE = True`
- [ ] Set `SESSION_COOKIE_SECURE = True`
- [ ] Configure CORS properly
- [ ] Use environment variables for secrets

## 🐛 Troubleshooting

### **Static files not loading**
```bash
python manage.py collectstatic --noinput
```

### **Images not displaying**
- Ensure media folder exists: `mkdir media`
- Check `MEDIA_ROOT` in settings

### **Contact form not working**
- Verify email settings in `settings.py`
- Check form validation in admin

### **Page not found (404)**
- Clear browser cache
- Check URLs in `urls.py`
- Verify template names

## 📚 Technologies Used

- **Backend**: Django 6.0+
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (dev), PostgreSQL (production)
- **Styling**: CSS Grid, Flexbox, Gradients, Animations
- **Icons**: Font Awesome
- **Forms**: Django Forms

## 📝 License

This portfolio template is free to use and modify for personal use.

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Django documentation: https://docs.djangoproject.com/
3. Contact support through the contact form

## 🎓 Learning Resources

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap 5: https://getbootstrap.com/docs/5.0/
- Font Awesome Icons: https://fontawesome.com/
- CSS Animations: https://developer.mozilla.org/en-US/docs/Web/CSS/animation

---

**Made with ❤️ to help you impress product-based companies!**

Start building your professional presence today! 🚀
"# sandeep_portfolio" 
