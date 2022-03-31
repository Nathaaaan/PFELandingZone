import 'package:flutter/material.dart';
import './form_screen.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Form',
      theme: ThemeData(
        scaffoldBackgroundColor: Colors.white,
      ),
      home: FormScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
