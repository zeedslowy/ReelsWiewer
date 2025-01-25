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
            background: linear-gradient(135deg, #feda75, #fa7e1e, #d62976, #962fbf, #4f5bd5);
            font-family: Arial, sans-serif;
            color: white;
        }
        .form-container {
            margin: 100px auto;
            width: 300px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.8);
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
            background: linear-gradient(135deg, #4f5bd5, #962fbf, #d62976, #fa7e1e, #feda75);
            font-family: Arial, sans-serif;
            color: white;
        }
        .form-container {
            margin: 100px auto;
            width: 300px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.8);
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
        <h2>Reels İşlemi</h2>
        <form method="POST">
            <input type="text" name="reels_link" placeholder="Reels Linki" required>
            <input type="number" name="views" placeholder="Kaç Adet?" min="1" required>
            <button type="submit">İzlenme Gönder</button>
        </form>
        {% if results %}
        <h3>Sonuçlar:</h3>
        <table border="1" style="width: 100%; margin-top: 10px; background: white; color: black;">
            <tr>
                <th>Reels Linki</th>
                <th>Gönderilen Adet</th>
                <th>Durum</th>
            </tr>
            {% for result in results %}
            <tr>
                <td>{{ result.link }}</td>
                <td>{{ result.views }}</td>
                <td>{{ result.status }}</td>
            </tr>
            {% endfor %}
        </table>
        {% endif %}
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

# Reels sonuçları için liste
results = []

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            L.login(username, password)
            flash("Giriş başarılı!", "success")
            return redirect(url_for('reels'))
        except Exception as e:
            flash(f"Giriş başarısız: {str(e)}", "danger")
            return redirect(url_for('login'))

    return render_template_string(login_template)


@app.route('/reels', methods=['GET', 'POST'])
def reels():
    global results
    if request.method == 'POST':
        reels_link = request.form.get('reels_link')
        views = request.form.get('views')
        try:
            # Simüle edilmiş izlenme işlemi
            results.append({"link": reels_link, "views": views, "status": "Başarılı"})
            flash("İzlenme gönderme işlemi başarılı!", "success")
        except Exception as e:
            results.append({"link": reels_link, "views": views, "status": f"Hata: {str(e)}"})
            flash("Bir hata oluştu.", "danger")
    return render_template_string(reels_template, results=results)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
