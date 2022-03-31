# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 20:20:50 2022

@author: gilbe
"""

from flask import Flask, jsonify, request
import json
from elasticsearch import Elasticsearch

# es = elastic_test.connect_elasticsearch()
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme':'http'}])

response = ''

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/test', methods = ['GET', 'POST'])

def nameRoute():
    
    global request_data
    global data_model
    final_price = 0.0
    dict = {}
    
    if(request.method == 'POST'):
        #On charge les données du formulaire
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))

        #On charge les données de la recette
        with open('recettecuisine_siteweb.json', 'r') as f:
            data_model = json.load(f)

        """
        print(request_data['id'])
        result = es.get(index='azuretemp', id=request_data['id'])
        print(result['_source']['Items']['unitPrice'])
        print(result['_source']['BillingCurrency'])
        price = result['_source']['Items']['unitPrice']
        currency = result['_source']['BillingCurrency']
        return jsonify({'unitPrice': price,
                        'currency': currency})
        # return jsonify({'Nombres_utilisateurs': request_data['Nombres_utilisateurs']})
        """
        print(request_data)
        print(type(data_model['Cloud Run']['CPU']['Prix']))

        #Calcul du prix selon les cas
        if request_data['But'] == 'Ecommerce':
            if request_data['Nombres_utilisateurs'] == '1-10000' and request_data['Exp'] == 'Oui':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 10
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 185
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 12
                price_cdn = data_model['Cloud CDN']['Prix'] * 3000
                final_price = round(price_cpu + price_memory + price_requests + price_cdn,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '1-10000' and request_data['Exp'] == 'Non':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 10
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 185
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 12
                final_price = round(price_cpu + price_memory + price_requests,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '10000-100000' and request_data['Exp'] == 'Oui':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 50
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 925
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 60
                price_cdn = data_model['Cloud CDN']['Prix'] * 15000
                final_price = round(price_cpu + price_memory + price_requests + price_cdn,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '10000-100000' and request_data['Exp'] == 'Non':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 50
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 925
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 60
                final_price = round(price_cpu + price_memory + price_requests,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '100000-500000' and request_data['Exp'] == 'Oui':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 250
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 4625
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 300
                price_cdn = data_model['Cloud CDN']['Prix'] * 75000
                final_price = round(price_cpu + price_memory + price_requests + price_cdn,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '100000-500000' and request_data['Exp'] == 'Non':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 250
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 4625
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 300
                final_price = round(price_cpu + price_memory + price_requests,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '500000+' and request_data['Exp'] == 'Oui':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 500
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 9250
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 600
                price_cdn = data_model['Cloud CDN']['Prix'] * 150000
                final_price = round(price_cpu + price_memory + price_requests + price_cdn,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '500000+' and request_data['Exp'] == 'Non':
                price_cpu = data_model['Cloud Run']['CPU']['Prix'] * 500
                price_memory = data_model['Cloud Run']['Memory']['Prix'] * 9250
                price_requests = data_model['Cloud Run']['Requests per Months']['Prix'] * 600
                final_price = round(price_cpu + price_memory + price_requests,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Cloud Run",
                             'Cpu': f"Cpu: {data_model['Cloud Run']['CPU']['Complements']}",
                             'Memory': f"Memory: {data_model['Cloud Run']['Memory']['Complements']}",
                             'Requests': f"Requests: {data_model['Cloud Run']['Requests per Months']['Complements']}"
                             })

        elif request_data['But'] == 'Site vitrine':
            if request_data['Nombres_utilisateurs'] == '1-10000' and request_data['Exp'] == 'Oui':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 2500
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 20
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 50
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 50
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 60
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 50
                price_cdn = data_model['Cloud CDN']['Prix'] * 3000
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting + price_cdn,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '1-10000' and request_data['Exp'] == 'Non':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 2500
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 20
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 50
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 50
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 60
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 50
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting,2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '10000-100000' and request_data['Exp'] == 'Oui':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 125000
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 100
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 250
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 250
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 300
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 250
                price_cdn = data_model['Cloud CDN']['Prix'] * 15000
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting + price_cdn, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '10000-100000' and request_data['Exp'] == 'Non':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 125000
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 100
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 250
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 250
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 300
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 250
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '100000-500000' and request_data['Exp'] == 'Oui':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 625000
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 500
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 1250
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 1250
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 1500
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 1250
                price_cdn = data_model['Cloud CDN']['Prix'] * 75000
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting + price_cdn, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '100000-500000' and request_data['Exp'] == 'Non':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 625000
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 500
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 1250
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 1250
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 1500
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 1250
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '500000+' and request_data['Exp'] == 'Oui':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 1250000
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 1000
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 2500
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 2500
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 3000
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 2500
                price_cdn = data_model['Cloud CDN']['Prix'] * 150000
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting + price_cdn, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '500000+' and request_data['Exp'] == 'Non':
                price_auth = data_model['Firebase Hosting']['Authentification']['Prix'] * 1250000
                price_firestore = data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Prix'] * 1000
                price_egress = data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Prix'] * 2500
                price_networking = data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Prix'] * 2500
                price_storage = data_model['Firebase Hosting']['Cloud Functions - Container storage']['Prix'] * 3000
                price_hosting = data_model['Firebase Hosting']['Hosting - Storage']['Prix'] * 2500
                final_price = round(price_auth + price_firestore + price_egress + price_networking + price_storage + price_hosting, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Firebase Hosting",
                             'Authentification': f"Authentification: {data_model['Firebase Hosting']['Authentification']['Complements']}",
                             'Stored data': f"Cloud Firestore - Stored data: {data_model['Firebase Hosting']['Cloud Firestore - Stored data']['Complements']}",
                             'Network egress': f"Cloud Firestore - Network egress: {data_model['Firebase Hosting']['Cloud Firestore - Network egress']['Complements']}",
                             'Outbound networking': f"Cloud Functions - Outbound networking: {data_model['Firebase Hosting']['Cloud Functions - Outbound networking']['Complements']}",
                             'Container storage': f"Cloud Functions - Container storage: {data_model['Firebase Hosting']['Cloud Functions - Container storage']['Complements']}",
                             'Hosting - Storage': f"Hosting - Storage: {data_model['Firebase Hosting']['Hosting - Storage']['Complements']}"
                             })

        elif request_data['But'] == 'Site base sur wordpress':
            if request_data['Nombres_utilisateurs'] == '1-10000' and request_data['Exp'] == 'Oui':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 10
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 36
                price_cdn = data_model['Cloud CDN']['Prix'] * 3000
                final_price = round(price_vm + price_disk + price_cdn, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '1-10000' and request_data['Exp'] == 'Non':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 10
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 36
                final_price = round(price_vm + price_disk, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '10000-100000' and request_data['Exp'] == 'Oui':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 50
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 180
                price_cdn = data_model['Cloud CDN']['Prix'] * 15000
                final_price = round(price_vm + price_disk + price_cdn, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '10000-100000' and request_data['Exp'] == 'Non':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 50
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 180
                final_price = round(price_vm + price_disk, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '100000-500000' and request_data['Exp'] == 'Oui':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 250
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 900
                price_cdn = data_model['Cloud CDN']['Prix'] * 75000
                final_price = round(price_vm + price_disk + price_cdn, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '100000-500000' and request_data['Exp'] == 'Non':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 250
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 900
                final_price = round(price_vm + price_disk, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '500000+' and request_data['Exp'] == 'Oui':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 500
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 1800
                price_cdn = data_model['Cloud CDN']['Prix'] * 150000
                final_price = round(price_vm + price_disk + price_cdn, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}",
                             'Cloud CDN': f"Cloud CDN: {data_model['Cloud CDN']['Complements']}"
                             })

            elif request_data['Nombres_utilisateurs'] == '500000+' and request_data['Exp'] == 'Non':
                price_vm = data_model['Compute Engine']['Instance de VM - e2-small']['Prix'] * 500
                price_disk = data_model['Compute Engine']['Disque persistant standard']['Prix'] * 1800
                final_price = round(price_vm + price_disk, 2)
                dict.update({'price': f"{final_price}",
                             'service': "Service: Compute Engine",
                             'Instance de VM': f"Instance de VM - e2-small: {data_model['Compute Engine']['Instance de VM - e2-small']['Complements']}",
                             'Disque': f"Disque persistant standard: {data_model['Compute Engine']['Disque persistant standard']['Complements']}"
                             })


        if request_data['Maintenance'] == 'Externe':
            final_price = round(final_price + ((final_price * 20)/100),2)
            dict['price'] = f"{final_price}"
            dict['maintenance'] = f"Maintenance: {data_model['Maintenance']['Complements']}"

        return jsonify(dict)


    else:
        # return jsonify({'Nombres_utilisateurs': request_data['Nombres_utilisateurs']})
        return ''

if __name__=="__main__":
    app.run(debug=True, port=5000)