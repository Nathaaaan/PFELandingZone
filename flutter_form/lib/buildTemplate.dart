import 'package:flutter/material.dart';

class buildTemplate extends StatefulWidget {
  String answer = '';
  final Function callbackFunction;

  buildTemplate({Key? key, required this.answer, required this.callbackFunction}) : super(key: key);

  @override
  _buildTemplateState createState() => _buildTemplateState();
}

class _buildTemplateState extends State<buildTemplate> {
  final List<String> template = ['Site web','BlockChain'];

  @override
  Widget build(BuildContext context) {
    return DropdownButtonFormField<String>(
      decoration: InputDecoration.collapsed(hintText: widget.answer),
      onChanged: (String? newValue) {
        setState(() {
          widget.answer = newValue!;
          widget.callbackFunction(widget.answer);
        });
      },
      validator: (value) {
        if (value == null) {
          return 'champs requis';
        }
        return null;
      },
      items: template.map((templates){
        return DropdownMenuItem(
          value: templates,
          child: Text(templates),
        );
      }).toList(),

    );
  }
}
