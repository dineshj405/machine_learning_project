import sys
print("__________________", sys.path)
import methods
from flask import Flask

app=Flask(__name__)


@app.route("/",methods['GET','POST'])
def undex():
    return "CI-CD pipeline has been established"


if __name__=="__main__":
    app.run(debug=True)