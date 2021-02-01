from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

data = [{'employee_id': i+1} for i in range(1000)]


def paginacao(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['data'] = results[(start - 1):(start - 1 + limit)]
    return obj





class Employees(Resource):
    def get(self):

        return jsonify(paginacao(
            data,
            '/employees',
            start=request.args.get('start', 1),
            limit=request.args.get('limit', 20)
        ))



#  "data": {
#                 "....": "...Dados a serem retornados pelo banco."
#             },
#             "paginator": {
#                 "per_page": "10 - quantidade de paginas",
# 		"page": "9",
# 		"pages": "9 quantidades de pagians da consulta retornada"
#             },
#             "count": "total de paginas"

#         }


api.add_resource(Employees, '/employees')


if __name__ == '__main__':
    app.run(port='5002', debug=True)


# http: // localhost: 5002/employees?start = 1 & limit = 3
# python paginacao.py
