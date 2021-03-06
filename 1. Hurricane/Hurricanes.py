# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damage(damage):
    updated_damages = []
    for item in damage:
        if item[-1] == "B":
            value = float(item[:-1]) * 1000000000
            updated_damages.append(value)
        elif item[-1] == "M":
            value = float(item[:-1]) * 1000000
            updated_damages.append(value)
        else:
            updated_damages.append(item)
    return updated_damages

# write your construct hurricane dictionary function here:
def combine_hurricane_data(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricane_data = {}
    for i, key in enumerate(names):
        # for month, year, max_sustained_wind, areas_affected_item, update_damage_item, deaths_item in zip(months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
        hurricane_data[key] = {
            "Name": key,
            "Month": months[i], 
            "Year": years[i], 
            "Max Sustained Wind": max_sustained_winds[i], 
            "Areas Affected": areas_affected[i], 
            "Damage": updated_damages[i], 
            "Deaths": deaths[i]
            }      
    return hurricane_data

# write your construct hurricane by year dictionary function here:
def combine_hurricane_data_year(combine_hurricane_data):
    years_lst = [n["Year"] for n in combine_hurricane_data.values()]
    years_index_dict = {}
    for year in years_lst:
        year_index = [i for i in range(len(years_lst)) if years_lst[i] == year]
        years_index_dict[year] = year_index

    hurricane_data_year = {}
    for key, index in years_index_dict.items():
        data_lst = []
        for idx in index:
            lst = [data for i, data in enumerate(combine_hurricane_data.values()) if i == idx]
            data_lst.append(lst[0])
            hurricane_data_year[key] = data_lst
    return hurricane_data_year

# write your count affected areas function here:
def area_affected_count_data(combine_hurricane_data):
    areas_lst_lst = [n["Areas Affected"] for n in combine_hurricane_data.values()]
    area_lst = []
    for areas_lst in areas_lst_lst:
        for areas in areas_lst:
            area_lst.append(areas)
    
    area_lst_unique = list(set(area_lst))
    area_dict = {}
    for area in area_lst_unique:
        count_area = area_lst.count(area)
        area_dict[area] = count_area
    return area_dict

# write your find most affected area function here:
def most_areas_affected(affected_count_data):
    max_values = max(affected_count_data.values())
    
    most_affected_areas = []

    for area in affected_count_data:
        if affected_count_data[area] == max_values:
            most_affected_areas.append(area)

    return most_affected_areas

# write your greatest number of deaths function here:
def most_deaths(combine_hurricane_data):
    max_deaths_list = [n["Deaths"] for n in combine_hurricane_data.values()]
    max_deaths_value = max(max_deaths_list)
    max_deaths_index = []

    for i, n in enumerate(max_deaths_list):
        if n == max_deaths_value:
            max_deaths_index.append(i)

    max_deaths = {}

    for i in range(len(max_deaths_index)):
        for j, key in enumerate(combine_hurricane_data):
            if max_deaths_index[i] == j:
                max_deaths[combine_hurricane_data[key]["Name"]] = combine_hurricane_data[key]["Deaths"]
    
    return max_deaths

# write your catgeorize by mortality function here:
def mortality_rating(combine_hurricane_data):
    mortality_rating_data = {}
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    lst_0 = []
    lst_1 = []
    lst_2 = []
    lst_3 = []
    lst_4 = []

    for n in combine_hurricane_data.values():
        deaths = n["Deaths"]
        if deaths > mortality_scale[4]:
            lst_4.append(n["Name"])
        elif deaths > mortality_scale[3]:
            lst_3.append(n["Name"])
        elif deaths > mortality_scale[2]:
            lst_2.append(n["Name"])
        elif deaths > mortality_scale[1]:
            lst_1.append(n["Name"])
        else:
            lst_0.append(n["Name"])
            
    mortality_rating_data[4] = lst_4
    mortality_rating_data[3] = lst_3
    mortality_rating_data[2] = lst_2
    mortality_rating_data[1] = lst_1
    mortality_rating_data[0] = lst_0

    return mortality_rating_data

# write your greatest damage function here:
def greatest_damage(combine_hurricane_data):
    max_damage_list = [n["Damage"] for n in combine_hurricane_data.values()]
    max_damage_list = [0 if n=="Damages not recorded" else n for n in max_damage_list]
    max_damage_value = max(max_damage_list)
    max_damage_index = []

    for i, n in enumerate(max_damage_list):
        if n == max_damage_value:
            max_damage_index.append(i)

    max_damage = {}

    for i in range(len(max_damage_index)):
        for j, key in enumerate(combine_hurricane_data):
            if max_damage_index[i] == j:
                max_damage[combine_hurricane_data[key]["Name"]] = combine_hurricane_data[key]["Damage"]
    
    return max_damage
    
# write your catgeorize by damage function here:
def damage_rating(combine_hurricane_data):
    damage_rating_data = {}
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    lst_0 = []
    lst_1 = []
    lst_2 = []
    lst_3 = []
    lst_4 = []

    for n in combine_hurricane_data.values():
        deaths = n["Damage"]
        if deaths == "Damages not recorded":
            deaths = 0
        if deaths > damage_scale[4]:
            lst_4.append(n["Name"])
        elif deaths > damage_scale[3]:
            lst_3.append(n["Name"])
        elif deaths > damage_scale[2]:
            lst_2.append(n["Name"])
        elif deaths > damage_scale[1]:
            lst_1.append(n["Name"])
        else:
            lst_0.append(n["Name"])
        
    damage_rating_data[4] = lst_4
    damage_rating_data[3] = lst_3
    damage_rating_data[2] = lst_2
    damage_rating_data[1] = lst_1
    damage_rating_data[0] = lst_0

    return damage_rating_data


def main():
    updated_damages = update_damage(damages)
    hurricane_combine = combine_hurricane_data(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
    hurricane_combine_date = combine_hurricane_data_year(hurricane_combine)
    affected_count_data = area_affected_count_data(hurricane_combine)
    most_affected_areas_data = most_areas_affected(affected_count_data)
    most_deaths_data = most_deaths(hurricane_combine)
    mortality_rating_data = mortality_rating(hurricane_combine)
    greatest_damage_data = greatest_damage(hurricane_combine)
    damage_rating_data = damage_rating(hurricane_combine)

main()

if __name__ == "__main__":
    pass
