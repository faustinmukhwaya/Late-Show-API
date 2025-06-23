from app import create_app
from models import db, User, Guest, Episode, Appearance
from datetime import date

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed users
    user = User(username='admin')
    user.set_password('password')
    db.session.add(user)

    # Seed guests
    guest1 = Guest(name='John Doe', occupation='Actor')
    guest2 = Guest(name='Jane Smith', occupation='Musician')
    db.session.add_all([guest1, guest2])

    # Seed episodes
    episode1 = Episode(date=date(2025, 6, 1), number=1)
    episode2 = Episode(date=date(2025, 6, 2), number=2)
    db.session.add_all([episode1, episode2])

    db.session.commit()

    # Seed appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2])
    db.session.commit()

print('Database seeded!')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

    @app.route("/")
    def index():
        return "Late Show API is running!"

    return app
