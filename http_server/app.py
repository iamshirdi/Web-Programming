from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import os
import json
import secrets
import string
import io


HOST_NAME = 'localhost'
PORT_NUMBER = 8080

database={}
database_scores={}
expire=600


class SessionHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        routes = {
            "login":   self.login,
            "highscorelist":   self.highscorelist

        }
        try:
            response = 200
            print(self.path)
            route=self.path[1:].split('/')
            user_id=int(route[0])
            if not 0 <=user_id <2**31:
                raise ValueError('not unsigned 31bit')

            score_id=user_id

            #create new session if user not there
            if user_id not in database.keys():
                sessionkey=None
            else:
                sessionkey=database[user_id][0]


            if route[1]=='login':
                content = routes[route[1]](user_id,sessionkey)

                #expiry token remove from database
                if time.time()-database[user_id][1]>expire:
                    sessionkey=None
                    database.pop(user_id)
                    # content=json.dumps({'user': 'user_id', 'session': 'expired reload to generate new'})
                    content=routes[route[1]](user_id,sessionkey)

        except:
            #browser also requesting favicon
            response = 404
            content = "Not Found"
            return content

        if route[1]=="highscorelist":
            score_id=user_id
            content = routes[route[1]](score_id)

            try:
                print(content)
            except:
                self.send_response(404)

        self.send_response(response)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(content.encode(encoding='utf_8'))
        return


    def do_POST(self):
        try:
            sc=self.path[1:].split('/')
            level=sc[0]
            sess_key=sc[1].strip('score?sessionkey=')
            print(sess_key)
            if not 0 <=int(level) <2**31:
                raise ValueError('not valid level')
        except:
            response = 404
            content = "Not Found"
            return content

        for key_user,value in database.items():

            if value[0]==sess_key:
                #expiry check
                if time.time()-database[key_user][1]>expire:
                    sessionkey=None
                    database.pop(key_user)
                    content_post=json.dumps({'user': 'user_id', 'session': 'expired request to generate new'})
                    self.wfile.write(content_post.encode(encoding='utf_8'))
                    return

                content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
                data  = self.rfile.read(content_length)  # <--- Gets the data
                post_data=json.loads(data)
                score_value=post_data['score']

                try:
                    if not 0 <=int(score_value) <2**31:
                        raise ValueError('not valid Score')
                except:
                    response = 404
                    content = "Not Found"
                    return content

                try:
                    database_scores[level]
                except:
                    database_scores[level]=[]
                    pass

                    #removes previous scores of user if new high score
                for index,i in enumerate(database_scores[level]):

                    try:
                        #list exception if user  not there
                        if i['user']==key_user:
                            if i['score']<post_data['score']:
                                print(index)
                                database_scores[level].pop(index)
                            else: #dont add to database ignore since not highscore
                                self.send_response(200)
                                self.end_headers()
                                json_str2=json.dumps({'score':score_value})
                                self.wfile.write(json_str2.encode(encoding='utf_8'))
                                return
                    except:
                        continue

                #adds new high scores of new and different users
                if len(database_scores[level])<16:
                    database_scores[level].append({"user":key_user,"score":score_value})
                else:
                    for index2,i2 in enumerate(database_scores[level]):
                        if i2['score']<post_data['score']:
                            database_scores[level].pop(index2)
                            database_scores[level].append({"user":key_user,"score":post_data[score]})


                self.send_response(200)
                self.end_headers()
                json_str2=json.dumps({'score':score_value})
                self.wfile.write(json_str2.encode(encoding='utf_8'))
                return
            #if not valid user
        response = 404
        content = "Not Found session key"
        return content


    def highscorelist(self,score_id):
        try:
            h_list=database_scores[str(score_id)]
            h_list.sort(key=lambda s: (s['score'],-s['user']), reverse=True)
        except:
            h_list=[]
        highscorelist=json.dumps(h_list)
        return highscorelist

    def login(self,user_id,sessionkey):
        # print(self.path)
        if sessionkey==None:
            s=time.time()
            alphabet = string.ascii_uppercase + string.digits
            sessionkey = ''.join(secrets.choice(alphabet) for i in range(7))
            database[user_id]=[sessionkey,s]

        json_str=json.dumps({'user': database[user_id][0]})

        return json_str


if __name__ == '__main__':

    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), SessionHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
