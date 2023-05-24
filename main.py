import eel
import pyowm

owm = pyowm.OWM("e4fd6f586b209c4dbf4c15e9013e123e")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    city = "New York, USA"
    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "ქალაქ" + city + "-ში ახლა არის " + str(temp) + "ტემპერატურა"



eel.init("web")
eel.start("main.html", size = (700,700))
