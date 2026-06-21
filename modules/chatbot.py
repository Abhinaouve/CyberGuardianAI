class SecurityChatbot:
    def __init__(self):
        self.knowledge_base = {
            'phishing': {
                'keywords': ['phishing', 'phish', 'fake email', 'scam email'],
                'response': "Phishing is when someone sends you a fake message (usually email) pretending to be a trusted company. They want you to click a bad link or give them your password. Always check the sender's email address carefully before clicking anything!"
            },
            'malware': {
                'keywords': ['malware', 'virus', 'trojan', 'spyware'],
                'response': "Malware is short for 'malicious software'. It's any program designed to harm your computer or steal your data. Common types include viruses, worms, ransomware, and spyware. Always keep your antivirus software updated!"
            },
            'ransomware': {
                'keywords': ['ransomware', 'ransom'],
                'response': "Ransomware is a type of malware that locks your files and demands payment to unlock them. Never pay the ransom! The best protection is to keep regular backups of your important files and keep your system updated."
            },
            'password': {
                'keywords': ['password', 'passwords', 'strong password', 'create password'],
                'response': "Strong passwords are your first line of defense! Use at least 12 characters with a mix of uppercase, lowercase, numbers, and symbols. Never reuse passwords across different sites. Consider using a password manager like Bitwarden or 1Password."
            },
            'mfa': {
                'keywords': ['mfa', '2fa', 'two factor', 'multi factor', 'authentication'],
                'response': "Multi-Factor Authentication (MFA) adds an extra layer of security. Even if someone gets your password, they can't log in without the second factor (like a code from your phone). Always enable MFA on every account that offers it!"
            },
            'instagram': {
                'keywords': ['instagram', 'ig', 'social media'],
                'response': "To secure your Instagram: 1) Enable Two-Factor Authentication in Settings > Security. 2) Use a strong, unique password. 3) Don't click suspicious links in DMs. 4) Check 'Apps and Websites' to remove unknown access. 5) Make your account private if you're concerned about stalkers."
            },
            'social engineering': {
                'keywords': ['social engineering', 'manipulation', 'tricked'],
                'response': "Social engineering is when someone tricks you into giving away information or access. They might pretend to be tech support, a coworker, or a friend. Always verify who you're talking to before sharing sensitive info!"
            }
        }
        
    def ask(self, question):
        question_lower = question.lower()
        
        for topic, data in self.knowledge_base.items():
            if any(kw in question_lower for kw in data['keywords']):
                return {
                    'question': question,
                    'answer': data['response'],
                    'topic': topic
                }
        
        return {
            'question': question,
            'answer': "That's a great question about cybersecurity! Here is a general tip: Always be cautious online. If something seems too good to be true, it probably is. Keep your software updated, use strong passwords, enable two-factor authentication, and never share personal information with strangers online.",
            'topic': 'general'
        }