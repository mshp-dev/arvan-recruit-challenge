from app import db
from sqlalchemy.dialects.postgresql import JSON

import json


class IpInfo(db.Model):
    __tablename__ = 'ip_info'

    id = db.Column(db.Integer, primary_key=True)
    ipv4 = db.Column(db.String())
    country = db.Column(db.String())
    province = db.Column(db.String())
    city = db.Column(db.String())
    latlng = db.Column(db.String())

    def __init__(self, ipv4, country, province, city, latlng):
        self.ipv4 = ipv4
        self.country = country
        self.province = province
        self.city = city
        self.latlng = latlng

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return json.dumps('\{"ip": "{ipv4}", "country": "{country}", "province": "{province}", "city": "{city}", "latlng": "{latlng}"\}'.format(
            ipv4=self.ipv4,
            country=self.country,
            province=self.province,
            city=self.city,
            latlng=self.latlng
        ))