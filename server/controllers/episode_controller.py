from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.episode import Episode, db
from models.appearance import Appearance

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': e.date.isoformat(), 'number': e.number} for e in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [
        {
            'id': a.id,
            'rating': a.rating,
            'guest_id': a.guest_id
        } for a in episode.appearances
    ]
    return jsonify({'id': episode.id, 'date': episode.date.isoformat(), 'number': episode.number, 'appearances': appearances})

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode and its appearances deleted'})
