from datetime import datetime

WIDTH_UI = 50

class Weather:
    def __init__(self, data):
        self.data = data

    # returns the date and hour of creation of the information in the API
    def get_creation_time(self):
        return self.data['elaborado']

    # returns the name of the town from where the data comes from
    def get_town(self):
        return self.data['municipio']['NOMBRE']

    # returns the name of the province of the town
    def get_province(self):
        return self.data['municipio']['NOMBRE_PROVINCIA']

    # returns the date of the prediction (format: YYYY-MM-DD)
    def get_today_date(self):
        return self.data['fecha']                        

    # returns the altitude of the town
    def get_altitude(self):
        return self.data['municipio']['ALTITUD']

    #returns a tuple of the corsd
    def get_coords(self):
        latitude = self.data['municipio']['LATITUD_ETRS89_REGCAN95']
        longitude = self.data['municipio']['LONGITUD_ETRS89_REGCAN95']
        return (latitude, longitude)
    
    # returns the actual state of the sky
    def get_state_sky(self):
        return self.data['stateSky']['description']
    
    # returns the actual temperature
    def get_actual_temp(self):
        return self.data['temperatura_actual']
    
    # returns the minimum temperature of today
    def get_today_min(self):
        return self.data['temperaturas']['min']
    
    # returns the maximum temperature of today
    def get_today_max(self):
        return self.data['temperaturas']['max']
    
    # returns the actual humidity of the ambience
    def get_actual_humidity(self):
        return self.data['humedad']
    
    # returns the actual speed of the wind
    def get_actual_wind_speed(self):
        return self.data['viento']

    # returns the actual probability of rain
    def get_actual_probability_rain(self):
        return self.data['lluvia']
    
    # returns the actual precipitation
    def get_actual_precipitation(self):
        return self.data['precipitacion']
    
    # returns the hour of today's sunrise
    def get_today_sunrise(self):
        return self.data['pronostico']['hoy']['@attributes']['orto']
    
    # returns the hour of today's sunset
    def get_today_sunset(self):
        return self.data['pronostico']['hoy']['@attributes']['ocaso']

    # returns a list with the stimated precipitation for each hour
    def get_today_precipitation(self):
        return self.data['pronostico']['hoy']['precipitacion']
    
    # returns a list with the probability of rain every 8 hours (3 values)
    def get_today_prob_rain(self):
        return self.data['pronostico']['hoy']['prob_precipitacion']
    
    # returns a list with the probability of storm every 8 hours
    def get_today_prob_storm(self):
        return self.data['pronostico']['hoy']['prob_tormenta']
    
    # returns a list with the amount of snow each hour
    def get_today_snow(self):
        return self.data['pronostico']['hoy']['nieve']
    
    # returns a list with the probability of snow every 8 hours
    def get_today_prob_snow(self):
        return self.data['pronostico']['hoy']['prob_nieve']
    
    # returns a list of all the values of todays temperature one each hour
    def get_today_temp(self):
        return self.data['pronostico']['hoy']['temperatura']
    
    # returns a list of all the values of todays thermal sensation, one each hour
    def get_today_thermal_sens(self):
        return self.data['pronostico']['hoy']['sens_termica']
    
    # returns a list of all the values of the relative humidity, one each hour
    def get_today_relative_hum(self):
        return self.data['pronostico']['hoy']['humedad_relativa']
    
    # returns a list of dicts with all the values of the wind (speed, and direction), one for each hour
    def get_today_wind(self):
        return self.data['pronostico']['hoy']['viento']
    
    # returns a list with the max speed of the wind, one each hour
    def get_today_max_wind(self):
        return self.data['pronostico']['hoy']['racha_max']
    
    # returns a list with the description of the sky, one for each hour
    def get_today_sky_description(self):
        return self.data['pronostico']['hoy']['estado_cielo_descripcion']
    
    # returns de date of tomorrow (format: YYYY-MM-DD)
    def get_tomorrow_date(self):
        return self.data['pronostico']['manana']['@attributes']['fecha']
    
    # returns the hour of tomorrow's sunrise
    def get_tomorrow_sunrise(self):
        return self.data['pronostico']['manana']['@attributes']['orto']
    
    # returns the hour of tomorrow's sunset
    def get_tomorrow_sunset(self):
        return self.data['pronostico']['manana']['@attributes']['ocaso']

    # returns a list with the stimated precipitation for each hour (tomorrow)
    def get_tomorrow_precipitation(self):
        return self.data['pronostico']['manana']['precipitacion']
    
    # returns a list with the probability of rain every 8 hours (3 values)
    def get_tomorrow_prob_rain(self):
        return self.data['pronostico']['manana']['prob_precipitacion']
    
    # returns a list with the probability of storm every 8 hours
    def get_tomorrow_prob_storm(self):
        return self.data['pronostico']['manana']['prob_tormenta']
    
    # returns a list with the amount of snow each hour
    def get_tomorrow_snow(self):
        return self.data['pronostico']['manana']['nieve']
    
    # returns a list with the probability of snow every 8 hours
    def get_tomorrow_prob_snow(self):
        return self.data['pronostico']['manana']['prob_nieve']
    
     # returns a list of all the values of todays temperature one each hour
    def get_tomorrow_temp(self):
        return self.data['pronostico']['manana']['temperatura']
    
    # returns a list of all the values of todays thermal sensation, one each hour
    def get_tomorrow_thermal_sens(self):
        return self.data['pronostico']['manana']['sens_termica']
    
    # returns a list of all the values of the relative humidity, one each hour
    def get_tomorrow_relative_hum(self):
        return self.data['pronostico']['manana']['humedad_relativa']
    
    # returns a list of dicts with all the values of the wind (speed, and direction), one for each hour
    def get_tomorrow_wind(self):
        return self.data['pronostico']['manana']['viento']
    
    # returns a list with the max speed of the wind, one each hour
    def get_tomorrow_max_wind(self):
        return self.data['pronostico']['manana']['racha_max']
    
    # returns a list with the description of the sky, one for each hour
    def get_tomorrow_sky_description(self):
        return self.data['pronostico']['manana']['estado_cielo_descripcion']
    
    def check_all_correct(self):
        actual_date = self.get_today_date()
        expected_date = datetime.now().strftime("%Y-%m-%d")

        if actual_date == expected_date:
            return True
        else:
            raise ValueError(
                f"Something is going wrong with the API, its not up to date (the date of the data is not from today)"
            )

    def __find_correct_time(self, arr):
        r = 23
        for i in reversed(arr):
            if r == int(datetime.now().strftime("%H")):
                string = f"{i}"
                return string
            else:
                r -= 1

    def __find_correct_period(self, arr):
        time = int(datetime.now().strftime("%H"))
        if time > 18:
            return arr[len(arr)-1]
        elif time > 12:
            return arr[len(arr)-2]
        elif time > 6:
            return arr[len(arr)-3]
        else:
            return arr[0]

    def __intro_report(self):
        intro_report = "WEATHER REPORT"
        where_report = f"for {self.get_town()} ({self.get_province()})"
        time_report = f"at {self.get_today_date()} {datetime.now().strftime("%H:%M")}"
                
        output_string = '\n' + '-' * WIDTH_UI +'\n'
        output_string += f"{intro_report:^{WIDTH_UI}}\n"
        output_string += f"{where_report:^{WIDTH_UI}}\n"
        output_string += f"{time_report:^{WIDTH_UI}}\n"
        output_string += '-' * WIDTH_UI + '\n'
        
        return output_string
    
    def __weather_conditions(self):
        title = "WEATHER CONDITIONS"
        current_temp = f"Current temperature: {self.get_actual_temp()}ºC"
        today_min = f"Today's minimum: {self.get_today_min()}ºC"
        today_max = f"Today's maximum: {self.get_today_max()}ºC"
        therm_sens = f"Current thermal sensation: {self.get_today_thermal_sens()[int(datetime.now().strftime("%H"))]}ºC"
        relative_hum = f"Current relative humidity: {self.get_actual_humidity()}%"

        output_string = f"{title:^{WIDTH_UI}}\n\n"
        output_string += f" {today_min:<{(WIDTH_UI//2)-1}}{today_max:>{(WIDTH_UI//2)-1}} \n" 
        output_string += f"{current_temp:^{WIDTH_UI}}\n"
        output_string += f"{therm_sens:^{WIDTH_UI}}\n"
        output_string += f"{relative_hum:^{WIDTH_UI}}\n"
        output_string += '-' * WIDTH_UI + '\n'
        
        return output_string

    def __state_sky(self):
        title = "STATE OF THE SKY"
        state_sky = self.get_state_sky()

        output_string = f"{title:^{WIDTH_UI}}\n\n"
        output_string += f"{state_sky:^{WIDTH_UI}}\n"
        output_string += '-' * WIDTH_UI + '\n'

        return output_string
    
    def __atomspheric_conditions(self):
        title = "ATMOSPHERIC CONDITIONS"
        wind_speed = f"Current speed of the wind: {self.get_actual_wind_speed()} km/h"
        for i in self.get_today_wind():
            if i['@attributes']['periodo'] == datetime.now().strftime("%H"):
                wind_speed += f" ({i['direccion']})"
                break
        max_wind = f"Current maximum wind gust: "
        max_wind += self.__find_correct_time(self.get_today_max_wind()) + " km/h"

        output_string = f"{title:^{WIDTH_UI}}\n\n"
        output_string += f"{wind_speed:^{WIDTH_UI}}\n"
        output_string += f"{max_wind:^{WIDTH_UI}}\n"
        output_string += '-' * WIDTH_UI + '\n'
        
        return output_string
    
    def __precipitation(self):
        title = "PRECIPITATION"
        current_precipitation = f"Current precipitation: {self.get_actual_precipitation()} mm"
        current_prob_rain = f"Current probability of rain: {self.get_actual_probability_rain()}%"
        current_prob_storm = f"Current probability of storm: "
        current_prob_storm += self.__find_correct_period(self.get_today_prob_storm())+ "%"
        current_snow = f"Current snow accumulation: "
        current_snow += self.__find_correct_time(self.get_today_snow()) + " cm"

        output_string = f"{title:^{WIDTH_UI}}\n\n"
        output_string += f"{current_precipitation:^{WIDTH_UI}}\n"
        output_string += f"{current_prob_rain:^{WIDTH_UI}}\n"
        output_string += f"{current_prob_storm:^{WIDTH_UI}}\n"
        output_string += f"{current_snow:^{WIDTH_UI}}\n"
        output_string += '-' * WIDTH_UI + '\n'

        return output_string
    
    def __astronomic_info(self):
        title = "ATRONOMIC INFORMATION"
        today_sunrise = f"Today's sunrise: {self.get_today_sunrise()}"
        today_sunset = f"Today's sunset: {self.get_today_sunset()}"
        tomorrow_sunrise = f"Tomorrow's sunrise: {self.get_tomorrow_sunrise()}"
        tomorrow_sunset = f"Tomorrow's sunset: {self.get_tomorrow_sunset()}"

        output_string = f"{title:^{WIDTH_UI}}\n\n"
        output_string += f" {today_sunrise:<{(WIDTH_UI//2)-1}}{today_sunset:>{(WIDTH_UI//2)-1}} \n" 
        output_string += f"{tomorrow_sunrise:<{(WIDTH_UI//2)}}{tomorrow_sunset:>{(WIDTH_UI//2)}}\n"
        output_string += '-' * WIDTH_UI + '\n'
        
        return output_string
    
    def __end_report(self):
        title = "END OF THE REPORT"

        output_string = f"{title:^{WIDTH_UI}}\n"
        output_string += '-' * WIDTH_UI + '\n'

        return output_string

    def __report(self):
        output_string = "Something is wrong"
        if self.check_all_correct():
            output_string = self.__intro_report()
            output_string += self.__weather_conditions()
            output_string += self.__state_sky()
            output_string += self.__atomspheric_conditions()
            output_string += self.__precipitation()
            output_string += self.__astronomic_info()
            output_string += self.__end_report()
        return output_string
    
    def __str__(self):
        return self.__report()