import os
import logging
from flask import Flask, render_template, session, request, redirect, url_for

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Language content
CONTENT = {
    'en': {
        'nav_home': 'Home',
        'nav_projects': 'Projects',
        'nav_education': 'Education',
        'nav_skills': 'Skills',
        'intro_text': 'My name is Munish and I am a passionate programmer. It brings me great joy and fulfillment to create new experiences through my work.',
        'projects_title': 'Projects',
        'projects_subtitle': 'Explore my work and contributions',
        'projects_coming_soon': 'Projects Coming Soon',
        'projects_description': "I'm working on showcasing my projects here. Check back soon!",
        'education_title': 'Education',
        'education_subtitle': 'My academic journey and learning path',
        'education_coming_soon': 'Education Details Coming Soon',
        'education_description': "I'm updating my educational background information. Stay tuned!",
        'skills_title': 'Skills',
        'skills_subtitle': 'Technologies and tools I work with',
        'skills_coming_soon': 'Skills Overview Coming Soon',
        'skills_description': "I'm preparing a comprehensive overview of my technical skills. Check back soon!",
        'footer_text': 'All rights reserved.',
        'dark_mode': 'Dark Mode',
        'light_mode': 'Light Mode',
        'my_projects': 'My Projects',
        'game_development': 'Game Development',
        'web_development': 'Web Development',
        'data_science': 'Data Science',
        'view_project': 'View Project',
        'view_on_github': 'View on GitHub',
        'view_live_site': 'View Live Site',
        'unity_games_desc': 'Collection of interactive games developed using Unity Engine. Experience different genres and gameplay mechanics.',
        'vibereader_desc': 'Immersive Reader - Developed with Gemini API and JavaScript to enable interactive partial translations in texts and automatically add clicked words to a vocabulary trainer, resulting in a 30% improvement in learning rate for new vocabulary.',
        'data_viz_desc': 'Comprehensive data visualization project showcasing various techniques for presenting complex datasets.',
        'strategic_mgmt_desc': 'Data-driven approach to strategic management with analytical insights and decision-making tools.',
        'education_gisma_title': 'GISMA University of Applied Sciences',
        'education_gisma_desc': '2 Semesters of BSc. in Data Science, AI and Digital Business',
        'education_gisma_details': 'Focus: Data Analysis. Course topics: Discrete Mathematics, Programming in Python, Object-Oriented Programming, Statistics',
        'education_gisma_period': 'Jan 2024 – June 2025',
        'education_school_title': 'The Doon Public Senior Secondary School',
        'education_school_desc': 'General Higher Education Entrance Qualification (Abitur)',
        'education_school_details': 'Focus: Mathematics (92%), Economics, English (99%)',
        'education_school_period': 'April 2020 – June 2021',
        'certificates_title': 'Certificates',
        'telc_title': 'Telc B2 German',
        'telc_desc': 'Successfully completed according to the Common European Framework of Reference (CEFR)',
        'telc_period': 'May 15, 2025',
        'testas_title': 'TestAS Certificate',
        'testas_desc': 'Achieved 81st percentile (standard score 108) in Core Test and 99th percentile (standard score 126) in Economics Module',
        'testas_period': 'April 22, 2023',
        'cs50_title': 'CS50x - Harvard University',
        'cs50_desc': 'Completed online course to acquire fundamental knowledge in computer science, algorithms, data structures and web development. Gained practical experience in C, Python, SQL, HTML/CSS and JavaScript',
        'cs50_period': '2025'
    },
    'de': {
        'nav_home': 'Startseite',
        'nav_projects': 'Projekte',
        'nav_education': 'Bildung',
        'nav_skills': 'Fähigkeiten',
        'intro_text': 'Mein Name ist Munish und ich bin ein leidenschaftlicher Programmierer. Es bereitet mir große Freude und Erfüllung, durch meine Arbeit neue Erlebnisse zu erschaffen.',
        'projects_title': 'Projekte',
        'projects_subtitle': 'Entdecken Sie meine Arbeit und Beiträge',
        'projects_coming_soon': 'Projekte kommen bald',
        'projects_description': 'Ich arbeite daran, meine Projekte hier zu präsentieren. Schauen Sie bald wieder vorbei!',
        'education_title': 'Bildung',
        'education_subtitle': 'Mein akademischer Werdegang und Lernpfad',
        'education_coming_soon': 'Bildungsdetails kommen bald',
        'education_description': 'Ich aktualisiere gerade meine Bildungshintergrundinformationen. Bleiben Sie dran!',
        'skills_title': 'Fähigkeiten',
        'skills_subtitle': 'Technologien und Tools, mit denen ich arbeite',
        'skills_coming_soon': 'Fähigkeitsübersicht kommt bald',
        'skills_description': 'Ich bereite eine umfassende Übersicht meiner technischen Fähigkeiten vor. Schauen Sie bald wieder vorbei!',
        'footer_text': 'Alle Rechte vorbehalten.',
        'dark_mode': 'Dunkler Modus',
        'light_mode': 'Heller Modus',
        'my_projects': 'Meine Projekte',
        'game_development': 'Spielentwicklung',
        'web_development': 'Webentwicklung',
        'data_science': 'Datenwissenschaft',
        'view_project': 'Projekt ansehen',
        'view_on_github': 'Auf GitHub ansehen',
        'view_live_site': 'Live-Website ansehen',
        'unity_games_desc': 'Sammlung interaktiver Spiele, entwickelt mit Unity Engine. Erleben Sie verschiedene Genres und Gameplay-Mechaniken.',
        'vibereader_desc': 'Immersive Reader - Entwickelt mit Gemini API und JavaScript, um interaktive Teilübersetzungen in Texten zu ermöglichen und angeklickte Wörter automatisch in einen Vokabeltrainer zu übernehmen, was zu einer verbesserten Lernrate von 30% bei neuen Vokabeln führte.',
        'data_viz_desc': 'Umfassendes Datenvisualisierungsprojekt, das verschiedene Techniken zur Präsentation komplexer Datensätze zeigt.',
        'strategic_mgmt_desc': 'Datengetriebener Ansatz für strategisches Management mit analytischen Einblicken und Entscheidungstools.',
        'education_gisma_title': 'GISMA University of Applied Sciences',
        'education_gisma_desc': '2 Semester BSc. in Datenwissenschaft, K.I. und Digitales Geschäft',
        'education_gisma_details': 'Schwerpunkte: Datenanalyse. Kursthemen: Diskrete Mathematik, Programmieren in Python, Objektorientierte Programmierung, Statistik',
        'education_gisma_period': 'Jan 2024 – Juni 2025',
        'education_school_title': 'The Doon Public Senior Secondary School',
        'education_school_desc': 'Allgemeine Hochschulreife',
        'education_school_details': 'Schwerpunkte: Mathematik (92%), Wirtschaft, Englisch (99%)',
        'education_school_period': 'April 2020 – Juni 2021',
        'certificates_title': 'Zertifikate',
        'telc_title': 'Telc B2 Deutsch',
        'telc_desc': 'Erfolgreich abgeschlossen nach dem Gemeinsamen Europäischen Referenzrahmen (GER)',
        'telc_period': '15. Mai 2025',
        'testas_title': 'TestAS Zertifikat',
        'testas_desc': 'Erreichte 81. Perzentil (Standardwert 108) im Core Test und 99. Perzentil (Standardwert 126) im Fachmodul Wirtschaft',
        'testas_period': '22. April 2023',
        'cs50_title': 'CS50x - Harvard University',
        'cs50_desc': 'Onlinekurs abgeschlossen, um fundierte Kenntnisse in Informatik, Algorithmen, Datenstrukturen und Webentwicklung zu erwerben. Praktische Erfahrung in C, Python, SQL, HTML/CSS und JavaScript gesammelt',
        'cs50_period': '2025'
    }
}

def get_current_language():
    """Get current language from session or default to English"""
    return session.get('language', 'en')

def get_content():
    """Get content for current language"""
    lang = get_current_language()
    return CONTENT.get(lang, CONTENT['en'])

@app.context_processor
def inject_content():
    """Make content available in all templates"""
    return {
        'content': get_content(),
        'current_lang': get_current_language(),
        'other_lang': 'de' if get_current_language() == 'en' else 'en'
    }

@app.route('/set_language/<language>')
def set_language(language):
    """Set language preference"""
    if language in ['en', 'de']:
        session['language'] = language
    return redirect(request.referrer or url_for('home'))

@app.route('/')
def home():
    """Home page route"""
    return render_template('home.html')

@app.route('/projects')
def projects():
    """Projects page route"""
    return render_template('projects.html')

@app.route('/education')
def education():
    """Education page route"""
    return render_template('education.html')

# Skills route removed as requested

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
