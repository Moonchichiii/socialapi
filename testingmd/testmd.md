## API Endpoint Testing

### Test Cases

| Endpoint | Testcase | Expected Result | Test Result | Screenshots |
| -------- | -------- | --------------- | ----------- | ----------- |
| **Authentication** | | | | |
| _[register](https://socialapi-ce69e07a68e6.herokuapp.com/api/register/)_ | Register | returns 201 response: new user is registered with access and refresh token | pass | [Screenshot](testingmd/images/auth/Screenshot%202024-05-01%20113635.png) |
| _[login](https://socialapi-ce69e07a68e6.herokuapp.com/api/login/)_ | Login | returns 200 response: user is logged in with access and refresh token | pass | [Screenshot](<images/auth/Screenshot 2024-05-01 113722.png>)  |
| _[logout](https://socialapi-ce69e07a68e6.herokuapp.com/api/logout/)_ | Logout | returns 205 response: user is logged out and refresh token is blacklisted | pass | [Screenshot](images/auth/logout.png) |
| _[current user](https://socialapi-ce69e07a68e6.herokuapp.com/api/current-user/)_ | Current User | returns 200 response: returns the profile of the requesting user | pass | [Screenshot](images/auth/currentuser.png) |
| _[current user](https://socialapi-ce69e07a68e6.herokuapp.com/api/current-user/)_ | Current User (Unauthenticated) | returns HTTP 401 Unauthorized  error: authentication credentials were not provided | pass |[Screenshot](images/auth/currentusernoauth401.png) |
| **Profiles** | | | | |
| _[profiles](https://socialapi-ce69e07a68e6.herokuapp.com/api/profiles/)_ | Profile List (GET Unauthenticated) | returns HTTP 401 Unauthorized error: authentication credentials were not provided | pass | [Screenshot](images/profile/ProfileGetNotAuthenticated401.png) |
| _[profiles](https://socialapi-ce69e07a68e6.herokuapp.com/api/profiles/)_ | Profile List (GET Authenticated) | returns 200 response: a list of all the profiles | pass | [Screenshot](images/profile/ProfilesGetAuth.png) |
| _[profiles](https://socialapi-ce69e07a68e6.herokuapp.com/api/profiles/)_ | Profile List (POST, PUT, DELETE) | Not provided | | |
| _[profile detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/profiles/1/)_ | Profile Detail (GET Unauthenticated) | returns 403 error: authentication credentials were not provided | pass | [Screenshot](images/profile/ProfileDetailGetNotAuthenticated403.png) |
| _[profile detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/profiles/1/)_ | Profile Detail (GET Authenticated) | returns 200 response: the profile specified by ID | pass | [Screenshot](images/profile/ProfileDetailGetAuthenticated200.png) |
| _[profile detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/profiles/1/)_ | Profile Detail (POST, PUT, DELETE) | Not provided | | |
| **Posts** | | | | |
| _[Post List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/)_ | Post List (GET Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/posts/getPostsNoAuth.png) |
| _[Post List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts//)_ | Post List (GET Authenticated) | Returns 200 response: a list of posts | Pass | [Screenshot](images/posts/getPostsAuthenticated.png) |
| _[Post List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/)_ | Post List (POST Authenticated) | Returns 201 response: allows authenticated users to create posts | Pass |[Screenshot](images/posts/postPostsAuth.png)  |
| _[Post List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/)_ | Post List (POST Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/posts/postPostsNoAuth.png) |
| _[Post Detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/)_ | Post Detail (PUT Authenticated Owner) | Returns 200 response: allows the owner to update the post | Pass | [Screenshot](images/posts/PutPostsAuthOk.png)  |
| _[Post Detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/)_ | Post Detail (PUT Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/posts/putPostsNoAuth401.png)  |
| **Post Likes** | | | | |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/post-likes/)_ | Post Like (GET Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/likes/LikePostNotAuthenticated.png) |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/post-likes/)_ | Post Like (GET Authenticated) | Returns 200 response: a list of profiles that liked the specified post | Pass | [Screenshot](images/likes/LikePostAuthenticated.png) |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/post-likes/)_ | Post Like (POST Authenticated) | Returns 201 or 204 response: allows authenticated users to like the specified post | Pass | [Screenshot](images/likes/LikePostAuthenticated.png) |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/post-likes/)_ | Post Like (POST Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/likes/LikePostNotAuthenticated.png) |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/post-likes/)_ | Post Like (POST Authenticated - Error) | Returns 403 error: you cannot like your own post | Pass | [Screenshot](images/likes/methodPostLikeErrorNotLikeYourOwnPost.png) |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/post-likes/)_ | Post Like (DELETE Authenticated) | Returns 200 response: allows authenticated users to unlike the specified post | Pass | [Screenshot](images/likes/UnLikePostAuthenticated.png) |
| _[Post Like](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/3/post-likes/)_ | Post Like (DELETE Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/likes/UnlikePostNotAuthenticated.png) |
| _[Liked Post List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/liked-posts/)_ | Liked Post List (GET Authenticated) | Returns 200 response: a list of all posts liked by the authenticated user | Pass | [Screenshot](images/likes/LikedPostListAuth.png) |
| **Comments** | | | | |
| _[Comment List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/4/comments/)_ | Comment List (GET Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/comments/GetCommentListNoAuthPass.png) |
| _[Comment List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/4/comments/)_ | Comment List (GET Authenticated) | Returns 200 response: a list of all the comments from a specified post | Pass | [Screenshot](images/comments/GetCommentlistAuthPass.png) |
| _[Comment List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/4/comments/)_ | Comment List (POST Authenticated) | Returns 201 response: allows authenticated users to create comments | Pass | [Screenshot](images/comments/NewCommentAuthPass.png) |
| _[Comment List](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/4/comments/)_ | Comment List (POST Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/comments/PostCommentNoAuthPass.png) |
| _[Comment Detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/4/comments/5/)_ | Comment Detail (PUT Authenticated Owner) | Returns 200 response: allows the owner to update the comment | Pass | [Screenshot](images/comments/UpdateCommentAuthPass.png) |
| _[Comment Detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/4/comments/5/)_ | Comment Detail (PUT Unauthenticated) | Returns 401 error: authentication credentials were not provided | Pass | [Screenshot](images/comments/PutCommentUpdateNoAuthPass.png) |
| _[Comment Detail](https://socialapi-ce69e07a68e6.herokuapp.com/api/posts/4/comments/5/)_ | Comment Detail (DELETE Authenticated Owner) | Returns 204 response: comment is deleted | Pass | [Screenshot](images/comments/DeleteCommentAuthPass.png) |


