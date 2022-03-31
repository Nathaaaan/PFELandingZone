import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ServiceItem extends StatelessWidget {
  String text;
  ServiceItem({Key? key, required this.text}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Center(
      /**height: 110,
      width: 200,
      margin: EdgeInsets.fromLTRB(10,0,0,0),
      padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
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
      ),**/
      child: Column(
        children: [
          Text(
            text,
            style: TextStyle(
                fontFamily: 'Montserrat',
                fontSize: 20
            ),
          ),
          SizedBox(height:40)
        ],
      ),
    );
  }
}
