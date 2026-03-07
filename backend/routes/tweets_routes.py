from flask import Blueprint, request, jsonify
from controllers.tweet_controller import TweetController

tweets_bp = Blueprint('tweets', __name__)
controller = TweetController()

@tweets_bp.route('/generate-tweets', methods=['POST'])
def generate_tweets():
    data = request.get_json()
    return controller.generate_tweets(data)

@tweets_bp.route('/tweets/<int:campaign_id>', methods=['GET'])
def get_tweets(campaign_id):
    return controller.get_tweets(campaign_id)

@tweets_bp.route('/campaigns', methods=['GET'])
def get_campaigns():
    return controller.get_campaigns()
