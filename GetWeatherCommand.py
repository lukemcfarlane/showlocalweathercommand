import sublime, sublime_plugin, re, urllib, json

class ShowLocalWeatherCommand(sublime_plugin.WindowCommand):
    def run(window):
        endpoint = 'http://metservice.com/publicData/oneMinObs_christchurch'
        page_html = urllib.request.urlopen(endpoint).read().decode('utf-8')
        data = json.loads(page_html)
        weatherOutput = 'Temp: ' + str(data['temperature']) + ' Wind: ' + str(data['windSpeed']) + '/' + str(data['windGustSpeed'])
        sublime.status_message(weatherOutput)
