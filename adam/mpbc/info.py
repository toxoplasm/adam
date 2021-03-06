#!/usr/bin/python3
""" Information on MPBC's MDMA Program """

import os


class Program:
    """ Data class to store MDMA Program information"""

    STUDIES = {
        'MP16',
        'MP17',
        'MP18',
        'MAPP1',
        'MAPP2',
        'MAPP3',
        'MJP1',
        'MPVA1'
    }

    SITES = [
        { 'name' : {'Charleston' : '01'}}, 
        { 'name' : {'Boulder' : '02'}}, 
        { 'name' : {'Fort Collins' : '03'}}, 
        { 'name' : {'Los Angeles' : '04'}}, 
        { 'name' : {'New Orleans' : '05'}},
        { 'name' : {'University of California, San Francisco' : '06'}},
        { 'name' : {'San Francisco Insight and Integration Center' : '07'}},
        { 'name' : {'University of Connecticut' : '08'}},
        { 'name' : {'University of Wisconsin at Madison' : '09'}},
        { 'name' : {'New York University' : '10'}},
        { 'name' : {'Affective Care' : '11'}},
        { 'name' : {'Boston' : '12'}},
        { 'name' : {'University of British Columbia' : '13'}},
        { 'name' : {'Dr. Simon Amar, LLC' : '14'}},
        { 'name' : {'Beer Yaakov' : '15'}},
        { 'name' : {'Tel Hashomer' : '16'}},
        { 'name' : {'Cardiff' : '17'}},
        { 'name' : {'Leiden/Oegstgeest' : '18'}},
        { 'name' : {'Maastricht' : '19'}},
        { 'name' : {'Prague' : '20'}},
        { 'name' : {'Bristol' : '21'}},
        { 'name' : {'Portugal' : '22'}},
        { 'name' : {'Norway' : '23'}},
        { 'name' : {'Berlin' : '24'}},
        { 'name' : {'Regensburg' : '25'}},
        { 'name' : {'Finland' : '26'}}
    ]

    SITE_NAMES = {
        '01' : 'Charleston',
        '02' : 'Boulder',
        '03' : 'Fort Collins',
        '04' : 'Los Angeles',
        '05' : 'New Orleans',
        '06' : 'University of California, San Francisco',
        '07' : 'San Francisco Insight and Integration Center',
        '08' : 'University of Connecticut',
        '09' : 'University of Wisconsin at Madison',
        '10' : 'New York University',
        '11' : 'Affective Care' ,
        '12' : 'Boston' ,
        '13' : 'University of British Columbia',
        '14' : 'Dr. Simon Amar, LLC',
        '15' : 'Beer Yaakov',
        '16' : 'Tel Hashomer',
        '17' : 'Cardiff',
        '18' : 'Leiden/Oegstgeest',
        '19' : 'Maastricht',
        '20' : 'Prague',
        '21' : 'Bristol',
        '22' : 'Portugal',
        '23' : 'Norway',
        '24' : 'Berlin',
        '25' : 'Regensburg',
        '25' : 'Finland'
    }

    VISITS =  [
        'V1',
        'V2',
        'V4',
        'V5',
        'V6',
        'V7',
        'V9',
        'V10',
        'V11',
        'V12',
        'V14',
        'V15',
        'V16',
        'V17',
        'V18',
        'V20'
    ]

    PARTICIPANTS = {'PARTD', 'TEST'}


class Default:

    def __init__(self):
        self.location = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        with open(os.path.join(self.location, 'default.info'), 'r') as d:
            study, site, participant, visit = (x.strip() for x in d.readlines()[:4])
        self.STUDY = study
        self.SITE = site
        self.PARTICIPANT = participant
        self.VISIT = visit

    def write(self, study, site, participant, visit, time, webcams, microphones):
        with open(os.path.join(self.location, 'default.info'), 'w') as d:
            d.write(study + '\n')
            d.write(site + '\n')
            d.write(participant + '\n')
            d.write(visit + '\n')
            d.write(time + '\n')
            d.write(webcams + '\n')
            d.write(microphones + '\n')
