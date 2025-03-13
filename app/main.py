from flask import Blueprint, render_template,request ,redirect
from .crud import get_all_blogs, create_blog, delete_blog, update_blog
from flask_login import login_required, current_user
from .forms import blogForm
from .account_service import user_get

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():  
    return "Your Profile"

@main.route('/blog')
@login_required
def blog():  
    return render_template('blog.html', blogs=get_all_blogs())


@main.route('/create_blog', methods=['GET', 'POST'])
# @login_required
def create_blog_page():  
    if request.method == 'POST':
        data = request.form
        if data['title'] == '' or data['content'] == '':
            return render_template('create_blog.html', form=blogForm(), errors="Title or Content is empty")
        user_data = user_get(current_user.username)
        result = create_blog(user_data.username, data['title'], data['content'], data['tag'])
        if result == "success":
            return redirect('/blog')
        return render_template('create_blog.html', form=blogForm(), errors="something went wrong")
        
    return render_template('create_blog.html', form=blogForm())


@main.route('/delete_blog/<blog_id>', methods=['POST'])
@login_required
def delete_blog_item(blog_id):  
    result = delete_blog(blog_id)
    if result == "success":
        return redirect('/blog')
    return render_template('blog.html', blogs=get_all_blogs())

@main.route('/edit_blog/<blog_id>', methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    if request.method == 'POST':
        data = request.form
        if data['title'] == '' or data['content'] == '':
            return render_template('edit_blog.html', form=blogForm(), errors="Title or Content is empty")
        user_data = user_get(current_user.username)
        result = update_blog(blog_id, user_data.username, data['title'], data['content'], data['tag'])
        if result == "success":
            return redirect('/blog')
        return render_template('edit_blog.html', form=blogForm(), errors="something went wrong")
        
    return render_template('edit_blog.html', form=blogForm())
    




# @main.route('/add_blog', methods=['GET', 'POST'])
# def add_blog():  
#     if request.method == 'POST':
#         data = request.get_json()
#         result = create_blog(data['username'], data['title'], data['content'], data['tag'])
#         return result
