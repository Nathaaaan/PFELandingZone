import 'dart:convert';
import 'dart:io';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_form/buildSiteQuestion.dart';
import 'package:json_annotation/json_annotation.dart';
import 'package:http/http.dart' as http;
import 'package:elastic_client/elastic_client.dart' as elastic;
import './buildTemplate.dart';
import './buildSiteQuestion.dart';
import 'package:intl/intl.dart';
import './imageBanner.dart';
import './dashboard_page.dart';

@JsonSerializable()
class FormScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return FormScreenState();
  }
}

@JsonSerializable()
class FormScreenState extends State<FormScreen> {

  String date = DateTime.now().toString();
  String _nbUsers = '1-10000';
  String _template = '';
  String _goal = 'Ecommerce';
  String _expUser = 'Oui';
  String _creation = 'Interne';
  String _maintenance = 'Interne';
  String price = '0.0';
  Map decoded ={};
  List<String> list = [];

  callback(varNbUsers){
    setState(() {
      _nbUsers = varNbUsers;
    });
  }

  callbackTemplate(varTemplate){
    setState(() {
      _template = varTemplate;
    });
  }
  callbackGoal(varGoal){
    setState(() {
      _goal = varGoal;
    });
  }

  callbackCreation(varCreation){
    setState(() {
      _creation = varCreation;
    });
  }

  callbackMaintenance(varMaintenance){
    setState(() {
      _maintenance = varMaintenance;
    });
  }

  callbackExpUser(varExpUser){
    setState(() {
      _expUser = varExpUser;
    });
  }

  callbackList(varList){
    setState(() {
      list = varList;
    });
  }

  Map<String, dynamic> toMap() {
    return {
      "question1": _nbUsers,
      "question2": _template,
    };
  }

  PostData() async{
    try {
      Map jsonBody = {};
      if(_template == 'Site web'){
        jsonBody = {
          "Date": date,
          "Modele_application": _template,
          "Nombres_utilisateurs": _nbUsers,
          "But": _goal,
          "Exp": _expUser,
          "Creation": _creation,
          "Maintenance": _maintenance
        };
      }
      else{
        jsonBody = {
          "Date": date,
          "Modele_application": _template
        };
      }
      var response = await http.post(
          Uri.parse("http://127.0.0.1:5000/test"),
          /**headers: {
            "Access-Control-Allow-Origin": "*", // Required for CORS support to work
            "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Content-Type": "application/json"
          },**/
          headers: {"Content-Type": "application/json"},
          body: jsonEncode(jsonBody)
      );

      decoded = json.decode(response.body) as Map<String, dynamic>;

      //return decoded['Nombres_utilisateurs'];
      setState(() {
        price = decoded['price'];
        decoded.forEach((k, v) {
          if (k != 'price') {
            list.add(v);
          }

        });
        //list = list.reversed.toList();
      });
      print(list);
    } catch(e) {
      print(e);
    }
  }

/**  getData() async{
    var responseGet = await http.get(
        Uri.parse("http://127.0.0.1:5000/test"));

    final decoded = json.decode(responseGet.body) as Map<String, dynamic>;

    setState(() {
      getUser = decoded["Nombres_utilisateurs"];
    });

  }**/

  PostId() async{
    try {
      Map jsonBody = {"id" : "QFlsHX8BytuWLXqXKR3P"};
      var response = await http.post(
          Uri.parse("http://127.0.0.1:5000/test"),
          /**headers: {
              "Access-Control-Allow-Origin": "*", // Required for CORS support to work
              "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
              "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
              "Content-Type": "application/json"
              },**/
          headers: {"Content-Type": "application/json"},
          body: jsonEncode(jsonBody)
      );

      final decoded = json.decode(response.body) as Map<String, dynamic>;
      //return decoded['Nombres_utilisateurs'];
      setState(() {
        price = decoded['unitPrice'];
      });
    } catch(e) {
      print(e);
    }
  }


