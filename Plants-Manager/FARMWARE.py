import os
import datetime
from API import API
from CeleryPy import log

class MyFarmware():

    def get_input_env(self):
        prefix = self.farmwarename.lower().replace('-','_')
        
        self.input_title = os.environ.get(prefix+"_title", '-')
        self.input_id = os.environ.get(prefix+"_id", '*')
        self.input_pointname = os.environ.get(prefix+"_pointname", '*')
        self.input_openfarm_slug = os.environ.get(prefix+"_openfarm_slug", '*')
        self.input_age_min_day = int(os.environ.get(prefix+"_age_min_day", -1))
        self.input_age_max_day = int(os.environ.get(prefix+"_age_max_day", 36500))
        self.input_filter_meta_key = os.environ.get(prefix+"_filter_meta_key", 'None')
        self.input_filter_meta_value = os.environ.get(prefix+"_filter_meta_value", 'None')
        self.input_filter_min_x = os.environ.get(prefix+"_filter_min_x", 'None')
        self.input_filter_max_x = os.environ.get(prefix+"_filter_max_x", 'None')
        self.input_filter_min_y = os.environ.get(prefix+"_filter_min_y", 'None')
        self.input_filter_max_y = os.environ.get(prefix+"_filter_max_y", 'None')
        self.input_save_name = os.environ.get(prefix+"_save_name", 'None')
        self.input_remove_all_metadata = os.environ.get(prefix+"_remove_all_metadata", 'No')
        self.input_save_meta_key = os.environ.get(prefix+"_save_meta_key", 'None')
        self.input_save_meta_value = os.environ.get(prefix+"_save_meta_value", 'None')
        self.input_save_date = os.environ.get(prefix+"_save_date", 'None')
        self.input_debug = int(os.environ.get(prefix+"_debug", 1))

        if self.input_debug >= 1:
            log('title: {}'.format(self.input_title), message_type='debug', title=self.farmwarename)
            log('id: {}'.format(self.input_id), message_type='debug', title=self.farmwarename)
            log('pointname: {}'.format(self.input_pointname), message_type='debug', title=self.farmwarename)
            log('openfarm_slug: {}'.format(self.input_openfarm_slug), message_type='debug', title=self.farmwarename)
            log('age_min_day: {}'.format(self.input_age_min_day), message_type='debug', title=self.farmwarename)
            log('age_max_day: {}'.format(self.input_age_max_day), message_type='debug', title=self.farmwarename)
            log('filter_meta_key: {}'.format(self.input_filter_meta_key), message_type='debug', title=self.farmwarename)
            log('filter_meta_value: {}'.format(self.input_filter_meta_value), message_type='debug', title=self.farmwarename)
            log('filter_min_x: {}'.format(self.input_filter_min_x), message_type='debug', title=self.farmwarename)
            log('filter_max_x: {}'.format(self.input_filter_max_x), message_type='debug', title=self.farmwarename)
            log('filter_min_y: {}'.format(self.input_filter_min_y), message_type='debug', title=self.farmwarename)
            log('filter_max_y: {}'.format(self.input_filter_max_y), message_type='debug', title=self.farmwarename)
            log('save_name: {}'.format(self.input_save_name), message_type='debug', title=self.farmwarename)
            log('remove_all_metadata: {}'.format(self.input_remove_all_metadata), message_type='debug', title=self.farmwarename)
            log('save_meta_key: {}'.format(self.input_save_meta_key), message_type='debug', title=self.farmwarename)
            log('save_meta_value: {}'.format(self.input_save_meta_value), message_type='debug', title=self.farmwarename)
            log('save_date: {}'.format(self.input_save_date), message_type='debug', title=self.farmwarename)
            log('debug: {}'.format(self.input_debug), message_type='debug', title=self.farmwarename)
        
    def __init__(self,farmwarename):
        self.farmwarename = farmwarename
        self.get_input_env()
        self.api = API(self)
        self.points = []

    def apply_filters(self, points, point_id='*', point_name='*', openfarm_slug='*', age_min_day=0, age_max_day=36500, meta_key='', meta_value='', min_x='none', max_x='none', min_y='none', max_y='none', pointer_type='Plant'):
        if self.input_debug >= 1: log(points, message_type='debug', title=str(self.farmwarename) + ' : load_points')
        filtered_points = []
        now = datetime.datetime.utcnow()
        for p in points:
            if p['pointer_type'].lower() == pointer_type.lower():
                b_meta = False
                age_day = (now - datetime.datetime.strptime(p['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')).days
                if str(meta_key).lower() != 'none':
                    try:
                        b_meta = ((p['meta'][meta_key]).lower() == meta_value.lower())
                    except Exception as e:
                        b_meta = False
                else:
                    b_meta = True
                if str(min_x).lower() == 'none' or str(min_y).lower() == 'none' or str(max_x).lower() == 'none' or str(max_y).lower() == 'none':
                    b_coordinate = True
                else:
                    if int(min_x) <= int(p['x']) <= int(max_x) and int(min_y) <= int(p['y']) <= int(max_y):
                        b_coordinate = True
                    else:
                        b_coordinate = False
                if  (p['id'] == point_id or point_id == '*') and (p['name'].lower() == point_name.lower() or point_name == '*') and (p['openfarm_slug'].lower() == openfarm_slug.lower() or openfarm_slug == '*') and (age_min_day <= age_day <= age_max_day) and b_meta==True and b_coordinate :
                    filtered_points.append(p.copy())
        return filtered_points

    def load_points_with_filters(self):
        self.points = self.apply_filters(
            points=self.api.api_get('points'),
            point_id=self.input_id,
            point_name=self.input_pointname,
            openfarm_slug=self.input_openfarm_slug,
            age_min_day=self.input_age_min_day,
            age_max_day=self.input_age_max_day,
            meta_key=self.input_filter_meta_key,
            meta_value=self.input_filter_meta_value,
            min_x=self.input_filter_min_x,
            min_y=self.input_filter_min_y,
            max_x=self.input_filter_max_x,
            max_y=self.input_filter_max_y,
            pointer_type='Plant')
        if self.input_debug >= 1: log(self.points, message_type='debug', title=str(self.farmwarename) + ' : load_points_with_filters')
        

    def sort_points(self):
        self.points = sorted(self.points , key=lambda elem: (int(elem['x']), int(elem['y'])))
        if self.input_debug >= 1: log(self.points, message_type='debug', title=str(self.farmwarename) + ' : sort_points')
        #self.points, self.tab_id = Get_Optimal_Way(self.points)

    def save_data(self,point):
            log('Before : ' + str(point) , message_type='info', title=str(self.farmwarename) + ' : save_data')            
            if str(self.input_remove_all_metadata).lower() == 'yes':
                point['meta'] = {}
            if str(self.input_save_meta_key).lower() != 'none':
                point['meta'][self.input_save_meta_key]=self.input_save_meta_value
            if str(self.input_save_name).lower() != 'none':
                point['name']=self.input_save_name
            if str(self.input_save_date).lower() != 'none':
                if str(self.input_save_date).lower() == '#now#':
                    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                    point['created_at']= now
                    point['updated_at']= now
                else:
                    d = datetime.datetime.strptime(self.input_save_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                    point['created_at']= d
                    point['updated_at']= d
            if self.input_debug < 2 :    
                endpoint = 'points/{}'.format(point['id'])
                self.api.api_put(endpoint=endpoint, data=point)
            log('After : ' + str(point) , message_type='info', title=str(self.farmwarename) + ' : save_data')

    def loop_points(self):
        for p in self.points:
            self.save_data(p)
    
    
    def run(self):
        self.load_points_with_filters()
        self.sort_points()
        if len(self.points) > 0 : self.loop_points()
        
        