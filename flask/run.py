from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("All tables created successfully!")
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run()
