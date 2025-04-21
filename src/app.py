from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{
  "label" : "the first task",
  "done" : False
}]

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
   request_body = request.json
   if "label" not in request_body or request_body["label"] is None or request_body["label"] == "":
     return jsonify({"message": "'label' is required"}), 400
   elif "done" not in request_body or request_body["done"] is None or request_body["done"] == "":
     return jsonify({"message": "'done' is required"}), 400
   else:
     todos.append(request_body)
   return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  del todos[position]
  return todos
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)