  Future<void> sendData() async {
    final transport = elastic.HttpTransport(url: 'http://localhost:9200/');
    final client = elastic.Client(transport);

    if(_template == 'Site web'){
      await client.updateDoc(
        index: 'questions',
        type: '_doc',
        id: 'my_id_1',
        doc: {
          "Date": date,
          "Modele_application": _template,
          "Nombres_utilisateurs": _nbUsers,
          "But": _goal,
          "Exp": _expUser,
          "Creation": _creation,
          "Maintenance": _maintenance
        },
      );
    }

    else {
      await client.updateDoc(
        index: 'questions',
        type: '_doc',
        id: 'my_id_1',
        doc: {
          "Date": date,
          "Modele_application": _template
        },
      );
    }
    await transport.close();
    print("done");

  }

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text(
            "Estimacloud",
            style: TextStyle(
              fontFamily: 'BebasNeue',
              fontSize: 50,
            ),
          ),
          centerTitle: true,
          backgroundColor: Color.fromRGBO(123,44,191,1.0),

        ),
        body: SingleChildScrollView(
          child: Container(
            margin: EdgeInsets.fromLTRB(24,80,24,0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    buildPresentation(),
                    ImageBanner("assets/images/idea.png")
                  ],
                ),
                Text(
                  "Quelle est votre idée?",
                  style: TextStyle(
                    fontFamily: 'Montserrat',
                    fontSize: 40,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Container(
                    margin: EdgeInsets.fromLTRB(0, 30, 0, 0),
                    padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                    height: 900,
                    decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(15),
                        color: Colors.white,
                        boxShadow: [
                          BoxShadow(
                            color: Colors.grey.shade500,
                            offset: Offset(4.0, 4.0),
                            blurRadius: 15.0,
                            spreadRadius: 1.0,
                          ),
                        ]
                    ),
                    child: Form(
                      key: _formKey,
                      child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children:<Widget>[
                            const Text(
                              "Quelle est votre modèle d'application?",
                              style: TextStyle(
                                fontFamily: 'Montserrat',
                                fontSize: 18,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            const SizedBox(height:20),
                            buildTemplate(answer: _template, callbackFunction: callbackTemplate),
                            const SizedBox(height:20),
                            if(_template == 'Site web') buildSiteQuestion(nbUsers: _nbUsers, goal: _goal, expUser: _expUser, creation: _creation, maintenance: _maintenance, callbackUsers: callback, callbackGoal: callbackGoal, callbackExpUser: callbackExpUser, callbackCreation: callbackCreation, callbackMaintenance: callbackMaintenance),
                            const SizedBox(height:50),
                            RaisedButton(
                              child: const Text(
                                "Envoyer",
                                style: TextStyle(
                                  color: Color.fromRGBO(123,44,191,1.0),
                                  fontFamily: 'Montserrat',
                                  fontSize:16,
                                ),
                              ),

                              onPressed: () async {
                                if (_formKey.currentState!.validate()) {
                                  _formKey.currentState!.save();
                                  //Map<String, dynamic> formMap = this.toMap();
                                  //var json = jsonEncode(formMap);
                                  //print(json.toString());
                                  //f.writeAsStringSync(json);
                                  await PostData();
                                  //await PostId();
                                  //await Future.delayed(Duration(seconds: 3));
                                  //getData();
                                  await Navigator.of(context)
                                      .push(
                                      MaterialPageRoute(
                                          builder: (context) => dashboard(price: price, list: list)
                                      )
                                  );
                                  setState(() {
                                    list.clear();
                                  });
                                  //sendData();
                                  //print(_nbUsers);
                                  //print(_template);
                                  //print(_goal);
                                  //print(_target);
                                  //print(_international);
                                  //print(_response);
                                  //print(_maintenance);
                                }
                              },
                            )
                          ]
                      ),

                    )

                ),
              ],
            ),
          ),
        )
    );
  }

  Widget buildPresentation() {
    return Flexible(
      child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Bienvenue,',
          style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: 50,
              fontWeight: FontWeight.bold,
              color: Color.fromRGBO(123,44,191,1.0)
          ),
        ),
        Text(
          "ESTIMACLOUD est le fruit de la collaboration entre des étudiants d'Efrei et l'entreprise OnePoint. Cet outil vous donnera une estimation du prix de votre idée de projet.",
          style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: 25,
              color: Colors.grey.shade600
          ),
        )
      ],
    )
    );
  }
}
