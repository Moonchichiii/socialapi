## API Endpoint Testing

### Test Cases

| Testcase                                                                     | Expected Result                                                                                             | Test Result | Screenshots                                                              |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------ |
| **Authentication**                                                           |                                                                                                             |             |                                                                          |
| _[register](https://socialapi-ce69e07a68e6.herokuapp.com/api/register/)_| ||
| _[login](https://socialapi-ce69e07a68e6.herokuapp.com/api/login/)_| ||
| _[logout](https://socialapi-ce69e07a68e6.herokuapp.com/api/logout/)_     |                                                                                                             |             |
|Register                                                                     |	returns 201 response: new user is registered with access and refresh token |pass||
|Login                                                                        |	returns 200 response: user is logged in with access and refresh token | pass ||
|Logout                                                                       |	returns 205 response: user is logged out and refresh token is blacklisted |	pass	||
|Current User                                                                 |	returns 200 response: returns the profile of the requesting user |	||	
|Current User (Unauthenticated)                                               |	returns 403 error: authentication credentials were not provided |		||

***Profiles***
 _[Login/register/logout](https://socialapi-ce69e07a68e6.herokuapp.com/api/profiles/)_ 
|Profile List|		
|GET Unauthenticated|	returns 403 error: authentication credentials were not provided		|||
GET Authenticated|	returns 200 response: a list of all the profiles		|| |
POST, PUT, DELETE	Not provided		|||

|Profile Detail			||||
|GET Unauthenticated|	returns 403 error: authentication credentials were not provided		|||
|GET Authenticated|	returns 200 response: the profile specified by id		|||
|POST, PUT, DELETE|	Not provided		|||

| **Posts**                                                                    |                                                                                                             |             |                                                                          |
| _[Post List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/)_       |                                                                                                             |             |
| GET Unauthenticated                                                          | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| POST Authenticated                                                           | returns 201 response: allows authenticated users to create posts                                            |             |                                                                          |
| POST Unauthenticated                                                         | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| _[Post Detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/{id}/)_ |                                                                                                             |             |
| GET Unauthenticated                                                          | returns 403 error: authentication credentials were not                                                              |             |                                                                          |
| GET Authenticated                                                            | returns 200 response: the post specified by id                                                              |             |                                                                          |
| PUT Authenticated Owner                                                      | returns 200 response: allows the owner to update the post                                                   |             |                                                                          |
| PUT Authenticated Not Owner                                                  | returns 403 error: user is not the owner of the post                                                        |             |                                                                          |
| PUT Unauthenticated                                                          | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| DELETE Authenticated Owner                                                   | returns 204 response: post is deleted                                                                       |             |                                                                          |
| DELETE Authenticated Not Owner                                               | returns 403 error: user is not the owner of the post                                                        |             |                                                                          |
| DELETE Unauthenticated                                                       | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/{post_id}/post-likes/)_ |                                                                                                             |             |
| GET Unauthenticated                                                          | returns 200 response: a list of profiles that liked the specified post                                      |             |                                                                          |
| GET Authenticated                                                            | returns 200 response: a list of profiles that liked the specified post                                      |             |                                                                          |
| POST Authenticated                                                           | returns 201 or 204 response: allows authenticated users to like the specified post                          |             |                                                                          |
| POST Unauthenticated                                                         | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| DELETE Authenticated                                                         | returns 200 response: allows authenticated users to unlike the specified post                               |             |                                                                          |
| DELETE Unauthenticated                                                       | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| _[Liked Post List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/liked-posts/)_ |                                                                                                             |             |
| GET Authenticated                                                           | returns 200 response: a list of all posts liked by the authenticated user                                   |             |                                                                          |
| GET Unauthenticated                                                         | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |


| **Comments**                                                                 |                                                                                                             |             |                                                                          |
| _[Comment List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/{post_id}/comments/)_ |                                                                                                             |             |
| GET Unauthenticated                                                         | returns 403 error: authentication credentials were not                                      |             |                                                                          |
| GET Authenticated                                                           | returns 200 response: a list of all the comments from a specified post                                      |             |                                                                          |
| POST Authenticated                                                          | returns 201 response: allows authenticated users to create comments                                         |             |                                                                          |
| POST Unauthenticated                                                        | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| _[Comment Detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/{post_id}/comments/{id}/)_ |                                                                                                             |             |
| GET Unauthenticated                                                         | returns 200 response: the comment specified by id                                                           |             |                                                                          |
| GET Authenticated                                                           | returns 200 response: the comment specified by id                                                           |             |                                                                          |
| PUT Authenticated Owner                                                     | returns 200 response: allows the owner to update the comment                                                |             |                                                                          |
| PUT Authenticated Not Owner                                                 | returns 403 error: user is not the owner of the comment                                                     |             |                                                                          |
| PUT Unauthenticated                                                         | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| DELETE Authenticated Owner                                                  | returns 204 response: comment is deleted                                                                    |             |                                                                          |
| DELETE Authenticated Not Owner                                              | returns 403 error: user is not the owner of the comment                                                     |             |                                                                          |
| DELETE Unauthenticated                                                      | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |

| **Followers**                                                                |                                                                                                             |             |                                                                          |
| _[Follower/unfollow](https://socialapi-ce69e07a68e6.herokuapp.com/api/followers/)_ |                                                                                                             |             |
| GET Unauthenticated                                                          | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| GET Authenticated                                                            | returns 200 response: a list of followers and following profiles                                            |             |                                                                          |
| POST Authenticated                                                           | returns 201 or 204 response: allows authenticated users to follow/unfollow profiles                         |             |                                                                          |
| POST Unauthenticated                                                         | returns 403 error: authentication credentials were not provided                                             |             |                                                                          |
| PUT, DELETE                                                                  | Not provided                                                                                                |             |                                                                          |

| 