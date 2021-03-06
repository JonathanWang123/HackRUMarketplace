# RUConnect

# Description
-RU connect is a fully realized online marketplace designed by and for Rutgers University students.  
-Provides students an intuitive means of selling and buying the various commodities that only students need.  

# Frontend
-We used React.js to create a web app for users to interact with and post items on the marketplace.  
-Users can register accounts to post items on the site, which is stored in a Mongo database.  
-To communicate with our user and items database for login/display, we used GET and POST requests to our backend.  
-Users can customize their profile and display socials and information.  
-Items are marked with tags which can be searched for and specified by the user.  

# Backend
-We utilized Python with Flask and MongoDB api to host our backend server and build user and item functionality.  
-Item search implements tag keyword matching as well as string similarity algorithms to bring the user the most  related listings.  
-We implemented Google Cloud Vision API to generate tags for listings based on their product images.  
-User functionality implements customization of user profile and the ability to change/update information fields.  
-Item functionality similarly allows users to create, edit and delete their listings. 

# Inspiration
-This idea was inspired by a team member who was having trouble selling his Expos textbook. We knew about the traditional methods of online transaction like ebay or amazon or even facebook post listings. However we thought that the traditional methods were often inconvenient and cluttered with unrelated content or other extraneous listings. Our RU Connect marketplace improves upon the limitations of traditional marketplaces by focusing on campus Rutgers students to deliver a straightforward, convenient solution to their marketing needs. 

# Challenges we ran into
-Advanced search engines use methods like stem matching and natural language queries to optimize searching to return the most relevant content. Implementing those methods however, we felt were unsuited for a 24 hour hackathon.  
-Connecting the front end and back end seamlessly was definitely a challenge that we're proud to have pulled off, taking up a sizeable chunk of our time debugging.

# Accomplishments that we're proud of
-Building a fully fledged product was incredibly satisfying and integrating back end with front end.  
-Advancing upon exact keyword-tag matching, we thought to implement a string similarity algorithm to scan through the title and descriptions of the items in order to include more relevant items in the search query.  
-We utilized Google Cloud Vision API to interpret product images and match products automatically with tags through machine learning.
 
# What's next for RU Connect?
-We'd love to continue working on RU Connect to maybe one day deliver a robust marketplace service for realtime use with Rutgers students. Some features that we would like to implement in the future is a chat feature and a more refined searching method.

# Authors and acknowledgment
Jeffrey Yang, Jonathan Wang, Justin Chen, Rahul Trivedi
