class PhishingDetector:
    def __init__(self):
        self.urgent_words = ['urgent', 'immediately', 'alert', 'suspended', 'locked', 'verify']
        self.suspicious_phrases = [
            'dear customer', 'dear user', 'click here', 'confirm your account',
            'reset your password', 'bank details', 'credit card', 'social security',
            'tax refund', 'won a prize', 'gift card', 'act now', 'limited time'
        ]
        
    def analyze(self, subject, content):
        score = 0
        findings = []
        
        text = (subject + " " + content).lower()
        
        # Check for urgent words
        urgent_found = [w for w in self.urgent_words if w in subject.lower()]
        if urgent_found:
            score += 20
            findings.append(f"Urgency detected in subject: {', '.join(urgent_found)}")
        
        # Check for suspicious phrases
        phrases_found = [p for p in self.suspicious_phrases if p in text]
        if phrases_found:
            score += len(phrases_found) * 10
            findings.append(f"Suspicious phrases: {', '.join(phrases_found[:4])}")
        
        # Check for excessive punctuation (!!!)
        if '!!!' in subject or '???' in subject:
            score += 10
            findings.append("Excessive punctuation detected - common in phishing")
        
        # Check for promises of money
        money_words = ['money', 'cash', 'bitcoin', 'paypal', 'transfer', '$', 'million']
        if any(w in text for w in money_words):
            score += 15
            findings.append("Financial promises or requests detected")
        
        # Check for generic greetings
        if 'dear' in subject.lower() and ('customer' in subject.lower() or 'user' in subject.lower()):
            score += 10
            findings.append("Generic greeting - doesn't address you by name")
        
        # Cap score at 100
        score = min(score, 100)
        
        # Determine severity
        if score >= 70:
            severity = "High"
        elif score >= 40:
            severity = "Medium"
        else:
            severity = "Low"
        
        return {
            'score': score,
            'severity': severity,
            'findings': findings,
            'safe': score < 30,
            'recommendations': [
                "Do NOT click any links in this email",
                "Do NOT download any attachments",
                "Verify the sender's email address carefully",
                "Contact the company directly using official contact info",
                "Report this as phishing to your email provider"
            ]
        }