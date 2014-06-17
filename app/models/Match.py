from app import db

class Match(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    HomeName = db.Column(db.String)
    
    AwayName = db.Column(db.String)
    
    Percentage = db.Column(db.Float)
    
    TSAdded = db.Column(db.Date)
    
    HomeScore = db.Column(db.Integer)
    
    AwayScore = db.Column(db.Integer)
    
    CurrentGameMinute = db.Column(db.Integer)
    
    StartTime = db.Column(db.Date)
    
    AwayTeamID = db.Column(db.String)
    
    HomeTeamID = db.Column(db.String)
    
    MatchID = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            HomeName = self.HomeName,
            AwayName = self.AwayName,
            Percentage = self.Percentage,
            TSAdded = self.TSAdded.isoformat(),
            HomeScore = self.HomeScore,
            AwayScore = self.AwayScore,
            CurrentGameMinute = self.CurrentGameMinute,
            StartTime = self.StartTime.isoformat(),
            AwayTeamID = self.AwayTeamID,
            HomeTeamID = self.HomeTeamID,
            MatchID = self.MatchID,
            id = self.id
        )

    def __repr__(self):
        return '<Match %r>' % (self.id)
