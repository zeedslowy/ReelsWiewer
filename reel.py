import instaloader
from flask import Flask, render_template_string, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Instaloader nesnesi
L = instaloader.Instaloader()

# HTML ŞABLONLARI
login_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Giriş</title>
    <style>
        body {
            background: url('https://www.instagram.com/static/images/homepage/home-phones.png/43cc71bb1b43.png') no-repeat center center fixed;
            background-size: cover;
            font-family: Arial, sans-serif;
        }
        .form-container {
            margin: 100px auto;
            width: 300px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            text-align: center;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            background: #3897f0;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #287dc0;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Instagram Giriş</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Kullanıcı Adı" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li style="color: {{ 'green' if category == 'success' else 'red' }};">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
"""

reels_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reels İşlemi</title>
    <style>
        body {
            background: url('https://www.instagram.com/static/images/homepage/screenshots/screenshot2.png/6f03eb85463c.png') no-repeat center center fixed;
            background-size: cover;
            font-family: Arial, sans-serif;
        }
        .form-container {
            margin: 100px auto;
            width: 300px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            text-align: center;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            background: #3897f0;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #287dc0;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Reels Linki Girin</h2>
        <form method="POST">
            <input type="text" name="reels_link" placeholder="Reels Linki" required>
            <button type="submit">İzlenme Gönder</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li style="color: {{ 'green' if category == 'success' else 'red' }};">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            # Instagram oturumu aç
            L.login(username, password)
            flash("Giriş başarılı!", "success")
            return redirect(url_for('reels'))
        except Exception as e:
            flash(f"Giriş başarısız: {str(e)}", "danger")
            return redirect(url_for('login'))

    return render_template_string(login_template)


@app.route('/reels', methods=['GET', 'POST'])
def reels():
    if request.method == 'POST':
        reels_link = request.form.get('reels_link')
        try:
            # Sadece izlenme gönderme işlemi simüle ediliyor
            # (Instagram'ın izlenme API'si olmadığı için bu işlem yapılamaz.)
            flash(f"İzlenme gönderme işlemi başarıyla simüle edildi: {reels_link}", "success")
        except Exception as e:
            flash(f"Hata oluştu: {str(e)}", "danger")
    return render_template_string(reels_template)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")