
from flask import Blueprint

# Blueprint for user-related routes
user_bp = Blueprint("user",__name__)

# Placeholder CRUD operations for user management


@user_bp.route('/get_user', methods=['GET'])
def get_user():
    return "This is Get-user-route."

@user_bp.route('/update_user', methods=['PUT'])
def update_user():
    return "This is Update-user-route."

@user_bp.route('/create_user', methods=['POST'])
def create_user():
    return "This is Create-user-route."

@user_bp.route('/delete_user', methods=['DELETE'])
def delete_user():
    return "This is Delete-user-route." 
