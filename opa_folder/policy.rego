package docker.compliance

deny[msg] {
  input.user == "root"
  msg := "Container must not run as root user"
}

// deny[msg] {
//   startswith(input.base_image, "ubuntu:14")
//   msg := sprintf("Base image %s is too old", [input.base_image])
// }

// deny[msg] {
//   some cmd
//   cmd := input.run_commands[_]
//   contains(cmd, "apt-get install") 
//   contains(cmd, "openssh-server")
//   msg := "Installing openssh-server is prohibited"
// }

// deny[msg] {
//   not input.user
//   msg := "USER instruction must be set in Dockerfile"
// }

// deny[msg] {
//   startswith(input.base_image, "alpine:3.4")
//   msg := "Alpine 3.4 is not supported"
// }
