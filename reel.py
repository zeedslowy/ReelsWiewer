from flask import Flask, render_template, request, redirect, url_for, flash
import instaloader

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Flash mesajlar için gerekli

# Instaloader oturumu
L = instaloader.Instaloader()

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

    return render_template('login.html')


@app.route('/reels', methods=['GET', 'POST'])
def reels():
    if request.method == 'POST':
        link = request.form.get('reels_link')
        try:
            # Reels video indirme
            post = instaloader.Post.from_shortcode(L.context, link.split('/')[-2])
            L.download_post(post, target="downloads")
            flash("Reels başarıyla indirildi!", "success")
        except Exception as e:
            flash(f"Hata oluştu: {str(e)}", "danger")
    return render_template('reels.html')


if __name__ == '__main__':
    app.run(debug=True)
