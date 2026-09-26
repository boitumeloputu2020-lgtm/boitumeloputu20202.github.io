import os

from flask import Flask, Response, render_template

app = Flask(__name__)

PORTFOLIO = {
    "name": "Charmaine Boitumelo Putu",
    "role": "Aspiring AI Engineer & Data Analyst",
    "email": "boitumelo.putu2020@gmail.com",
    "github": "https://github.com/boitumeloputu2020-lgtm/boitumeloputu2020.github.io",
    "linkedin": "https://www.linkedin.com/in/boitumelo-putu-525415391?utm_source=share_via&utm_content=profile&utm_medium=member_android",
    "about": "I am a dedicated and passionate individual who loves everything she does. I am very passionate about technology. I would like to be an AI Engineer or a Data Analyst and advance in the career.",
    "skills": {
        "Technical skills": ["Python programming", "Data analytics", "Machine learning fundamentals", "AI fundamentals", "Microsoft AI fundamentals", "Computer literacy"],
        "Soft skills": ["Problem solving", "Teamwork and collaboration", "Attention to detail", "Time management", "Communication", "Adaptability"]
    },
    "education": [
        {"title": "N4 Chemical Engineering", "institution": "Johannesburg Institute of Engineering and Technology", "year": "2021"},
        {"title": "Grade 12", "institution": "Ahmed Timol Secondary School", "year": "2013"},
        {"title": "Current learning", "institution": "CS50's Introduction to Programming with Python and data-focused online learning", "year": "In progress"}
    ],
    "certifications": [
        {"title": "AI Essentials", "issuer": "Google · Coursera", "file": "Charmaine Boitumelo Putu AI Google essentials Certificate Coursera B4GP5JWOZVST.pdf"},
        {"title": "Introduction to AI", "issuer": "Coursera", "file": "Charmaine Boitumelo Putu Introduction to AI Certificate Coursera 71CH2H52D1CR.pdf"},
        {"title": "Discover the Art of Prompting", "issuer": "Coursera", "file": "Charmaine Boitumelo Putu Discover the art of prompting Certificate Coursera Q7LLEWPSFRMH.pdf"},
        {"title": "Use AI Responsibly", "issuer": "Coursera", "file": "Charmaine Boitumelo Putu Use AI responsibly Certificate Coursera MWKKCFKG7FG1.pdf"},
        {"title": "Maximising Productivity with AI Tools", "issuer": "Coursera", "file": "Charmaine Boitumelo Putu Maximising productivity with AI tools Certificate Coursera VKR9SVWOYAGD.pdf"},
        {"title": "Data Analytics", "issuer": "Professional certificate", "file": "Charmaine Putu Data Analytics Certificate"},
        {"title": "Microsoft credentials", "issuer": "Microsoft Learn", "file": "Credentials - boitumeloputu-1549 _ Microsoft Learn.pdf"}
    ],
    "projects": [
        {"title": "Calculator", "description": "A Python command-line calculator practising arithmetic operations, input handling and division-by-zero checks.", "file": "calculator.py"},
        {"title": "String Formatter", "description": "An interactive Python program that formats names, creates usernames and transforms a short bio message.", "file": "string_formatter.py"},
        {"title": "Student Information Tool", "description": "A beginner-friendly Python program that captures student details, transforms values and prints a clear summary.", "file": "student _info.py"}
    ]
}


@app.route('/')
def home():
    return render_template('index.html', portfolio=PORTFOLIO)


@app.route('/robots.txt')
def robots_txt():
    return Response(
        'User-agent: *\nAllow: /\nSitemap: https://charmaineputu.com/sitemap.xml\n',
        mimetype='text/plain',
    )


@app.route('/sitemap.xml')
def sitemap_xml():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url><loc>https://charmaineputu.com/</loc></url>
      <url><loc>https://charmaineputu.com/#about</loc></url>
      <url><loc>https://charmaineputu.com/#skills</loc></url>
      <url><loc>https://charmaineputu.com/#projects</loc></url>
      <url><loc>https://charmaineputu.com/#education</loc></url>
      <url><loc>https://charmaineputu.com/#certifications</loc></url>
      <url><loc>https://charmaineputu.com/#contact</loc></url>
    </urlset>
    '''
    return Response(xml, mimetype='application/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
