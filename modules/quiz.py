class QuizManager:
    def __init__(self):
        self.questions = [
            {
                'id': 1,
                'question': 'What is the best way to identify a phishing email?',
                'options': [
                    'a) It has a pretty design',
                    'b) It asks for your personal information',
                    'c) It comes from a friend',
                    'd) The subject line is short'
                ],
                'correct': 1,
                'explanation': 'Phishing emails often ask for personal information like passwords or credit card numbers. Legitimate companies never ask for this via email.'
            },
            {
                'id': 2,
                'question': 'What does HTTPS stand for in a website URL?',
                'options': [
                    'a) Hyper Text Transfer Protocol Secure',
                    'b) High Tech Transfer Standard',
                    'c) Hyper Text Transfer Standard',
                    'd) High Transfer Protocol Secure'
                ],
                'correct': 0,
                'explanation': 'HTTPS means the connection between your browser and the website is encrypted and secure. Always look for the padlock icon!'
            },
            {
                'id': 3,
                'question': 'Which of these is a strong password?',
                'options': [
                    'a) password123',
                    'b) Il0v3Cyb3r$ecur!ty!',
                    'c) qwerty',
                    'd) 123456789'
                ],
                'correct': 1,
                'explanation': 'Strong passwords have uppercase, lowercase, numbers, symbols, and are at least 12 characters long. Never use common words or sequences!'
            },
            {
                'id': 4,
                'question': 'What should you do if you click on a phishing link by accident?',
                'options': [
                    'a) Ignore it and continue browsing',
                    'b) Change your passwords immediately',
                    'c) Turn off your computer',
                    'd) Send an email to the hacker'
                ],
                'correct': 1,
                'explanation': 'If you click a suspicious link, immediately change your passwords, enable MFA, run a virus scan, and monitor your accounts for unusual activity.'
            },
            {
                'id': 5,
                'question': 'What is Multi-Factor Authentication (MFA)?',
                'options': [
                    'a) Using multiple email accounts',
                    'b) Using two or more verification methods to log in',
                    'c) Having many passwords',
                    'd) Using multiple browsers'
                ],
                'correct': 1,
                'explanation': 'MFA requires two or more proofs to log in: something you know (password), something you have (phone), or something you are (fingerprint).'
            }
        ]
    
    def get_questions(self):
        return self.questions
    
    def check_answers(self, form_data):
        score = 0
        total = len(self.questions)
        results = []
        
        for q in self.questions:
            q_id = str(q['id'])
            user_answer = form_data.get(f'q{q_id}', 'no-answer')
            is_correct = (user_answer == str(q['correct']))
            
            if is_correct:
                score += 1
            
            results.append({
                'id': q['id'],
                'question': q['question'],
                'user_answer': q['options'][int(user_answer)] if user_answer != 'no-answer' else 'No answer',
                'correct_answer': q['options'][q['correct']],
                'is_correct': is_correct,
                'explanation': q['explanation']
            })
        
        percentage = round((score / total) * 100)
        
        return {
            'score': score,
            'total': total,
            'percentage': percentage,
            'results': results
        }