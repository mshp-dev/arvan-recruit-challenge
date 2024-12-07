from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

import os, json, geocoder


# pg_user = "postgres"
# pg_password = "PG@db#110"
# pg_host = "localhost"
# pg_port = 5432
# pg_database = "ip-info"
# pg_url = f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}'

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# from models import IpInfo


@app.route('/api/ip-info', methods = ['POST'])
def ip_info():
    if request.method == "POST":
        print(request.data['ip'])
        response = app.response_class(
            response=json.dumps({"result": "OK"}),
            status=200,
            mimetype='application/json'
        )
        # request_history = session.exec(select(RequestHistory).where(RequestHistory.ip == ip_addr.ip)) #.all()
        # print(type(request_history))
        # print(request_history)
        # if not request_history:
        #     requested_ip = geocoder.ip(ip_addr.ip)
        #     type(requested_ip.latlng[0])
        #     request_history = RequestHistory(
        #         ip=ip_addr.ip,
        #         country=requested_ip.country,
        #         province=requested_ip.province,
        #         city=requested_ip.city,
        #         latitude=requested_ip.latlng[0],
        #         longitude=requested_ip.latlng[1]
        #     )
        #     session.add(RequestHistory.model_validate(request_history))
        #     session.commit()
        return response


if __name__ == '__main__':
    app.run(debug=True)