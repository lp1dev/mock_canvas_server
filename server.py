#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"


@app.route("/api/v1/courses/")
def courses():
        print(request, request.headers, request.get_data())
        course1 = {
                "id":1,
                "name":"'\"><script>alert(1)</script>TestCourse",
        }
        courses = [course1]
        return jsonify(courses)
        #return jsonify(dict(content=courses))

@app.route("/api/v1/courses/<course>/modules")
def modules(course):
        print(request, request.headers, request.get_data())
        module1 = {
                
        }
        return jsonify([{},{},{}])

@app.route("/api/v1/courses/<course>/quizzes")
def quizzes(course):
        print(request, request.headers, request.get_data())
        return jsonify([{"id":1, "title":"testQuizz1", "description":"test desc 1 <script>alert(1)</script>", "html_url":"https://test"},{"id":2,"title":"testQuizz2","description":"testDesc2 <script>alert(1)</script>", "html_url":"https://test"}])

@app.route("/api/v1/courses/1/quizzes/<quizz>")
def quizz(quizz):
        print(request, request.headers, request.get_data())
        return jsonify({"id":quizz, "title":"testQuizz1", "description":"test desc 1 <script>alert(1)</script>", "html_url":"https://test"})


@app.route("/api/v1/courses/1/quizzes/<quizz>/questions")
def questions(quizz):
        print(request, request.headers, request.get_data())
        answers = [{"id":1,"weight":1,"text":"test content","comments":"test comment"}, {"id":2,"weight":0,"text":"test content","comments":"test comment"}]
        return jsonify([{"id":1, "question_name":"test1","question_text":"Hello","quizz_id":1,"position":1,"question_type":"fill_in_multiple_blanks_question","answers":answers},{"id":2, "question_name":"test2", "question_text":"test","quizz_id":2,"position":2,"question_type":"multiple_choice_question", "answers":answers}])        

@app.route("/api/v1/courses/<course>/users")
def users(course):
        print(request, request.headers, request.get_data())
        return jsonify([{"id":1, "name":"test1"},{"id":2, "name":"test2"}])        
        
        
app.run(threaded=True)
