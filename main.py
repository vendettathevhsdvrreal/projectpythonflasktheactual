#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 


#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)