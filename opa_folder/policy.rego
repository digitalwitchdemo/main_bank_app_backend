package docker.authz

default allow := false

# allow if the user is granted read/write access.
allow if {
	user_id := input.Headers["Authz-User"]
	user := users[user_id]
	not user.readOnly
}

# allow if the user is granted read-only access and the request is a GET.
allow if {
	user_id := input.Headers["Authz-User"]
	users[user_id].readOnly
	input.Method == "GET"
}

# users defines permissions for the user. In this case, we define a single
# attribute 'readOnly' that controls the kinds of commands the user can run.
users := {
	"bob": {"readOnly": true},
	"alice": {"readOnly": false},
}