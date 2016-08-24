from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
## Common Gateway Interface
import cgi

## Import Database Schemas
from database_setup import Base, Restaurant, MenuItem

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

## Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            ## Retrieve all restaurants
            if self.path.endswith('/restaurants'):
                restaurants = session.query(Restaurant).all()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<a href='/restaurants/new'>Creat a New Restaurant</a>"
                output += "</br></br>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    output += "<a href='/restaurants/%s/edit'>Edit</a>" % restaurant.id
                    output += "</br>"
                    output += "<a href='/restaurants/%s/delete'>Delete</a>" % restaurant.id
                    output += "</br></br>"
                output += "</body></html>"
                self.wfile.write(output)
                # print output
                return

            ## Create new restaurant
            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1> Create A New Restaurant </h1>"
                output += """<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>
                            <input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>
                            <input type='submit' value='Submit'>
                            </form>"""
                output += "</body></html>"
                self.wfile.write(output)
                return

            ## Edit Restaurant
            if self.path.endswith('/edit'):
                restaurantID = self.path.split('/')[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=restaurantID).one()
                if restaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1> Edit Restaurant </h1>"
                    output += "<h2>%s</h2>" % restaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantID
                    output += "<input name='newRestaurantName' type='text' placeholder='%s'>" % restaurantQuery.name
                    output += "<input type='submit' value='Submit'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)

            # Delete Restaurant
            if self.path.endswith('/delete'):
                restaurant_id = self.path.split('/')[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=restaurant_id).one()

                if restaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1> Delete Restaurant? </h1>"
                    output += "<h2>%s</h2>" % restaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurant_id
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    # output += "<button href='/restaurants'>Cancel</button>"
                    output += "</body></html>"

                    self.wfile.write(output)
                    return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            ## Create ne restaurant
            if self.path.endswith('/restaurants/new'):
                ## Extract information from the form
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    ## Redirects to restaurants page
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            ## Edit Restaurant(Post)
            if self.path.endswith('/edit'):
                ## Extract information from the form
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantID = self.path.split('/')[2]

                    restaurantQuery = session.query(Restaurant).filter_by(id=restaurantID).one()
                    print restaurantQuery
                    if restaurantQuery != []:
                        restaurantQuery.name = messagecontent[0]
                        session.add(restaurantQuery)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        ## Redirects to restaurants page
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            ## Delete Restaurant
            if self.path.endswith('/delete'):
                restaurantID = self.path.split('/')[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=restaurantID).one()

                if restaurantQuery:
                    session.delete(restaurantQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    ## Redirects to restaurants page
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Making Magic On Port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopped web server..."
        server.socket.close()

## makes sure the server only runs if
## the script is executed directly from
## the Python interpreter and not
## used as an imported module.
if __name__ == '__main__':
    main()