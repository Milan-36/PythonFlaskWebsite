"""Routes for user authentication."""
from flask import Blueprint, render_template, request
from .forms import SignupForm


# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/actors/login', methods=['GET', 'POST'])
def login():
    # Login route logic goes here


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        # User sign-up logic will go here.
        ...
    return render_template(
        '/signup.html',
        title='Create a new Account',
        form=SignupForm(),
        template='signup-page',
        body="Enter Email, and a new password to create an account"
    )
