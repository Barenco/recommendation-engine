from flask import Flask
import engine

app = Flask(__name__)

@app.route('/api/recommendations/<int:id>', methods=['GET'])
def get_recommendations(id):
    print("Product id requested: " + str(id))
    return engine.get_recommendations(id)


if __name__ == '__main__':
    app.run()