import re

class URLAnalyzer:
    def __init__(self):
        self.suspicious_tlds = ['.xyz', '.top', '.club', '.gq', '.ml', '.cf', '.tk']
        self.known_good_domains = [
            'google.com', 'facebook.com', 'instagram.com', 'youtube.com',
            'amazon.com', 'microsoft.com', 'github.com', 'linkedin.com',
            'twitter.com', 'x.com', 'whatsapp.com', 'telegram.org',
            'paypal.com', 'netflix.com', 'spotify.com', 'apple.com'
        ]
        
    def scan(self, url):
        score = 0
        findings = []
        
        url_lower = url.lower().strip()
        
        # Check for IP address instead of domain
        ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
        if re.search(ip_pattern, url_lower):
            score += 25
            findings.append("URL uses an IP address instead of a domain name")
        
        # Check for suspicious TLD
        for tld in self.suspicious_tlds:
            if tld in url_lower:
                score += 20
                findings.append(f"Suspicious top-level domain: {tld}")
                break
        
        # Check for HTTPS missing
        if not url_lower.startswith('https://'):
            score += 15
            findings.append("Website does not use HTTPS (secure connection)")
        
        # Check for URL shortening
        shorteners = ['bit.ly', 'tinyurl', 'tiny.cc', 't.co', 'goo.gl', 'ow.ly', 'buff.ly']
        for s in shorteners:
            if s in url_lower:
                score += 20
                findings.append(f"URL shortener detected: {s} - hides the real destination")
                break
        
        # Check for misspelled domains (typosquatting)
        for domain in self.known_good_domains:
            if domain in url_lower:
                continue
        
        # Check for @ symbol (browser ignores everything before @)
        if '@' in url_lower:
            score += 25
            findings.append("'@' symbol found - could redirect to a different site")
        
        # Check for too many subdomains
        if url_lower.count('.') > 3:
            score += 10
            findings.append("Excessive subdomains - may be misleading")
        
        # Check for hyphens in domain
        domain_part = url_lower.split('/')[2] if '//' in url_lower else url_lower.split('/')[0]
        if domain_part.count('-') > 2:
            score += 10
            findings.append("Unusual number of hyphens in domain name")
        
        # Check for numerical domain
        if re.search(r'\d{4,}', domain_part):
            score += 10
            findings.append("Domain contains long number sequence")
        
        score = min(score, 100)
        
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
            'url': url,
            'recommendations': [
                "Do NOT visit this URL if score is Medium or High",
                "Hover over the link to see the real destination",
                "Type the official website address manually instead",
                "Use a URL expander for shortened links",
                "Report suspicious URLs to Google Safe Browsing"
            ]
        }