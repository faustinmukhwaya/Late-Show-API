from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.appearance import Appearance, db
from models.guest import Guest
from models.episode import Episode

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    if not (rating and guest_id and episode_id):
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
        return jsonify({'message': 'Appearance created', 'id': appearance.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
