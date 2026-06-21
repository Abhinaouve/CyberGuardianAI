import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from modules.phishing_detector import PhishingDetector
from modules.url_analyzer import URLAnalyzer
from modules.chatbot import SecurityChatbot
from modules.quiz import QuizManager
from modules.report_generator import ReportGenerator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cyber-guardian-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/cyberguardian.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ========== DATABASE MODELS ==========
class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    input_data = db.Column(db.Text)
    score = db.Column(db.Integer)
    severity = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    total = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

# ========== ROUTES ==========
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    total_analyses = Analysis.query.count()
    avg_score = db.session.query(db.func.avg(Analysis.score)).scalar() or 0
    recent = Analysis.query.order_by(Analysis.timestamp.desc()).limit(5).all()
    quiz_results = QuizResult.query.order_by(QuizResult.timestamp.desc()).limit(5).all()
    return render_template('dashboard.html', total=total_analyses, avg=round(avg_score, 1), recent=recent, quiz_results=quiz_results)

@app.route('/phishing', methods=['GET', 'POST'])
def phishing():
    result = None
    if request.method == 'POST':
        subject = request.form.get('subject', '')
        content = request.form.get('content', '')
        detector = PhishingDetector()
        result = detector.analyze(subject, content)
        
        entry = Analysis(type='Email', input_data=subject[:100], score=result['score'], severity=result['severity'])
        db.session.add(entry)
        db.session.commit()
    
    return render_template('phishing.html', result=result)

@app.route('/url-analyzer', methods=['GET', 'POST'])
def url_analyzer():
    result = None
    if request.method == 'POST':
        url = request.form.get('url', '')
        analyzer = URLAnalyzer()
        result = analyzer.scan(url)
        
        entry = Analysis(type='URL', input_data=url[:100], score=result['score'], severity=result['severity'])
        db.session.add(entry)
        db.session.commit()
    
    return render_template('url_analyzer.html', result=result)

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    response = None
    if request.method == 'POST':
        question = request.form.get('question', '')
        bot = SecurityChatbot()
        response = bot.ask(question)
    
    return render_template('chatbot.html', response=response)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    manager = QuizManager()
    result = None
    
    if request.method == 'POST':
        answers = request.form
        result = manager.check_answers(answers)
        
        if result:
            qr = QuizResult(score=result['score'], total=result['total'])
            db.session.add(qr)
            db.session.commit()
    
    questions = manager.get_questions()
    return render_template('quiz.html', questions=questions, result=result)

@app.route('/report/<int:analysis_id>')
def report(analysis_id):
    analysis = Analysis.query.get_or_404(analysis_id)
    generator = ReportGenerator()
    report_data = generator.generate(analysis)
    return render_template('report.html', report=report_data)

# ========== API ROUTES FOR AJAX (Bonus: Makes it work without page reload) ==========
@app.route('/api/chatbot', methods=['POST'])
def api_chatbot():
    data = request.get_json()
    question = data.get('question', '')
    bot = SecurityChatbot()
    response = bot.ask(question)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)