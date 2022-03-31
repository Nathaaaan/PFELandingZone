import 'package:flutter/material.dart';

class buildSiteQuestion extends StatefulWidget {
  String nbUsers = '';
  String goal = '';
  String expUser= '';
  String creation = '';
  String maintenance = '';

  final Function callbackUsers;
  final Function callbackGoal;
  final Function callbackExpUser;
  final Function callbackCreation;
  final Function callbackMaintenance;

  buildSiteQuestion({Key? key, required this.nbUsers, required this.goal, required this.expUser, required this.creation, required this.maintenance, required this.callbackUsers, required this.callbackGoal, required this.callbackExpUser, required this.callbackCreation, required this.callbackMaintenance}) : super(key: key);

  @override
  _buildSiteQuestionState createState() => _buildSiteQuestionState();
}

class _buildSiteQuestionState extends State<buildSiteQuestion> {
  final List<String> users = ['1-10000','10000-100000','100000-500000','500000+'];
  final List<String> listgoal = ['Ecommerce','Site vitrine','Site base sur wordpress'];
  final List<bool> selectedExp = [true,false];
  final List<String> listcreation = ['Interne','Externe'];
  final List<String> listmaintenance = ['Interne','Externe'];
  final List<bool> selectedInter = [true,false];
  final List<String> choice = ['Oui','Non'];

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Nombres d'utilisateurs par jours?",
            style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height:20),
          DropdownButtonFormField<String>(
          decoration: InputDecoration.collapsed(hintText: widget.nbUsers),
          onChanged: (String? newValue) {
            setState(() {
              widget.nbUsers = newValue!;
              widget.callbackUsers(widget.nbUsers);
            });
          },
          validator: (value) {
            if (value == null) {
              return 'champs requis';
            }
            return null;
          },
          items: users.map((user){
            return DropdownMenuItem(
              value: user,
              child: Text(user),
            );
          }).toList(),
          ),
          SizedBox(height: 20),
          Text(
            "Quelle est le but de votre site?",
            style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          SizedBox(height: 20),
          DropdownButtonFormField<String>(
            decoration: InputDecoration.collapsed(hintText: widget.goal),
            onChanged: (String? newValue) {
              setState(() {
                widget.goal = newValue!;
                widget.callbackGoal(widget.goal);
              });
            },
            validator: (value) {
              if (value == null) {
                return 'champs requis';
              }
              return null;
            },
            items: listgoal.map((goals){
              return DropdownMenuItem(
                value: goals,
                child: Text(goals),
              );
            }).toList(),
          ),
          SizedBox(height: 20),
          Text(
            "L'expérience utilisateur est-elle un point central du parcours souhaité?",
            style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          SizedBox(height: 20),
          ToggleButtons(
            isSelected: selectedExp,
            fillColor: Color.fromRGBO(123,44,191,1.0),
            selectedColor: Colors.white,
            renderBorder: false,
            borderRadius: BorderRadius.circular(30),
            children: <Widget>[
              Text(
                choice[0],
                style: TextStyle(
                    fontFamily: 'Montserrat',
                    fontSize:15,
                    fontWeight: FontWeight.bold
                ),
              ),
              Text(
                choice[1],
                style: TextStyle(
                    fontFamily: 'Montserrat',
                    fontSize:15,
                    fontWeight: FontWeight.bold
                ),
              ),
            ],
            onPressed: (int newIndex) {
              setState(() {
                for (int index = 0; index < selectedInter.length; index++){
                  if(index == newIndex) {
                    selectedExp[index] = true;
                    widget.expUser = choice[index];
                    widget.callbackExpUser(widget.expUser);
                  } else {
                    selectedExp[index] = false;
                  }
                }
              });
            },
          ),
          SizedBox(height: 20),
          Text(
            "Préférez-vous une création de votre site en interne ou en externe?",
            style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          SizedBox(height: 20),
          DropdownButtonFormField<String>(
            decoration: InputDecoration.collapsed(hintText: widget.creation),
            onChanged: (String? newValue) {
              setState(() {
                widget.creation = newValue!;
                widget.callbackCreation(widget.creation);
              });
            },
            validator: (value) {
              if (value == null) {
                return 'champs requis';
              }
              return null;
            },
            items: listcreation.map((element){
              return DropdownMenuItem(
                value: element,
                child: Text(element),
              );
            }).toList(),
          ),
          SizedBox(height: 20),
          Text(
            "Préférez-vous une maintenance de votre site en interne ou en externe?",
            style: TextStyle(
              fontFamily: 'Montserrat',
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          SizedBox(height: 20),
          DropdownButtonFormField<String>(
            decoration: InputDecoration.collapsed(hintText: widget.maintenance),
            onChanged: (String? newValue) {
              setState(() {
                widget.maintenance = newValue!;
                widget.callbackMaintenance(widget.maintenance);
              });
            },
            validator: (value) {
              if (value == null) {
                return 'champs requis';
              }
              return null;
            },
            items: listmaintenance.map((element){
              return DropdownMenuItem(
                value: element,
                child: Text(element),
              );
            }).toList(),
          ),

        ],
      ),
    );
  }
}
