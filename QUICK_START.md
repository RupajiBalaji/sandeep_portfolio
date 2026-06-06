# 🚀 QUICK START GUIDE

## Option 1: Automated Setup (Windows)

1. **Double-click** `setup.bat`
2. Follow the prompts
3. When asked, create your admin account
4. Open `http://localhost:8000` in your browser

## Option 2: Manual Setup

### Step 1: Install Dependencies
```bash
cd myportfolio
pip install -r ../requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py migrate
```

### Step 3: Create Admin Account
```bash
python manage.py createsuperuser
```
Enter your desired username, email, and password

### Step 4: Populate Portfolio
```bash
python manage.py populate_portfolio
```

### Step 5: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 6: Start Server
```bash
python manage.py runserver
```

## ✅ What to Do Next

### 1. Visit Your Portfolio
- **Home Page**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin (use your admin credentials)

### 2. Customize Content
- Go to http://localhost:8000/admin
- Click on each section (Skills, Projects, Experience, etc.)
- Edit, add, or delete entries as needed
- Add project images
- Update social media links

### 3. Upload Project Images
- In Admin Panel, go to "Projects"
- Click on a project
- Upload an image
- Save

### 4. Customize Website Colors
- Open: `portfolio/static/portfolio/css/style.css`
- Find the `:root` section at the top
- Change color values:
  ```css
  --primary-color: #6366f1;      /* Change main color */
  --secondary-color: #ec4899;    /* Change accent */
  ```

### 5. Update Social Links
- Open: `portfolio/templates/portfolio/base.html`
- Find the LinkedIn, GitHub, and Email sections
- Update URLs to your profiles

## 📱 Testing Responsive Design

1. Open your portfolio in browser
2. Press `F12` to open Developer Tools
3. Click the device toggle (phone icon) to see mobile view
4. Test on different screen sizes

## 🔐 Before Deploying

1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to something random
3. Update `ALLOWED_HOSTS`
4. Set up proper database (PostgreSQL)
5. Configure email settings
6. Use environment variables for secrets

## 🆘 Common Issues & Fixes

### **Port 8000 already in use**
```bash
python manage.py runserver 8080
# Then visit: http://localhost:8080
```

### **Static files not loading**
```bash
python manage.py collectstatic --noinput
```

### **Images not showing**
1. Make sure `media/` folder exists
2. Check image path in browser (F12 > Network tab)

### **Admin panel styling looks broken**
```bash
python manage.py collectstatic --noinput
# Then restart server
```

## 🎨 Site Sections

- **Home** `/` - First impression, featured work
- **Portfolio** `/portfolio/` - All projects
- **About** `/about/` - Your story, experience, skills
- **Contact** `/contact/` - Get in touch form

## 📊 Data Your Portfolio Includes

✅ **Skills** (22 skills organized by category)
✅ **Projects** (3 featured projects)
✅ **Experience** (3 job positions)
✅ **Education** (Bachelor's Degree info)
✅ **Certifications** (2 certifications)

## 💡 Pro Tips

1. **Add more projects** - More projects = more impressive
2. **Keep skills updated** - Add new technologies as you learn them
3. **Write detailed descriptions** - Help companies understand your work
4. **Add project images** - Visual appeal matters
5. **Keep experience current** - Update current roles to "Current"
6. **Get feedback** - Ask mentors to review your portfolio

## 🚀 Next: Deployment

Once you're happy with your portfolio:

1. **Simple**: Deploy to Heroku (free tier available)
2. **Professional**: Deploy to AWS, DigitalOcean, or Linode
3. **Easiest**: PythonAnywhere (Python hosting)

See `README.md` for deployment instructions.

---

**You're all set! Start impressing companies with your portfolio!** 🎉
