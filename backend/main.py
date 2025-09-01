from app import create_app\n\napp = create_app()\n\nif __name__ == '__main__':\n    app.run(debug=True, host='0.0.0.0', port=5000)
