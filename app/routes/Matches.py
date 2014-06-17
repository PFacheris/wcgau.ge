from app import app, db
from app.models import Match
from flask import abort, jsonify, request
import datetime
import json

@app.route('/WCGUA.GE/Matches', methods = ['GET'])
def get_all_Matches():
    entities = Match.Match.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/WCGUA.GE/Matches/<int:id>', methods = ['GET'])
def get_Match(id):
    entity = Match.Match.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/WCGUA.GE/Matches', methods = ['POST'])
def create_Match():
    entity = Match.Match(
        HomeName = request.json['HomeName']
        , AwayName = request.json['AwayName']
        , Percentage = request.json['Percentage']
        , TSAdded = datetime.datetime.strptime(request.json['TSAdded'], "%Y-%m-%d").date()
        , HomeScore = request.json['HomeScore']
        , AwayScore = request.json['AwayScore']
        , CurrentGameMinute = request.json['CurrentGameMinute']
        , StartTime = datetime.datetime.strptime(request.json['StartTime'], "%Y-%m-%d").date()
        , AwayTeamID = request.json['AwayTeamID']
        , HomeTeamID = request.json['HomeTeamID']
        , MatchID = request.json['MatchID']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/WCGUA.GE/Matches/<int:id>', methods = ['PUT'])
def update_Match(id):
    entity = Match.Match.query.get(id)
    if not entity:
        abort(404)
    entity = Match.Match(
        HomeName = request.json['HomeName'],
        AwayName = request.json['AwayName'],
        Percentage = request.json['Percentage'],
        TSAdded = datetime.datetime.strptime(request.json['TSAdded'], "%Y-%m-%d").date(),
        HomeScore = request.json['HomeScore'],
        AwayScore = request.json['AwayScore'],
        CurrentGameMinute = request.json['CurrentGameMinute'],
        StartTime = datetime.datetime.strptime(request.json['StartTime'], "%Y-%m-%d").date(),
        AwayTeamID = request.json['AwayTeamID'],
        HomeTeamID = request.json['HomeTeamID'],
        MatchID = request.json['MatchID'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/WCGUA.GE/Matches/<int:id>', methods = ['DELETE'])
def delete_Match(id):
    entity = Match.Match.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
