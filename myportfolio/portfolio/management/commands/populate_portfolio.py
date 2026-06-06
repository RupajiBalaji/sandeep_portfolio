from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from portfolio.models import Skill, Project, Experience, Education, Certification


class Command(BaseCommand):
    help = 'Populate the portfolio with sample data based on your resume'

    def handle(self, *args, **options):
        self.stdout.write('Starting portfolio population...')
        
        # Clear existing data
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        
        # Add Skills
        skills_data = [
            # Programming Languages
            ('Python', 'Programming Languages', 5),
            ('Java', 'Programming Languages', 4),
            ('SQL', 'Programming Languages', 4),
            
            # AI & Machine Learning
            ('Machine Learning', 'AI & Machine Learning', 5),
            ('Deep Learning', 'AI & Machine Learning', 4),
            ('NLP', 'AI & Machine Learning', 4),
            ('Computer Vision', 'AI & Machine Learning', 4),
            
            # Libraries & Frameworks
            ('TensorFlow', 'Libraries & Frameworks', 4),
            ('PyTorch', 'Libraries & Frameworks', 4),
            ('Scikit-learn', 'Libraries & Frameworks', 5),
            ('Pandas', 'Libraries & Frameworks', 5),
            ('NumPy', 'Libraries & Frameworks', 5),
            
            # Web & Tools
            ('MERN Stack', 'Web & Tools', 4),
            ('Flask', 'Web & Tools', 4),
            ('Git', 'Web & Tools', 5),
            ('GitHub', 'Web & Tools', 5),
            
            # Data Skills
            ('Data Cleaning', 'Data Skills', 5),
            ('Feature Engineering', 'Data Skills', 4),
            ('Model Training', 'Data Skills', 5),
            ('Model Evaluation', 'Data Skills', 4),
            
            # Other Skills
            ('API Integration', 'Other Skills', 4),
            ('Automation Scripts', 'Other Skills', 4),
            ('Data Visualization', 'Other Skills', 4),
        ]
        
        for i, (name, category, proficiency) in enumerate(skills_data):
            Skill.objects.create(
                name=name,
                category=category,
                proficiency=proficiency,
                order=i
            )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(skills_data)} skills'))
        
        # Add Projects
        projects_data = [
            {
                'title': 'Path2Learn - AI-Based Smart Study Platform',
                'description': 'An AI-powered education platform to help students focus and improve learning efficiency.',
                'detailed_description': 'Developed an AI-powered education platform featuring study reminders, performance tracking, and smart learning suggestions. Built with full-stack technologies including HTML, CSS, JavaScript frontend and Python backend integration.',
                'technologies': 'Python, HTML, CSS, JavaScript, AI/ML, Database Design',
                'featured': True,
                'order': 0,
            },
            {
                'title': 'Current Crunches - AI News Aggregator',
                'description': 'Real-time news aggregation platform with AI-based text summarization.',
                'detailed_description': 'Developed a comprehensive news aggregation platform that fetches and displays latest news from multiple sources. Integrated external News APIs and implemented AI-based text summarization using NLP/LLM APIs. Features include search, category filtering, and optimized UI for better readability.',
                'technologies': 'React, Node.js, Express, News API, NLP, LLM APIs, MongoDB',
                'featured': True,
                'order': 1,
            },
            {
                'title': 'AI-Powered Chatbot',
                'description': 'Intelligent chatbot system for customer support.',
                'detailed_description': 'Built an intelligent chatbot system using NLP and machine learning to provide automated customer support. Integrated with various communication channels and implemented natural language understanding for better user interaction.',
                'technologies': 'Python, NLP, TensorFlow, API Integration, Cloud Deployment',
                'featured': False,
                'order': 2,
            },
        ]
        
        for proj in projects_data:
            Project.objects.create(**proj)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(projects_data)} projects'))
        
        # Add Experience
        experiences_data = [
            {
                'position': 'Tech Lead',
                'company': 'Viswam AI',
                'employment_type': 'Freelance',
                'description': 'Led a student development team and provided technical guidance on MERN Stack development. Trained team members on setting up development environments and integrating API keys and backend services. Guided developers in building scalable web applications.',
                'start_date': date(2023, 6, 1),
                'end_date': None,
                'is_current': True,
                'order': 0,
            },
            {
                'position': 'Software Development Intern',
                'company': 'Urvha Dynamic Private Limited',
                'employment_type': 'Internship',
                'description': 'Developing a company-focused software product based on organizational requirements. Contributing to backend development and feature implementation using modern development tools. Assisting in testing, debugging, and optimizing system performance.',
                'start_date': date(2024, 1, 1),
                'end_date': None,
                'is_current': True,
                'order': 1,
            },
            {
                'position': 'AI & Cloud Intern',
                'company': 'Edunet Foundation',
                'employment_type': 'Internship',
                'description': 'Completed hands-on internship focused on Artificial Intelligence and Machine Learning applications. Built and tested machine learning models using Python, NumPy, Pandas, and Scikit-learn. Worked on real-world datasets involving data preprocessing, visualization, and model training.',
                'start_date': date(2023, 1, 1),
                'end_date': date(2023, 5, 31),
                'is_current': False,
                'order': 2,
            },
        ]
        
        for exp in experiences_data:
            Experience.objects.create(**exp)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(experiences_data)} experience entries'))
        
        # Add Education
        education_data = [
            {
                'degree': 'Bachelor of Technology',
                'institution': 'Geethanjali College of Engineering and Technology',
                'field_of_study': 'Computer Science (AI & ML Specialization)',
                'description': 'Pursuing B.Tech in Computer Science with specialization in Artificial Intelligence and Machine Learning.',
                'start_date': date(2023, 7, 1),
                'end_date': date(2027, 5, 31),
                'order': 0,
            },
        ]
        
        for edu in education_data:
            Education.objects.create(**edu)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(education_data)} education entries'))
        
        # Add Certifications
        certifications_data = [
            {
                'title': 'Data Science and Gen AI',
                'issuer': 'Aimerz.ai',
                'description': 'Advanced Data Science and Generative AI & Agentic AI certification program.',
                'date': date(2024, 3, 1),
                'order': 0,
            },
            {
                'title': 'Introduction to Quantum Computing',
                'issuer': 'Microsoft',
                'description': 'Quantum principles and applications fundamentals.',
                'date': date(2024, 2, 1),
                'order': 1,
            },
        ]
        
        for cert in certifications_data:
            Certification.objects.create(**cert)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(certifications_data)} certifications'))
        
        self.stdout.write(self.style.SUCCESS('\n✨ Portfolio populated successfully!'))
        self.stdout.write('\nNext steps:')
        self.stdout.write('1. Run: python manage.py migrate')
        self.stdout.write('2. Run: python manage.py createsuperuser')
        self.stdout.write('3. Run: python manage.py runserver')
        self.stdout.write('4. Visit: http://localhost:8000/admin to manage content')
