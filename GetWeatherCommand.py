import sublime, sublime_plugin, re, urllib, json

class ShowLocalWeatherCommand(sublime_plugin.WindowCommand):
    def getWindDir(self, deg) :
        val = round((deg - 11.25) / 22.5)
        arr = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        windDirStr = arr[val % 16]
        return windDirStr


    def run(self):
        endpoint = 'http://metservice.com/publicData/oneMinObs_christchurch'
        page_html = urllib.request.urlopen(endpoint).read().decode('utf-8')
        data = json.loads(page_html) 
        windDirDeg = data['windDirection']
        weatherOutput = 'Temp: ' + str(data['temperature']) + ' Wind: ' + str(data['windSpeed']) + '/' + str(data['windGustSpeed']) + ' ' + self.getWindDir(windDirDeg)
        sublime.status_message(weatherOutput)

