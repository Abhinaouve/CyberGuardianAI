from datetime import datetime

class ReportGenerator:
    def generate(self, analysis):
        report = {
            'id': analysis.id,
            'type': analysis.type,
            'input': analysis.input_data,
            'score': analysis.score,
            'severity': analysis.severity,
            'timestamp': analysis.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'threat_level': self._get_threat_level(analysis.score),
            'summary': self._get_summary(analysis.score, analysis.severity),
            'actions': self._get_actions(analysis.score)
        }
        return report
    
    def _get_threat_level(self, score):
        if score >= 70:
            return "Critical"
        elif score >= 40:
            return "Warning"
        else:
            return "Safe"
    
    def _get_summary(self, score, severity):
        if score >= 70:
            return "This is highly suspicious and likely malicious. Immediate action is required."
        elif score >= 40:
            return "This shows some suspicious indicators. Proceed with caution."
        else:
            return "This appears to be safe based on our analysis."
    
    def _get_actions(self, score):
        if score >= 70:
            return ["Do not interact with this content", "Report to your security team", "Run a full system scan"]
        elif score >= 40:
            return ["Verify the source before proceeding", "Monitor for unusual activity", "Enable additional security measures"]
        else:
            return ["No action needed", "Stay vigilant", "Continue safe browsing practices"]