from flask import Flask, request, render_template
import sqlalchemy
from sqlalchemy.sql import text
from datetime import datetime

app = Flask(__name__)
db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/wcoding")

#HOMEPAGE GET ARTICLES/COMMENTS
#==================================================================================================
@app.route("/", methods = ['POST', 'GET'])
def homepage(): 
    if request.form.get("activity_action") == "writearticle":
        with db.begin() as conn:
            res = conn.execute(text("INSERT INTO articles (title, tag, author, content, created_at) VALUES (:title, :tag, :author, :content, NOW())"), 
                {
                    "title": request.form.get("title"),
                    "tag": request.form.get("tag"),
                    "author": request.form.get("author"),
                    "content": request.form.get("content")
                }
            )
    elif request.form.get("activity_action") == "writecomment":
        with db.begin() as conn:
            res = conn.execute(text("INSERT INTO comments (article_id, author, comment, created_at) VALUES (:article_id, :author, :comment, NOW())"), {
                "article_id":request.form.get("article_id"),
                "author": request.form.get("author"),
                "comment": request.form.get("comment")
            })
    with db.begin() as conn:
        article_res = conn.execute(text("SELECT * FROM articles ORDER BY created_at DESC"))
        comment_res = conn.execute(text("SELECT * FROM comments"))
        return render_template("index.html", article_res=article_res, comment_res=comment_res.all())

    
#POST ARTICLE
#===================================================================================================    
@app.post("/writearticle")
def writearticle():
    with db.begin() as conn:
        res = conn.execute(text("INSERT INTO articles (title, tag, author, content, created_at) VALUES (:title, :tag, :author, :content, NOW())"), 
            {
                "title": request.form.get("title"),
                "tag": request.form.get("tag"),
                "author": request.form.get("author"),
                "content": request.form.get("content")
            }
        )
        print(res)
        return "OK"
    
#POST COMMENT 
#===================================================================================================
@app.post("/writecomment")
def writecomment():
    with db.begin() as conn:
        res = conn.execute(text("INSERT INTO comments (article_id, author, comment, created_at) VALUES (:article_id, :author, :comment, NOW())"), {
            "article_id":request.form.get("article_id"),
            "author": request.form.get("author"),
            "comment": request.form.get("comment")
        })
    return "OK"

    
