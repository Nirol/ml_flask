from app_wrapper.main_app.app import create_app

app = create_app()
app.run(host='0.0.0.0', port=5000, debug=True)