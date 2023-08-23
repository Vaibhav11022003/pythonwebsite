from flask import Flask
app=Flask(__name__)
@app.route('/')
def home_fun():
   return "hello Jovian"
if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0')
  